

import json, requests, time 
import datetime #used for date and time
import pyttsx3 #Text to speech engine, requires a pip install to work
from Config import api_key #You will need your own Config file
engine = pyttsx3.init() #starts the Text to speech engine

#engine.say("This is a test sequence")
#engine.runAndWait()

#VARIABLES
temp_list = [] #empty list to record the temps change over time

#FUNCTIONS 

def wait(x): #useless function that just renames time.sleep()
    return time.sleep(x)

def convert_temp(x): #converts temperature to F
    a = x - 273.15
    b = a * 9
    c = b / 5
    d = c + 32
    return round(d)

def weather(city_name): #main API request function
    t = datetime.datetime.now() #pull time

    print(t) #print time

    api_kei = api_key #grab API key from Config file

    base_url = "http://api.openweathermap.org/data/2.5/weather?" #base URL for API requests

    print("From {}".format(city_name)) #print the city name to console

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name #build the request URL
    

    response = requests.get(complete_url) #request the Json
    dec = response.json() #convert the JSON

    if dec["cod"] != "404": #start picking apart the Json and saving the Variables 
        y = dec["main"] #access the main section

        current_temp = y["temp"] #grab the temp

        current_pressure = y["pressure"] #grab pressure

        current_humidity = y["humidity"] #grab humidity 

        z = dec["weather"] #access the weather section

        weather_description = z[0]["description"] #grab the weather description

        temp = convert_temp(current_temp) #convert the temp to a new unit
        
        msg = "The weather in {} is...\n{} Degrees\n{} Percent humidity\n{}\n".format(city_name, temp, current_humidity, weather_description)
        engine.say(msg) #TEXt to speech woooooo
        print(msg) #print to console 
        engine.runAndWait() #not sure i need this.
        
        temp_list.append(temp)
        print(temp_list)
        print("\n")

    else:
        print("Could not find city")
        wait(2)
        city = input("please enter the name of the nearest major city:  ")
        while True:
            weather(city) #Ew recursion, why did i do this  but it works soooo
            wait(3000)
   
#ACTUAL CODE THAT RUNS.
#The part that actually runs is right here.   Everything above are functions i can call.
 
city = input("please enter the name of the nearest major city:  ") #asks user for a city name they want via command line


while True: #forever loop
    weather(city) #runs the weather function with city as argument 
    wait(300) #waits 5 mins before looping.  this is the same as time.sleep(300)