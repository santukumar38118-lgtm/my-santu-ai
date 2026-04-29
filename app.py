import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Santu AI Agent", page_icon="🤖")
st.title("Santu AI Agent 🚀")

# API Key डालने का सुरक्षित बॉक्स
api_key = st.sidebar.text_input("अपनी API Key यहाँ डालें:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    user_input = st.text_input("मुझसे कुछ भी पूछें:")
    if user_input:
        response = model.generate_content(user_input)
        st.write("AI का जवाब:", response.text)
else:
    st.info("नमस्ते संतु भाई! ऐप चलाने के लिए साइड में अपनी API Key पेस्ट करें।")
      
