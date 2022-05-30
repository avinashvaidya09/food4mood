from crypt import methods
import json
from optparse import Values
from flask import request, Blueprint, jsonify
from cfenv import AppEnv
from hdbcli import dbapi
import HanaDbService 

healthyuser_bp = Blueprint('HealthyUserController', __name__)

@healthyuser_bp.route('/user', methods=['GET'])
def get_user_by_email():
   user_email = request.args.get('email') or ''
   try:
      hanadb_obj = HanaDbService.HanaDb()
      table_name_with_schema = hanadb_obj.get_table_name_with_schema("USER")
      ro = hanadb_obj.query_one("select USERID, EMAIL, FIRSTNAME, LASTNAME from " + table_name_with_schema + " where email = '" + user_email + "'")
      user_dto = {
         'userId': ro["USERID"],
         'email': ro["EMAIL"],
         'firstName': ro["FIRSTNAME"],
         'lastName': ro["LASTNAME"]
      }
   except Exception as err:
      print("Exception in get_user_by_email >>>>>>>", err)
   return jsonify(user_dto)

@healthyuser_bp.route('/food-feedback', methods=['POST'])
def add_food_feedback_for_mood():
   result = "FAIL"
   try:
      payload_data = json.loads(request.data)
      print(payload_data)
      hanadb_obj = HanaDbService.HanaDb()
      table_name_with_schema = hanadb_obj.get_table_name_with_schema("MOOD")
      sql = (
         "INSERT INTO " + table_name_with_schema + " (USERID, MOOD, ENERGY, MINDSET, CRAVINGFOR, HEALTHGOAL, FOODCHOICE, USERIMAGEURL)"
         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
      )
      vals =  ( payload_data['id'] , payload_data['mood'], payload_data['energy'],
      payload_data['mindset'],payload_data['cravingFor'],payload_data['healthGoal'],
      payload_data['foodChoice'],payload_data['userImageUrl'])
      hanadb_obj.add_one(sql, vals)
      result = "SUCCESS"
   except Exception as ex:
      print("Exception in add_food_feedback_for_mood >>>>>>>", ex)
   return result
