import pickle
import numpy as np
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

model_path = "model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open("log_reg.pkl", "rb") as f:
    model_lr = pickle.load(f)


@app.post("/predict")
async def root(request: Request):
    try:
        body = await request.json()
        experience = body["experience"]
        input_data = np.array([[experience]])
        prediction = model.predict(input_data)
        # print(prediction)
        response_data = {"prediction_salary": prediction.tolist()}
        return JSONResponse(response_data)
    except Exception as e:
        error_message = str(e)
        response_data = {"error": error_message}
        return JSONResponse(response_data)


@app.post("/titanic")
async def root(request: Request):
    try:
        body = await request.json()
        pclass, sex, age, sibsp, parch, fare = body.values()
        input_data = np.array([[pclass, sex, age, sibsp, parch, fare]])
        prediction = model_lr(input_data)
        return f"{prediction}"
        response_data = {"prediction_salary": f"{prediction[0]}"}
        return JSONResponse(response_data)
    except Exception:
        print("")
