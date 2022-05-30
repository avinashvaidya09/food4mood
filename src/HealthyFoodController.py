from crypt import methods
from flask import request, Blueprint, jsonify
import joblib


healthyfood_bp = Blueprint('HealthyFoodController', __name__)

mood_map = {'Happy':1,'Sad':2,'OK':3}
energy_map = {'High':4,'Low':5,'Exhausted':6}
mindset_map = {'Focused':7, 'Distracted':8, 'Calm':9, 'Stressed':10}
cravings_map = {'Sweet':11, 'Junk':12, 'Spicy':13}
health_goals_map = {'Increase Muscles':15, 'Reduce Weight':16, 'Increase Weight':17}

food_choices_inverse_map = {18:'Burger', 19:'Burger & Juice', 20:'Burger & Energy Drink', 21:'Burger & Ice Cream', 
                    22:'Mediterrenean wrap & Juice', 23:'Mediterrenean wrap', 24:'Mediterrenean wrap with Cheese', 
                    25:'Mediterrenean wrap & Ice Cream', 26:'Salad with Protein & Juice'}

health_tip_map = {18:'Eat Less Walk More', 19:'Take a bite and walk', 20:'Run', 21:'Burn some calories today evening', 
                    22:'A quick 15 minutes walk is good for your health', 23:'Meditation is good for your health', 24:'Try some new activity today', 
                    25:'Swimming is good in summer', 26:'Morning is good time for workout'
}

@healthyfood_bp.route('/', methods=['GET'])
def get_healthy_food():
    input_mood = request.args.get('mood') or 'OK'
    input_energy = request.args.get('energy') or 'High'
    input_mindset = request.args.get('mindset') or 'Calm'
    input_cravings = request.args.get('cravings') or 'Junk'
    input_health_goals = request.args.get('health_goals') or 'Reduce Weight'

    input_arr = [[mood_map[input_mood], energy_map[input_energy],mindset_map[input_mindset],cravings_map[input_cravings],health_goals_map[input_health_goals]]]

    joblib_NB_Model = joblib.load('./resources/joblib_nb_trained_model.pkl')

    nb_predict_real_data = joblib_NB_Model.predict(input_arr)

    response_object = {
        'food': food_choices_inverse_map[nb_predict_real_data[0]],
        'healthTip': health_tip_map[nb_predict_real_data[0]]
    }   

    return jsonify(response_object)

