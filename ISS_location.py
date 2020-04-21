import urllib.parse     # These needs to be pip installed and imported before running.
import requests         #   
import datetime         #    
import time             #


main_api = "http://api.open-notify.org/iss-pass.json?" # These are the source url's that this program use to get information about ISS Spaceship
second_api = "http://api.open-notify.org/astros.json"  #
third_api = "http://api.open-notify.org/iss-now.json"  #


while True:
    lat = input("This is application that shows how many times ISS will pass specific location in next 24 hours. Insert first coordinate (lat), (or quit by ""q""): ") # Latitude needs to be set.
    if lat == "quit" or lat == "q":
        break
    lon = input("Insert second coordinate (lon), (or quit by ""q""): ") # Longitude needs to be set.
    if lon == "quit" or lon == "q":
        break
    inspace = input("Do you want to know how many people are in the space at the moment? y/n: ") # This asks user if they want to see how many people are in the space at the moment.

    loc = input ("Do you want to know which location ISS is at the moment? y/n: ") # This gives exact lat and lon, where the ISS Spaceship is at the moment.
    
    url = main_api + urllib.parse.urlencode({"lat":lat,"lon":lon}) # This is the main url, that is used to get information. Takes user inputs lat and lon and paste it into the url with urllib.parse library.
    json_data = requests.get(url).json() # Sets the request to the API.
    print("URL: " + (url)) # Prints used url.
    json_status = json_data["message"] # API Status.

    url2 = second_api # Second url that is used to get information.
    json_data2 = requests.get(url2).json() # Sets the request to the API.
    print("URL: " + (url2)) # Prints used url.
    json_status2 = json_data2["message"] # Second API Status.

    url3 = third_api # Third url that is used to get information.
    json_data3 = requests.get(url3).json() # Sets request to the API.
    print("URL: " + (url3)) # Prints used url.
    json_status3 = json_data3["message"] # Third API Status.
    
    print("==============================================") # I'm printing these, to make the output more clear for user.

    if json_status == "success": # If first API status is OK and API is available, program will continue. 
        print("API Status: " + str(json_status) + " = A successful route call. \n") # Prints the status.
        print("ISS will pass inputted location: " + str(json_data["request"]["passes"])+ " time(s)") # Prints the first 5 times the ISS Spaceship is going to pass given location from the time request is made.
        for each in json_data ["response"]: #
            print (time.ctime(each["risetime"])) #

    print("==============================================") # I'm printing these, to make the output more clear for user.
    
    if json_status2 == "success" and inspace == "y": # If first API status is OK and API is available and user wants to see number of people in the space, program will continue.
        print("There is " + str(json_data2["number"]) + " people(s) in space at the moment. And their names are: ") # This prints names of the people in the space with separator '\n'.
        for each in json_data2 ["people"]: #
            print (each["name"]) #
        
    print("==============================================") # I'm printing these, to make the output more clear for user.

    if json_status3 == "success" and loc == "y": # If first API status is OK and API is available and user wants to see number of people in the space, program will continue.
        print(("Current location of the ISS is: ") + str(json_data3["iss_position"]["latitude"])+ " (lat)" + " & " + str(json_data3["iss_position"]["longitude"]) + " (lon)") # This tells current location of the ISS Spaceship.
       
    print("==============================================") # I'm printing these, to make the output more clear for user.
            
    
