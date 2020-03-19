from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *

def win():
    def new_win():
        win()

    def open_file():
        of = askopenfilename()
        file = open(of, "r")
        txt.insert(END, file.read())
        file.close()

    def save_file():
        sf = asksaveasfilename()
        final_text = txt.get(1.0, END)
        file = open(sf, "w")
        file.write(final_text)
        file.close()

    def exit_app():
        root.quit()

    root = Tk()
    root.title("Текстовый редактор")

    main_menu = Menu(root)
    root.configure(menu=main_menu)

    first_item = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="File", menu=first_item)

    first_item.add_command(label="Open", command=open_file)
    first_item.add_command(label="Save", command=save_file)
    first_item.add_command(label="Exit", command=exit_app)


    first_item = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Edit", menu=first_item)

    first_item.add_command(label="New", command=new_win)

    txt = Text(root, width=40, height=15, font=12)
    txt.pack(expand=YES, fill=BOTH)

    root.mainloop()

win()