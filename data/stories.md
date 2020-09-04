
## chatbot - 1
* greet
    - utter_greet
* restaurant_search_details
    - utter_ask_location
* restaurant_search_details{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* affirm
    - utter_goodbye
    - action_Dialogue_Complete


## chatbot - 2
* greet
    - utter_greet
* restaurant_search_details{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "aurangabad"}
    - slot{"location": "aurangabad"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* affirm
    - utter_goodbye
    - action_Dialogue_Complete

## chatbot - 3
* greet
    - utter_greet
* restaurant_search_details{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_yes{"email": "hariharanp1094@gmail.com"}
    - slot{"email": "hariharanp1094@gmail.com"}
    - action_validate_email
    - action_send_email
* affirm
    - utter_goodbye
    - action_Dialogue_Complete

## chatbot - 4
* greet
    - utter_greet
* restaurant_search_details
    - utter_ask_location
* restaurant_search_details{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_yes{"email": "hariharanp1094@gmail.com"}
    - slot{"email": "hariharanp1094@gmail.com"}
    - action_validate_email
    - action_send_email
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete



## interactive_story_8
* greet
    - utter_greet
* restaurant_search_details{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "korean"}
    - slot{"cuisine": "korean"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ""}
    - slot{"price": ""}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_yes
    - utter_ask_email
* email_affirm_yes{"email": "hira@@gmail.ciom"}
    - slot{"email": "hira@@gmail.ciom"}
    - action_validate_email
    - slot{"email": null}
* email_affirm_yes{"email": "siva@gmail.com"}
    - slot{"email": "siva@gmail.com"}
    - action_validate_email
    - action_send_email
* affirm
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"location": "aligarh"}
    - slot{"location": "aligarh"}
    - action_is_Location_Available
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_is_Cuisine_Available
    - utter_ask_location
* restaurant_search_details{"location": "amravati"}
    - slot{"location": "amravati"}
    - action_is_Location_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_is_Price_Available
    - slot{"price_class": "Med"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* affirm
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_is_Price_Available
    - slot{"price_class": "Med"}
    - utter_ask_location
* restaurant_search_details{"location": "nanded"}
    - slot{"location": "nanded"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ""}
    - slot{"price": ""}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": ""}
    - slot{"price": ""}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_is_Price_Available
    - slot{"price_class": "Med"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_is_Location_Available
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "asansol"}
    - slot{"location": "asansol"}
    - action_is_Location_Available
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "bareilly"}
    - slot{"location": "bareilly"}
    - action_is_Location_Available
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "belgaum"}
    - slot{"location": "belgaum"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "bhavnagar"}
    - slot{"location": "bhavnagar"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "bhiwandi"}
    - slot{"location": "bhiwandi"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "bhubaneswar"}
    - slot{"location": "bhubaneswar"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "bikaner"}
    - slot{"location": "bikaner"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "bokaro steel city"}
    - slot{"location": "bokaro steel city"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "dehradun"}
    - slot{"location": "dehradun"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "durg-bhilai nagar"}
    - slot{"location": "durg-bhilai nagar"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "erode"}
    - slot{"location": "erode"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_is_Location_Available
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "firozabad"}
    - slot{"location": "firozabad"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "ghaziabad"}
    - slot{"location": "ghaziabad"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "gorakhpur"}
    - slot{"location": "gorakhpur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "gulbarga"}
    - slot{"location": "gulbarga"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "guntur"}
    - slot{"location": "guntur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "guwahati"}
    - slot{"location": "guwahati"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "gwalior"}
    - slot{"location": "gwalior"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "hubli"}
    - slot{"location": "hubli"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "indore"}
    - slot{"location": "indore"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "jammu"}
    - slot{"location": "jammu"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "jamnagar"}
    - slot{"location": "jamnagar"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "jamshedpur"}
    - slot{"location": "jamshedpur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "jhansi"}
    - slot{"location": "jhansi"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "kannur"}
    - slot{"location": "kannur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "kakinada"}
    - slot{"location": "kakinada"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "kottayam"}
    - slot{"location": "kottayam"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "kolhapur"}
    - slot{"location": "kolhapur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "kollam"}
    - slot{"location": "kollam"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "kota"}
    - slot{"location": "kota"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "kozhikode"}
    - slot{"location": "kozhikode"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "kurnool"}
    - slot{"location": "kurnool"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "madurai"}
    - slot{"location": "madurai"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "malappuram"}
    - slot{"location": "malappuram"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "mathura"}
    - slot{"location": "mathura"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "goa"}
    - slot{"location": "goa"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "mangalore"}
    - slot{"location": "mangalore"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "mangalore"}
    - slot{"location": "mangalore"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "meerut"}
    - slot{"location": "meerut"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"location": "moradabad"}
    - slot{"location": "moradabad"}
    - action_is_Location_Available
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ""}
    - slot{"price": ""}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_yes
    - utter_ask_email
* irrelevant_text
    - utter_text_not_relevant
* email_affirm_yes{"email": "hariharanp1094"}
    - slot{"email": "hariharanp1094"}
    - action_validate_email
    - slot{"email": null}
* email_affirm_yes{"email": "hariharanp1094@gmail.com"}
    - slot{"email": "hariharanp1094@gmail.com"}
    - action_validate_email
    - action_send_email
* affirm
    - utter_goodbye
    - action_Dialogue_Complete


## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"price": "300 and below"}
    - slot{"price": "300 and below"}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
    - utter_ask_location
* restaurant_search_details{"location": "rourkela"}
    - slot{"location": "rourkela"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - action_search_restaurants
    - utter_email_bool
* irrelevant_text
    - utter_text_not_relevant
* email_affirm_yes{"email": "testaccn94@gmail.com"}
    - slot{"email": "testaccn94@gmail.com"}
    - action_validate_email
    - action_send_email
* affirm
    - utter_goodbye
    - action_Dialogue_Complete


## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "dindigul"}
    - slot{"location": "dindigul"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "chinallapatti"}
    - slot{"location": "chinallapatti"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "seerkali"}
    - slot{"location": "seerkali"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "raipur"}
    - slot{"location": "raipur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* irrelevant_text{"price": ">700"}
    - slot{"price": ">700"}
    - action_search_restaurants
    - utter_email_bool
* irrelevant_text
    - utter_text_not_relevant
* email_affirm_yes{"email": "testaccn94@gmail.com"}
    - slot{"email": "testaccn94@gmail.com"}
    - action_validate_email
    - action_send_email
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - utter_ask_location
* restaurant_search_details{"location": "rajahmundry"}
    - slot{"location": "rajahmundry"}
    - action_is_Location_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_is_Price_Available
    - slot{"price_class": "Med"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"price": "above three hundred"}
    - slot{"price": "above three hundred"}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - utter_ask_location
* restaurant_search_details{"location": "pollachi"}
    - slot{"location": "pollachi"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"cuisine": "vietnamese"}
    - slot{"cuisine": "vietnamese"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - utter_ask_location
* restaurant_search_details{"location": "sangli"}
    - slot{"location": "sangli"}
    - action_is_Location_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_is_Price_Available
    - slot{"price_class": "Med"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* affirm
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - utter_ask_location
* restaurant_search_details{"location": "dindigul"}
    - slot{"location": "dindigul"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"cuisine": "korean"}
    - slot{"cuisine": "korean"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_is_Cuisine_Available
    - utter_ask_location
* irrelevant_text
    - utter_text_not_relevant
* restaurant_search_details{"location": "ujjain"}
    - slot{"location": "ujjain"}
    - action_is_Location_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "below 700"}
    - slot{"price": "below 700"}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"location": "vasai-virar city"}
    - slot{"location": "vasai-virar city"}
    - action_is_Location_Available
    - utter_ask_cuisine
* irrelevant_text
    - utter_text_not_relevant
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details
    - utter_ask_location
* restaurant_search_details{"location": "amsterdam"}
    - slot{"location": "amsterdam"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "thiruvananthapuram"}
    - slot{"location": "thiruvananthapuram"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "tamil food"}
    - slot{"cuisine": "tamil food"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* irrelevant_text
    - utter_text_not_relevant
* restaurant_search_details
    - utter_ask_location
* restaurant_search_details{"location": "bokaro steel city"}
    - slot{"location": "bokaro steel city"}
    - action_is_Location_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_yes{"email": "testaccn94@gmail.com"}
    - slot{"email": "testaccn94@gmail.com"}
    - action_validate_email
    - action_send_email
* affirm
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_is_Location_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_yes{"email": "testaccn94@gmail.com"}
    - slot{"email": "testaccn94@gmail.com"}
    - action_validate_email
    - action_send_email
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"cuisine": "american", "location": "coimbatore"}
    - slot{"cuisine": "american"}
    - slot{"location": "coimbatore"}
    - action_is_Location_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"location": "Delhi", "price": "<300"}
    - slot{"location": "Delhi"}
    - slot{"price": "<300"}
    - action_is_Location_Budget_Available
    - slot{"price_class": "Low"}
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"cuisine": "italian", "price": ">700"}
    - slot{"cuisine": "italian"}
    - slot{"price": ">700"}
    - action_is_Cuisine_Budget_Available
    - slot{"price_class": "High"}
    - utter_ask_location
* restaurant_search_details{"location": "vijayawada"}
    - slot{"location": "vijayawada"}
    - action_is_Location_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"cuisine": "south indian", "location": "chennai", "price": "300-700"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chennai"}
    - slot{"price": "300-700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"price_class": "Med"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* affirm
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"cuisine": "vietnamese", "location": "Delhi"}
    - slot{"cuisine": "vietnamese"}
    - slot{"location": "Delhi"}
    - action_is_Location_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_is_Price_Available
    - slot{"price_class": "Med"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"cuisine": "south indian", "location": "nevada"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "nevada"}
    - action_is_Location_Cuisine_Available
    - slot{"location": null}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"location": "Delhi", "price": "above 300"}
    - slot{"location": "Delhi"}
    - slot{"price": "above 300"}
    - action_is_Location_Budget_Available
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"location": "Delhi", "price": "1000"}
    - slot{"location": "Delhi"}
    - slot{"price": "1000"}
    - action_is_Location_Budget_Available
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_yes{"email": "testaccn94@gmail.com"}
    - slot{"email": "testaccn94@gmail.com"}
    - action_validate_email
    - action_send_email
* affirm
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"location": "new york", "price": "300-700"}
    - slot{"location": "new york"}
    - slot{"price": "300-700"}
    - action_is_Location_Budget_Available
    - slot{"location": null}
    - slot{"price_class": "Med"}
* restaurant_search_details{"location": "thrissur"}
    - slot{"location": "thrissur"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"cuisine": "italian", "price": "below seven hundred"}
    - slot{"cuisine": "italian"}
    - slot{"price": "below seven hundred"}
    - action_is_Cuisine_Budget_Available
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - utter_ask_location
* restaurant_search_details{"location": "kollam"}
    - slot{"location": "kollam"}
    - action_is_Location_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"price": "below 700", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "below 700"}
    - action_is_Cuisine_Budget_Available
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - utter_ask_location
* restaurant_search_details{"location": "gorakhpur"}
    - slot{"location": "gorakhpur"}
    - action_is_Location_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"cuisine": "italian", "location": "Delhi", "price": "2000"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Delhi"}
    - slot{"price": "2000"}
    - action_is_Location_Cuisine_Budget_Available
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"location": "rourkela", "cuisine": "japanese", "price": "300-700"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "rourkela"}
    - slot{"price": "300-700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"cuisine": null}
    - slot{"price_class": "Med"}
* restaurant_search_details{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "chinallapatti", "cuisine": "mexican", "price": "300-700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chinallapatti"}
    - slot{"price": "300-700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"price_class": "Med"}
* restaurant_search_details{"location": "rajahmunry"}
    - slot{"location": "rajahmunry"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "rajahmundry"}
    - slot{"location": "rajahmundry"}
    - action_is_Location_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "bihar", "cuisine": "mexican", "price": "<300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bihar"}
    - slot{"price": "<300"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"price_class": "Low"}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Delhi", "cuisine": "korean", "price": "below 700"}
    - slot{"cuisine": "korean"}
    - slot{"location": "Delhi"}
    - slot{"price": "below 700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "italian", "price": ">700"}
    - slot{"cuisine": "italian"}
    - slot{"price": ">700"}
    - action_is_Cuisine_Budget_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_details{"cuisine": "vietnamese", "location": "Delhi", "price": "<300"}
    - slot{"cuisine": "vietnamese"}
    - slot{"location": "Delhi"}
    - slot{"price": "<300"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"cuisine": null}
    - slot{"price_class": "Low"}
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Delhi", "cuisine": "Japanese", "price": "above 300"}
    - slot{"cuisine": "Japanese"}
    - slot{"location": "Delhi"}
    - slot{"price": "above 300"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_is_Price_Available
    - slot{"price_class": "Med"}
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Delhi", "cuisine": "Japanese", "price": "above 300"}
    - slot{"cuisine": "Japanese"}
    - slot{"location": "Delhi"}
    - slot{"price": "above 300"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Delhi", "cuisine": "Japanese", "price": "above 300"}
    - slot{"cuisine": "Japanese"}
    - slot{"location": "Delhi"}
    - slot{"price": "above 300"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"cuisine": "Japanese", "price": "above 300"}
    - slot{"cuisine": "Japanese"}
    - slot{"price": "above 300"}
    - action_is_Cuisine_Budget_Available
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Delhi", "cuisine": "Japanese", "price": "above 300"}
    - slot{"cuisine": "Japanese"}
    - slot{"location": "Delhi"}
    - slot{"price": "above 300"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"cuisine": "Japanese", "price": "above 300"}
    - slot{"cuisine": "Japanese"}
    - slot{"price": "above 300"}
    - action_is_Cuisine_Budget_Available
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"cuisine": "chinese", "price": "above 300"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "above 300"}
    - action_is_Cuisine_Budget_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Dindigul", "cuisine": "Italian", "price": "below 700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Dindigul"}
    - slot{"price": "below 700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"location": "meerut", "price": "below 700"}
    - slot{"location": "meerut"}
    - slot{"price": "below 700"}
    - action_is_Location_Budget_Available
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Dindigul", "cuisine": "Italian", "price": "below 700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Dindigul"}
    - slot{"price": "below 700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"location": "dindigul", "price": ">700"}
    - slot{"location": "dindigul"}
    - slot{"price": ">700"}
    - action_is_Location_Budget_Available
    - slot{"location": null}
    - slot{"price_class": "High"}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Dindigul", "cuisine": "Italian", "price": "below 700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Dindigul"}
    - slot{"price": "below 700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"location": "chennai", "price": "<300"}
    - slot{"location": "chennai"}
    - slot{"price": "<300"}
    - action_is_Location_Budget_Available
    - slot{"price_class": "Low"}
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Dindigul", "cuisine": "japanese", "price": ">700"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "Dindigul"}
    - slot{"price": ">700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price_class": "High"}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Dindigul", "cuisine": "japanese", "price": ">700"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "Dindigul"}
    - slot{"price": ">700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price_class": "High"}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "Dindigul", "cuisine": "japanese", "price": "below 700"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "Dindigul"}
    - slot{"price": "below 700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"location": "Dindigul", "cuisine": "japanese", "price": ">700"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "Dindigul"}
    - slot{"price": ">700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price_class": "High"}
* restaurant_search_details{"location": "chennai", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"location": "chennai"}
    - action_is_Location_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"price": "between 500-600", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "between 500-600 and"}
    - action_is_Cuisine_Budget_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - utter_ask_location
* restaurant_search_details{"location": "dindigul"}
    - slot{"location": "dindigul"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"location": "paris", "price": ">700"}
    - slot{"location": "paris"}
    - slot{"price": ">700"}
    - action_is_Location_Budget_Available
    - slot{"location": null}
    - slot{"price_class": "High"}
* restaurant_search_details{"location": "jamnagar"}
    - slot{"location": "jamnagar"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* email_affirm_yes{"email": "upgradbot123@gmail.com"}
    - slot{"email": "upgradbot123@gmail.com"}
    - action_validate_email
    - action_send_email
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"cuisine": "japanese", "location": "jalna", "price": "below 700"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "jalna"}
    - slot{"price": "below 700"}
    - action_is_Location_Cuisine_Budget_Available
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"location": "chennai", "cuisine": "korean"}
    - slot{"cuisine": "korean"}
    - slot{"location": "chennai"}
    - action_is_Location_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_is_Cuisine_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_yes{"email": "upgrad@.com"}
    - slot{"email": "upgrad@.com"}
    - action_validate_email
    - slot{"email": null}
* email_details{"email": "abc@def@c.c"}
    - slot{"email": "abc@def@c.c"}
    - action_validate_email
    - slot{"email": null}
* email_affirm_yes{"email": "hariharanp1094@gmail.com"}
    - slot{"email": "hariharanp1094@gmail.com"}
    - action_validate_email
    - action_send_email
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"price": "below 700"}
    - slot{"price": "below 700"}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": "<300"}
    - slot{"price": "<300"}
    - action_is_Price_Available
    - slot{"price_class": "Low"}
    - utter_ask_location
* restaurant_search_details{"location": "dindigul"}
    - slot{"location": "dindigul"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - utter_ask_location
* restaurant_search_details{"location": "dindigul"}
    - slot{"location": "dindigul"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - utter_ask_avg_budget
* restaurant_search_details{"price": ""}
    - slot{"price": ""}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": ">700"}
    - slot{"price": ">700"}
    - action_is_Price_Available
    - slot{"price_class": "High"}
    - action_search_restaurants
    - utter_email_bool
* email_affirm_no
    - utter_mail_not_send
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete

## interactive_story_1
* restaurant_search_details{"price": "between 300 and 900"}
    - slot{"price": "between 300 and 900"}
    - action_is_Price_Available
    - slot{"price": null}
    - slot{"price_class": null}
* restaurant_search_details{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_is_Price_Available
    - slot{"price_class": "Med"}
    - utter_ask_location
* restaurant_search_details{"location": "dindigul"}
    - slot{"location": "dindigul"}
    - action_is_Location_Available
    - slot{"location": null}
* restaurant_search_details{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_is_Location_Available
    - utter_ask_cuisine
* restaurant_search_details{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_is_Cuisine_Available
    - slot{"cuisine": null}
* restaurant_search_details{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_is_Cuisine_Available
    - action_search_restaurants
    - utter_email_bool
* goodbye
    - utter_goodbye
    - action_Dialogue_Complete