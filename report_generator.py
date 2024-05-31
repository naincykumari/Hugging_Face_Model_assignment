from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import requests

# Define API endpoint and headers
API_ENDPOINT = "https://huggingface.co/api/models"
HEADERS = {"Authorization": "Bearer YOUR_HUGGINGFACE_TOKEN"}

# Replace with your Hugging Face token
YOUR_HUGGINGFACE_TOKEN = "YOUR_TOKEN"

def get_top_downloaded_models():
  """
  Fetches data from the Hugging Face model hub API and returns the top 10 downloaded models.
  """
  response = requests.get(API_ENDPOINT, headers=HEADERS)
  data = response.json()
  
  # Sort models by downloads and get top 10
  models = sorted(data, key=lambda model: model["total_downloads"], reverse=True)[:10]
  
  # Extract relevant information
  top_models = []
  for model in models:
    top_models.append({
      "model_id": model["id"],
      "name": model["name"],
      "downloads": model["total_downloads"],
    })
  
  return top_models

def generate_report(top_models):
  """
  Generates a report with the top 10 downloaded models.
  """
  with open("report.txt", "a") as f:
    f.write("Top 10 Downloaded Models on Hugging Face Hub:\n")
    for i, model in enumerate(top_models):
      f.write(f"{i+1}. {model['name']} ({model['model_id']}): {model['downloads']} downloads\n")

if __name__ == "__main__":
  top_models = get_top_downloaded_models()
  generate_report(top_models)
