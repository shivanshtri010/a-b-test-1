import streamlit as st
import os
import google.generativeai as genai
from PIL import Image



# Configure the Gemini API
genai.configure(api_key="AIzaSyAVdMsVX_vqD03IzE0c92dGrG4BSNrq6RU")

def get_gemini_response(prompt, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me the total calories")

default_prompt = """
You are an expert in solving aptitude, coding, data analytics, and interview questions. An image will be shared with the question in it, and you have to provide the answer as fast as possible without showing the steps for solving the question.
"""

# If the submit button is clicked
if submit:
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(default_prompt, image_data)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.error("Please provide an input prompt and upload an image.")
