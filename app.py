import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
<<<<<<< HEAD
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
=======


app=Flask(__name__)
model=pickle.load(open('model_classification.pkl','rb'))
>>>>>>> 1810569 (first test commit)
@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():

    data=request.json['data']
    print(data)
<<<<<<< HEAD
    new_data=[list(data.values())]
    output=model.predict(new_data)[0]
=======
    new_data = [list(data.values())]
    output = model.predict(new_data)[0]
>>>>>>> 1810569 (first test commit)
    return jsonify(output)

@app.route('/predict',methods=['POST'])
def predict():

    data=[float(x) for x in request.form.values()]
    final_features = [np.array(data)]
    print(data)
    
    output=model.predict(final_features)[0]
    print(output)
<<<<<<< HEAD
    #output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="Airfoil pressure is  {}".format(output))
=======
    if output == -1:
        fire = 'No Fire'
    else:
        fire = 'Fire'
    #output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="Airfoil pressure is  {}".format(fire))
>>>>>>> 1810569 (first test commit)



if __name__=="__main__":
    app.run(debug=True)


