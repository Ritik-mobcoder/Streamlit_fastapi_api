import pickle
import numpy as np
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/predict")
async def root(request: Request):
    try:
        body = await request.json()
        experience = body["experience"]
        input_data = np.array([[experience]])
        model_path = "model.pkl"
        with open(model_path, "rb") as f:
            model = pickle.load(f)
            prediction = model.predict(input_data)
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
        input_data = np.array([[pclass, sex, age, sibsp, parch, fare]]).astype(
            np.float64
        )
        with open("log_reg.pkl", "rb") as f:
            model_lr = pickle.load(f)
            prediction = model_lr.predict(input_data)
            return f"{prediction}"
    except Exception as e:
        error_message = str(e)
        response_data = {"error": error_message}
        return JSONResponse(response_data)
