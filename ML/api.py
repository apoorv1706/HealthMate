import pickle
from fastapi import FastAPI
import spacy
import json

app=FastAPI(title="C:\Users\apoor\OneDrive\Desktop\healthmate\voting_classifier_model_Disease_pred_97_percent_acc.pkl")
mymodel=pickle.load('{model_name}','rb')


@app.get("/disease_prediction")


async def predict_disease(text :str):
    result=mymodel.predict(str)
    return result