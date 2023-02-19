import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np


app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))



app=Flask(__name__)
model=pickle.load(open('model_classification.pkl','rb'))

@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():

    data=request.json['data']
    print(data)

    new_data=[list(data.values())]
    output=model.predict(new_data)[0]


    return jsonify(output)

@app.route('/predict',methods=['POST'])
def predict():

    data=[float(x) for x in request.form.values()]
    final_features = [np.array(data)]
    print(data)
    

    output = round(prediction[0], 2)

    if output == -1:
        fire = 'No Fire'
    else:
        fire = 'Fire'

    return render_template('home.html', prediction_text="Airfoil pressure is  {}".format(fire))




if __name__=="__main__":
    app.run(debug=True)


