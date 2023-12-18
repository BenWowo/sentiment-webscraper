from services.sentiment_model import Sentiment_model

model = Sentiment_model()

output = model.query({
	"inputs": "I like you. I love you",
})

print(output)