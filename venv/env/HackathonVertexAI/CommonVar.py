
from Embeddingg import createVectorStore
from langchain.embeddings import VertexAIEmbeddings
from langchain.llms import VertexAI


class Mainfnn():
## load all the Documents
    folderPath ="./RelevantSOPs"
    loader = [] # create an object of the class when the function has self int it.
    pages = ""
    ### create vector Store
    vertex_llm_text = VertexAI(model_name="text-bison@001")
    vertex_embeddings = VertexAIEmbeddings(model_name="textembedding-gecko@001")
    db = createVectorStore.create(pages, vertex_embeddings)
    