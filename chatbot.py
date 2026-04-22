# chatbot.py
import streamlit as st
import google.generativeai as genai

def app():
    st.title('Chat with our AI ✨', anchor=False)
    st.subheader('Ask me anything about your university tasks, courses, or general knowledge.')

    # حط الـ API Key بتاعك هنا
    api_key = "AIzaSyCiILuTxniyRx6t942rFYomsaABIduVoU8" 
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-3.1-flash-lite-preview')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض الرسائل السابقة
    for message in st.session_state.messages:
        # بنحول 'model' لـ 'ai' عشان أيقونة Streamlit تظهر صح
        display_role = "ai" if message["role"] == "model" else "user"
        with st.chat_message(display_role):
            st.markdown(message["content"])

    prompt = st.chat_input('Enter your question...', accept_audio=False)

    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        # حفظ رسالة المستخدم بصيغة متوافقة مع Gemini
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("ai"):
            with st.spinner("Generating... ✨"):
                try:
                    # تمرير الهيستوري لـ Gemini (هياخد user و model بس بدون مشاكل)
                    history = [{"role": m["role"], "parts": [m["content"]]} for m in st.session_state.messages[:-1]]
                    chat = model.start_chat(history=history)
                    
                    response = chat.send_message(prompt)
                    st.markdown(response.text)
                    
                    # حفظ رد الموديل بصيغة متوافقة مع Gemini
                    st.session_state.messages.append({"role": "model", "content": response.text})
                except Exception as e:
                    st.error(f"Error: {e}")