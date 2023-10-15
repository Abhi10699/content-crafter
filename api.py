import requests
import json


hf_base = "https://api-inference.huggingface.co/models"
headers = {"Authorization": "Bearer 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"}


def blip_image_caption(image_data):
  api_url = f"{hf_base}/Salesforce/blip-image-captioning-large"
  api_request = requests.post(api_url, data=image_data, headers=headers)
  api_json = api_request.json()

  blip_large_caption = api_json[0]['generated_text']
  return blip_large_caption


def mistral_prompt_request(image_description):
  prompt = f"""<s>[INST]
You are a social media content creator. 
You have a deep understanding on how to produce content given a trend. 
You will be provided with a image description and list of trends that are trending right now. 
Use the image description and the list of trends to assist user on how they can use that idea and make a video.Also add some captions and hashtags to maximize the reach.
Properly format your response with each trend. Use styling, new lines and emjois where necessary.
Use the response template as example for all the trends in the list but add your own creativity while being safe.

Response Template Example for each item in the list: 
Content Idea for Trend 1: [Your ideas to tell a story relating a through using a short video].


Image Description: {image_description}
Trend List:
1: Pair an audio with a caption that highlights a risk you’ve recently taken and let the delusion soar.
2: The perfect opportunity to showcase a killer fit. 
3: Highlight an unexpected moment or a relatable struggle.[/INST]</s>"""

  api_url = "http://854a-34-126-125-2.ngrok-free.app/generate/"
  api_request = requests.post(api_url, json={
    "prompt": image_description
  })

  api_json = api_request.json()
  generated_text = api_json['generated_text'] 
 
  # postprocess the text

  generated_text_clean = generated_text.split("[/INST]</s>")[1].replace("</s>","")
  return generated_text_clean


def stable_diffusion_api(prompt):
  api_url = f"{hf_base}/stabilityai/stable-diffusion-xl-base-1.0"
  api_request = requests.post(api_url, json={"inputs": prompt}, headers=headers)
  image_data = api_request.content
  return image_data
