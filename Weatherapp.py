

import tkinter as tk
from tkinter import ttk
import requests


root = tk.Tk()
root.title("Weather App")
root.geometry("500x500")
root.config(bg="blue")

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=32762c95e3fcd58d604aa423e5d23f25").json()
    weather_climate_value.config(text=data["weather"][0]["main"])
    weather_description_value.config(text=data["weather"][0]["description"])
    weather_temprature_value.config(text=str(int(data["main"]["temp"]-273.15)))
    weather_pressure_value.config(text=data["main"]["pressure"])
    

title_label = tk.Label(root, text="Weather App",font=("Poppins",24,"bold"),bg="light gray",fg="black")
title_label.place(x=120,y=30,width=260,height=50)


city_label = [
    "Andhra Pradesh",
    "Nashik",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttarakhand",
    "Uttar Pradesh",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli",
    "Daman and Diu",
    "Delhi",
    "Lakshadweep",
    "Puducherry"
]

city_name = tk.StringVar()
com = ttk.Combobox(root,values=city_label,font=("Poppins",13),textvariable=city_name)
com.place(x=80, y=100, width=340 , height=40)

click_btn = tk.Button(root,text="Show Details", font=("Poppins",13),bg="white",fg="black",relief="raise",command = data_get)
click_btn.place(x=200,y=160,width=100,height=40)

weather_climate_label = tk.Label(root,text="Weather Climate", font=("Poppins", 13,"bold"),bg="light gray",fg="black",relief="solid")
weather_climate_label.place(x=50,y=220, width=200, height=40)
weather_climate_value = tk.Label(root,text="", font=("Poppins" , 13),bg="white",fg="black",relief="solid")
weather_climate_value.place(x=260,y=220, width=200, height=40)

weather_description_label = tk.Label(root,text="Weather Description", font=("Poppins", 13,"bold"),bg="light gray",fg="black",relief="solid")
weather_description_label.place(x=50,y=270, width=200, height=40)
weather_description_value = tk.Label(root,text="", font=("Poppins", 13),bg="white",fg="black",relief="solid")
weather_description_value.place(x=260,y=270, width=200, height=40)

weather_temperature_label = tk.Label(root,text="Weather Temperature", font=("Poppins", 13,"bold"),bg="light gray",fg="black",relief="solid")
weather_temperature_label.place(x=50,y=320, width=200, height=40)
weather_temprature_value = tk.Label(root,text="", font=("Poppins" , 13),bg="white",fg="black",relief="solid")
weather_temprature_value.place(x=260,y=320, width=200, height=40)

weather_pressure_label = tk.Label(root,text="Weather Pressure", font=("Poppins", 13,"bold"),bg="light gray",fg="black",relief="solid")
weather_pressure_label.place(x=50,y=370, width=200, height=40)
weather_pressure_value = tk.Label(root,text="", font=("Poppins", 13),bg="white",fg="black",relief="solid")
weather_pressure_value.place(x=260,y=370, width=200, height=40)

tk.mainloop()


 