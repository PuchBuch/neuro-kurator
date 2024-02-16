import streamlit as st
from function import *
import os

def main():

    st.title("Ассистент знаний на основе загруженных фаилов Pdf+ChatGPT ")

    uploaded_file = st.file_uploader("Выбрать PDF фаил для загрузки", type="pdf")
    if uploaded_file is not None:
        if st.button("Читать PDF"):
            save_uploaded_file(uploaded_file)
            st.write("Пожалуйста подождите, чтение фаила PDF.")

            update_assistant_knowledgebase(uploaded_file.name)
            st.write("PDF готов! Теперь вы можете задавать вопросы")
            
            os.remove(uploaded_file.name)
    user_input = st.text_input("Введите ваш вопрос:")

    if st.button("Отправить"):
        st.write("Вы:", user_input)
        response = get_assistant_response(user_input)
        st.write("Бот: "+response)

if __name__ == "__main__":
    main()
