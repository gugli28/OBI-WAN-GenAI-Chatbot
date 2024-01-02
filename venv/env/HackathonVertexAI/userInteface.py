import os
import openai
import gradio
from langchain.vectorstores import DocArrayInMemorySearch
from Embeddingg import createVectorStore
from CommonVar import Mainfnn
from prompt import Promptt
from callVectorAI import TintinAI

class GraphicalInterFace():


    def message_and_history(input, history):
        relevantContext = createVectorStore.getRelevantContext(input, Mainfnn.db)
        print("+++++++++++===================", len(relevantContext))
        myPrompt = Promptt.getPrompt(relevantContext,input)
        history = history or []
        s = list(sum(history, ()))
        # s = []
        s.append(myPrompt)
        inp = ' '.join(s)
        output = TintinAI.getResponse(inp)
        history.append((input, output))
        return history, history
 