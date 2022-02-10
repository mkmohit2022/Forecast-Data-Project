# Forecast-Data-Project

This repository contains Weather forecast project using an API call. This applications takes in the latitude and longitude value as an input and provide the next day weather forecast temperature as an output.

The application is developmed in two independent ways- one using python and other one using dynamic webpage(javascript and jQuery). 
In Both of the above mentioned methods, the latitude and longitude values entered by user is set with weather API and an API call is made and when gets a successfull response, the forecast data is displayed, else the message is shown up to user for entering correct location details

Using the application using Dynamic Webpage method (index.html) file:

The index.html file needs to be run on any browser which in turn provide the front end view where the user can provide the latitude and longitude values.
After entering the required inputs, once user clicks on 'Fetch Forecast Data' button, the forecast results gets displayed below it. 

Using the application using python file:
Before running the python file, one python package is required to be installed which is 'requests' package (pip install requests)
Once the package is installed, the python file can run on python platform. Once it complies and runs, it will require user to enter Latitude and Longitude values as and input to the application and once enters the details, it will provide the forecast data.



