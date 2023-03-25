import requests
import json


def huggingBart(text, length):
    API_TOKEN = "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"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    def query(payload):
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))
    output = query(
        {
            "inputs": text,
            "parameters": {"min_length": length*18, "max_length": length*25},
        }
    )[0]['summary_text']
    return output
