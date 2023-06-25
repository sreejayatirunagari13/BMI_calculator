import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def clearChild(C_Height,C_Weight,Age,Gender):
    Age.delete(0,100)
    C_Height.delete(0,100)
    C_Weight.delete(0,100)
    Gender.delete(0,100)

def clearadult(A_Weight,A_Height):    
    A_Height.delete(0,100)
    A_Weight.delete(0,100)

#--------------------------------------ADULT BMI-----------------------------------------------#   
def adult_bmi(A_Weight,A_Height):  
    
    try:
        height = int(A_Height.get())
        weight = int(A_Weight.get())
        height = height / 100.0
        a_bmi = round(weight / (height ** 2))

    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if a_bmi == 0:
            messagebox.showinfo("Result", "Please Enter Positive Weight!")
        elif 0 < a_bmi <= 16.0:
            res = "Your BMI is " + str(a_bmi) + "\nHealthy BMI range: 18.5 - 25 \nRemarks: Skinny :("
            messagebox.showinfo("Result", res)
        elif 16.0 < a_bmi < 18.5:
            res = "Your BMI is " + str(a_bmi) + "\nHealthy BMI range: 18.5 - 25 \nRemarks: Underweight!" 
            messagebox.showinfo("Result", res)       
        elif 18.5 <= a_bmi <= 25.0:
            res = "Your BMI is " + str(a_bmi) + "\nHealthy BMI range: 18.5 - 25 \nRemarks: Congratulations! Normal."
            messagebox.showinfo("Result", res)      
        elif 25.0 < a_bmi <= 30:
            res = "Your BMI is " + str(a_bmi) + "\nHealthy BMI range: 18.5 - 25 \nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < a_bmi <= 35.0:
            res = "Your BMI is " + str(a_bmi) + "\nHealthy BMI range: 18.5 - 25 \nRemarks: Obese :("
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(a_bmi) + "\nHealthy BMI range: 18.5 - 25 \nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)
        
#--------------------------------------------CHILD BMI----------------------------------------------------#
def child_bmi(C_Height,C_Weight,Age,Gender):

    try:    
        height = int(C_Height.get())
        weight = int(C_Weight.get())
        height = height / 100.0
        bmi = round(weight / (height ** 2))
        
        age = int(Age.get())
        gender = str(Gender.get())
        if gender.isalpha():
            gender = str(Gender.get())
        else:
            messagebox.showinfo("Result", "Please enter M or F in gender")
        
        bmis = [
        "Your BMI is " + str(bmi) + "\nRemarks: Underweight!", 
        "Your BMI is " + str(bmi) + "\nRemarks: Congratulations! Normal.",
        "Your BMI is " + str(bmi) + "\nRemarks: You are at a risk of Overweight.",
        "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
        ]
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:   
        if (age in range (2,12) and gender == 'M'): # Children Boys
            if bmi < 14:
                messagebox.showinfo("Result", bmis[0])
            elif 14 <= bmi < 19:
                messagebox.showinfo("Result", bmis[1])
            elif 19 <= bmi <= 21:
                messagebox.showinfo("Result", bmis[2])
            else:
                messagebox.showinfo("Result", bmis[3])
        
        if (age in range (2,12) and gender == 'F'): # Children Girls
            if bmi < 13:
                messagebox.showinfo("Result", bmis[0])
            elif 13 <= bmi < 17:
                messagebox.showinfo("Result", bmis[1])
            elif 17 <= bmi <= 21:
                messagebox.showinfo("Result", bmis[2])
            else:
                messagebox.showinfo("Result", bmis[3])

        if (age in range(12,18) and gender == 'M'): #Teens Boys
            if bmi < 15:
                messagebox.showinfo("Result", bmis[0]) 
            elif 15 <= bmi < 25 :
                messagebox.showinfo("Result", bmis[1]) 
            elif 25 <= bmi < 28 :
                messagebox.showinfo("Result", bmis[2])
            else:
                messagebox.showinfo("Result", bmis[3])

        if(age in range(12,18) and gender == 'F'): #Teens Girls
            if bmi < 14:
                messagebox.showinfo("Result", bmis[0]) 
            elif 14 <= bmi < 26 :
                messagebox.showinfo("Result", bmis[1]) 
            elif 26 <= bmi < 30 :
                messagebox.showinfo("Result", bmis[2])
            else:
                messagebox.showinfo("Result", bmis[3])

#----------------------------------------Adult PAGE----------------------------------------#
def adult_page():

    bg_img = ImageTk.PhotoImage(Image.open("bmiimgg.jpg"))
    label_bg = tkinter.Label(image=bg_img)
    label_bg.image = bg_img
    label_bg.place(x=10, y=10)

    LABLE = Label(TOP, bg="#cef0f1", text="Adult BMI Calculator", font=("Imprint MT Shadow", 22, "bold"), pady=5, padx=5)
    LABLE.place(x=100, y=12)

    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter Weight (in Kg):", bd=6, font=("Helvetica", 12, "bold"), pady=5)
    LABLE1.place(x=128, y=110)
    A_Weight  = Entry(TOP, bd=8, width=8, font="Roboto 11")
    A_Weight.place(x=300, y=110)

    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter Height (in cm):", bd=6, font=("Helvetica", 12, "bold"), pady=5)
    LABLE2.place(x=128, y=180)
    A_Height = Entry(TOP, bd=8, width=8, font="Roboto 11")
    A_Height.place(x=300, y=180)

    BUTTON = Button (TOP,bg="DarkSeaGreen", bd=12, text="Clear", padx=10, pady=10, command=lambda :clearadult(A_Weight,A_Height), font=("Helvetica", 10, "bold"))
    BUTTON.place(x=165, y=250)

    BUTTON = Button(TOP,bg="#2187e7", bd=12, text="BMI", padx=33, pady=15, command=lambda :adult_bmi(A_Weight,A_Height), font=("Helvetica", 15, "bold"))
    BUTTON.place(x=250, y=250)

    BUTTON = Button (TOP,bg="AntiqueWhite3", bd=10, text="Back", padx=4, pady=4, command=lambda :back(), font=("Helvetica", 10, "bold"))
    BUTTON.place(x=50, y=420)

    TOP.mainloop()

#-------------------------------------Child PAGE-------------------------------------------#
def child_page():

    bg_img = ImageTk.PhotoImage(Image.open("bmiimgg.jpg"))
    label_bg = tkinter.Label(image=bg_img)
    label_bg.image = bg_img
    label_bg.place(x=10, y=10)

    LABLE = Label(TOP, bg="#cef0f1", text="Child & Teen BMI Calculator", font=("Imprint MT Shadow", 22, "bold"), pady=5, padx=5)
    LABLE.place(x=65, y=12)

    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter Your Age:", bd=6, font=("Helvetica", 11, "bold"), pady=5)
    LABLE1.place(x=115, y=80)
    Age = Entry(TOP, bd=8, width=8, font="Roboto 11")
    Age.place(x=300, y=80)

    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter Your Gender:", bd=6, font=("Helvetica", 11, "bold"), pady=5)
    LABLE2.place(x=115, y=130)
    Gender = Entry(TOP, bd=8, width=8, font="Roboto 11")
    Gender.place(x=300, y=130)

    LABLE3 = Label(TOP, bg="#cef0f1", text="Enter Weight (in Kg):", bd=6, font=("Helvetica", 11, "bold"), pady=5)
    LABLE3.place(x=115, y=180)
    C_Weight = Entry(TOP, bd=8, width=8, font="Roboto 11")
    C_Weight.place(x=300, y=180)

    LABLE4 = Label(TOP, bg="#cef0f1", text="Enter Height (in cm):", bd=6, font=("Helvetica", 11, "bold"), pady=5)
    LABLE4.place(x=115, y=230)
    C_Height = Entry(TOP, bd=8, width=8, font="Roboto 11")
    C_Height.place(x=300, y=230)

    BUTTON = Button (TOP,bg="DarkSeaGreen", bd=12, text="Clear", padx=10, pady=10, command=lambda :clearChild(C_Height,C_Weight,Age,Gender), font=("Helvetica", 10, "bold"))
    BUTTON.place(x=175, y=300)

    BUTTON = Button(TOP,bg="#2187e7", bd=12, text="BMI", padx=33, pady=15, command=lambda :child_bmi(C_Height,C_Weight,Age,Gender), font=("Helvetica", 15, "bold"))
    BUTTON.place(x=260, y=300)

    BUTTON = Button (TOP,bg="AntiqueWhite3", bd=10, text="Back", padx=4, pady=4, command=lambda :back(), font=("Helvetica", 10, "bold"))
    BUTTON.place(x=50, y=420)

    TOP.mainloop()

#--------------------------------Home Page-----------------------------------------------#     
TOP = Tk()   
TOP.geometry("500x500")  
TOP.title("BMI Calculator")

bg_img = ImageTk.PhotoImage(Image.open("bmiimgg.jpg"))
label_bg = tkinter.Label(image=bg_img)
label_bg.image = bg_img
label_bg.place(x=10, y=10)

LABLE = Label(TOP, bg="#cef0f1", text="Welcome to BMI Calculator", font=("Imprint MT Shadow", 24, "bold"), pady=5, padx=5)
LABLE.place(x=60, y=12)

BUTTON = Button (bg="yellow", bd=12, text="Age<18", padx=10, pady=10, command=lambda :child_page(), font=("Helvetica", 10, "bold"))
BUTTON.place(x=160, y=200)

BUTTON = Button (bg="#2187e7", bd=12, text="Age>=18", padx=10, pady=10, command=lambda :adult_page(), font=("Helvetica", 10, "bold"))
BUTTON.place(x=265, y=200)

def back():

    bg_img = ImageTk.PhotoImage(Image.open("bmiimgg.jpg"))
    label_bg = tkinter.Label(image=bg_img)
    label_bg.image = bg_img
    label_bg.place(x=10, y=10)

    LABLE = Label(TOP, bg="#cef0f1", text="Welcome to BMI Calculator", font=("Imprint MT Shadow", 24, "bold"), pady=5, padx=5)
    LABLE.place(x=60, y=12)

    BUTTON = Button (bg="yellow", bd=12, text="Age<18", padx=10, pady=10, command=lambda :child_page(), font=("Helvetica", 10, "bold"))
    BUTTON.place(x=160, y=200)

    BUTTON = Button (bg="#2187e7", bd=12, text="Age>=18", padx=10, pady=10, command=lambda :adult_page(), font=("Helvetica", 10, "bold"))
    BUTTON.place(x=265, y=200)

TOP.mainloop()
