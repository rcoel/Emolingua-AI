# import boto3
# import sagemaker
import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()

H_API = os.getenv("HUGGINGFACE_API")

auth_key = "Bearer " + H_API
API_URL = "https://api-inference.huggingface.co/models/janedsa/model"
headers = {"Authorization": auth_key}

def query_bert(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	if response.status_code != 200:
		time.sleep(10)
		response = requests.post(API_URL, headers=headers, json=payload)
	print(response)
	print(response.json)
	response_data = response.json()[0]
	dict = {}
	for item in response_data:
		label = item['label'] 
		score = item['score']  
		dict[label] = score
	return dict
	