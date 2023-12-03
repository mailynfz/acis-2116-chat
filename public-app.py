from openai import OpenAI
import streamlit as st
import time
from PIL import Image
import re

# Configure the logo filepath
logo_filepath = "C:\\Users\\mfdez\\Dropbox\\Active Projects\\007 GPTs\\ACIS 2116 TA\\Vertical_VT_Full_Color_RGB.png"

# Configure site title, icon, and other
site_title = "ACIS 2116 TA Chat"
site_icon = ":nerd_face:"

# Set the page title, description, and other text
page_title = "ACIS 2116 - Principles of Managerial Accounting Chat"
description = "A GPT4-powered chat assistant to answer your questions about ACIS 2116 at Virginia Tech's Pamplin School of Business"
instructions = 'Ask me anything about your managerial accounting class. I am trained on your class materials, and can answer questions from your class syllabus, course lectures, and more.'
chat_box_text = 'Click on the Start a New Chat button in the left sidebar to get started. Then, type your question here.'
footer_text = "Made with 🧡 by Mailyn 😊"


# Set up the Streamlit page with a title and icon
st.set_page_config(page_title= site_title, page_icon= site_icon)

# Main chat interface setup
st.markdown(f"<h1 style='color: rgba(134, 31, 65, 1);'>{page_title}</h1>", unsafe_allow_html=True)
st.caption(description)

st.write(instructions)


# Display the image in the sidebar
image = Image.open(logo_filepath)
st.sidebar.image(image)


if "THREAD_ID" not in st.session_state:
    st.session_state.THREAD_ID = None

if "messages" not in st.session_state:
    st.session_state.messages = []


# Create a sidebar for API key configuration and additional features
st.sidebar.divider()

feedback_text = "This app is a work-in-process. Please help improve it and share your feedback [here](https://forms.gle/3DfPAG86RyepVXMo8)."

st.sidebar.markdown(feedback_text)

st.sidebar.divider()


other_text_line_1 = "To get started, click on the 'Start a New Chat' button below. Then, type your question in the chat box to the right." 

other_text_line_2 = "I have prepaid some credits for everyone to use this bot for free. To continue using this bot after those credits are used up, you can [create your own API key](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/) and enter it below. You don't have to be a ChatGPT Plus subscriber to create an API key. If I'm not mistaken, new users get some free API credits that you can use to chat with this bot." 

other_text_line_3 = "The cost per user should be relatively inexpensive. This app uses the gpt-4-1106-preview model, which costs \$0.01/1K tokens for input and \$0.03/1K tokens for output (response). For reference, 1K tokens is equivalent to approximately 750 words. In addition to your prompt, the app will take as input any information it retrieves from its knowledge base (i.e., the lecture notes I uploaded). To retain context, the app will also resubmit the entire conversation (i.e., thread), which increases the number of input tokens per prompt. Learn more about [OpenAI's pricing here](https://openai.com/pricing)."

other_text_line_4 = "You can help extend the budget for this app by starting a new chat when you want to ask about a new topic by clicking the 'Start New Chat' button again. That will clear the chat box and start a new thread on the API. Also, if you can afford to do so, please consider paying for your usage by using your own API key."

st.sidebar.markdown(other_text_line_1)

if st.sidebar.button("Start New Chat"):
    thread = client.beta.threads.create()
    st.session_state.THREAD_ID = thread.id
    st.sidebar.write("Thread ID: ", thread.id)
    st.session_state.messages = []

st.sidebar.markdown(other_text_line_2)
st.sidebar.markdown(other_text_line_4)

# Set OpenAI contants 
if st.secrets:
    if 'ASSISTANT_ID' in st.secrets:
        ASSISTANT_ID = st.secrets['ASSISTANT_ID']

    if 'OPENAI_API_KEY' in st.secrets:
        OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")
if api_key:
    client = OpenAI(api_key=api_key)
else:    
    client = OpenAI(api_key=OPENAI_API_KEY)

st.sidebar.markdown(other_text_line_3)



st.markdown("""
    <style>
    .element-container .stTextInput input::placeholder {
        color: #E5751F; 
    }
    .element-container .stTextInput input {
        color: black; 
    }
    </style>
    """, unsafe_allow_html=True)



# Display existing messages in the chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input for the user
if prompt := st.chat_input(chat_box_text):
    if st.session_state.THREAD_ID is None:
        st.write("Please click on the Start a New Chat button in the left sidebar to get started.")
    else:
        format_prompt = prompt.replace("$", "\\$")
        # Add user message to the state and display it
        st.session_state.messages.append({"role": "user", "content": format_prompt})
        with st.chat_message("user"):
            st.write(str(format_prompt))

        # Add the user's message to the existing thread
        client.beta.threads.messages.create(
            thread_id = st.session_state.THREAD_ID,
            role="user",
            content=prompt
        )

        # Create a run with additional instructions
        run = client.beta.threads.runs.create(
            thread_id = st.session_state.THREAD_ID,
            assistant_id=ASSISTANT_ID
        )

        # Poll for the run to complete and retrieve the assistant's messages
        while run.status != 'completed':
            time.sleep(.5)
            run = client.beta.threads.runs.retrieve(
                thread_id = st.session_state.THREAD_ID,
                run_id=run.id
            )

        # Retrieve messages added by the assistant
        messages = client.beta.threads.messages.list(
            thread_id =  st.session_state.THREAD_ID, 
            order="asc"
        )

        # Process and display assistant messages
        assistant_messages_for_run = [
            message for message in messages 
            if message.run_id == run.id and message.role == "assistant"
        ]
        for message in assistant_messages_for_run:
            response = message.content[0].text.value
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(f"{response}", unsafe_allow_html=True)
                st.write("Session State Thread ID: ", st.session_state.THREAD_ID)




def footer(text):
    footer_html = f"""
    <style>
    .footer {{
        position: fixed;
        left: 10;
        bottom: 0;
        width: 100%;
        background-color: rgba(241, 241, 241, 0);
        color: rgba(117, 120, 123, 1);
        text-align: left;
    }}
    </style>
    <div class='footer'>
        <p>{text}</p>
    </div>
    """
    st.sidebar.markdown(footer_html, unsafe_allow_html=True)

footer(footer_text)

