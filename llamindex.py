import openai
import os
import streamlit as st

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("OPENAI_API_KEY")
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,ServiceContext
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core import PromptTemplate
openai.api_key = SECRET_KEY
documents = SimpleDirectoryReader("sample_data/data").load_data()
service_context = ServiceContext.from_defaults(chunk_size=1000)

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(streaming=True)
input1=st.text_input("Input1", "What is summary of the content?")
input2=st.text_input("Input2", "When did Laxman Joined Infosys")
input3=st.text_input("Input3","What is Laxman's Linked URL , Email Id and Phone number")

response = query_engine.query(input1)
st.text_area("Response",response)
response1 = query_engine.query(input2)
st.text_area("Response1",response1)
response3 = query_engine.query(input3)
st.text_area("Response3",response3)
