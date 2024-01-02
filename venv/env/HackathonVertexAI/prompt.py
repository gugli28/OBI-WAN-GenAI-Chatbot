
from langchain import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

class Promptt ():
    def getPrompt(qdocs: str,query:str) -> str:
        role = """
        You are offer related query answering module for promotions platform on Flipkart.\
        You answer questions with a high degree of precision & wherever you do not have enough precision, \
        you always provide an output saying the answers might not be fully correct. \
        Promotions Platform has capabilities to create and maintain an offer via its \
        offer creation console- 'Grumbles' and maintenance console-- 'Casper'. Business users\
        can ask multiple questions related to capabilities for creating and maintaining an offer.
        """

        prompt = f""" 
        Role: {role}
        Follow exactly these 3 steps:
        1. Read the context below and aggregrate this data
        Context : {qdocs}
        2. Answer the question using only this context
        3. Show the source for your answers
        User Question: {query}

        If you don't have any context and are unsure of the answer, reply that you don't know about this topic.

        """
        print(len(prompt))

        return prompt
    
    def getmapReducePrompt(context: str, question:str):
        # question = "What is Insufficient Participation?"
        question_prompt_template = """
                            Answer the question as precise as possible using the provided context. \n\n
                            Context: \n {context} \n
                            Question: \n {question} \n
                            Answer:
                            """
        # question_prompt = PromptTemplate(
        #     template=question_prompt_template, input_variables=["context", "question"]
        # )

        question_prompt = PromptTemplate(
            template=question_prompt_template, 
            input_variables=["question", "context"]
        )

        # summaries is required. a bit confusing.
        combine_prompt_template = """Given the extracted content and the question, create a final answer.
        If the answer is not contained in the context, say "answer not available in context. \n\n
        Summaries: \n {summaries}?\n
        Question: \n {question} \n
        Answer:
        """
        
        combine_prompt = PromptTemplate(template=combine_prompt_template, input_variables=[ "summaries","question"])

        
