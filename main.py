from tkinter import *


def submit():
    print("Your phone number is: " +
          str(phone_number_scale1.get()) +
          str(phone_number_scale2.get()) +
          str(phone_number_scale3.get()) +
          str(phone_number_scale4.get()) +
          str(phone_number_scale5.get()) +
          str(phone_number_scale6.get()) +
          str(phone_number_scale7.get()) +
          str(phone_number_scale8.get()) +
          str(phone_number_scale9.get()) +
          str(phone_number_scale10.get()) +
          str(phone_number_scale11.get()))
    submit_button.config(state=DISABLED)


window = Tk()

window.geometry("300x650")
window.title("GUI experiment")
window.config(background="grey")

phone_number_question = Label(window, text="Please enter your phone number below:",
                              font=("Times New Roman", 16, "bold"))
phone_number_scale1 = Scale(window, from_=0,
                            to=9,
                            orient=HORIZONTAL)
phone_number_scale2 = Scale(window, from_=0,
                            to=9,
                            orient=HORIZONTAL)
phone_number_scale3 = Scale(window, from_=0,
                            to=9,
                            orient=HORIZONTAL)
phone_number_scale4 = Scale(window, from_=0,
                            to=9,
                            orient=HORIZONTAL)
phone_number_scale5 = Scale(window, from_=0,
                            to=9,
                            orient=HORIZONTAL)
phone_number_scale6 = Scale(window, from_=0,
                            to=9,
                            orient=HORIZONTAL)
phone_number_scale7 = Scale(window, from_=0,
                            to=9,
                            orient=HORIZONTAL)
phone_number_scale8 = Scale(window, from_=0,
                            to=9,
                            orient=HORIZONTAL)
phone_number_scale9 = Scale(window, from_=0,
                            to=9,
                            orient=HORIZONTAL)
phone_number_scale10 = Scale(window, from_=0,
                             to=9,
                             orient=HORIZONTAL)
phone_number_scale11 = Scale(window, from_=0,
                             to=9,
                             orient=HORIZONTAL)

submit_button = Button(window,
                       text="submit",
                       command=submit)


phone_number_question.place(x=0, y=0)
phone_number_scale1.place(x=0, y=50)
phone_number_scale2.place(x=0, y=100)
phone_number_scale3.place(x=0, y=150)
phone_number_scale4.place(x=0, y=200)
phone_number_scale5.place(x=0, y=250)
phone_number_scale6.place(x=0, y=300)
phone_number_scale7.place(x=0, y=350)
phone_number_scale8.place(x=0, y=400)
phone_number_scale9.place(x=0, y=450)
phone_number_scale10.place(x=0, y=500)
phone_number_scale11.place(x=0, y=550)
submit_button.place(x=0, y=600)

window.mainloop()
