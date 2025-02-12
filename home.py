import streamlit as st
import pymongo
import openai

mongo_uri = st.secrets["MONGOURI"]

client = pymongo.MongoClient(mongo_uri)
db=client['valentine_tech']
collection = db["responses"]

# Sam Maltman needs to see my valentine's stuff
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Custom CSS for styling
# I hate doing frontend but hey, valentine's stuff should be cute right?
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #FCE4EC;
        }
        .title {
            text-align: center;
            color: #E91E63;
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .question-box {
            background: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        .submit-button {
            background-color: #E91E63 !important;
            color: white !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
            width: 100%;
        }
        .valen-img {
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💖 Hacker Spirit + Valentines Recommendation 💖</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://image.freepik.com/free-vector/hand-drawn-valentine-s-day-penguins-couple_23-2148390371.jpg" width="400" class="valen-img">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### Fill the questions below to get your techie match 💻")

favorite_coffee = st.text_input("What's your go-to coffee shop drink?", placeholder="e.g., Latte, Cappuccino", key="coffee", help="Enter your favorite coffee shop drink")
favorite_keycap = st.text_input("Which keycap type makes your heart sing?", placeholder="e.g., Cherry MX Blue, Gateron Red", key="keycap", help="Enter your favorite keycap type")
programming_language = st.text_input("Which programming language do you love the most?", placeholder="e.g., Python, JavaScript", key="language", help="Enter your favorite programming language")
text_editor = st.text_input("What's your favorite code editor for sweet coding sessions?", placeholder="e.g., VS Code, Sublime Text", key="editor", help="Enter your favorite code editor")
favorite_snack = st.text_input("What's your favorite snack to munch on while coding?", placeholder="e.g., Chocolate, Chips", key="snack", help="Enter your favorite snack")
favorite_browser = st.text_input("Which browser do you adore for surfing the web?", placeholder="e.g., Chrome, Firefox", key="browser", help="Enter your favorite browser")

# Custom CSS for input box size
st.markdown("""
    <style>
        .stTextInput > div > div > input {
            height: 50px;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

if st.button("Submit"):
    # recommendation function
    st.success("Match has been found yei!")
else:
    st.warning("Please fill all of the question blanks")


