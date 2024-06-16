import streamlit as st 
from langchain import HuggingFaceHub, PromptTemplate,LLMChain
llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b-instruct',
                        huggingfacehub_api_token = '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',
                        model_kwargs = {'temperature':0.5,'max_new_tokens':500})
template = '''Give the list of 3 books to study{topic}'''
prompt = PromptTemplate(template = template,input_variables = ['topic'])
chain = LLMChain(llm = llm,prompt = prompt)
st.title("Book Recommendation App")
topic = st.text_input('Enter Topic: ')

if st.button('submit'):
    result = chain.run(topic)
    st.write(result)
    
    
    
    
    