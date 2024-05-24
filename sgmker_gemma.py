import boto3
import sagemaker
from dotenv import load_dotenv
import os
import time
import json

load_dotenv()

ACCESS_KEY_ID = os.getenv('AWS_ACESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS')
REGION_NAME = os.getenv('AWS_REGION')
ENDPOINT = os.getenv('ENDPOINT')

sagemaker_client = boto3.session.Session().client("sagemaker-runtime", aws_access_key_id= ACCESS_KEY_ID,
                       aws_secret_access_key= SECRET_KEY, region_name = REGION_NAME)


def query_gemma(userText):
    prompt = f"""
    Give the detailed sentiment of the following text in a single line:{userText} Let the response be detailed and begin as: The sentiment expresses
    """
    json = {"inputs": "prompt"}
    try:
    # send the request to the sagemaker endpoint
      output = sagemaker_client.invoke_endpoint(
      EndpointName=ENDPOINT, 
      ContentType="application/json", 
      Body= json.dumps(json))

      response = json.loads(output["generated_text"].read().decode("utf-8"))
      print(response)
    except Exception as e:
      response = "Error: {}".format(str(e))
      print(response)
      
    return response