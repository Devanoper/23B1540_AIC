import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings

class ChatBot():
    os.environ['PINECONE_API_KEY'] = 'ca849d1c-4b47-41d5-a2b1-569bd8f538e9'
    os.environ['HUGGINGFACE_API_KEY'] = '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'
    loader = TextLoader("ugrulebook.txt", encoding = 'UTF-8')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=4000, chunk_overlap=4)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings()
    from langchain.vectorstores import Pinecone
    import pinecone

    from pinecone import Pinecone, ServerlessSpec
    from langchain_pinecone import PineconeVectorStore

    pc = Pinecone(
            api_key=os.environ.get("PINECONE_API_KEY")
        )

    # Define Index Name
    index_name = "myindex3"

    # Checking Index
    if 'myindex3' not in pc.list_indexes().names():
        docsearch= pc.create_index(
            name='myindex3',
                dimension=1536,
                metric='euclidean',
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-east-1'
                )
            )
        docsearch = PineconeVectorStore.from_documents(docs, embedding=embeddings, index_name=index_name)

    else:
      # Link to the existing index
      docsearch = PineconeVectorStore.from_documents(docs, embedding=embeddings, index_name=index_name)
    from langchain.llms import HuggingFaceHub

    # Define the repo ID and connect to Mixtral model on Huggingface
    repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    llm = HuggingFaceHub(
      repo_id=repo_id,
      model_kwargs={"temperature": 0.8, "top_k": 50},
      huggingfacehub_api_token=os.getenv('HUGGINGFACE_API_KEY')
    )
    from langchain import PromptTemplate

    template = """
    You are an academic councillor . The user will ask you queries about academic infrastructure or academic
    policies. Answer in a formal way and keep it precise
    
    Context: {context}
    Question: {question}
    Answer: 
    
    """

    prompt = PromptTemplate(
      template=template,
      input_variables=["context", "question"]
    )
    from langchain.schema.runnable import RunnablePassthrough
    from langchain.schema.output_parser import StrOutputParser

    rag_chain = (
      {"context": docsearch.as_retriever(),  "question": RunnablePassthrough()}
      | prompt
      | llm
      | StrOutputParser()
    )
    rag_chain = (
        {"context": docsearch.as_retriever(),  "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
      )