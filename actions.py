from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
import pandas as pd
from itertools import islice
import zomatopy
import json
import re
import smtplib
import param


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
        
    def run(self, dispatcher, tracker, domain):
        
        zomato = zomatopy.initialize_app(param.user_key)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price=tracker.get_slot('price')

        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'south indian':85,'north indian':50}
        df=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),price, 5)
        response="  "
        if df.empty:
            response= "No Results Found"
        else:
            iter_count=1
            for restaurant in df.itertuples():
                response=response+"  "+str(iter_count)+". "+ list(restaurant)[1]+ " in "+ list(restaurant)[2]+" has been rated "+str(list(restaurant)[3])+"\n"
                iter_count+=1
            response=response+"\n"
				        
        dispatcher.utter_message(response)
        return []


class AvailableLocation(Action):
    def name(self):
        return "action_is_Location_Available"
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if loc.lower() not in param.operating_cities:
            dispatcher.utter_message("We do not operate in city " + loc + " yet. Please search Tier-1 and Tier-2 cities.")
            return [SlotSet('location', None)]
        return []

class AvailableCuisine(Action):
    def name(self):
        return "action_is_Cuisine_Available"
    
    def run(self, dispatcher, tracker, domain):
        cuisine = tracker.get_slot('cuisine')
        if cuisine.lower() not in param.valid_cusines:
            dispatcher.utter_message("The cuisine "+cuisine+" is not available. Please enter from the following cuisine.\n\n  1.chinese\n  2.mexican\n  3.italian\n  4.american\n  5.north indian\n  6.south indian")
            return [SlotSet('cuisine', None)]
        return []

class AvailablePriceOptions(Action):
    def name(self):
        return "action_is_Price_Available"
    
    def run(self, dispatcher, tracker, domain):
        price = tracker.get_slot('price')

        if price in param.valid_price_range:
            if(price=='>700'):
                return[SlotSet('price_class','High')]
            if(price=='<300'):
                return[SlotSet('price_class','Low')]
            if(price=='300-700'):
                return[SlotSet('price_class','Med')]
        
        else:
            dispatcher.utter_message("Please select from the given price range.\n\n  1.Lesser than Rs.300\n  2.Rs 300 to 700\n  3.More than Rs 700\n\n")
            return [SlotSet('price', None),SlotSet('price_class', None)]

class CheckEmail(Action):
    def name(self):
        return 'action_validate_email'
        
    def run(self, dispatcher, tracker, domain):  
        email=tracker.get_slot('email')
        if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
            dispatcher.utter_message("Please enter a valid email ID.")
            return [SlotSet("email", None)]
        return []


class SendEmail(Action):
    def name(self):
        return 'action_send_email'
        
    def run(self, dispatcher, tracker, domain):
        try:
            rec_email=tracker.get_slot('email')
            zomato = zomatopy.initialize_app(param.user_key)
            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')
            price=tracker.get_slot('price')
            location_detail=zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'south indian':85,'north indian':50}
            df=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),price, 10)

            mail_content1=""
            if df.empty:
                mail_content1= "No Results Found"
            else:
                iter_count=1
                for restaurant in df.itertuples():
                    mail_content1=mail_content1+str(iter_count)+". "+ str(list(restaurant)[1])+ " in "+ str(list(restaurant)[2])+" has been rated "+str(list(restaurant)[3])+"\n\n"
                    iter_count+=1

            mail_content= "Hi,\n\t"
            mail_content= mail_content+"Top rated restuartants based on your city & cuisine preference are :\n\n"
            mail_content= mail_content+mail_content1


            subject='Top rated {} restuartants for your preference - '.format(tracker.get_slot('cuisine'))
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            sender_email=param.email
            server.login(param.email, param.password)
            message = 'Subject: {}\n\n{}'.format(subject, mail_content)
            server.sendmail(sender_email,rec_email, message)    
            dispatcher.utter_message('Email sent,Bon Appetit')
            return []

        except Exception as e:
            dispatcher.utter_message('Email could not be sent successfully \n')
            return [SlotSet("email", None)]

class RestartAction(Action):
	def name(self):
		return 'action_Dialogue_Complete'
		
	def run(self, dispatcher, tracker, domain):
	    return [Restarted()]


class Available_Location_Cuisine_Budget(Action):
    def name(self):
        return "action_is_Location_Cuisine_Budget_Available"
    
    def run(self, dispatcher, tracker, domain):
        return_list=[]
        is_error=False
        response=""

        loc = tracker.get_slot('location')
        if loc.lower() not in param.operating_cities:
            is_error=True
            response+="We do not operate in city " + loc + " yet. Please search Tier-1 and Tier-2 cities.\n \n"
            return_list.append(SlotSet('location', None))
        
        cuisine = tracker.get_slot('cuisine')
        if cuisine.lower() not in param.valid_cusines:
            is_error=True
            response+="The cuisine "+cuisine+" is not available. Please enter from the following cuisine.\n\n  1.chinese\n  2.mexican\n  3.italian\n  4.american\n  5.north indian\n  6.south indian\n \n"
            return_list.append(SlotSet('cuisine', None))
            
        price = tracker.get_slot('price')
        if price in param.valid_price_range:
            if(price=='>700'):
                return_list.append(SlotSet('price_class','High'))
            if(price=='<300'):
                return_list.append(SlotSet('price_class','Low'))
            if(price=='300-700'):
                return_list.append(SlotSet('price_class','Med'))
            #return_list.append(SlotSet('price_class', 'if')) 
        else:
            is_error=True
            response+="Please select from the given price range.\n\n  1.Lesser than Rs.300\n  2.Rs 300 to 700\n  3.More than Rs 700\n \n"
            return_list.append(SlotSet('price', None))
            return_list.append(SlotSet('price_class', None))

        if(is_error):
            dispatcher.utter_message(response)

   
        return return_list


class Available_Location_Cuisine(Action):
    def name(self):
        return "action_is_Location_Cuisine_Available"
    
    def run(self, dispatcher, tracker, domain):
        return_list=[]
        is_error=False
        response=""

        loc = tracker.get_slot('location')
        if loc.lower() not in param.operating_cities:
            is_error=True
            response+="We do not operate in city " + loc + " yet. Please search Tier-1 and Tier-2 cities.\n\n"
            return_list.append(SlotSet('location', None))
        
        cuisine = tracker.get_slot('cuisine')
        if cuisine.lower() not in param.valid_cusines:
            is_error=True
            response+="The cuisine "+cuisine+" is not available. Please enter from the following cuisine.\n\n  1.chinese\n  2.mexican\n  3.italian\n  4.american\n  5.north indian\n  6.south indian\n\n"
            return_list.append(SlotSet('cuisine', None))

        if(is_error):
            dispatcher.utter_message(response)

   
        return return_list

class Available_Cuisine_Budget(Action):
    def name(self):
        return "action_is_Cuisine_Budget_Available"
    
    def run(self, dispatcher, tracker, domain):
        return_list=[]
        is_error=False
        response=""
        
        cuisine = tracker.get_slot('cuisine')
        if cuisine.lower() not in param.valid_cusines:
            is_error=True
            response+="The cuisine "+cuisine+" is not available. Please enter from the following cuisine.\n\n  1.chinese\n  2.mexican\n  3.italian\n  4.american\n  5.north indian\n  6.south indian\n\n"
            return_list.append(SlotSet('cuisine', None))
            
        price = tracker.get_slot('price')
        if price in param.valid_price_range:
            if(price=='>700'):
                return_list.append(SlotSet('price_class','High'))
            if(price=='<300'):
                return_list.append(SlotSet('price_class','Low'))
            if(price=='300-700'):
                return_list.append(SlotSet('price_class','Med'))
        else:
            is_error=True
            response+="Please select from the given price range.\n\n  1.Lesser than Rs.300\n  2.Rs 300 to 700\n  3.More than Rs 700\n\n"
            return_list.append(SlotSet('price', None))
            return_list.append(SlotSet('price_class', None))

        if(is_error):
            dispatcher.utter_message(response)
   
        return return_list

class Available_Location_Budget(Action):
    def name(self):
        return "action_is_Location_Budget_Available"
    
    def run(self, dispatcher, tracker, domain):
        return_list=[]
        is_error=False
        response=""

        loc = tracker.get_slot('location')
        if loc.lower() not in param.operating_cities:
            is_error=True
            response+="We do not operate in city " + loc + " yet. Please search Tier-1 and Tier-2 cities.\n\n"
            return_list.append(SlotSet('location', None))
        
            
        price = tracker.get_slot('price')
        if price in param.valid_price_range:
            if(price=='>700'):
                return_list.append(SlotSet('price_class','High'))
            if(price=='<300'):
                return_list.append(SlotSet('price_class','Low'))
            if(price=='300-700'):
                return_list.append(SlotSet('price_class','Med'))
        
        else:
            is_error=True
            response+="Please select from the given price range.\n\n  1.Lesser than Rs.300\n  2.Rs 300 to 700\n  3.More than Rs 700\n\n"
            return_list.append([SlotSet('price', None),SlotSet('price_class', None)])

        if(is_error):
            dispatcher.utter_message(response)
   
        return return_list
