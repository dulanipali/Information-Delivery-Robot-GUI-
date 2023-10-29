from tkinter import *
import requests
import json
#from PIL import ImageTk, Image

# Will it rain?
#Temperature - done
#Flood warning? Snow? Black ice warning?

def generateWeather():
    wroot = Tk()

    request = "https://api.weatherbit.io/v2.0/current?lat=33.584455714451366&lon=-101.87821782989839&key=ff208caa987b4800b4b54a502b104752&include=minutely,alerts"

    response = requests.get(request)
    weather_data = json.loads(response.content)

    #weather_data = {"count":1,"data":[{"app_temp":25.4,"aqi":10,"city_name":"Lubbock","clouds":0,"country_code":"US","datetime":"2023-03-23:00","dewpt":-3.3,"dhi":57.7,"dni":540.41,"elev_angle":11.8,"ghi":160.43,"gust":8.9,"h_angle":64.3,"lat":33.5845,"lon":-101.8782,"ob_time":"2023-03-23 00:00","pod":"d","precip":0,"pres":906.2,"rh":14,"slp":1012.9,"snow":0,"solar_rad":160.4,"sources":["1810W"],"state_code":"TX","station":"1810W","sunrise":"12:46","sunset":"01:00","temp":26.3,"timezone":"America/Chicago","ts":1679529600,"uv":1.8671794,"vis":16,"weather":{"icon":"c01d","description":"Clear sky","code":800},"wind_cdir":"WSW","wind_cdir_full":"west-southwest","wind_dir":254,"wind_spd":4.02}]}

    temp_c = weather_data["data"][0]["temp"]
    temp_f = temp_c*(9/5) + 32
    icon = weather_data["data"][0]["weather"]["icon"]
    description = weather_data["data"][0]["weather"]["description"]
    wind_spd = weather_data["data"][0]["wind_spd"]

    
    dataLabel = Label(wroot, text="Temperature "+ str(temp_c) + "C / " + str(temp_f)+ " F" + "\n" + description + "\t"+ icon + "\n" + str(wind_spd))
    dataLabel.pack()

    wroot.mainloop()

if __name__ == "__main__":
    generateWeather()
