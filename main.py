import diseases
from disease_class import Disease
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from operator import attrgetter
#import autocomplete.py
root = tk.Tk()


#making an image
logo = tk.PhotoImage(file="Syringe.png")





#Global Variables
mystring =''
mystring2 = ''
mystring3 = ''
dnames=[]


#Genereates the welcome screen, with user inputs
def welcome_screen(root):
  global input1
  global input2
  global input3
  global heading
  root.title("Health Application")
  root.geometry("640x640+0+0")
  root.configure(bg="#212121")
  #Creates head label
  heading = tk.Label(root, text="Am I Dying", fg='#32e0c4', bg='#212121', font="AppHighlightFont 40 bold italic").pack()

  info = tk.Label(root,text="ENTER THREE SYMPTOMS:", fg='white', bg='#212121', font="AppHighlightFont 20 bold").pack()
  #Button Input(3)
  lab0=tk.Label(root,fg='#212121',bg='#212121',height=2).pack()
  input1 = tk.Entry(root, textvariable=mystring, width=25, bg="#eeeeee").pack()
  lab1=tk.Label(root,fg='#212121',bg='#212121').pack()
  input2 = tk.Entry(root, textvariable=mystring2, width=25, bg="#eeeeee").pack()
  lab2=tk.Label(root,fg='#212121',bg='#212121').pack()
  input3 = tk.Entry(root, textvariable=mystring3, width=25, bg="#eeeeee").pack()
  lab3=tk.Label(root,fg='#212121',bg='#212121').pack()

  


#global variable
user_symptoms = []



#Prints the second screen after user presses search
def second_screen(): 
    if my_string != '':
        user_symptoms.append(mystring.get())
        user_symptoms.append(mystring2.get())
        user_symptoms.append(mystring3.get())
        root=tk.Tk()
        root.title("Health Application")
        root.geometry("640x640+0+0")
        root.configure(bg="#32e0c4")
        heading = Label(root, text="YOU ARE DEAD", fg='black',bg='#32e0c4', font="AppHighlightFont 40 bold").pack()
        info = Label(root, text="DISEASES FOR YOUR SYMPTOMS", fg='white',bg='#32e0c4', font="AppHighlightFont 20 bold").pack()
        symc=user_symptoms[:]
        for symp in symc:
            if symp=='':
                user_symptoms.remove(symp)
        
        dl=dismatch(user_symptoms)
        z=125
        root.update()
        for dis in dl:
            b = tk.Label(root, text=f"{dis.name}:\n{dis}", fg='black',bg='#32e0c4').pack()
            #b.pack
            #b.place(y=z)
            z+=80

#Code that allows for new screen
def new_screen():
    global user_symptoms
    global my_string
    global my_string2
    global my_string3
    my_string = mystring.get().lower()
    my_string2 = mystring2.get().lower()
    my_string3 = mystring3.get().lower()
    second_screen()
    

symptoms=[]

def dismatch(smps):
    """
    Sorts diseases based on likelyness
    returns: a sorted list of Disease objects

    Parameter smps: list of symptoms
    Precondition: non-empty list of non-empty strings, eache string must correspond to a symptom.
    """
    d=diseases.createlib()
    for dis in d:
        for s in dis.symptoms:
            if not(s in symptoms):
                symptoms.append(s)
    assert type(smps)==list
    for smp in smps:
        assert smp in symptoms,'invalid symptom'
    discopy=d[:]
    for dis in discopy:
        dis.likeness=dis.likehood(smps)
    discopy.sort(key=attrgetter('likeness'),reverse=True)
    for dis in d:
        s=0
        for i in smps:
            if not(i in dis.symptoms):
                s+=1
        if s==len(smps):
            discopy.remove(dis)
    #if len(discopy)>3:
        #discopy=discopy[0:3]
    return discopy  




mystring = StringVar(root)
mystring2 = StringVar(root)
mystring3 = StringVar(root)
welcome_screen(root)
search = tk.Button(root, text="SEARCH", width=30, height=5, bg="#32e0c4", command=new_screen).pack()
w1 = tk.Label(root, image=logo, bg='#212121').pack()
tk.mainloop()



