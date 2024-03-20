import pickle
import joblib
from fastapi import FastAPI
import spacy
import json

app=FastAPI(title="Disease prediction API")
MODEL_PATH=r'C:\Users\LENOVO\Desktop\HealthMate\backend\voting_classifier_model_Disease_pred_97_percent_acc.pkl'
mymodel=joblib.load(MODEL_PATH)
fans=mymodel.predict("I have been experiencing symptoms such as high fever, red spots on my body whcih is causing itching and they are getting bigger and swollen.")

print(fans)


@app.get("/disease_prediction")


async def predict_disease(text :str):
    result=mymodel.predict(str)
    return result


