import tkinter as tk
from tkinter import messagebox
import requests


API_KEY = "3f3ec6c0e61ca9e2e3beb28a4841af21"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()

        result_label.config(
            text=f"City: {city.title()}\n\n"
                 f"Temperature: {temp}°C\n"
                 f"Feels Like: {feels_like}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Weather: {weather}"
        )

    except:
        messagebox.showerror("Error", "Network Error")


# ---------------- UI DESIGN ----------------

root = tk.Tk()
root.title("Professional Weather App")
root.geometry("420x520")
root.config(bg="#0f172a")

title_label = tk.Label(
    root, text="🌦️ Weather Application",
    font=("Poppins", 18, "bold"),
    bg="#0f172a", fg="white"
)
title_label.pack(pady=15)

city_entry = tk.Entry(
    root, font=("Poppins", 14),
    justify="center", width=22
)
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

get_btn = tk.Button(
    root, text="Get Weather",
    font=("Poppins", 13, "bold"),
    bg="#38bdf8", fg="black",
    width=15, command=get_weather
)
get_btn.pack(pady=10)

result_label = tk.Label(
    root, text="",
    font=("Poppins", 13),
    bg="#1e293b", fg="white",
    width=32, height=10, justify="center"
)
result_label.pack(pady=20)

footer = tk.Label(
    root, text="Made using Python",
    font=("Poppins", 9),
    bg="#0f172a", fg="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()

