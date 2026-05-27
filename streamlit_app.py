import streamlit as st
from groq import Groq
import base64

st.set_page_config(page_title="JYNXIQ", page_icon="🚀", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap');
* { font-family: 'Rajdhani', sans-serif; }
.stApp { background: radial-gradient(ellipse at top, #0d0221 0%, #000000 50%, #0a0a2e 100%); color: white; }
.main-title { font-family: 'Orbitron', monospace !important; text-align: center; font-size: 2.2em; font-weight: 900; background: linear-gradient(90deg, #00d4ff, #7b2fff, #00d4ff); background-size: 200%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; padding: 15px 0 5px 0; letter-spacing: 3px; }
.subtitle { text-align: center; color: #7b8ab8; font-size: 1em; letter-spacing: 2px; margin-bottom: 5px; }
.pill { display: inline-block; background: rgba(0,212,255,0.08); border: 1px solid rgba(0,212,255,0.3); border-radius: 20px; padding: 4px 14px; font-size: 0.85em; color: #00d4ff; margin: 3px; }
.divider { height: 1px; background: linear-gradient(90deg, transparent, #00d4ff44, #7b2fff44, transparent); margin: 15px 0; }
.user-bubble { background: linear-gradient(135deg, #00d4ff22, #0066cc33); border: 1px solid #00d4ff55; color: #ffffff; padding: 14px 18px; border-radius: 20px 20px 4px 20px; margin: 10px 0; margin-left: 15%; box-shadow: 0 0 20px #00d4ff22; font-size: 1.05em; }
.assistant-bubble { background: linear-gradient(135deg, #7b2fff11, #0d0221cc); border: 1px solid #7b2fff44; color: #ffffff; padding: 14px 18px; border-radius: 20px 20px 20px 4px; margin: 10px 0; margin-right: 15%; box-shadow: 0 0 20px #7b2fff22; line-height: 1.7; font-size: 1.05em; }
.welcome-box { background: linear-gradient(135deg, #0d022188, #0a0a2e88); border: 1px solid #00d4ff33; border-radius: 20px; padding: 20px 25px; margin: 10px 0; }
.stTextInput > div > div > input { background: rgba(0,212,255,0.08) !important; color: #ffffff !important; border: 1px solid #00d4ff66 !important; border-radius: 15px !important; font-size: 1.05em !important; padding: 12px 16px !important; }
.stTextInput > div > div > input::placeholder { color: #7799aa !important; font-style: italic; }
.stButton > button { background: linear-gradient(135deg, #00d4ff, #7b2fff) !important; color: white !important; font-weight: bold !important; border-radius: 15px !important; border: none !important; box-shadow: 0 0 20px #00d4ff44 !important; font-size: 1.2em !important; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #0d0221, #0a0a2e) !important; border-right: 1px solid #00d4ff22 !important; }
[data-testid="stSidebar"] p, [data-testid="stSidebar"] label { color: #aabbdd !important; }
.footer { text-align: center; color: #2a3a5a; font-size: 0.8em; letter-spacing: 2px; padding: 10px; }
.voice-box { background: rgba(123,47,255,0.08); border: 2px dashed #7b2fff44; border-radius: 15px; padding: 15px; margin: 10px 0; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Voice input JavaScript
st.markdown("""
<script>
function startVoice() {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        alert('Voice not supported in this browser. Try Chrome!');
        return;
    }
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-IN';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    
    document.getElementById('voiceBtn').innerHTML = '🔴 Listening...';
    document.getElementById('voiceBtn').style.background = 'red';
    
    recognition.start();
    
    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        document.getElementById('voiceBtn').innerHTML = '🎤 Voice Input';
        document.getElementById('voiceBtn').style.background = '';
        
        const inputs = window.parent.document.querySelectorAll('input[type=text]');
        if (inputs.length > 0) {
            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            nativeInputValueSetter.call(inputs[0], text);
            inputs[0].dispatchEvent(new Event('input', { bubbles: true }));
        }
    };
    
    recognition.onerror = function(event) {
        document.getElementById('voiceBtn').innerHTML = '🎤 Voice Input';
        document.getElementById('voiceBtn').style.background = '';
        alert('Error: ' + event.error + '. Make sure microphone is allowed!');
    };
    
    recognition.onend = function() {
        document.getElementById('voiceBtn').innerHTML = '🎤 Voice Input';
    };
}
</script>

<div style="text-align:center; margin: 10px 0;">
<button id="voiceBtn" onclick="startVoice()" style="
    background: linear-gradient(135deg, #7b2fff, #00d4ff);
    color: white;
    border: none;
    padding: 12px 25px;
    border-radius: 15px;
    font-size: 1em;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 0 20px #7b2fff44;
    font-family: Rajdhani, sans-serif;
    letter-spacing: 1px;
">🎤 Voice Input</button>
<div style="color:#445577; font-size:0.8em; margin-top:5px;">Click and speak your question in English or Telugu</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">⚡ JYNXIQ</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">I N T E L L I G E N T   L E A R N I N G   A I</div>', unsafe_allow_html=True)
st.markdown('''<div style="text-align:center; margin:10px 0 20px 0;">
<span class="pill">⚡ JEE/IIT</span>
<span class="pill">🧪 NEET/MBBS</span>
<span class="pill">📐 MPC</span>
<span class="pill">🏛️ UPSC</span>
<span class="pill">📚 INTER</span>
<span class="pill">🎤 VOICE</span>
<span class="pill">🖼️ IMAGE</span>
</div>''', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ⚡ JYNXIQ")
    st.markdown("Intelligent Learning AI")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown("### 📚 TRY ASKING")
    st.markdown("• Explain Newton's laws")
    st.markdown("• UPSC current affairs")
    st.markdown("• NEET biology tips")
    st.markdown("• IIT JEE maths tricks")
    st.markdown("• 🎤 Speak your question!")
    st.markdown("• 📸 Upload question photo!")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    subject = st.selectbox("📖 Select Subject Mode", [
        "🎯 General (All Subjects)",
        "⚡ Physics",
        "🧪 Chemistry",
        "📐 Maths",
        "🌿 Biology/NEET",
        "🏛️ UPSC/History",
        "💻 Computer Science",
    ])
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.image_data = None
        st.rerun()
    st.markdown("🚀 Powered by Groq AI")
    st.markdown("✅ Free Forever")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "image_data" not in st.session_state:
    st.session_state.image_data = None

if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="welcome-box">
        <div style="color:#00d4ff; font-size:1.3em; font-weight:bold;">👋 NAMASTE! WELCOME TO JYNXIQ</div>
        <div style="color:#aabbdd; margin:8px 0;">Your Intelligent Learning AI for ALL exams!</div>
        <br>
        <div style="color:#ffffff;">⚡ <b>JEE/IIT</b> — Maths, Physics, Chemistry</div>
        <div style="color:#ffffff;">🧪 <b>NEET/MBBS</b> — Biology, Chemistry, Physics</div>
        <div style="color:#ffffff;">🏛️ <b>UPSC</b> — History, Polity, Geography, Economy</div>
        <div style="color:#ffffff;">📚 <b>Inter Board</b> — MPC, BiPC, All Subjects</div>
        <div style="color:#ffffff;">🎤 <b>Voice Input</b> — Speak your question!</div>
        <div style="color:#ffffff;">🖼️ <b>Image Q&A</b> — Upload photo of question!</div>
        <br>
        <div style="color:#7799aa; font-size:0.9em;">✦ Ask in English or Telugu ✦ Voice & Image supported ✦</div>
    </div>
    """, unsafe_allow_html=True)

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown('<div class="user-bubble">🧑‍🎓 ' + message["content"] + '</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="assistant-bubble">🤖 ' + message["content"] + '</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div style="color:#00d4ff; font-size:1em; margin:5px 0;">📸 Upload Question Image (Optional)</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg","jpeg","png"], label_visibility="collapsed")

if uploaded_file:
    st.image(uploaded_file, caption="Your Question", width=300)
    image_bytes = uploaded_file.read()
    st.session_state.image_data = base64.b64encode(image_bytes).decode('utf-8')
    st.success("✅ Image uploaded! Now click Send 🚀")

col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input("", placeholder="✦ Type or use 🎤 Voice above...", label_visibility="collapsed")
with col2:
    send_button = st.button("🚀")

if send_button and (user_input or st.session_state.image_data):
    question = user_input if user_input else "Please solve this question from the image"
    st.session_state.messages.append({"role": "user", "content": question})
    st.markdown('<div class="user-bubble">🧑‍🎓 ' + question + '</div>', unsafe_allow_html=True)
    with st.spinner("⚡ JYNXIQ Thinking..."):
        try:
            client = Groq(api_key=API_KEY)
            system_prompt = f"""You are JYNXIQ, an intelligent learning AI for Indian students.
Current subject mode: {subject}
Help with JEE, NEET, UPSC, Inter Board and all subjects.
Give clear step by step explanations.
Use simple English. If asked in Telugu, reply in Telugu mixed English.
If an image is provided, carefully read and solve the question in the image.
Always encourage the student!"""

            if st.session_state.image_data:
                api_messages = [{"role": "user", "content": [
                    {"type": "text", "text": system_prompt + "\n\n" + question},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{st.session_state.image_data}"}}
                ]}]
                response = client.chat.completions.create(
                    model="llama-3.2-11b-vision-preview",
                    messages=api_messages,
                    max_tokens=1500
                )
                st.session_state.image_data = None
            else:
                messages = [{"role": "system", "content": system_prompt}]
                for m in st.session_state.messages:
                    messages.append({"role": m["role"], "content": m["content"]})
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    max_tokens=1500
                )

            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.markdown('<div class="assistant-bubble">🤖 ' + reply + '</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error("❌ Error: " + str(e))

elif send_button:
    st.warning("Please type a question or upload an image first!")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">✦ JYNXIQ ✦ VOICE & IMAGE AI ✦ FREE FOREVER ✦ MADE FOR INDIAN STUDENTS 🇮🇳 ✦</div>', unsafe_allow_html=True)
