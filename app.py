import streamlit as st
import google.generativeai as genai

# पन्ने का सेटअप
st.set_page_config(page_title="Royal AI Agent", page_icon="👑")

st.title("Royal AI Agent 👑")

# साइडबार में चाबी मांगने का सिस्टम - अब यह सबके लिए है
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("नमस्ते! अपनी Gemini API Key यहाँ डालें:", type="password")
    st.info("ऐप को सक्रिय करने के लिए कृपया अपनी Google API Key दर्ज करें।")

if api_key:
    # Google AI सेटअप
    genai.configure(api_key=api_key)
    
    # नया मॉडल (Gemini 1.5 Flash)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # चैट का इतिहास सुरक्षित रखने के लिए
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # पहला स्वागत संदेश जो सबको दिखेगा
        st.session_state.messages.append({"role": "assistant", "content": "नमस्ते! मैं आपका Royal AI Agent हूँ। मैं आपकी क्या मदद कर सकता हूँ?"})

    # मैसेज दिखाने के लिए
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # नया मैसेज लिखने की जगह
    if prompt := st.chat_input("मुझसे कुछ भी पूछें..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI से जवाब मंगाना
        with st.chat_message("assistant"):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"ओह! कुछ दिक्कत आ गई: {e}")
else:
    # मुख्य स्क्रीन पर स्वागत संदेश (बिना नाम के)
    st.warning("नमस्ते! इस रॉयल एजेंट से बात करने के लिए कृपया साइडबार में अपनी API Key डालें।")
        
