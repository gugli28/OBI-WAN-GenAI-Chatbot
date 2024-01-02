
import pathlib
from langchain.document_loaders import PyPDFLoader
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

class LoadPDFs():
    def loadPdfDocuments(self, folderPath) -> List[Any]:
        desktop = pathlib.Path(folderPath)
        pages1 = []
        for item in list(desktop.iterdir()):
            try:
                print(str(item))
                fileLoader = PyPDFLoader(str(item))
                pages1.append(fileLoader.load_and_split())
            except:
                print("An exception occurred while reading Documemets")

        print("Document Loading done!!")
        return self.appendPageContent(pages1)
        
    

    def appendPageContent(self, input_list: List[Any]) -> List[Any] :
        pages = []
        print(len(input_list))
        for item in input_list:
            try:
                if(item.page_content):
                    pages.append(item)
                    print(item)
            except:
                for item2 in item:
                    pages.append(item2)
        print(len(pages))
        return pages
        