from tkinter import *       #importing Modules & Functions
import string
import random
import pyperclip
from PIL import ImageTk, Image



def password_generator():                       #Password Genrating Function
    small_alpha = string.ascii_lowercase
    capital_alpha = string.ascii_uppercase
    number = string.digits
    special_symbol = string.punctuation

    all = small_alpha+capital_alpha+number+special_symbol+number
    passwordlength = int(length_box.get())                       #Gather the data which is enterd by user in langth box


    if choice.get()==1:                                                         # Decision Making Statements
        password_field.insert(0,random.sample(small_alpha,passwordlength))

    if choice.get()==2:
        password_field.insert(0,random.sample(small_alpha+capital_alpha,passwordlength))

    if choice.get()==3:
        password_field.insert(0,random.sample(all,passwordlength))



def copy_pass():                        # Copy Password Function
    copy = password_field.get()
    pyperclip.copy(copy)



def pop_msg():                      # Display POP-UP Message
    popmsg.config(text="Password Copied To Clipboard",bg='indigo',fg='yellow', font=highlights)
    popmsg.grid(padx=5,pady=5)







class_object =Tk()       # GUI Windows & object


class_object.title("Password Generator By Pr@T!k")          #Window Title
class_object.geometry("580x650")                #Window Size
class_object.config(bg='indigo')#         #Window BG Color

choice = IntVar()
labels = ('cursive','30','bold','italic')
label2 = ('cursive','20','bold','italic')
radio_buttons = ('terminal','10','bold')
buttons = ('terminal','10','bold')
highlights = ('system','12','bold')


passwordlabel = Label(class_object, text=" Generate Random Passwords Here", font=labels , bg='indigo', fg='white')  # First Headline
passwordlabel.grid(pady=10)                             #printing label

headline = Label(class_object, text="\nSelect Password Type", font=label2 , bg='indigo', fg='white')  # Second Headline
headline.grid(pady=5)

# blank_label2 = Label(class_object,text='',border=0, bg='indigo')
# blank_label2.grid(pady=5)

weak_radio_button = Radiobutton(class_object, text='Weak Password', value=1, variable=choice,bg='aqua',highlightbackground='black', font = radio_buttons,fg='black')      # Radio Buttons
weak_radio_button.grid(pady=5)
medium_radio_button = Radiobutton(class_object , text='Medium Password', value=2, variable=choice, bg='aqua',highlightbackground='black' ,font = radio_buttons,fg='black')
medium_radio_button.grid(pady=5)
strong_radio_button = Radiobutton(class_object, text='Strong Password', value=3, variable=choice, bg='aqua',highlightbackground='black' ,font=radio_buttons,fg='black')
strong_radio_button.grid(pady=5)


blank_label2 = Label(text="",bg='indigo',border=0)      # Blank Headline for Padding
blank_label2.grid(pady=20)



passwordlength = Label(class_object , text='Password Length', font = label2, bg='indigo',fg='white')
passwordlength.grid(pady=5)
length_box = Spinbox(class_object, font=buttons, from_=5, to=20, width=20,highlightbackground='black')
length_box.grid(pady=5)

photo = Image.open("Images/Button1.png")
re_size = photo.resize((200,40))
photo2 = ImageTk.PhotoImage(re_size)
lab1 = Label(image=photo2)
# lab1.grid(padx=10,pady=30)

generate_button = Button(class_object, image=photo2,bd=0,bg='indigo',highlightbackground='indigo',activebackground='indigo',borderwidth=0,command=password_generator)            #Creating a Button
generate_button.grid(pady=10)



photo3 = Image.open("Images/Button2.png")
re_size2 = photo3.resize((180,35))
photo4 = ImageTk.PhotoImage(re_size2)
lab2 = Label(image=photo4)

password_field = Entry(class_object,width=20, bd=0, font=buttons,show='*')           # Print Password
password_field.grid(pady=5)
copy_button = Button(class_object,image=photo4,bd=0,bg='indigo',highlightbackground='indigo',activebackground='indigo',borderwidth=0,command = lambda : [copy_pass(), pop_msg()])      #Copy Button
copy_button.grid(pady=10)
popmsg=Label(class_object,text='',border=0,bg='indigo')             # Blank Label
popmsg.grid()

endlabel = Label(text='Design and Developed by Pr@T!k Nidane',font=('cursive','15','bold','italic'), bg='indigo', fg='white' )      # Footer
endlabel.grid(padx=50,pady=50)


class_object.mainloop()