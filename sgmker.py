import boto3
import sagemaker
import json




payload = {
    "inputs": "idu olle movie",
}

try:
    # send the request to the sagemaker endpoint
    output = sagemaker_client.invoke_endpoint(
        EndpointName=ENDPOINT, 
        ContentType="application/json", 
        Body= json.dumps(payload))

    # parse the results
    response = json.loads(output["Body"].read().decode("utf-8"))
    print(response)

except Exception as e:
    response = "Error: {}".format(str(e))
    print(response)