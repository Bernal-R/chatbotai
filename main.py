#pip install PyPDF2
#pip install openai
#pip install streamlit==1.14.0

from io import StringIO
import streamlit as st
import openai
import PyPDF2 

openai.api_key = "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"

document_list3 = []
docs = []

def procesar(txt):
    
    if txt != "":
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=st.session_state.doc+"\n\nQ:"+ txt + "\nA:",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        st.write('AI:', response.choices[0].text)
    else:
        st.write('AI:', "")

#----------------- UI -----------------
st.title('Chatbot powered by GPT-3')
tab1, tab2 = st.tabs(["Consultar AI", "Cargar Archivos"])

with tab1:
    st.header("Consultar AI")
    option = st.selectbox('Seleccione tipo de documento',('Ley', 'Test2', 'Test 3'))
    st.write('Usuario:')
    txt = st.text_area('Ingrese su consulta:')

    procesar(txt)
    
#Cargar archivo
with tab2:
   st.header("Cargar Archivos")
   uploaded_file = st.file_uploader("Seleccione su archivo")
   
   if uploaded_file is not None:
    pdfReader = PyPDF2.PdfFileReader(uploaded_file) 
    
    for page in range(1,pdfReader.numPages):
        pageObj = pdfReader.getPage(page) 
        document_list3.append(pageObj.extractText())
    
    st.session_state['doc'] = "".join(document_list3)


