from config.configs import Config
import requests

class Sentiment_model():
	def __init__(self):
		config = Config()
		API_TOKEN = config.get_model_api_key()
		self.API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
		self.headers = {"Authorization": f"Bearer {API_TOKEN}"}

	def query(self, payload):
		response = requests.post(self.API_URL, headers=self.headers, json=payload)
		return response.json()
	
