import os
import gradio
import openai

from userInteface import GraphicalInterFace

import PDFLoader

from Embeddingg import createVectorStore
from langchain.embeddings import VertexAIEmbeddings
from langchain.llms import VertexAI

from CommonVar import Mainfnn


    # def getVectorStore():
    #     return self.db

    # folderPath ="./RelevantSOPs"
    # loader = PDFLoader.LoadPDFs() # create an object of the class when the function has self int it.
    # pages = loader.loadPdfDocuments(folderPath)

    # print("=====", len(pages))

    # ### create vector Store
    # vertex_llm_text = VertexAI(model_name="text-bison@001")
    # vertex_embeddings = VertexAIEmbeddings(model_name="textembedding-gecko@001")

# db = createVectorStore.create(pages, vertex_embeddings)

# query = "how does deferred Giveaway works for offer"
# relevantContext = createVectorStore.getRelevantContext(query, db)
# print("+++++")
# print(relevantContext)

# myPrompt = Promptt.getPrompt(relevantContext,query)
print("Settting up...")
Mainfnn.loader = PDFLoader.LoadPDFs()
folderPath ="./RelevantSOPs"
Mainfnn.pages = Mainfnn.loader.loadPdfDocuments(folderPath)

print("=====", len(Mainfnn.pages))

    ### create vector Store
Mainfnn.vertex_llm_text = VertexAI(model_name="text-bison@001")
Mainfnn.vertex_embeddings = VertexAIEmbeddings(model_name="textembedding-gecko@001")
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