# Onde estarão todas as funções deste pacote
# Ele é quem vai cooderndar este pacote (gerenciador)
from carbonmail.utils import root_folder
import urllib
import json
import os
import requests

def extract_code(code_path):
    with open(code_path, encoding='utf-8') as code_file:
        code = code_file.read()

    code_encoded = urllib.parse.quote(code)

    return code_encoded

def prepare_payload(code_path):
    json_path = os.path.join(root_folder(), "config.json")

    with open(json_path) as json_file:
        payload = json.load(json_file)

    payload["code"] = extract_code(code_path)
    
    return payload


def download_image(code_path):
    api_url = "https://carbonara.vercel.app/api/cook" # <- meu link do heroko, que n tenho ainda
    payload = prepare_payload(code_path)

    image_folder = os.path.join(root_folder(), "images")

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    
    image_name = os.path.basename(code_path)
    image_name = os.path.splitext(image_name)[0]
    image_path = os.path.join(image_folder, f"{image_name}.png")

    response = requests.post(api_url, json = payload)

    with open(image_path, "wb") as image:
        image.write(response.content)

    return image_path

    response.content