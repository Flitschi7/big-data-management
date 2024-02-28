from fastapi import FastAPI
import uvicorn
import pickle 
from pydantic import BaseModel

class PrognoseEingabe(BaseModel):
    Druck_rolling: float
    Vibration_rolling: float
    Temperatur_rolling: float
    Ausschuss_rolling: float
    Anzahlwarning_rolling: float
    Druck_std: float
    Vibration_std: float
    Temperatur_std: float
    Anzahlwarning_std: float

from fastapi import FastAPI
import pickle

app = FastAPI()

#Laden des Modells
model_path = 'notebook/finalized_model.pkl'
with open('finalized_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.post('/prognose')
def prognose(eingabe: PrognoseEingabe):
    eingabe_daten = [
        [
            eingabe.Druck_rolling,
            eingabe.Vibration_rolling,
            eingabe.Temperatur_rolling,
            eingabe.Ausschuss_rolling,
            eingabe.Anzahlwarning_rolling,
            eingabe.Druck_std,
            eingabe.Vibration_std,
            eingabe.Temperatur_std,
            eingabe.Anzahlwarning_std
        ]
    ]

    try:
        prediction = model.predict(eingabe_daten)
    except Exception as e:
        return {"Fehler": str(e)}
    return {"Prognose": prediction.tolist()}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
