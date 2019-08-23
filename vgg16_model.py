# VGG16 model

# set FLASK_APP=vgg16_model.py
# flask run --host=0.0.0.0
# http://127.0.0.1:5000/static/vgg16_predict.html

import base64
import numpy as np
import io
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16
import os
from flask import Flask, request, jsonify

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def get_model():
    global model
    model = VGG16()
    print("[info] Model loaded ...")

print("[info] Loading Keras model ...")
get_model()

app =  Flask(__name__)

@app.route("/vgg16_predict", methods=['post'])
def predict():
	message =  request.get_json(force=True)
	encoded =  message['image']
	decoded = base64.b64decode(encoded)

	image = Image.open(io.BytesIO(decoded))
	if image.mode != "RGB":
		image = image.convert("RGB")

	image = image.resize((224, 224))
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = preprocessing_input(image)
	yhat = model.predict(image)
	labels = decode_predictions(yhat)
	
	prd1 = labels[0][0]
	prd2 = labels[0][1]
	prd3 = labels[0][2]
	prd4 = labels[0][3]
	prd5 = labels[0][4]

	response = {
	   'prediction': {
	   		'prd1': prd1[1],
	   		'prd1_v': prd1[2]*100,
	   		'prd2': prd2[1],
	   		'prd2_v': prd2[2]*100,
	   		'prd3': prd3[1],
	   		'prd3_v': prd3[2]*100,
	   		'prd4': prd4[1],
	   		'prd4_v': prd4[2]*100,
	   		'prd5': prd5[1],
	   		'prd5_v': prd5[2]*100,
	   }

	}
	return jsonify(response)