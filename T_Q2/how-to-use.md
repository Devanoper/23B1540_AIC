## Dependencies
install these dependencies using pip
* langchain
* pinecone-client
* streamlit
* langchain-pinecone
* langchain-community
* sentence-transformers
* **OR** : download requirements.txt file and run command 'pip install -r requirements.txt'
  
## API keys
* make account on Huggingfaces and generate token , replace HUGGINGFACE API KEY with your token in ragchatbot.py
* make account on pinecone and replace the api key PINECONE API key with your key in ragchatbot.py

## custom use
* replace the context prompt with your prompt in ragchatbot , by default it is an academic councillor
* replace the contents of ugrulebook.txt with your txt contents , alternatively change the txt file entirely and replace the file path in ragchatbot.py
* replace titles in runner.py , currently they are acadmeic councillor

## final run
* in the command terminal of the T_Q2 directory , write 'streamlit run runner.py' , the chatot should open in your default browser
NOTE : It may take 1-2 mins if your txt file is large , as in the case of ugrulebook

