import requests
import streamlit as st

api_key = "NsqkRzfFW8LWWdvbWEefF2q5sIalRq1tkXdi6lw3"
url = "https://api.nasa.gov/planetary/apod?" \
    f"api_key={api_key}"

response1 = requests.get(url)
data = response1.json()

title = data["title"]
description = data["explanation"]
img_url = data["url"]

image_filepath = "img.png"
response2 = requests.get(img_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(description)