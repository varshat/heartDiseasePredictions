
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
import sklearn

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def predict():
    if request.method == 'POST':
        try:
            age = float(request.form['age'])
            sex = float(request.form['sex'])
            cp = float(request.form['cp'])
            trestbps = float(request.form['trestbps'])
            chol = float(request.form['chol'])
            fbs = float(request.form['fbs'])
            restecg = float(request.form['restecg'])
            thalach = float(request.form['thalach'])
            exang = float(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = float(request.form['slope'])
            ca = float(request.form['ca'])
            thal = float(request.form['thal'])
            filename = 'HeartDiseaes.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            #prediction = loaded_model.predict([[63,1,3,145,233,1,0,150,0,2.3,0,0,1]])
            print('prediction is', prediction)
            return render_template('result.html', prediction=prediction[0])
        except Exception as e:
            print('The Exception message is: ', e)
        return 'something is wrong'
        # return render_template('results.html')
    else:
        return render_template('home.html')


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app