from flask import Flask
#import azure-ai-textanalytics
app = Flask(__name__)

@app.route("/")
print("abc")

#def hello():
#    return "running 2"


#from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
#from azure.storage.blob import BlockBlobService, BlobServiceClient, BlobClient, ContainerClient
#print(dir())
#print("Hola")
