import os
import gradio
import openai

from userInteface import GraphicalInterFace

import PDFLoader

from Embeddingg import createVectorStore
from langchain.embeddings import OpenAIEmbeddings
# from langchain.llms import VertexAI
from langchain.chat_models import ChatOpenAI

from CommonVar import Mainfnn

print("Settting up...")
### setup OpenAI
# openai.api_key  = os.getenv('API_KEY')
# openai.api_key  = "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"

### load context
Mainfnn.loader = PDFLoader.LoadPDFs()
folderPath ="./RelevantSOPs"
Mainfnn.pages = Mainfnn.loader.loadPdfDocuments(folderPath)

print("=====", len(Mainfnn.pages))

    ### create vector Store
# Mainfnn.vertex_llm_text = VertexAI(model_name="text-bison@001")
# ChatOpenAI
# Mainfnn.vertex_embeddings = VertexAIEmbeddings(model_name="textembedding-gecko@001")
Mainfnn.vertex_embeddings  = OpenAIEmbeddings(openai_api_key="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")
Mainfnn.db = createVectorStore.create(Mainfnn.pages , Mainfnn.vertex_embeddings)

print("Settting up DONE...")
# openai.api_key = "YOUR_API_KEY"
prompt = "Enter Your Query Here"
print("STARTING UI...................")
# block = gradio.Blocks(theme=gradio.themes.Monochrome())
block = gradio.Blocks(theme=gradio.themes.Default())

with block:
    gradio.Markdown("""<h1><center>SANTA OBI-WAN 
    ChatBot </center></h1>
    """)
    chatbot = gradio.Chatbot()
    message = gradio.Textbox(placeholder=prompt)
    state = gradio.State()
    submit = gradio.Button("SEND")
    submit.click(GraphicalInterFace.message_and_history, 
                 inputs=[message, state], 
                 outputs=[chatbot, state])
block.launch(debug = True)