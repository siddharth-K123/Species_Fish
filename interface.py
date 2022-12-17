
from flask import Flask, jsonify, render_template, request, redirect
import config
import utils
from utils import FishSpecies

app = Flask(__name__)
@app.route('/')
def man():
    return render_template('self.html')


@app.route('/predict',methods = ['GET', "POST"])

def self():
    if request.method == 'POST':
        data = request.form
        
        print('data :',data)

        species_fish = FishSpecies(data)
        pred_class = species_fish.get_prediction()
        #print("::::::::::",pred_class)

        if pred_class == "Perch":
            pred_class = 0
        elif pred_class == "Bream":
            pred_class = 1
        elif pred_class == "Roach":
            pred_class = 2
        elif pred_class == "Whitefish":
            pred_class = 3
        elif pred_class == "Parkki":
            pred_class = 4
        elif pred_class == "Smelt":
            pred_class = 5
        else:
             
            pred_class = 6
        
        return render_template('self_after.html', data=pred_class)
        # if pred_class == 1:
        #return jsonify({"Fish Species": pred_class})

    #     else:
    #         return jsonify({"Outcome": "Person has no Diabetes"})
    #    return f"{pred_class}"
    #     return jsonify({"class" :0 })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
