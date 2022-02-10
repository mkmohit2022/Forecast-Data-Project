import requests

latitude=str(input("Enter the location Latitue: "))
longitude=str(input("Enter the location Longitude: "))
  
# api call
URL = "https://api.weather.gov/points/"+latitude+","+longitude


  
#calling api url
response1 = requests.get(url = URL)

if response1.status_code==200:
  
    # extracting response in json format

    data = response1.json()
    
    #fetching forecast url
    forecast_url=data["properties"]["forecast"]

    #calling forecast api endpoint
    response2=requests.get(url = forecast_url)

    if response2.status_code==200:       
        #reading the response from forecast api
        data2=response2.json()

        for i in range(len(data2["properties"]["periods"])):
            if data2["properties"]["periods"][i]["name"]=="Wednesday Night":
                #printing the forecast result
                print("Forecast Temperature on upcoming "+data2["properties"]["periods"][i]["name"]+" will be "+str(data2["properties"]["periods"][i]["temperature"])+" "+data2["properties"]["periods"][i]["temperatureUnit"])
                break
    else:
        print("Sorry could not fetch data currently")
else:
    print("Please check the Latitude and Logitue provided")
