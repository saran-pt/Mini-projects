import tkinter
from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Grade Calculater")

def calculate_mark():
    math = int(math_mark.get())
    english = int(english_mark.get())
    computer = int(computer_mark.get())
    physics = int(physics_mark.get())
    chemistry = int(chemistry_mark.get())

    total = (math+english+computer+physics+chemistry)
    Label(root, text=f'{total}', font="arial 20").place(x=230 ,y=220)
    ave = (total/5)
    if ave < 50:
        value = "FAIL"
    else:
        value = "PASS"

    Label(root, text=f"{value}", font="arial 20").place(x=230, y=260)

sub_1 = Label(root, text="Maths", font="arial 15")
sub_1.place(x=20, y=20)
sub_2 = Label(root, text="English", font="arial 15")
sub_2.place(x=20, y=60)
sub_3 = Label(root, text="Computer", font="arial 15")
sub_3.place(x=20, y=100)
sub_4 = Label(root, text="Physics", font="arial 15")
sub_4.place(x=20, y=140)
sub_5 = Label(root, text="Chemistry", font="arial 15")
sub_5.place(x=20, y=180)
total = Label(root, text="Total", font="arial 18")
total.place(x=20, y=220)
result = Label(root, text="Result", font="arial 18")
result.place(x=20, y=260)


math_value = StringVar()
english_value = StringVar()
computer_value = StringVar()
physics_value = StringVar()
chemistry_value = StringVar()


math_mark = Entry(root, textvariable=math_value, font="arial 15", width=18)
math_mark.place(x=230,y=20)
english_mark = Entry(root, textvariable=english_value, font="arial 15", width=18)
english_mark.place(x=230, y=60)
computer_mark = Entry(root, textvariable=computer_value, font="arial 15", width=18)
computer_mark.place(x=230, y=100)
physics_mark = Entry(root, textvariable=physics_value, font="arial 15", width=18)
physics_mark.place(x=230, y=140)
chemistry_mark = Entry(root, textvariable=chemistry_value, font="arial 15", width=18)
chemistry_mark.place(x=230, y=180)

Button(root, text="Calculate", font="arial 18", bg="green", bd=3, width=8, command=calculate_mark).place(x=20, y=320)
Button(root, text="Exit", font="arial 18", bg="red", bd=3, width=8, command=lambda: exit()).place(x=250, y=320)

root.mainloop()