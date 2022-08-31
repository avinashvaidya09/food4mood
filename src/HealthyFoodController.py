from crypt import methods
from flask import request, Blueprint, jsonify
import joblib


healthyfood_bp = Blueprint('HealthyFoodController', __name__)

mood_map = {'Happy':1,'Sad':2,'OK':3,'Angry':4}
energy_map = {'High':5,'Low':6,'Exhausted':7,'Energized':8}
mindset_map = {'Focused':9, 'Distracted':10, 'Calm':11, 'Stressed':12}
cravings_map = {'Sweet':13, 'Junk':14, 'Spicy':15,'Healthy':16}
health_goals_map = {'LowSugar':17, 'HighCalorie':18, 'LowCalorie':19, 'LowCarb':20}

food_choices_inverse_map = {21:'Tuna salad & Green tea', 22:'Burger & Juice', 23:'Burger & Energy Drink', 24:'Burger & Ice Cream', 
                    25:'Mediterrenean wrap & Juice', 26:'Mediterrenean wrap & Cheese', 
                    27:'Mediterrenean wrap & Ice Cream', 28:'Salad with Protein & Juice', 29:'Croissant & Smoothie'}

health_tip_map = {22:'Eat Less Walk More and drink lots of water', 23:'Take a bite and walk a mile', 26:'Burn some calories today evening', 
                    27:'A quick 15 minutes walk is good for your health', 21:'Meditation is good for your health', 28:'Try some new activity today and relax', 
                    24:'Swimming is good to burn calories', 25:'Morning is a great time for workout'}

@healthyfood_bp.route('/', methods=['GET'])
def get_healthy_food():
    input_mood = request.args.get('mood') or 'OK'
    input_energy = request.args.get('energy') or 'High'
    input_mindset = request.args.get('mindset') or 'Calm'
    input_cravings = request.args.get('cravings') or 'Junk'
    input_health_goals = request.args.get('health_goals') or 'LowCarb'

    input_arr = [[mood_map[input_mood], energy_map[input_energy],mindset_map[input_mindset],cravings_map[input_cravings],health_goals_map[input_health_goals]]]

    joblib_NB_Model = joblib.load('./resources/joblib_NB_Trained_Model.pkl')

    nb_predict_real_data = joblib_NB_Model.predict(input_arr)

    response_object = {
        'food': food_choices_inverse_map[nb_predict_real_data[0]],
        'healthTip': health_tip_map[nb_predict_real_data[0]]
    }   

    return jsonify(response_object)

