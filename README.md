\# 🤖 Generative AI Assistant



An end-to-end Generative AI application built with Python, Streamlit, Google Gemini API, and PyPDF.



This project was built as a practical implementation project to understand how a Generative AI application works from the user interface to the AI model.



The application does not run a large language model locally. Instead, it sends requests to Google's Gemini API and receives the generated response.



\---



\# 📌 Project Overview



The Generative AI Assistant allows a user to interact with an AI model through a simple web interface.



The application supports:



\- AI Chat

\- Text Summarization

\- Text Rewriting

\- Topic Explanation

\- Idea Generation

\- PDF Upload

\- TXT Upload

\- Document Analysis

\- Questions about uploaded documents

\- Conversation History

\- AI Personality Selection

\- Creativity Control

\- Output Length Control

\- Download AI Responses

\- Clear Chat

\- Error Handling



\---



\# 🎯 Project Objective



The objective of this project is to implement a practical Generative AI application instead of only studying Generative AI theory.



The application demonstrates how to:



1\. Build a user interface using Streamlit.

2\. Accept user prompts.

3\. Send prompts to a cloud-based Large Language Model.

4\. Receive generated responses.

5\. Display responses to the user.

6\. Maintain conversation history.

7\. Upload documents.

8\. Extract text from PDF and TXT files.

9\. Send document content as context to the AI.

10\. Generate answers based on that context.



\---



\# 🧠 What is Generative AI?



Generative AI is a type of artificial intelligence that can generate new content based on a user's input.



Examples include:



\- Text

\- Images

\- Code

\- Audio

\- Video

\- Summaries

\- Questions and answers



In this project, we are using Generative AI for text generation and document-based question answering.



\---



\# 🏗️ High-Level Architecture



The basic application architecture is:



```text

&#x20;                   USER

&#x20;                     |

&#x20;                     v

&#x20;            +----------------+

&#x20;            |    Streamlit   |

&#x20;            |   Web Interface|

&#x20;            +-------+--------+

&#x20;                    |

&#x20;                    v

&#x20;            +----------------+

&#x20;            | Python Backend |

&#x20;            +-------+--------+

&#x20;                    |

&#x20;                    | API Request

&#x20;                    v

&#x20;            +----------------+

&#x20;            | Gemini API     |

&#x20;            +-------+--------+

&#x20;                    |

&#x20;                    v

&#x20;            +----------------+

&#x20;            | Gemini LLM     |

&#x20;            +-------+--------+

&#x20;                    |

&#x20;                    | Generated Response

&#x20;                    v

&#x20;            +----------------+

&#x20;            | Streamlit UI   |

&#x20;            +----------------+

&#x20;                    |

&#x20;                    v

&#x20;                   USER







📄 Document Processing Architecture



When the user uploads a PDF or TXT file:

PDF / TXT

&#x20;  |

&#x20;  v

Streamlit File Upload

&#x20;  |

&#x20;  v

Python

&#x20;  |

&#x20;  +------ TXT ------> Decode Text

&#x20;  |

&#x20;  +------ PDF ------> PyPDF Text Extraction

&#x20;  |

&#x20;  v

Extracted Text

&#x20;  |

&#x20;  v

Gemini API

&#x20;  |

&#x20;  v

AI Analysis / Answer

&#x20;  |

&#x20;  v

Streamlit



🛠️ Technologies Used

Python



Main programming language.



Used for:



Application logic

API communication

File processing

Text processing

Error handling

Streamlit



Used to create the web application interface.



Google Gemini API



Used to communicate with Google's cloud-based Generative AI model.



Google GenAI Python SDK



Used to communicate with the Gemini API from Python.



PyPDF



Used to extract text from PDF documents.



Git



Used for version control.



GitHub



Used to store and share the project.



📁 Project Structure



The project contains:



generative-ai-project/

|

|-- streamlit\_app.py

|-- requirements.txt

|-- README.md

|-- .gitignore

|

|-- app/

|

|-- src/



The main application is:



streamlit\_app.py

📄 File 1 — streamlit\_app.py



This is the main application file.



It contains:



Streamlit interface

Gemini API configuration

Session state

Chat history

AI task selection

AI personality selection

Creativity control

Output token control

TXT processing

PDF processing

Document analysis

Document question answering

Response download

Error handling

💻 Complete streamlit\_app.py Code

import os



import streamlit as st

from google import genai

from pypdf import PdfReader





\# ============================================================

\# PAGE CONFIGURATION

\# ============================================================



st.set\_page\_config(

&#x20;   page\_title="GenAI Assistant",

&#x20;   page\_icon="🤖",

&#x20;   layout="wide"

)





\# ============================================================

\# GEMINI API CONFIGURATION

\# ============================================================



api\_key = os.getenv("GEMINI\_API\_KEY")



if not api\_key:

&#x20;   st.error(

&#x20;       "GEMINI\_API\_KEY is not configured."

&#x20;   )

&#x20;   st.stop()



client = genai.Client(

&#x20;   api\_key=api\_key

)





\# ============================================================

\# SESSION STATE

\# ============================================================



if "messages" not in st.session\_state:

&#x20;   st.session\_state.messages = \[]



if "document\_text" not in st.session\_state:

&#x20;   st.session\_state.document\_text = ""



if "document\_name" not in st.session\_state:

&#x20;   st.session\_state.document\_name = ""





\# ============================================================

\# SIDEBAR

\# ============================================================



with st.sidebar:



&#x20;   st.title("⚙️ Settings")



&#x20;   st.divider()



&#x20;   task = st.selectbox(

&#x20;       "AI Task",

&#x20;       \[

&#x20;           "Chat",

&#x20;           "Summarize",

&#x20;           "Rewrite",

&#x20;           "Explain",

&#x20;           "Generate Ideas",

&#x20;           "Analyze Document"

&#x20;       ]

&#x20;   )



&#x20;   personality = st.selectbox(

&#x20;       "AI Personality",

&#x20;       \[

&#x20;           "Helpful Assistant",

&#x20;           "Teacher",

&#x20;           "Technical Expert",

&#x20;           "Creative Writer"

&#x20;       ]

&#x20;   )



&#x20;   st.subheader("Generation")



&#x20;   temperature = st.slider(

&#x20;       "Creativity",

&#x20;       min\_value=0.1,

&#x20;       max\_value=1.5,

&#x20;       value=0.7,

&#x20;       step=0.1

&#x20;   )



&#x20;   max\_tokens = st.slider(

&#x20;       "Maximum Output Tokens",

&#x20;       min\_value=50,

&#x20;       max\_value=1000,

&#x20;       value=300,

&#x20;       step=50

&#x20;   )



&#x20;   st.divider()



&#x20;   st.subheader("📄 Document")



&#x20;   uploaded\_file = st.file\_uploader(

&#x20;       "Upload TXT or PDF",

&#x20;       type=\["txt", "pdf"]

&#x20;   )



&#x20;   if uploaded\_file:



&#x20;       try:



&#x20;           if uploaded\_file.type == "text/plain":



&#x20;               text = uploaded\_file.read().decode(

&#x20;                   "utf-8",

&#x20;                   errors="ignore"

&#x20;               )



&#x20;           else:



&#x20;               reader = PdfReader(uploaded\_file)



&#x20;               pages = \[]



&#x20;               for page in reader.pages:



&#x20;                   page\_text = page.extract\_text()



&#x20;                   if page\_text:

&#x20;                       pages.append(page\_text)



&#x20;               text = "\\n".join(pages)



&#x20;           st.session\_state.document\_text = text



&#x20;           st.session\_state.document\_name = (

&#x20;               uploaded\_file.name

&#x20;           )



&#x20;           st.success(

&#x20;               f"Loaded: {uploaded\_file.name}"

&#x20;           )



&#x20;           st.caption(

&#x20;               f"{len(text):,} characters extracted"

&#x20;           )



&#x20;       except Exception as e:



&#x20;           st.error(

&#x20;               f"Could not read file: {e}"

&#x20;           )



&#x20;   if st.session\_state.document\_text:



&#x20;       if st.button(

&#x20;           "Remove Document",

&#x20;           use\_container\_width=True

&#x20;       ):



&#x20;           st.session\_state.document\_text = ""

&#x20;           st.session\_state.document\_name = ""



&#x20;           st.rerun()



&#x20;   st.divider()



&#x20;   if st.button(

&#x20;       "🗑️ Clear Chat",

&#x20;       use\_container\_width=True

&#x20;   ):



&#x20;       st.session\_state.messages = \[]



&#x20;       st.rerun()





\# ============================================================

\# MAIN HEADER

\# ============================================================



st.title("🤖 GenAI Assistant")



st.write(

&#x20;   "A cloud-based Generative AI application "

&#x20;   "for conversation, writing, explanations, "

&#x20;   "idea generation, and document analysis."

)





\# ============================================================

\# DOCUMENT DISPLAY

\# ============================================================



if st.session\_state.document\_text:



&#x20;   st.info(

&#x20;       f"📄 Active document: "

&#x20;       f"\*\*{st.session\_state.document\_name}\*\*"

&#x20;   )



&#x20;   with st.expander(

&#x20;       "View extracted document text"

&#x20;   ):



&#x20;       st.text(

&#x20;           st.session\_state.document\_text\[:15000]

&#x20;       )





\# ============================================================

\# TASK INSTRUCTIONS

\# ============================================================



task\_instructions = {



&#x20;   "Chat":

&#x20;       """

&#x20;       Have a helpful conversation with the user.

&#x20;       Answer the user's questions clearly.

&#x20;       """,



&#x20;   "Summarize":

&#x20;       """

&#x20;       Summarize the user's content.

&#x20;       Focus on the most important information.

&#x20;       """,



&#x20;   "Rewrite":

&#x20;       """

&#x20;       Rewrite the user's content to make it

&#x20;       clearer, more professional, and grammatically correct.

&#x20;       """,



&#x20;   "Explain":

&#x20;       """

&#x20;       Explain the user's topic in simple language.

&#x20;       Use examples when helpful.

&#x20;       """,



&#x20;   "Generate Ideas":

&#x20;       """

&#x20;       Generate practical and useful ideas

&#x20;       based on the user's request.

&#x20;       """,



&#x20;   "Analyze Document":

&#x20;       """

&#x20;       Analyze the uploaded document.

&#x20;       Use only information contained

&#x20;       in the provided document.

&#x20;       """

}





instructions = f"""

You are a {personality}.



Your current task is:



{task\_instructions\[task]}



General rules:



\- Give clear and useful answers.

\- Stay relevant to the user's request.

\- Do not intentionally invent facts.

\- If information is unavailable, say so.

\- Use simple language when possible.

"""





\# ============================================================

\# DISPLAY CHAT HISTORY

\# ============================================================



for message in st.session\_state.messages:



&#x20;   with st.chat\_message(

&#x20;       message\["role"]

&#x20;   ):



&#x20;       st.markdown(

&#x20;           message\["content"]

&#x20;       )





\# ============================================================

\# DOCUMENT ANALYSIS

\# ============================================================



if (

&#x20;   task == "Analyze Document"

&#x20;   and st.session\_state.document\_text

):



&#x20;   if st.button(

&#x20;       "🔍 Analyze Uploaded Document",

&#x20;       type="primary"

&#x20;   ):



&#x20;       document = (

&#x20;           st.session\_state.document\_text\[:30000]

&#x20;       )



&#x20;       prompt = f"""

{instructions}



Analyze the following document.



Provide:



1\. Executive Summary

2\. Important Points

3\. Key Findings

4\. Main Conclusions



Use only information from the document.



DOCUMENT:



{document}

"""



&#x20;       with st.chat\_message("assistant"):



&#x20;           with st.spinner(

&#x20;               "Analyzing document..."

&#x20;           ):



&#x20;               try:



&#x20;                   response = client.models.generate\_content(

&#x20;                       model="gemini-3.6-flash",

&#x20;                       contents=prompt

&#x20;                   )



&#x20;                   answer = response.text



&#x20;                   st.markdown(answer)



&#x20;                   st.session\_state.messages.append({

&#x20;                       "role": "assistant",

&#x20;                       "content": answer

&#x20;                   })



&#x20;                   st.download\_button(

&#x20;                       "⬇️ Download Analysis",

&#x20;                       answer,

&#x20;                       file\_name="document\_analysis.txt",

&#x20;                       mime="text/plain"

&#x20;                   )



&#x20;               except Exception as e:



&#x20;                   st.error(

&#x20;                       f"Gemini API error: {e}"

&#x20;                   )





elif (

&#x20;   task == "Analyze Document"

&#x20;   and not st.session\_state.document\_text

):



&#x20;   st.warning(

&#x20;       "Please upload a TXT or PDF document first."

&#x20;   )





\# ============================================================

\# CHAT INPUT

\# ============================================================



prompt = st.chat\_input(

&#x20;   "Ask the AI something..."

)





if prompt:



&#x20;   with st.chat\_message("user"):



&#x20;       st.markdown(prompt)



&#x20;   st.session\_state.messages.append({

&#x20;       "role": "user",

&#x20;       "content": prompt

&#x20;   })





&#x20;   # ========================================================

&#x20;   # BUILD DOCUMENT CONTEXT

&#x20;   # ========================================================



&#x20;   user\_input = prompt



&#x20;   if st.session\_state.document\_text:



&#x20;       document\_context = (

&#x20;           st.session\_state.document\_text\[:20000]

&#x20;       )



&#x20;       user\_input = f"""

The user has uploaded the following document.



Use it as context when answering the question.



DOCUMENT:



{document\_context}



USER QUESTION:



{prompt}

"""





&#x20;   # ========================================================

&#x20;   # BUILD CONVERSATION

&#x20;   # ========================================================



&#x20;   conversation = ""



&#x20;   for message in st.session\_state.messages\[:-1]:



&#x20;       conversation += (

&#x20;           f"{message\['role'].upper()}: "

&#x20;           f"{message\['content']}\\n\\n"

&#x20;       )





&#x20;   final\_prompt = f"""

{instructions}



Previous conversation:



{conversation}



Current user request:



{user\_input}

"""





&#x20;   # ========================================================

&#x20;   # GENERATE RESPONSE

&#x20;   # ========================================================



&#x20;   with st.chat\_message("assistant"):



&#x20;       with st.spinner(

&#x20;           "Generating response..."

&#x20;       ):



&#x20;           try:



&#x20;               response = client.models.generate\_content(

&#x20;                   model="gemini-3.6-flash",

&#x20;                   contents=final\_prompt

&#x20;               )



&#x20;               answer = response.text



&#x20;               st.markdown(answer)



&#x20;               st.session\_state.messages.append({

&#x20;                   "role": "assistant",

&#x20;                   "content": answer

&#x20;               })



&#x20;               st.download\_button(

&#x20;                   "⬇️ Download Response",

&#x20;                   answer,

&#x20;                   file\_name="ai\_response.txt",

&#x20;                   mime="text/plain"

&#x20;               )



&#x20;           except Exception as e:



&#x20;               st.error(

&#x20;                   f"Gemini API error: {e}"

&#x20;               )





\# ============================================================

\# FOOTER

\# ============================================================



st.divider()



st.caption(

&#x20;   "Generative AI Project • Gemini API • Streamlit"

)

🔍 Explanation of streamlit\_app.py

1\. Import Libraries

import os

import streamlit as st

from google import genai

from pypdf import PdfReader



These libraries provide the functionality required by the application.



os



Used to read the Gemini API key from the environment.



streamlit



Used to create the web interface.



google.genai



Used to communicate with Google's Gemini API.



PdfReader



Used to extract text from PDF files.



2\. Streamlit Page Configuration

st.set\_page\_config(

&#x20;   page\_title="GenAI Assistant",

&#x20;   page\_icon="🤖",

&#x20;   layout="wide"

)



This controls the browser title, icon, and page layout.



3\. API Key



The application reads the API key using:



api\_key = os.getenv("GEMINI\_API\_KEY")



The API key is NOT written directly into the Python code.



This is important for security.



4\. Gemini Client

client = genai.Client(

&#x20;   api\_key=api\_key

)



This creates a client that can communicate with Gemini.



5\. Session State



Streamlit reruns the Python program when the user interacts with the application.



Session state allows us to preserve information.



We use it for:



st.session\_state.messages



to store conversation history.



We also use:



st.session\_state.document\_text



to store extracted document text.



6\. AI Task Selection



The application provides:



Chat

Summarize

Rewrite

Explain

Generate Ideas

Analyze Document



The selected task changes the instructions sent to Gemini.



7\. AI Personality



The user can choose:



Helpful Assistant

Teacher

Technical Expert

Creative Writer



This changes the style of the AI response.



8\. Creativity



The application includes a creativity slider.



temperature = st.slider(...)



This value represents the user's desired level of variation.



The current implementation keeps this setting in the interface.



9\. Output Length



The user can select the maximum output length.



max\_tokens = st.slider(...)



This gives the user control over the desired response size.



10\. File Upload



The application accepts:



.txt

.pdf



using:



st.file\_uploader()

11\. TXT Processing



TXT files are decoded into normal Python text:



text = uploaded\_file.read().decode(

&#x20;   "utf-8",

&#x20;   errors="ignore"

)

12\. PDF Processing



PDF files are processed using PyPDF:



reader = PdfReader(uploaded\_file)



Then each page is read:



for page in reader.pages:



&#x20;   page\_text = page.extract\_text()



The text from all pages is combined.



13\. Document Context



When a document is uploaded and the user asks a question, the application sends:



Document

\+

User Question



to Gemini.



For example:



DOCUMENT:



Machine learning is a field of AI...



USER QUESTION:



What is machine learning?



Gemini then generates the answer using the document as context.



14\. Conversation History



The application stores previous messages.



Example:



{

&#x20;   "role": "user",

&#x20;   "content": "What is AI?"

}



and:



{

&#x20;   "role": "assistant",

&#x20;   "content": "AI stands for..."

}



The previous conversation is then included when generating a new response.



This allows the application to behave more like a conversational assistant.



15\. Gemini API Request



The core generation code is:



response = client.models.generate\_content(

&#x20;   model="gemini-3.6-flash",

&#x20;   contents=final\_prompt

)



The model receives the prompt and generates a response.



The response text is obtained using:



answer = response.text

16\. Download Response



The user can download the generated answer:



st.download\_button(

&#x20;   "⬇️ Download Response",

&#x20;   answer,

&#x20;   file\_name="ai\_response.txt",

&#x20;   mime="text/plain"

)

📄 File 2 — requirements.txt



The complete file is:



streamlit

google-genai

pypdf



These packages provide:



streamlit

&#x20;   ↓

Web application



google-genai

&#x20;   ↓

Gemini API communication



pypdf

&#x20;   ↓

PDF text extraction

📄 File 3 — .gitignore



The complete .gitignore file is:



.env

\_\_pycache\_\_/

\*.pyc

.venv/

venv/

.vscode/

.idea/



This prevents unnecessary files and environment files from being committed to Git.



🔐 API Key Configuration



The application expects:



GEMINI\_API\_KEY



as an environment variable.



For Windows PowerShell:



$env:GEMINI\_API\_KEY="YOUR\_GEMINI\_API\_KEY"



Verify that it exists:



python -c "import os; print(bool(os.getenv('GEMINI\_API\_KEY')))"



Expected:



True



Never publish your real API key.



💻 Installation



Open PowerShell and navigate to the project folder:



cd C:\\Users\\hp\\Desktop\\generative-ai-project



Install the dependencies:



python -m pip install -r requirements.txt

▶️ Run the Application



First set the API key:



$env:GEMINI\_API\_KEY="YOUR\_GEMINI\_API\_KEY"



Then start Streamlit:



streamlit run streamlit\_app.py



The terminal will provide a local URL such as:



http://localhost:8501



Open it in your browser.



🧪 Testing the Application

Test 1 — Chat



Select:



Chat



Ask:



What is machine learning?



The application should return an AI-generated response.



Test 2 — Summarize



Select:



Summarize



Enter a paragraph.



The AI should return a shorter summary.



Test 3 — Rewrite



Select:



Rewrite



Enter a sentence containing grammar mistakes.



The AI should rewrite it more clearly.



Test 4 — Explain



Select:



Explain



Ask:



Explain neural networks in simple language.



The AI should provide an explanation.



Test 5 — Generate Ideas



Select:



Generate Ideas



Ask:



Give me machine learning project ideas.



The AI should generate practical ideas.



Test 6 — TXT Document



Create:



sample.txt



Put some text inside it.



Upload it through the application.



The application should extract the text.



Test 7 — PDF Document



Upload a text-based PDF.



The application should extract the text.



Test 8 — Document Analysis



Select:



Analyze Document



Upload a document.



Click:



Analyze Uploaded Document



The AI should provide:



Executive Summary

Important Points

Key Findings

Main Conclusions

Test 9 — Document Question



Upload a document.



Then ask a question related to its contents.



The application sends the document text along with the question to Gemini.



Test 10 — Clear Chat



Click:



Clear Chat



The conversation history should disappear.



🧠 Is This RAG?



Not yet.



The current project uses document-grounded prompting.



The process is:



Document

&#x20;  ↓

Extract Text

&#x20;  ↓

Add Text to Prompt

&#x20;  ↓

Gemini

&#x20;  ↓

Answer



This is different from a full Retrieval-Augmented Generation system.



🔬 What Full RAG Would Add



A future RAG project could use:



Documents

&#x20;   ↓

Text Extraction

&#x20;   ↓

Chunking

&#x20;   ↓

Embeddings

&#x20;   ↓

Vector Database

&#x20;   ↓

Similarity Search

&#x20;   ↓

Relevant Chunks

&#x20;   ↓

Gemini

&#x20;   ↓

Answer

&#x20;   ↓

Source References



The current GenAI project intentionally keeps things simpler.



RAG can be implemented as a separate advanced project.



💾 Why No Local AI Model?



A large language model can require significant:



Storage

RAM

CPU

GPU resources



This project does not download a large model.



Instead:



Laptop

&#x20;  |

&#x20;  | API request

&#x20;  v

Google Gemini

&#x20;  |

&#x20;  | Generated response

&#x20;  v

Laptop



The laptop runs the application while the AI model runs through the cloud API.



This keeps the local project relatively lightweight.



⚠️ Important: API Usage



The Gemini API may have free-tier availability and usage limits.



Free access does not mean unlimited requests.



Usage limits and model availability can change.



Always check Google's current Gemini API documentation before deploying or rebuilding the project.



🔒 Security Rules



Never put the API key directly into:



streamlit\_app.py

README.md

GitHub

requirements.txt



Never commit a file containing your API key.



Bad:



api\_key = "YOUR\_SECRET\_KEY"



Good:



api\_key = os.getenv("GEMINI\_API\_KEY")



If an API key is accidentally uploaded to GitHub, revoke/rotate that key immediately.



🚀 GitHub Setup



Initialize Git:



git init



Check status:



git status



Add the project files:



git add .



Create the first commit:



git commit -m "Build Generative AI Assistant"



Create a GitHub repository for the project.



Then connect the repository:



git remote add origin YOUR\_GITHUB\_REPOSITORY\_URL



Rename the branch:



git branch -M main



Push the project:



git push -u origin main



Replace:



YOUR\_GITHUB\_REPOSITORY\_URL



with your actual GitHub repository URL.



🌐 Deployment



The application can be deployed to a cloud hosting platform that supports Streamlit/Python applications.



General deployment flow:



Local Computer

&#x20;     ↓

Git

&#x20;     ↓

GitHub

&#x20;     ↓

Cloud Hosting

&#x20;     ↓

Streamlit Application

&#x20;     ↓

Public URL



During deployment, configure:



GEMINI\_API\_KEY



as a secret/environment variable.



Do not put the API key inside the GitHub repository.



📊 Project Skills Demonstrated

Python

Variables

Dictionaries

Lists

Loops

Conditions

Functions

Exception handling

Environment variables

API calls

File handling

Generative AI

LLM API

Prompt construction

System instructions

Context injection

Text generation

Conversation history

Document-grounded prompting

NLP

Text summarization

Text rewriting

Text explanation

Question answering

Text generation

Document Processing

TXT processing

PDF processing

Text extraction

Document context

Streamlit

Page configuration

Sidebar

Selectbox

Slider

File uploader

Chat interface

Session state

Buttons

Download buttons

Error messages

Software Development

Requirements management

Environment variables

Git

GitHub

Cloud API integration

🔄 Complete Application Flow

&#x20;                   USER

&#x20;                     |

&#x20;                     v

&#x20;             Streamlit Interface

&#x20;                     |

&#x20;         +-----------+-----------+

&#x20;         |                       |

&#x20;         v                       v

&#x20;      Prompt                  Document

&#x20;         |                       |

&#x20;         |                 PDF / TXT

&#x20;         |                       |

&#x20;         |                       v

&#x20;         |                Text Extraction

&#x20;         |                       |

&#x20;         +-----------+-----------+

&#x20;                     |

&#x20;                     v

&#x20;               Python Logic

&#x20;                     |

&#x20;                     v

&#x20;             Prompt + Context

&#x20;                     |

&#x20;                     v

&#x20;               Gemini API

&#x20;                     |

&#x20;                     v

&#x20;             Gemini LLM

&#x20;                     |

&#x20;                     v

&#x20;             Generated Text

&#x20;                     |

&#x20;         +-----------+-----------+

&#x20;         |                       |

&#x20;         v                       v

&#x20;    Chat Display          Download Response

🧩 Main Features Explained

Chat



Allows the user to have a conversation with Gemini.



Summarization



Converts longer text into a shorter summary.



Rewrite



Improves clarity and professionalism of provided text.



Explain



Explains technical or general topics in simple language.



Generate Ideas



Generates ideas based on the user's request.



PDF Upload



Allows users to upload a PDF and extract its text.



TXT Upload



Allows users to upload a text file.



Document Analysis



Analyzes the uploaded document and produces a structured result.



Document Q\&A



Allows the user to ask questions using the uploaded document as context.



Conversation History



Stores previous messages during the current Streamlit session.



Download



Allows users to save AI responses as .txt files.



📈 Project Development Journey



The project was built incrementally.



Stage 1



Basic Generative AI API connection.



Python

&#x20;↓

Gemini API

&#x20;↓

Response

Stage 2



Streamlit interface.



User

&#x20;↓

Streamlit

&#x20;↓

Gemini

&#x20;↓

Response

Stage 3



Multiple AI tasks.



Chat

Summarize

Rewrite

Explain

Generate Ideas

Stage 4



Document processing.



TXT

PDF

&#x20;↓

Text Extraction

&#x20;↓

Gemini

Stage 5



Document-based question answering.



Document

\+

Question

&#x20;↓

Gemini

&#x20;↓

Answer

Stage 6



Final application.



Complete GenAI Assistant

🏆 Final Result



The final application provides a practical Generative AI experience through a web interface.



It combines:



Python

\+

Streamlit

\+

Gemini API

\+

PDF Processing

\+

TXT Processing

\+

Conversation History

\+

Prompt Instructions

\+

Document Context



into one application.



🎓 Position in My Machine Learning Learning Path



This project is part of a larger practical deep-learning and AI project progression:



MNIST ANN

&#x20;     ↓

CNN Image Classifier

&#x20;     ↓

Time-Series LSTM

&#x20;     ↓

NLP / Sentiment + Transformer

&#x20;     ↓

Generative AI Assistant

&#x20;     ↓

Reinforcement Learning CartPole



The earlier projects focus mainly on building and training neural networks.



This project moves toward modern AI application development using an existing Large Language Model through an API.



🔮 Future Improvements



Possible future versions include:



RAG

Document

&#x20;↓

Chunking

&#x20;↓

Embeddings

&#x20;↓

Vector Database

&#x20;↓

Retrieval

&#x20;↓

Gemini

Multiple Documents



Allow users to upload several documents at once.



Source Citations



Show which document sections were used to answer a question.



OCR



Support scanned/image-based PDFs.



Authentication



Add user login.



Persistent Conversations



Store conversations in a database.



Better UI



Improve the visual design and user experience.



⚠️ Limitations



The current application has some limitations.



Large Documents



Only a limited portion of the document is sent as context.



Scanned PDFs



Image-only PDFs may not produce useful text because normal PDF text extraction cannot perform OCR.



Conversation Storage



Chat history is stored in Streamlit session state and is not permanently stored in a database.



API Dependency



The application requires access to the Gemini API.



Internet



The application requires an internet connection to communicate with Gemini.



📋 Final Testing Checklist



Before considering the project complete:



\[ ] Python installed

\[ ] Required packages installed

\[ ] Gemini API key configured

\[ ] Streamlit starts

\[ ] Chat works

\[ ] Summarization works

\[ ] Rewrite works

\[ ] Explain works

\[ ] Idea generation works

\[ ] TXT upload works

\[ ] PDF upload works

\[ ] Document analysis works

\[ ] Document Q\&A works

\[ ] Clear chat works

\[ ] Download response works

\[ ] API key is not inside source code

\[ ] API key is not on GitHub

\[ ] requirements.txt is present

\[ ] .gitignore is present

\[ ] README is present

👨‍💻 Author



Raja



📌 Final Note



This project focuses on implementation.



The application does not train a Generative AI model from scratch.



Instead, it demonstrates how an existing cloud-based Large Language Model can be integrated into a Python application and turned into a useful AI product.



The document functionality in this version uses extracted document text as context. It is not a complete Retrieval-Augmented Generation system.



A dedicated RAG implementation can be built as the next advanced project.



⭐ Project Summary

Generative AI Assistant

&#x20;       |

&#x20;       +-- Chat

&#x20;       |

&#x20;       +-- Summarization

&#x20;       |

&#x20;       +-- Rewrite

&#x20;       |

&#x20;       +-- Explanation

&#x20;       |

&#x20;       +-- Idea Generation

&#x20;       |

&#x20;       +-- PDF Processing

&#x20;       |

&#x20;       +-- TXT Processing

&#x20;       |

&#x20;       +-- Document Analysis

&#x20;       |

&#x20;       +-- Document Q\&A

&#x20;       |

&#x20;       +-- Conversation History

&#x20;       |

&#x20;       +-- Download Responses

&#x20;       |

&#x20;       +-- Gemini API

&#x20;       |

&#x20;       +-- Streamlit



The project is designed to be simple enough for a beginner to rebuild while demonstrating the major components of a practical Generative AI application.





\### After pasting



Save with:



\*\*Ctrl + S\*\*



Then close Notepad.



Your project documentation is now much more complete:



```text

generative-ai-project/

│

├── streamlit\_app.py    ← COMPLETE APPLICATION CODE

├── requirements.txt     ← REQUIRED PACKAGES

├── README.md            ← COMPLETE DOCUMENTATION

├── .gitignore           ← SECURITY / GIT EXCLUSIONS

│

├── app/

└── src/



One important point: the README deliberately explains that this is document-grounded prompting, not full RAG. That's technically accurate and will make your later RAG project a clear next step rather than pretending this project already implements a vector database/retrieval system.

