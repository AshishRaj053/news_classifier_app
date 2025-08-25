from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load pipeline model (includes vectorizer + classifier)
model = joblib.load("models/news_classifier_model.pkl")

app = FastAPI()

class NewsItem(BaseModel):
    headline: str

@app.post("/predict")
def predict_category(item: NewsItem):
    prediction = model.predict([item.headline])[0]
    return {"category": prediction}