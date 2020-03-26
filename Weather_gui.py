from tkinter import *
import pyowm
from tkinter import messagebox

root = Tk()
root.title("Погода")

def weather(event):
	try:
		place = city_ent.get()
		owm = pyowm.OWM("6d00d1d4e704068d70191bad2673e0cc", language="ru")
		observation = owm.weather_at_place(place)
		w = observation.get_weather()
		temp = w.get_temperature("celsius")["temp"]

		lbl1['text'] = "В городе " + place + " сейчас"
		lbl2['text'] = w.get_detailed_status()
		lbl3['text'] = "Температура ≈ " + str(temp) + "°C"
	except Exception as e:
		        messagebox.showinfo("Ошибка!", 
"""Произошла непредвиденная ошибка!
Повторите попытку позже!

###############
Возможные варианты решения проблемы:
>Проверьте подключение к интернету
>Проверьте правильно ли написано назавание населенного пункта
>Если ничего из вышеперечисленного не помогает, 
напишите нам через форму обратной связи""")


tit = Label(root, text='Погода', font=20)
city_txt = Label(root, text='Введите город', font=15)
city_ent = Entry(root, font=15)
lbl1 = Label(root, font=15)
lbl2 = Label(root, font=15)
lbl3 = Label(root, font=15)
btn1 = Button(root, text='Узнать погоду', font=10)

tit.grid(row=0, column=0)
city_txt.grid(row=1, column=0)
city_ent.grid(row=2, column=0)
lbl1.grid(row=3, column=0)
lbl2.grid(row=4, column=0)
lbl3.grid(row=5, column=0)
btn1.grid(row=6, column=0)

btn1.bind("<Button-1>", weather)

root.mainloop()