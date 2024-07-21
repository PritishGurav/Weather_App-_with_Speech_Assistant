import pyttsx3
import datetime
from tkinter import *
from tkinter import ttk
import requests



engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good Evening!")

    speak("Where do you want to known the weather report")


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=694882066401cee13648ed6813252998").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Pgurav Tech")
win.config(bg="blue")
win.geometry("500x570")

name_label = Label(win,text="Weather App",fg="yellow",bg="black",
                   font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Pgurav Whether App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

done_button = Button(win,text="Weather Climate",bg="yellow",
                   font=("Time New Roman",20))
done_button.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win,text="",bg="black",fg="white",
                   font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)


done_button = Button(win,text="Weather Description",bg="yellow",
                   font=("Time New Roman",17))
done_button.place(x=25,y=330,height=50,width=210)
wb_label1 = Label(win,text="",bg="black",fg="white",
                  font=("Time New Roman",17))
wb_label1.place(x=250,y=330,height=50,width=210)


done_button = Button(win,text="Temperature",bg="yellow",
                   font=("Time New Roman",20))
done_button.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="",bg="black",fg="white",
                   font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)

done_button = Button(win,text="Pressure",bg="yellow",
                   font=("Time New Roman",20))
done_button.place(x=25,y=470,height=50,width=210)
per_label1 = Label(win,text="",bg="black",fg="White",
                   font=("Time New Roman",20))
per_label1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Done",bg="White",
                   font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)


if __name__=="__main__":
    speak("Wellcome to our weather report app")
    wishMe()

win.mainloop()


