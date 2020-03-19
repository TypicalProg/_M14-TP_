from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from tkinter import messagebox

root = Tk()
root.title("Главное меню")

def new_win():
	root = Tk()
	root.title("О программе")
	root.resizable(0, 0)

	lbl1 = Label(root, text='© Michurin Andrey 2020\n'
		'Все вопросы задавать в разделе "Обратная связь"',
		 fg='blue', bg='white')
	lbl1.grid(row=0, column=0)

	root.mainloop()

def feedback():
	root = Tk()
	root.title("Обратная связь")
	root.resizable(0, 0)

	def send(event):
		def send_mail():
		    # Логин
		    login = " "
		    # Пароль
		    password = " "
		    # Сервер
		    url = " "
		    # Кому
		    toaddr = " "

		    msg = MIMEMultipart()
		    # Тема
		    theme = tema_ent.get()
		    msg['Subject'] = '-=Feedback from _M14-TP_=-    ' + theme
		    # От кого
		    msg['From'] = login
		    # Текст письма
		    leter = txt_ent.get(1.0, END)
		    body = leter
		    msg.attach(MIMEText(body, 'plain'))

		    try:
		        server = smtplib.SMTP_SSL(url, 465)
		    except TimeoutError:
		        print('No connect')
		    server.login(login, password)
		    server.sendmail(login, toaddr, msg.as_string())

		    messagebox.showinfo("Успешно!", "Письмо отправлено! \nСпасибо за отзывчивость!")


		def main():
		    send_mail()

		if __name__ == "__main__":
		    main()


	lbl1 = Label(root, text='Обратная связь', font='12')
	tema = Label(root, text='Тема', font='11')
	tema_ent = Entry(root, font='11')
	text = Label(root, text='Текст сообщения', font='11')
	txt_ent = Text(root, width=15, height=5, font=12)
	send_btn = Button(root, text='Отправить', font='10')

	lbl1.grid(row=0, columnspan=2)
	tema.grid(row=1, columnspan=2)
	tema_ent.grid(row=2, columnspan=2)
	text.grid(row=3, columnspan=2)
	txt_ent.grid(row=4, columnspan=2)
	send_btn.grid(row=5, columnspan=2)

	send_btn.bind("<Button-1>", send)

	root.mainloop()

def calc(event):
	os.startfile(r'calc.exe')

def kal(event):
	os.startfile(r'Calendar.exe')

def sec(event):
	os.startfile(r'stopwatch.exe')

def txtRED(event):
	os.startfile(r'Text_editor.exe')

def wea(event):
	os.startfile(r'Weather_gui.exe')

def ball_def(event):
	os.startfile(r'balls.exe')

def ttt_def(event):
	os.startfile(r'tic_tac_toe.exe')

def snake_def(event):
	os.startfile(r'Змейка.exe')

def pp_def(event):
	os.startfile(r'Пин-понг.exe')

def game(event):
	root = Tk()
	root.title("Игры")

	lbl1 = Label(root, text='Выбор игры', font=20)
	ball = Button(root, text='Арканоид', font=20)
	ttt = Button(root, text='Крестики-\nнолики', font=20)
	snake = Button(root, text='Змейка', font=20)
	pp = Button(root, text="Пин-понг\n(на двоих)", font=20)

	lbl1.grid(row=0, columnspan=2)
	ball.grid(row=1, column=0, sticky=N+S+W+E)
	ttt.grid(row=1, column=1)
	snake.grid(row=2, column=0, sticky=N+S+W+E)
	pp.grid(row=2, column=1)

	ball.bind("<Button-1>", ball_def)
	ttt.bind("<Button-1>", ttt_def)
	snake.bind("<Button-1>", snake_def)
	pp.bind("<Button-1>", pp_def)


main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Помощь", menu=first_item)
first_item.add_command(label="О программе", command=new_win)
first_item.add_command(label="Обратная связь", command=feedback)

tit = Label(root, text="_M14-TP_", font=30)
calc_btn = Button(root, text="Калькулятор", font=30)
kal_btn = Button(root, text="Календарь", font=30)
sec_btn = Button(root, text="Секундомер", font=30)
txtRED_btn = Button(root, text="Текстовый\nредактор", font=30)
wea_btn = Button(root, text="Погода", font=30)
game_btn = Button(root, text="Игры", font=30)

tit.grid(row=0, columnspan=2)
calc_btn.grid(row=1, column=0)
kal_btn.grid(row=1, column=1)
sec_btn.grid(row=2, column=0, sticky=N+S+W+E)
txtRED_btn.grid(row=2, column=1)
wea_btn.grid(row=3, column=0, sticky=N+S+W+E)
game_btn.grid(row=3, column=1, sticky=N+S+W+E)

calc_btn.bind("<Button-1>", calc)
kal_btn.bind("<Button-1>", kal)
sec_btn.bind("<Button-1>", sec)
txtRED_btn.bind("<Button-1>", txtRED)
wea_btn.bind("<Button-1>", wea)
game_btn.bind("<Button-1>", game)

root.mainloop()
