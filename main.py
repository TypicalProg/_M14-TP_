vvod = float(input("Введите пароль: "))
passw = 123

if vvod == passw:

    deystvie = input("Добро пожаловать в Программное Обеспечение _M14-TP_ \n"
          "Выбирете, что выхотите сделать:\n"
          "1 - Запустить калькулятор;\n"
          "2 - Посмотреть погоду;\n"
          "3 - Запустить календарь;\n"
          "4 - Игры\n"
          "Введите число действия!")

    # Калькулятор
    if deystvie == "1":
        from tkinter import *
        from decimal import *

        root = Tk()
        root.title('Calculator')

        buttons = (('7', '8', '9', '/', '4'),
                   ('4', '5', '6', '*', '4'),
                   ('1', '2', '3', '-', '4'),
                   ('0', '.', '=', '+', '4')
                   )

        activeStr = ' '
        stack = []


        def calculate():
            global stack
            global label
            result = 0
            operand2 = Decimal(stack.pop())
            operation = stack.pop()
            operand1 = Decimal(stack.pop())

            if operation == '+':
                result = operand1 + operand2
            if operation == '-':
                result = operand1 - operand2
            if operation == '/':
                result = operand1 / operand2
            if operation == '*':
                result = operand1 * operand2
            label.configure(text=str(result))


        def click(text):
            global activeStr
            global stack
            if text == 'CE':
                stack.clear()
                activeStr = ''
                label.configure(text='0')
            elif '0' <= text <= '9':
                activeStr += text
                label.configure(text=activeStr)
            elif text == '.':
                if activeStr.find('.') == -1:
                    activeStr += text
                    label.configure(text=activeStr)
            else:
                if len(stack) >= 2:
                    stack.append(label['text'])
                    calculate()
                    stack.clear()
                    stack.append(label['text'])
                    activeStr = ''
                    if text != '=':
                        stack.append(text)
                else:
                    if text != '=':
                        stack.append(label['text'])
                        stack.append(text)
                        activeStr = ''
                        label.configure(text='0')


        label = Label(root, text='0', width=35)
        label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        button = Button(root, text='CE', command=lambda text='CE': click(text))
        button.grid(row=1, column=3, sticky="nsew")
        for row in range(4):
            for col in range(4):
                button = Button(root, text=buttons[row][col],
                                command=lambda row=row, col=col: click(buttons[row][col]))
                button.grid(row=row + 2, column=col, sticky="nsew")

        root.grid_rowconfigure(6, weight=1)
        root.grid_columnconfigure(4, weight=1)

        root.mainloop()

    elif deystvie == "2":

        # Погода

        import pyowm

        owm = pyowm.OWM("6d00d1d4e704068d70191bad2673e0cc", language="ru")

        place = input("В каком городе?: ")

        observation = owm.weather_at_place(place)
        w = observation.get_weather()

        temp = w.get_temperature("celsius")["temp"]

        print("В городе " + place + " сейчас " + w.get_detailed_status())
        print("Температура сейчас в районе " + str(temp))

        if temp < 10:
            print("Сейчас ппц как холодно, одевайтесь как танк!")
        elif temp < 20:
            print("Сейчас прохладно, оденься теплее!")
        else:
            print("Температура норм, одевай что угодно!\n")

        input("Нажмите <Enter> чтобы закрыть программу")

    elif deystvie == "3":

        # Календарь
        from tkinter import *
        import calendar
        import datetime

        root = Tk()
        root.title('Calendar')
        days = []
        now = datetime.datetime.now()
        year = now.year
        month = now.month


        def prew():
            global month, year
            month -= 1
            if month == 0:
                month = 12
                year -= 1
            fill()


        def next():
            global month, year
            month += 1
            if month == 13:
                month = 1
                year += 1
            fill()


        def fill():
            info_label['text'] = calendar.month_name[month] + ', ' + str(year)
            month_days = calendar.monthrange(year, month)[1]
            if month == 1:
                prew_month_days = calendar.monthrange(year - 1, 12)[1]
            else:
                prew_month_days = calendar.monthrange(year, month - 1)[1]
            week_day = calendar.monthrange(year, month)[0]
            for n in range(month_days):
                days[n + week_day]['text'] = n + 1
                days[n + week_day]['fg'] = 'black'
                if year == now.year and month == now.month and n == now.day:
                    days[n + week_day]['background'] = 'green'
                else:
                    days[n + week_day]['background'] = 'lightgray'
            for n in range(week_day):
                days[week_day - n - 1]['text'] = prew_month_days - n
                days[week_day - n - 1]['fg'] = 'gray'
                days[week_day - n - 1]['background'] = '#f3f3f3'
            for n in range(6 * 7 - month_days - week_day):
                days[week_day + month_days + n]['text'] = n + 1
                days[week_day + month_days + n]['fg'] = 'gray'
                days[week_day + month_days + n]['background'] = '#f3f3f3'


        prew_button = Button(root, text='<', command=prew)
        prew_button.grid(row=0, column=0, sticky='nsew')
        next_button = Button(root, text='>', command=next)
        next_button.grid(row=0, column=6, sticky='nsew')
        info_label = Label(root, text='0', width=1, height=1,
                           font=('Verdana', 16, 'bold'), fg='blue')
        info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

        for n in range(7):
            lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1,
                        font=('Verdana', 10, 'normal'), fg='darkblue')
            lbl.grid(row=1, column=n, sticky='nsew')
        for row in range(6):
            for col in range(7):
                lbl = Label(root, text='0', width=4, height=2,
                            font=('Verdana', 16, 'bold'))
                lbl.grid(row=row + 2, column=col, sticky='nsew')
                days.append(lbl)
        fill()
        root.mainloop()

    elif deystvie == "4":

        game = input("В какую игру вы хотите сыграть?\n"
                           "1 - Змейка;\n"
                           "2 - Сапер;\n"
                           "3 - Пин-понг(игра на двоих);\n"
                           "4 - Крестики-нолики")

        if game == "1":
            from tkinter import Tk, Canvas
            import random

            # Globals
            WIDTH = 800
            HEIGHT = 600
            SEG_SIZE = 20
            IN_GAME = True


            # Helper functions
            def create_block():
                """ Creates an apple to be eaten """
                global BLOCK
                posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
                posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
                BLOCK = c.create_oval(posx, posy,
                                      posx + SEG_SIZE, posy + SEG_SIZE,
                                      fill="red")


            def main():
                """ Handles game process """
                global IN_GAME
                if IN_GAME:
                    s.move()
                    head_coords = c.coords(s.segments[-1].instance)
                    x1, y1, x2, y2 = head_coords
                    # Check for collision with gamefield edges
                    if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
                        IN_GAME = False
                    # Eating apples
                    elif head_coords == c.coords(BLOCK):
                        s.add_segment()
                        c.delete(BLOCK)
                        create_block()
                    # Self-eating
                    else:
                        for index in range(len(s.segments) - 1):
                            if head_coords == c.coords(s.segments[index].instance):
                                IN_GAME = False
                    root.after(100, main)
                # Not IN_GAME -> stop game and print message
                else:
                    set_state(restart_text, 'normal')
                    set_state(game_over_text, 'normal')


            class Segment(object):
                """ Single snake segment """

                def __init__(self, x, y):
                    self.instance = c.create_rectangle(x, y,
                                                       x + SEG_SIZE, y + SEG_SIZE,
                                                       fill="white")


            class Snake(object):
                """ Simple Snake class """

                def __init__(self, segments):
                    self.segments = segments
                    # possible moves
                    self.mapping = {"Down": (0, 1), "Right": (1, 0),
                                    "Up": (0, -1), "Left": (-1, 0)}
                    # initial movement direction
                    self.vector = self.mapping["Right"]

                def move(self):
                    """ Moves the snake with the specified vector"""
                    for index in range(len(self.segments) - 1):
                        segment = self.segments[index].instance
                        x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
                        c.coords(segment, x1, y1, x2, y2)

                    x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
                    c.coords(self.segments[-1].instance,
                             x1 + self.vector[0] * SEG_SIZE, y1 + self.vector[1] * SEG_SIZE,
                             x2 + self.vector[0] * SEG_SIZE, y2 + self.vector[1] * SEG_SIZE)

                def add_segment(self):
                    """ Adds segment to the snake """
                    last_seg = c.coords(self.segments[0].instance)
                    x = last_seg[2] - SEG_SIZE
                    y = last_seg[3] - SEG_SIZE
                    self.segments.insert(0, Segment(x, y))

                def change_direction(self, event):
                    """ Changes direction of snake """
                    if event.keysym in self.mapping:
                        self.vector = self.mapping[event.keysym]

                def reset_snake(self):
                    for segment in self.segments:
                        c.delete(segment.instance)


            def set_state(item, state):
                c.itemconfigure(item, state=state)


            def clicked(event):
                global IN_GAME
                s.reset_snake()
                IN_GAME = True
                c.delete(BLOCK)
                c.itemconfigure(restart_text, state='hidden')
                c.itemconfigure(game_over_text, state='hidden')
                start_game()


            def start_game():
                global s
                create_block()
                s = create_snake()
                # Reaction on keypress
                c.bind("<KeyPress>", s.change_direction)
                main()


            def create_snake():
                # creating segments and snake
                segments = [Segment(SEG_SIZE, SEG_SIZE),
                            Segment(SEG_SIZE * 2, SEG_SIZE),
                            Segment(SEG_SIZE * 3, SEG_SIZE)]
                return Snake(segments)


            # Setting up window
            root = Tk()
            root.title("Змейка")

            c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
            c.grid()
            # catch keypressing
            c.focus_set()
            game_over_text = c.create_text(WIDTH / 2, HEIGHT / 2, text="GAME OVER!",
                                           font='Arial 20', fill='red',
                                           state='hidden')
            restart_text = c.create_text(WIDTH / 2, HEIGHT - HEIGHT / 3,
                                         font='Arial 30',
                                         fill='white',
                                         text="Click here to restart",
                                         state='hidden')
            c.tag_bind(restart_text, "<Button-1>", clicked)
            start_game()
            root.mainloop()

        elif game == "2":
            # !/usr/bin/env python

            __author__ = "Dmitriy Krasota aka g0t0wasd"

            # Minesweeper in Python using Tkinter.
            # More at http://pythonicway.com/python-games/python-arcade/31-python-minesweep

            from tkinter import *
            import random

            GRID_SIZE = 20  # Размер поля
            SQUARE_SIZE = 20  # Размер клетки
            MINES_NUM = 40  # Количество мин на поле
            mines = set(
                random.sample(range(1, GRID_SIZE ** 2 + 1), MINES_NUM))  # Устанавливаем случайным образом мины на поле
            clicked = set()  # Сет, хранящий все клетки, по которым мы кликнули


            def check_mines(neighbors):
                """ Функция, возвращающая количество мин вокруг neighbors """
                return len(mines.intersection(neighbors))


            def generate_neighbors(square):
                """ Возвращает клетки соседствующие с square """
                # Левая верхняя клетка
                if square == 1:
                    data = {GRID_SIZE + 1, 2, GRID_SIZE + 2}
                # Правая нижняя
                elif square == GRID_SIZE ** 2:
                    data = {square - GRID_SIZE, square - 1, square - GRID_SIZE - 1}
                # Левая нижняя
                elif square == GRID_SIZE:
                    data = {GRID_SIZE - 1, GRID_SIZE * 2, GRID_SIZE * 2 - 1}
                # Верхняя правая
                elif square == GRID_SIZE ** 2 - GRID_SIZE + 1:
                    data = {square + 1, square - GRID_SIZE, square - GRID_SIZE + 1}
                # Клетка в левом ряду
                elif square < GRID_SIZE:
                    data = {square + 1, square - 1, square + GRID_SIZE,
                            square + GRID_SIZE - 1, square + GRID_SIZE + 1}
                # Клетка в правом ряду
                elif square > GRID_SIZE ** 2 - GRID_SIZE:
                    data = {square + 1, square - 1, square - GRID_SIZE,
                            square - GRID_SIZE - 1, square - GRID_SIZE + 1}
                # Клетка в нижнем ряду
                elif square % GRID_SIZE == 0:
                    data = {square + GRID_SIZE, square - GRID_SIZE, square - 1,
                            square + GRID_SIZE - 1, square - GRID_SIZE - 1}
                # Клетка в верхнем ряду
                elif square % GRID_SIZE == 1:
                    data = {square + GRID_SIZE, square - GRID_SIZE, square + 1,
                            square + GRID_SIZE + 1, square - GRID_SIZE + 1}
                # Любая другая клетка
                else:
                    data = {square - 1, square + 1, square - GRID_SIZE, square + GRID_SIZE,
                            square - GRID_SIZE - 1, square - GRID_SIZE + 1,
                            square + GRID_SIZE + 1, square + GRID_SIZE - 1}
                return data


            def clearance(ids):
                """ Итеративная (эффективная) функция очистки поля """
                clicked.add(ids)  # добавляем нажатую клетку в сет нажатых
                ids_neigh = generate_neighbors(ids)  # Получаем все соседние клетки
                around = check_mines(ids_neigh)  # высчитываем количество мин вокруг нажатой клетки
                c.itemconfig(ids, fill="green")  # окрашиваем клетку в зеленый

                # Если вокруг мин нету
                if around == 0:
                    # Создаем список соседних клеток
                    neigh_list = list(ids_neigh)
                    # Пока в списке соседей есть клетки
                    while len(neigh_list) > 0:
                        # Получаем клетку
                        item = neigh_list.pop()
                        # Окрашиваем ее в зеленый цвет
                        c.itemconfig(item, fill="green")
                        # Получаем соседение клетки данной клетки
                        item_neigh = generate_neighbors(item)
                        # Получаем количество мин в соседних клетках
                        item_around = check_mines(item_neigh)
                        # Если в соседних клетках есть мины
                        if item_around > 0:
                            # Делаем эту проверку, чтобы писать по нескольку раз на той же клетке
                            if item not in clicked:
                                # Получаем координаты этой клетки
                                x1, y1, x2, y2 = c.coords(item)
                                # Пишем на клетке количество мин вокруг
                                c.create_text(x1 + SQUARE_SIZE / 2,
                                              y1 + SQUARE_SIZE / 2,
                                              text=str(item_around),
                                              font="Arial {}".format(int(SQUARE_SIZE / 2)),
                                              fill='yellow')
                        # Если в соседних клетках мин нету
                        else:
                            # Добавляем соседние клетки данной клетки в общий список
                            neigh_list.extend(set(item_neigh).difference(clicked))
                            # Убираем повторяющиеся элементы из общего списка
                            neigh_list = list(set(neigh_list))
                        # Добавляем клетку в нажатые
                        clicked.add(item)
                # Если мины вокруг есть
                else:
                    # Высчитываем координаты клетки
                    x1, y1, x2, y2 = c.coords(ids)
                    # Пишем количество мин вокруг
                    c.create_text(x1 + SQUARE_SIZE / 2,
                                  y1 + SQUARE_SIZE / 2,
                                  text=str(around),
                                  font="Arial {}".format(int(SQUARE_SIZE / 2)),
                                  fill='yellow')


            def rec_clearance(ids):
                """ Рекурсивная (неэффективная) функция очистки поля """
                clicked.add(ids)
                neighbors = generate_neighbors(ids)
                around = check_mines(neighbors)
                if around:
                    x1, y1, x2, y2 = c.coords(ids)
                    c.itemconfig(ids, fill="green")
                    c.create_text(x1 + SQUARE_SIZE / 2,
                                  y1 + SQUARE_SIZE / 2,
                                  text=str(around),
                                  font="Arial {}".format(int(SQUARE_SIZE / 2)),
                                  fill='yellow')
                else:
                    for item in set(neighbors).difference(clicked):
                        c.itemconfig(item, fill="green")
                        rec_clearance(item)


            def click(event):
                ids = c.find_withtag(CURRENT)[0]
                if ids in mines:
                    c.itemconfig(CURRENT, fill="red")
                elif ids not in clicked:
                    clearance(ids)
                    c.itemconfig(CURRENT, fill="green")
                c.update()


            def mark_mine(event):
                ids = c.find_withtag(CURRENT)[0]
                if ids not in clicked:
                    clicked.add(ids)
                    x1, y1, x2, y2 = c.coords(ids)
                    c.itemconfig(CURRENT, fill="yellow")
                else:
                    clicked.remove(ids)
                    c.itemconfig(CURRENT, fill="gray")


            root = Tk()
            root.title("Pythonicway Minesweep")
            c = Canvas(root, width=GRID_SIZE * SQUARE_SIZE, height=GRID_SIZE * SQUARE_SIZE)
            c.bind("<Button-1>", click)
            c.bind("<Button-3>", mark_mine)
            c.pack()
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE,
                                       i * SQUARE_SIZE + SQUARE_SIZE,
                                       j * SQUARE_SIZE + SQUARE_SIZE, fill='gray')
            root.mainloop()

        elif game == "3":
            from tkinter import *
            # импортируем библиотеку random
            import random

            # Добавляем глобальные переменные

            # глобальные переменные
            # настройки окна
            WIDTH = 900
            HEIGHT = 300

            # настройки ракеток

            # ширина ракетки
            PAD_W = 10
            # высота ракетки
            PAD_H = 100

            # настройки мяча
            # Насколько будет увеличиваться скорость мяча с каждым ударом
            BALL_SPEED_UP = 1.05
            # Максимальная скорость мяча
            BALL_MAX_SPEED = 40
            # радиус мяча
            BALL_RADIUS = 30

            INITIAL_SPEED = 20
            BALL_X_SPEED = INITIAL_SPEED
            BALL_Y_SPEED = INITIAL_SPEED

            # Счет игроков
            PLAYER_1_SCORE = 0
            PLAYER_2_SCORE = 0

            # Добавим глобальную переменную отвечающую за расстояние
            # до правого края игрового поля
            right_line_distance = WIDTH - PAD_W


            def update_score(player):
                global PLAYER_1_SCORE, PLAYER_2_SCORE
                if player == "right":
                    PLAYER_1_SCORE += 1
                    c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
                else:
                    PLAYER_2_SCORE += 1
                    c.itemconfig(p_2_text, text=PLAYER_2_SCORE)


            def spawn_ball():
                global BALL_X_SPEED
                # Выставляем мяч по центру
                c.coords(BALL, WIDTH / 2 - BALL_RADIUS / 2,
                         HEIGHT / 2 - BALL_RADIUS / 2,
                         WIDTH / 2 + BALL_RADIUS / 2,
                         HEIGHT / 2 + BALL_RADIUS / 2)
                # Задаем мячу направление в сторону проигравшего игрока,
                # но снижаем скорость до изначальной
                BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)


            # функция отскока мяча
            def bounce(action):
                global BALL_X_SPEED, BALL_Y_SPEED
                # ударили ракеткой
                if action == "strike":
                    BALL_Y_SPEED = random.randrange(-10, 10)
                    if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
                        BALL_X_SPEED *= -BALL_SPEED_UP
                    else:
                        BALL_X_SPEED = -BALL_X_SPEED
                else:
                    BALL_Y_SPEED = -BALL_Y_SPEED


            # устанавливаем окно
            root = Tk()
            root.title("PythonicWay Pong")

            # область анимации
            c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
            c.pack()

            # элементы игрового поля

            # левая линия
            c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="white")
            # правая линия
            c.create_line(WIDTH - PAD_W, 0, WIDTH - PAD_W, HEIGHT, fill="white")
            # центральная линия
            c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")

            # установка игровых объектов

            # создаем мяч
            BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                                 HEIGHT / 2 - BALL_RADIUS / 2,
                                 WIDTH / 2 + BALL_RADIUS / 2,
                                 HEIGHT / 2 + BALL_RADIUS / 2, fill="white")

            # левая ракетка
            LEFT_PAD = c.create_line(PAD_W / 2, 0, PAD_W / 2, PAD_H, width=PAD_W, fill="yellow")

            # правая ракетка
            RIGHT_PAD = c.create_line(WIDTH - PAD_W / 2, 0, WIDTH - PAD_W / 2,
                                      PAD_H, width=PAD_W, fill="yellow")

            p_1_text = c.create_text(WIDTH - WIDTH / 6, PAD_H / 4,
                                     text=PLAYER_1_SCORE,
                                     font="Arial 20",
                                     fill="white")

            p_2_text = c.create_text(WIDTH / 6, PAD_H / 4,
                                     text=PLAYER_2_SCORE,
                                     font="Arial 20",
                                     fill="white")

            # добавим глобальные переменные для скорости движения мяча
            # по горизонтали
            BALL_X_CHANGE = 20
            # по вертикали
            BALL_Y_CHANGE = 0


            def move_ball():
                # определяем координаты сторон мяча и его центра
                ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
                ball_center = (ball_top + ball_bot) / 2

                # вертикальный отскок
                # Если мы далеко от вертикальных линий - просто двигаем мяч
                if ball_right + BALL_X_SPEED < right_line_distance and \
                        ball_left + BALL_X_SPEED > PAD_W:
                    c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
                # Если мяч касается своей правой или левой стороной границы поля
                elif ball_right == right_line_distance or ball_left == PAD_W:
                    # Проверяем правой или левой стороны мы касаемся
                    if ball_right > WIDTH / 2:
                        # Если правой, то сравниваем позицию центра мяча
                        # с позицией правой ракетки.
                        # И если мяч в пределах ракетки делаем отскок
                        if c.coords(RIGHT_PAD)[1] < ball_center < c.coords(RIGHT_PAD)[3]:
                            bounce("strike")
                        else:
                            # Иначе игрок пропустил - тут оставим пока pass, его мы заменим на подсчет очков и респаун мячика
                            update_score("left")
                            spawn_ball()
                    else:
                        # То же самое для левого игрока
                        if c.coords(LEFT_PAD)[1] < ball_center < c.coords(LEFT_PAD)[3]:
                            bounce("strike")
                        else:
                            update_score("right")
                            spawn_ball()
                # Проверка ситуации, в которой мячик может вылететь за границы игрового поля.
                # В таком случае просто двигаем его к границе поля.
                else:
                    if ball_right > WIDTH / 2:
                        c.move(BALL, right_line_distance - ball_right, BALL_Y_SPEED)
                    else:
                        c.move(BALL, -ball_left + PAD_W, BALL_Y_SPEED)
                # горизонтальный отскок
                if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
                    bounce("ricochet")


            # зададим глобальные переменные скорости движения ракеток
            # скорось с которой будут ездить ракетки
            PAD_SPEED = 20
            # скорость левой платформы
            LEFT_PAD_SPEED = 0
            # скорость правой ракетки
            RIGHT_PAD_SPEED = 0


            # функция движения обеих ракеток
            def move_pads():
                # для удобства создадим словарь, где ракетке соответствует ее скорость
                PADS = {LEFT_PAD: LEFT_PAD_SPEED,
                        RIGHT_PAD: RIGHT_PAD_SPEED}
                # перебираем ракетки
                for pad in PADS:
                    # двигаем ракетку с заданной скоростью
                    c.move(pad, 0, PADS[pad])
                    # если ракетка вылезает за игровое поле возвращаем ее на место
                    if c.coords(pad)[1] < 0:
                        c.move(pad, 0, -c.coords(pad)[1])
                    elif c.coords(pad)[3] > HEIGHT:
                        c.move(pad, 0, HEIGHT - c.coords(pad)[3])


            def main():
                move_ball()
                move_pads()
                # вызываем саму себя каждые 30 миллисекунд
                root.after(30, main)


            # Установим фокус на Canvas чтобы он реагировал на нажатия клавиш
            c.focus_set()


            # Напишем функцию обработки нажатия клавиш
            def movement_handler(event):
                global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
                if event.keysym == "w":
                    LEFT_PAD_SPEED = -PAD_SPEED
                elif event.keysym == "s":
                    LEFT_PAD_SPEED = PAD_SPEED
                elif event.keysym == "Up":
                    RIGHT_PAD_SPEED = -PAD_SPEED
                elif event.keysym == "Down":
                    RIGHT_PAD_SPEED = PAD_SPEED


            # Привяжем к Canvas эту функцию
            c.bind("<KeyPress>", movement_handler)


            # Создадим функцию реагирования на отпускание клавиши
            def stop_pad(event):
                global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
                if event.keysym in "ws":
                    LEFT_PAD_SPEED = 0
                elif event.keysym in ("Up", "Down"):
                    RIGHT_PAD_SPEED = 0


            # Привяжем к Canvas эту функцию
            c.bind("<KeyRelease>", stop_pad)

            # запускаем движение
            main()

            # запускаем работу окна
            root.mainloop()

        elif game == "4":
            from tkinter import *
            import random

            root = Tk()
            root.title('Criss-cross')
            game_run = True
            field = []
            cross_count = 0


            def new_game():
                for row in range(3):
                    for col in range(3):
                        field[row][col]['text'] = ' '
                        field[row][col]['background'] = 'lavender'
                global game_run
                game_run = True
                global cross_count
                cross_count = 0


            def click(row, col):
                if game_run and field[row][col]['text'] == ' ':
                    field[row][col]['text'] = 'X'
                    global cross_count
                    cross_count += 1
                    check_win('X')
                    if game_run and cross_count < 5:
                        computer_move()
                        check_win('O')


            def check_win(smb):
                for n in range(3):
                    check_line(field[n][0], field[n][1], field[n][2], smb)
                    check_line(field[0][n], field[1][n], field[2][n], smb)
                check_line(field[0][0], field[1][1], field[2][2], smb)
                check_line(field[2][0], field[1][1], field[0][2], smb)


            def check_line(a1, a2, a3, smb):
                if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
                    a1['background'] = a2['background'] = a3['background'] = 'pink'
                    global game_run
                    game_run = False


            def can_win(a1, a2, a3, smb):
                res = False
                if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
                    a3['text'] = 'O'
                    res = True
                if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
                    a2['text'] = 'O'
                    res = True
                if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
                    a1['text'] = 'O'
                    res = True
                return res


            def computer_move():
                for n in range(3):
                    if can_win(field[n][0], field[n][1], field[n][2], 'O'):
                        return
                    if can_win(field[0][n], field[1][n], field[2][n], 'O'):
                        return
                if can_win(field[0][0], field[1][1], field[2][2], 'O'):
                    return
                if can_win(field[2][0], field[1][1], field[0][2], 'O'):
                    return
                for n in range(3):
                    if can_win(field[n][0], field[n][1], field[n][2], 'X'):
                        return
                    if can_win(field[0][n], field[1][n], field[2][n], 'X'):
                        return
                if can_win(field[0][0], field[1][1], field[2][2], 'X'):
                    return
                if can_win(field[2][0], field[1][1], field[0][2], 'X'):
                    return
                while True:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    if field[row][col]['text'] == ' ':
                        field[row][col]['text'] = 'O'
                        break


            for row in range(3):
                line = []
                for col in range(3):
                    button = Button(root, text=' ', width=4, height=2,
                                    font=('Verdana', 20, 'bold'),
                                    background='lavender',
                                    command=lambda row=row, col=col: click(row, col))
                    button.grid(row=row, column=col, sticky='nsew')
                    line.append(button)
                field.append(line)
            new_button = Button(root, text='new game', command=new_game)
            new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
            root.mainloop()

        else:
            print("Введено неверное значение!\n")

    else:
        print("Введено неверное значение!\n")

else:
    print("Введен неверный пороль!!!\n")

input("Нажмите <Enter> чтобы закрыть программу")