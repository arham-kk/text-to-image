import openai
import PIL.Image
import urllib.request
import gradio as gr

def generate_image(prompt_data):
    openai.api_key = 'ENTER OPENAI KEY'
    response = openai.Image.create(prompt=prompt_data, n=1, size="1024x1024")
    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, "new.jpeg")
    img = PIL.Image.open("new.jpeg")
    return img

iface = gr.Interface(fn=generate_image, inputs="text", outputs="image", title="Text to Image Generator")
iface.launch()
