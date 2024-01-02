


## Pycharm
- already had a project in venv
- just opened my project 
- after opening 
	- cmd + , -> Project:env ->Python Interpreter -> Add interpreter -> Add local interpreer -> existing -> select python in your venv


============
https://github.com/Vision-CAIR/MiniGPT-4
Teams FK https://docs.google.com/spreadsheets/d/1a9Vm7JQoMOTIyv1MFhuUcyZGlVb5SZ4w2uqVT0s-7bo/edit#gid=291791168


### cleanup
https://cloud.google.com/vertex-ai/docs/predictions/get-predictions
https://cloud.google.com/vertex-ai/docs/training-overview
https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide
https://towardsdatascience.com/developing-and-deploying-a-machine-learning-model-on-vertex-ai-using-python-865b535814f8
https://github.com/GoogleCloudPlatform/llm-pipeline-examples
https://towardsdatascience.com/giving-vertex-ai-the-new-unified-ml-platform-on-google-cloud-a-spin-35e0f3852f25
https://betterprogramming.pub/a-step-by-step-guide-to-train-a-model-on-google-clouds-vertex-ai-47faafae1330
https://www.cloudskillsboost.google/focuses/63251?catalog_rank=%7B%22rank%22%3A2%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=24315832
https://www.steamship.com/learn/agent-guidebook

https://confluence.fkinternal.com/display/CLOUDOPS/GCP+Platform+FAQ#GCPPlatformFAQ-SelfSignedcertificateErrors
https://docs.google.com/document/d/176GyOlP9PksW-LDN1_Ps29doIFlOgwqacYs3dt4SiHw/edit?resourcekey=0-yE7mRKxNOmR2t-6Itlq47w
https://platform.openai.com/docs/guides/gpt/chat-completions-api
https://platform.openai.com/docs/api-reference/fine-tunes/create
https://api.python.langchain.com/en/latest/modules/embeddings.html

##story
https://writingatlas.com/author/author--haruki-murakami

========
gcloud auth application-default login

printenv

openssl version

source env/bin/activate

https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
https://mljar.com/blog/install-jupyter-notebook/
https://www.codingforentrepreneurs.com/blog/install-jupyter-notebooks-virtualenv/


https://www.jetbrains.com/pycharm/download/#section=mac

./google-cloud-sdk/bin/gcloud init


brew uninstall python

python3 -m certifi



### To open jupyter UI
- cd to a folder where u want to store jupyter files
-  run `jupyter-lab`


###
!pip3 install openai
pip3 install dotenv

- upgrade pip
- `python3.11 -m pip install --upgrade pip`

- run `!pip3 install python-dotenv` in jupyter notebook itself

- getting key - https://help.socialintents.com/article/188-how-to-find-your-openai-api-key-for-chatgpt
    - update key in ../JupyteNotes/.env
========
## installing jupyter notebook
- brew install jupyter
	- took around 15 min to finish

- to run the server
	- `jupyter-lab`

- to find the installation path 
	- `which jupyter` 
		-  `/usr/local/bin/jupyter`

- verison
	- `jupyter --version`
		- return slist of dependency and its version



/Library/Frameworks/Python.framework/Versions/3.7/

Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python@3.11/libexec/bin

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.11/site-packages
