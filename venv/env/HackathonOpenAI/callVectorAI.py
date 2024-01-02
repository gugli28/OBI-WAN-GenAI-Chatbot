import urllib
import warnings
from pathlib import Path as p
from pprint import pprint

import pandas as pd
from langchain import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import VertexAIEmbeddings
from langchain.llms import VertexAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from IPython.display import display, Markdown
from vertexai.preview.language_models import TextGenerationModel
from vertexai.language_models._language_models import TextGenerationResponse

warnings.filterwarnings("ignore")


print("123")

# vertex_llm_text = VertexAI(model_name="text-bison@001")
# vertex_embeddings = VertexAIEmbeddings(model_name="textembedding-gecko@001")

class TintinAI():
    def getResponse(prompt ,temperature: float = 0.2)-> TextGenerationResponse:
        """Ideation example with a Large Language Model"""

        # TODO developer - override these parameters as needed:
        parameters = {
            "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
            "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
            "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
            "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
        }

        model = TextGenerationModel.from_pretrained("text-bison@001")
        response = model.predict(
            prompt,
            **parameters,
        )
        
        return str(response)

    # def getMapReduceChain():
    #     map_reduce_chain = load_qa_chain(
    #     vertex_llm_text,
    #     chain_type="map_reduce",
    #     return_intermediate_steps=True,
    #     question_prompt=question_prompt,
    #     combine_prompt=combine_prompt,
    #     )