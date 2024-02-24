import openai
import os
from os.path import join, dirname
from dotenv import load_dotenv
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("MYTESTKEY")
PERSIST_DIR = "./storage"
openai.api_key = SECRET_KEY



# check if storage already exists
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("sample_data/data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# either way we can now query the index
query_engine = index.as_query_engine()
response = query_engine.query("What is summary of the content?")
print(response)
response = query_engine.query("When did Laxman Joined Infosys")
print(response)
response3 = query_engine.query("What is Laxman's Linked URL , Email Id and Phone number")
print(response3)
