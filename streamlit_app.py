import os

import streamlit as st
from google import genai
from pypdf import PdfReader


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="GenAI Assistant",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# GEMINI API CONFIGURATION
# ============================================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error(
        "GEMINI_API_KEY is not configured."
    )
    st.stop()

client = genai.Client(
    api_key=api_key
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "document_name" not in st.session_state:
    st.session_state.document_name = ""


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("⚙️ Settings")

    st.divider()

    task = st.selectbox(
        "AI Task",
        [
            "Chat",
            "Summarize",
            "Rewrite",
            "Explain",
            "Generate Ideas",
            "Analyze Document"
        ]
    )

    personality = st.selectbox(
        "AI Personality",
        [
            "Helpful Assistant",
            "Teacher",
            "Technical Expert",
            "Creative Writer"
        ]
    )

    st.subheader("Generation")

    temperature = st.slider(
        "Creativity",
        min_value=0.1,
        max_value=1.5,
        value=0.7,
        step=0.1
    )

    max_tokens = st.slider(
        "Maximum Output Tokens",
        min_value=50,
        max_value=1000,
        value=300,
        step=50
    )

    st.divider()

    st.subheader("📄 Document")

    uploaded_file = st.file_uploader(
        "Upload TXT or PDF",
        type=["txt", "pdf"]
    )

    if uploaded_file:

        try:

            if uploaded_file.type == "text/plain":

                text = uploaded_file.read().decode(
                    "utf-8",
                    errors="ignore"
                )

            else:

                reader = PdfReader(uploaded_file)

                pages = []

                for page in reader.pages:

                    page_text = page.extract_text()

                    if page_text:
                        pages.append(page_text)

                text = "\n".join(pages)

            st.session_state.document_text = text

            st.session_state.document_name = (
                uploaded_file.name
            )

            st.success(
                f"Loaded: {uploaded_file.name}"
            )

            st.caption(
                f"{len(text):,} characters extracted"
            )

        except Exception as e:

            st.error(
                f"Could not read file: {e}"
            )

    if st.session_state.document_text:

        if st.button(
            "Remove Document",
            use_container_width=True
        ):

            st.session_state.document_text = ""
            st.session_state.document_name = ""

            st.rerun()

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🤖 GenAI Assistant")

st.write(
    "A cloud-based Generative AI application "
    "for conversation, writing, explanations, "
    "idea generation, and document analysis."
)


# ============================================================
# DOCUMENT DISPLAY
# ============================================================

if st.session_state.document_text:

    st.info(
        f"📄 Active document: "
        f"**{st.session_state.document_name}**"
    )

    with st.expander(
        "View extracted document text"
    ):

        st.text(
            st.session_state.document_text[:15000]
        )


# ============================================================
# TASK INSTRUCTIONS
# ============================================================

task_instructions = {

    "Chat":
        """
        Have a helpful conversation with the user.
        Answer the user's questions clearly.
        """,

    "Summarize":
        """
        Summarize the user's content.
        Focus on the most important information.
        """,

    "Rewrite":
        """
        Rewrite the user's content to make it
        clearer, more professional, and grammatically correct.
        """,

    "Explain":
        """
        Explain the user's topic in simple language.
        Use examples when helpful.
        """,

    "Generate Ideas":
        """
        Generate practical and useful ideas
        based on the user's request.
        """,

    "Analyze Document":
        """
        Analyze the uploaded document.
        Use only information contained
        in the provided document.
        """
}


instructions = f"""
You are a {personality}.

Your current task is:

{task_instructions[task]}

General rules:

- Give clear and useful answers.
- Stay relevant to the user's request.
- Do not intentionally invent facts.
- If information is unavailable, say so.
- Use simple language when possible.
"""


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# DOCUMENT ANALYSIS
# ============================================================

if (
    task == "Analyze Document"
    and st.session_state.document_text
):

    if st.button(
        "🔍 Analyze Uploaded Document",
        type="primary"
    ):

        document = (
            st.session_state.document_text[:30000]
        )

        prompt = f"""
{instructions}

Analyze the following document.

Provide:

1. Executive Summary
2. Important Points
3. Key Findings
4. Main Conclusions

Use only information from the document.

DOCUMENT:

{document}
"""

        with st.chat_message("assistant"):

            with st.spinner(
                "Analyzing document..."
            ):

                try:

                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=prompt
                    )

                    answer = response.text

                    st.markdown(answer)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer
                    })

                    st.download_button(
                        "⬇️ Download Analysis",
                        answer,
                        file_name="document_analysis.txt",
                        mime="text/plain"
                    )

                except Exception as e:

                    st.error(
                        f"Gemini API error: {e}"
                    )


elif (
    task == "Analyze Document"
    and not st.session_state.document_text
):

    st.warning(
        "Please upload a TXT or PDF document first."
    )


# ============================================================
# CHAT INPUT
# ============================================================

prompt = st.chat_input(
    "Ask the AI something..."
)


if prompt:

    with st.chat_message("user"):

        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })


    # ========================================================
    # BUILD DOCUMENT CONTEXT
    # ========================================================

    user_input = prompt

    if st.session_state.document_text:

        document_context = (
            st.session_state.document_text[:20000]
        )

        user_input = f"""
The user has uploaded the following document.

Use it as context when answering the question.

DOCUMENT:

{document_context}

USER QUESTION:

{prompt}
"""


    # ========================================================
    # BUILD CONVERSATION
    # ========================================================

    conversation = ""

    for message in st.session_state.messages[:-1]:

        conversation += (
            f"{message['role'].upper()}: "
            f"{message['content']}\n\n"
        )


    final_prompt = f"""
{instructions}

Previous conversation:

{conversation}

Current user request:

{user_input}
"""


    # ========================================================
    # GENERATE RESPONSE
    # ========================================================

    with st.chat_message("assistant"):

        with st.spinner(
            "Generating response..."
        ):

            try:

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=final_prompt
                )

                answer = response.text

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

                st.download_button(
                    "⬇️ Download Response",
                    answer,
                    file_name="ai_response.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(
                    f"Gemini API error: {e}"
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Generative AI Project • Gemini API • Streamlit"
)