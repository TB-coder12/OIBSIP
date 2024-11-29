from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox

def data_get():
    city = city_name.get()
    if city == "":
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    api_key = "b0450a32baefd0d1303340ae46eb6c05"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        data = requests.get(base_url).json()
        
        if data["cod"] != "404":
            # Extract weather data
            weather = data["weather"][0]
            main = data["main"]
            wind = data["wind"]
            
            # Update labels with the fetched data
            w_label1.config(text=weather["main"])
            wb_label1.config(text=weather["description"])
            temp_label1.config(text=f"{main['temp'] - 273.15:.2f}°C")
            humidity_label1.config(text=f"{main['humidity']}%")
            pressure_label1.config(text=f"{main['pressure']} hPa")
            wind_label1.config(text=f"{wind['speed']} m/s")
            
        else:
            w_label1.config(text="City not found")
            wb_label1.config(text="")
            temp_label1.config(text="")
            humidity_label1.config(text="")
            pressure_label1.config(text="")
            wind_label1.config(text="")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", f"Error fetching weather data: {e}")

win = Tk()
win.title("Global Weather App")
win.config(bg="green")
win.geometry("600x700")

# Title
name_label = Label(win, text="GLOBAL WEATHER APP", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=25, height=50, width=550)

# City entry field
city_name = StringVar()
city_entry = Entry(win, textvariable=city_name, font=("Times New Roman", 20, "bold"))
city_entry.place(x=25, y=120, height=50, width=550)

# Weather data labels
w_label = Label(win, text="Weather Condition", font=("Times New Roman", 18))
w_label.place(x=25, y=250, height=50, width=250)
w_label1 = Label(win, text="", font=("Times New Roman", 18))
w_label1.place(x=300, y=250, height=50, width=250)

wb_label = Label(win, text="Weather Description", font=("Times New Roman", 15))
wb_label.place(x=25, y=320, height=50, width=250)
wb_label1 = Label(win, text="", font=("Times New Roman", 15))
wb_label1.place(x=300, y=320, height=50, width=250)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 15))
temp_label.place(x=25, y=390, height=50, width=250)
temp_label1 = Label(win, text="", font=("Times New Roman", 15))
temp_label1.place(x=300, y=390, height=50, width=250)

humidity_label = Label(win, text="Humidity", font=("Times New Roman", 15))
humidity_label.place(x=25, y=460, height=50, width=250)
humidity_label1 = Label(win, text="", font=("Times New Roman", 15))
humidity_label1.place(x=300, y=460, height=50, width=250)

pressure_label = Label(win, text="Pressure", font=("Times New Roman", 15))
pressure_label.place(x=25, y=530, height=50, width=250)
pressure_label1 = Label(win, text="", font=("Times New Roman", 15))
pressure_label1.place(x=300, y=530, height=50, width=250)

wind_label = Label(win, text="Wind Speed", font=("Times New Roman", 15))
wind_label.place(x=25, y=600, height=50, width=250)
wind_label1 = Label(win, text="", font=("Times New Roman", 15))
wind_label1.place(x=300, y=600, height=50, width=250)

# Done button
done_button = Button(win, text="Check Weather", font=("Times New Roman", 20, "bold"), command=data_get)
done_button.place(y=190, height=50, width=200, x=200)

win.mainloop()
