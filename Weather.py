# importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

def getNotification():
    cityName = place.get()  # getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # base url from where we extract weather report
    try:
        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(url)  # ✅ fixed variable name here
        x = response.json()  # converting it into json 

        if x["cod"] != 200:
            mb.showerror('Error', f"City '{cityName}' not found!")
            return

        y = x["main"]  # getting the "main" key from the json object
        temp = y["temp"] - 273.15  # converting temperature from kelvin to celsius
        pres = y["pressure"]
        hum = y["humidity"]
        weather_desc = x["weather"][0]["description"]

        # combining the above values as a string 
        info = (
            f"Here is the weather description of {cityName}:\n"
            f"Temperature = {temp:.2f}°C\n"
            f"Atmospheric Pressure = {pres} hPa\n"
            f"Humidity = {hum}%\n"
            f"Description = {weather_desc.title()}"
        )

        # showing the notification 
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,
            timeout=5  # seconds
        )
        time.sleep(5)

    except Exception as e:
        mb.showerror('Error', str(e))  # show pop up message if any error occurred


# creating the window
wn = Tk()
wn.title("Weather Desktop Notifier")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="Python Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=120, y=15)

# Getting the place name 
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

# Button to get notification
Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification).place(relx=0.4, rely=0.75)

# run the window till closed by user
wn.mainloop()
