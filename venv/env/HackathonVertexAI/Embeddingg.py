

from langchain.vectorstores import DocArrayInMemorySearch
from langchain.embeddings import VertexAIEmbeddings

from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

class createVectorStore():
    def create(inputList: List, vertex_embeddings: VertexAIEmbeddings ) -> DocArrayInMemorySearch:
        db = DocArrayInMemorySearch.from_documents(
            inputList, 
            vertex_embeddings
        )
        return db
    
    def getRelevantContext(query: str ,db:DocArrayInMemorySearch) -> str:
        # query = "how does deferred Giveaway works for offer"
        # query = "how do I create a Promise Callout Offer"
        # query = "how do I create a Basket Offer"
        # query = "What is insufficient participation ?"
        # query = "What is Either or Offer ?"
        # query = """I am from lifestyle Business unit, I want to create an /
        # offer for increaisng units per order. How do I do that?"""

        relevantDocs = db.max_marginal_relevance_search(query, k=7)
        # relevantDocs = db.similarity_search(query, k=10)

        # print(len(relevantDocs))
        # print(relevantDocs)

        qdocs = "".join([relevantDocs[i].page_content for i in range(len(relevantDocs))])
        # print(qdocs)
        # for i in range(0,len(qdocs)-2):
        #     print(relevantDocs[i])
        #     relevantDocs[i].page_content
        #     print(item, "======\n\n\n")
        
        return qdocs