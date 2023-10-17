''' The goal of this project is to create a weather app that
shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Done - Use the requests library to make an API call to a
    weather service (e.g. OpenWeatherMap) to retrieve
    the weather data for a specific location.

    Done - Use the json library to parse the JSON data returned by the API call.

    Done - Use the tkinter library to create a GUI for the app,
    including widgets such as labels, buttons and text boxes.

    Done - Use the Pillow library to display the weather icons.

    Done - Use the datetime library to display the current time and date. '''

# https://openweathermap.org/find?q=berlin
# Berlin, DE
# Latitude 52.5244
# Longitude 13.4105
# The OpenWeatherMap API returns the weather data for Mitte sometimes,
# for these coordinates, instead of the data for Berlin.

# https://openweathermap.org/find?q=bremen
# Bremen, DE
# Latitude 53.0752
# Longitude 8.8078

# After starting the app, accessing 'Edit', then 'Change location coordinates'
# opens a window where the app can receive latitude and longitude values.
# After clicking the 'Apply' button, the app
# displays weather data from different locations during runtime.
# Accessing 'File', then 'Refresh data', the app will display
# updated information about the location coordinates in use.
# 'File', then 'Exit' will exit the window.


import requests
import json
import tkinter as tk
from PIL import ImageTk, Image
from io import BytesIO
import datetime


class WeatherApp:

    labelTime = None
    labelLongitude = None
    labelLatitude = None
    labelWeatherId = None
    labelMain = None
    labelDescription = None
    iconCode = None
    weatherIconRequest = None
    weatherIcon = None
    weatherIconPhotoImage = None
    weatherIconLabel = None
    labelWeatherBase = None
    labelTemperature = None
    labelTemperatureFeelsLike = None
    labelTempMin = None
    labelTempMax = None
    labelPressure = None
    labelWeatherHumidity = None
    labelSeparator = None
    labelSeparator2 = None
    labelWeatherVisibility = None
    labelWindSpeed = None
    labelWindDeg = None
    labelSeparator3 = None
    labelClouds = None
    labelWeatherDt = None
    labelSysType = None
    labelSysId = None
    labelSysCountry = None
    labelSysSunrise = None
    labelSysSunset = None
    labelTimezone = None
    labelID = None
    labelName = None
    labelCod = None
    dataDict = None

    def setObtainedDataInDict(self, latitude="52.5244", longitude="13.4105"):
        requestAddress = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID=586d685517e2a294c0682f5465b95ef7&units=metric"
        print(requestAddress)
        response = requests.get(requestAddress)
        # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
        # https://openweathermap.org/weathermap?zoom=12&lat=52.5244&lon=13.4105

        self.dataDict = json.loads(response.text)
        print(self.dataDict)

    def initiateLabels(self):
        time = datetime.datetime.now()
        timeFormatted = time.strftime("%d-%m-%Y %H:%M:%S")
        # print(timeFormatted)
        # labelCoord = tk.Label(root, text=f"Location coordinates: {self.dataDict['coord']}")
        self.labelTime = tk.Label(root, text=f"Time: {timeFormatted}")
        self.labelLongitude = tk.Label(root, text=f"Longitude: {self.dataDict['coord']['lon']}")
        self.labelLatitude = tk.Label(root, text=f"Latitude: {self.dataDict['coord']['lat']}")
        self.labelWeatherId = tk.Label(root, text=f"Weather ID: {self.dataDict['weather'][0]['id']}")
        self.labelMain = tk.Label(root, text=f"Main: {self.dataDict['weather'][0]['main']}")
        self.labelDescription = tk.Label(root, text=f"Description: {self.dataDict['weather'][0]['description']}")
        self.iconCode = self.dataDict['weather'][0]['icon']
        self.weatherIconRequest = requests.get("https://openweathermap.org/img/wn/" + self.iconCode + "@2x.png")
        # print(weatherIconRequest.content)
        self.weatherIcon = Image.open(BytesIO(self.weatherIconRequest.content))
        # weatherIcon.show()
        self.weatherIconPhotoImage = ImageTk.PhotoImage(self.weatherIcon)
        self.weatherIconLabel = tk.Label(root, image=self.weatherIconPhotoImage)
        self.weatherIconLabel.image = self.weatherIconPhotoImage
        self.weatherIconLabel.config(background="lightblue")
        self.labelWeatherBase = tk.Label(root, text=f"Base: {self.dataDict['base']}")
        self.labelTemperature = tk.Label(root, text=f"Temperature (Celsius): {self.dataDict['main']['temp']}")
        self.labelTemperatureFeelsLike = tk.Label(root, text=f"Feels like (Celsius): {self.dataDict['main']['feels_like']}")
        self.labelTempMin = tk.Label(root, text=f"Minimum temperature (Celsius): {self.dataDict['main']['temp_min']}")
        self.labelTempMax = tk.Label(root, text=f"Maximum temperature (Celsius): {self.dataDict['main']['temp_max']}")
        self.labelPressure = tk.Label(root, text=f"Pressure: {self.dataDict['main']['pressure']} hPa")
        self.labelWeatherHumidity = tk.Label(root, text=f"Humidity: {self.dataDict['main']['humidity']}%")
        self.labelSeparator = tk.Label(root, text="")
        self.labelSeparator2 = tk.Label(root, text="")
        self.labelWeatherVisibility = tk.Label(root, text=f"Visibility: {self.dataDict['visibility']} m")
        self.labelWindSpeed = tk.Label(root, text=f"Wind speed: {self.dataDict['wind']['speed']}")
        self.labelWindDeg = tk.Label(root, text=f"Wind deg: {self.dataDict['wind']['deg']}")
        # labelWindGust = tk.Label(root, text=f"Wind gust: {self.dataDict['wind']['gust']}")
        self.labelSeparator3 = tk.Label(root, text="")
        self.labelClouds = tk.Label(root, text=f"Clouds: {self.dataDict['clouds']['all']}")
        self.labelWeatherDt = tk.Label(root, text=f"Dt: {self.dataDict['dt']}")
        self.labelSysType = tk.Label(root, text=f"Type: {self.dataDict['sys']['type']}")
        self.labelSysId = tk.Label(root, text=f"Sys Id: {self.dataDict['sys']['id']}")
        self.labelSysCountry = tk.Label(root, text=f"Country: {self.dataDict['sys']['country']}")
        self.labelSysSunrise = tk.Label(root, text=f"Sunrise: {self.dataDict['sys']['sunrise']}")
        self.labelSysSunset = tk.Label(root, text=f"Sunset: {self.dataDict['sys']['sunset']}")
        self.labelTimezone = tk.Label(root, text=f"Timezone: {self.dataDict['timezone']}")
        self.labelID = tk.Label(root, text=f"ID: {self.dataDict['id']}")
        self.labelName = tk.Label(root, text=f"Name: {self.dataDict['name']}")
        self.labelCod = tk.Label(root, text=f"Cod: {self.dataDict['cod']}")

    def packLabels(self):
        self.weatherIconLabel.pack()
        self.labelName.config(background="lightblue")
        self.labelName.pack()
        self.labelSysCountry.config(background="lightblue")
        self.labelSysCountry.pack()
        self.labelTime.config(background="lightblue")
        self.labelTime.pack()
        self.labelDescription.config(background="lightblue")
        self.labelDescription.pack()
        self.labelSeparator.config(background="lightblue")
        self.labelSeparator.pack()
        self.labelTemperature.config(background="lightblue")
        self.labelTemperature.pack()
        self.labelTemperatureFeelsLike.config(background="lightblue")
        self.labelTemperatureFeelsLike.pack()
        self.labelTempMin.config(background="lightblue")
        self.labelTempMin.pack()
        self.labelTempMax.config(background="lightblue")
        self.labelTempMax.pack()
        self.labelPressure.config(background="lightblue")
        self.labelPressure.pack()
        self.labelWeatherHumidity.config(background="lightblue")
        self.labelWeatherHumidity.pack()
        self.labelWeatherVisibility.config(background="lightblue")
        self.labelWeatherVisibility.pack()
        self.labelWindSpeed.config(background="lightblue")
        self.labelWindSpeed.pack()
        self.labelWindDeg.config(background="lightblue")
        self.labelWindDeg.pack()
        # labelWindGust.config(background="lightblue")
        # labelWindGust.pack()
        self.labelSeparator2.config(background="lightblue")
        self.labelSeparator2.pack()
        self.labelLatitude.config(background="lightblue")
        self.labelLatitude.pack()
        self.labelLongitude.config(background="lightblue")
        self.labelLongitude.pack()
        self.labelMain.config(background="lightblue")
        self.labelMain.pack()
        self.labelWeatherId.config(background="lightblue")
        self.labelWeatherId.pack()
        self.labelWeatherBase.config(background="lightblue")
        self.labelWeatherBase.pack()
        self.labelSeparator3.config(background="lightblue")
        self.labelSeparator3.pack()
        self.labelClouds.config(background="lightblue")
        self.labelClouds.pack()
        self.labelWeatherDt.config(background="lightblue")
        self.labelWeatherDt.pack()
        self.labelSysType.config(background="lightblue")
        self.labelSysType.pack()
        self.labelSysId.config(background="lightblue")
        self.labelSysId.pack()
        self.labelSysSunrise.config(background="lightblue")
        self.labelSysSunrise.pack()
        self.labelSysSunset.config(background="lightblue")
        self.labelSysSunset.pack()
        self.labelTimezone.config(background="lightblue")
        self.labelTimezone.pack()
        self.labelID.config(background="lightblue")
        self.labelID.pack()
        self.labelCod.config(background="lightblue")
        self.labelCod.pack()

    def refreshData(self, lat="", lon=""):
        # self.setObtainedDataInDict(latitude=lat, longitude=lon)
        time = datetime.datetime.now()
        timeFormatted = time.strftime("%d-%m-%Y %H:%M:%S")
        # print(timeFormatted)
        self.labelTime.config(text=f"Time: {timeFormatted}")
        self.labelLatitude.config(text=f"Latitude: {self.dataDict['coord']['lat']}")
        self.labelLongitude.config(text=f"Longitude: {self.dataDict['coord']['lon']}")
        self.labelWeatherId.config(text=f"Weather ID: {self.dataDict['weather'][0]['id']}")
        self.labelMain.config(text=f"Main: {self.dataDict['weather'][0]['main']}")
        self.labelDescription.config(text=f"Description: {self.dataDict['weather'][0]['description']}")
        self.iconCode = self.dataDict['weather'][0]['icon']
        self.weatherIconRequest = requests.get("https://openweathermap.org/img/wn/" + self.iconCode + "@2x.png")
        # print(weatherIconRequest.content)
        self.weatherIcon = Image.open(BytesIO(self.weatherIconRequest.content))
        # weatherIcon.show()
        self.weatherIconPhotoImage = ImageTk.PhotoImage(self.weatherIcon)
        self.weatherIconLabel.config(image=self.weatherIconPhotoImage)
        self.weatherIconLabel.image = self.weatherIconPhotoImage
        self.weatherIconLabel.config(background="lightblue")
        self.labelWeatherBase.config(text=f"Base: {self.dataDict['base']}")
        self.labelTemperature.config(text=f"Temperature (Celsius): {self.dataDict['main']['temp']}")
        self.labelTemperatureFeelsLike.config(text=f"Feels like (Celsius): {self.dataDict['main']['feels_like']}")
        self.labelTempMin.config(text=f"Minimum temperature (Celsius): {self.dataDict['main']['temp_min']}")
        self.labelTempMax.config(text=f"Maximum temperature (Celsius): {self.dataDict['main']['temp_max']}")
        self.labelPressure.config(text=f"Pressure: {self.dataDict['main']['pressure']} hPa")
        self.labelWeatherHumidity.config(text=f"Humidity: {self.dataDict['main']['humidity']}%")
        self.labelSeparator.config(text="")
        self.labelSeparator2.config(text="")
        self.labelWeatherVisibility.config(text=f"Visibility: {self.dataDict['visibility']} m")
        self.labelWindSpeed.config(text=f"Wind speed: {self.dataDict['wind']['speed']}")
        self.labelWindDeg.config(text=f"Wind deg: {self.dataDict['wind']['deg']}")
        # labelWindGust.config(text=f"Wind gust: {self.dataDict['wind']['gust']}")
        self.labelSeparator3.config(text="")
        self.labelClouds.config(text=f"Clouds: {self.dataDict['clouds']['all']}")
        self.labelWeatherDt.config(text=f"Dt: {self.dataDict['dt']}")
        self.labelSysType.config(text=f"Type: {self.dataDict['sys']['type']}")
        self.labelSysId.config(text=f"Sys Id: {self.dataDict['sys']['id']}")
        self.labelSysCountry.config(text=f"Country: {self.dataDict['sys']['country']}")
        self.labelSysSunrise.config(text=f"Sunrise: {self.dataDict['sys']['sunrise']}")
        self.labelSysSunset.config(text=f"Sunset: {self.dataDict['sys']['sunset']}")
        self.labelTimezone.config(text=f"Timezone: {self.dataDict['timezone']}")
        self.labelID.config(text=f"ID: {self.dataDict['id']}")
        self.labelName.config(text=f"Name: {self.dataDict['name']}")
        self.labelCod.config(text=f"Cod: {self.dataDict['cod']}")

    def applyButtonFunctionality(self, latitudeEntry, longitudeEntry, window):
        latitudeVal = latitudeEntry.get()
        print('latitudeVal: ', latitudeVal)
        longitudeVal = longitudeEntry.get()
        print('longitudeVal: ', longitudeVal)
        self.setObtainedDataInDict(latitudeVal, longitudeVal)
        self.refreshData()
        window.destroy()

    def changeLocationCoordinates(self):
        root2 = tk.Tk()
        root2.title("Change location coordinates")
        root2.config(background="lightblue")
        newLabelLatitude = tk.Label(root2, text=f"Latitude: ")
        newLabelLatitude.config(background='lightblue')
        newLabelLatitude.pack()
        latitudeEntry = tk.Entry(root2)
        latitudeEntry.pack()
        newLabelLongitude = tk.Label(root2, text=f"Longitude: ")
        newLabelLongitude.config(background='lightblue')
        newLabelLongitude.pack()
        longitudeEntry = tk.Entry(root2)
        longitudeEntry.pack()

        buttonApply = tk.Button(root2, text="Apply", command=lambda: self.applyButtonFunctionality(latitudeEntry, longitudeEntry, root2))
        buttonApply.pack(pady=5)

        root2.mainloop()


w = WeatherApp()

root = tk.Tk()
root.title("WeatherApp")

# latInit = '52.5244'
# lonInit = '13.4105'

menu = tk.Menu(root)
fileSection = tk.Menu(menu, tearoff=0)
fileSection.add_command(label="Refresh data", command=w.refreshData)#(lat = latInit, lon = lonInit))
fileSection.add_command(label="Exit", command=root.destroy)
menu.add_cascade(label="File", menu=fileSection)

editSection = tk.Menu(menu, tearoff=0)
editSection.add_command(label="Change location coordinates", command=w.changeLocationCoordinates)
menu.add_cascade(label="Edit", menu=editSection)

root.config(menu=menu)
root.config(background="lightblue")
w.setObtainedDataInDict()
w.initiateLabels()
w.packLabels()
# refreshButton = tk.Button(root, text="Refresh data", command=w.refreshData)
# refreshButton.pack()
root.mainloop()




