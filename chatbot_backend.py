from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.prompts import PromptTemplate

# Load model and tokenizer
model_id = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

# HuggingFace pipeline
pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=768,        
    temperature=0.7,           
    top_p=0.95,
    repetition_penalty=1.3    # Reducing repetitive responses
)

llm = HuggingFacePipeline(pipeline=pipe)

# Load embedding model and vector store
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

retriever = vectordb.as_retriever(search_kwargs={"k": 5})  # Fetch top 5 chunks for better context

#  Defining a custom prompt to guide LLM response style
prompt_template = PromptTemplate.from_template(
    """You are an insurance assistant helping users understand insurance policies.
Use the following context to answer the question in a helpful, complete, and detailed manner. 
Answer in **at least 50 words**. If the context includes multiple details, explain them all in the response. 
If you don’t know the answer, just say "I don’t know" — don’t try to make one up.
Avoid repeating the same sentence or phrase.

Context:
{context}

Question: {question}
Answer (in detailed, clear explanation):"""
)

# Use RetrievalQA with the prompt
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template},
    return_source_documents=True  # Helps debugging and showing the source of the answer
)

# Function to handle a user query
def get_bot_response(query):
    result = qa_chain(query)
    return result["result"]
