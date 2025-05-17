from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.applications.vgg16 import VGG16, decode_predictions, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

app = FastAPI()
model = VGG16(weights="imagenet")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).resize((224, 224)).convert("RGB")
    arr = img_to_array(image)
    arr = preprocess_input(np.expand_dims(arr, axis=0))
    
    preds = model.predict(arr)
    decoded = decode_predictions(preds, top=3)[0]
    return {"predictions": [{ "label": l, "description": d, "score": float(s) } for (l, d, s) in decoded]}
