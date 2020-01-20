import json
from tkinter import *
import tkinter as TK
from tkinter import ttk
import random
import time as t

tries = 0
n = 0
s = 0
w = 0
aval = []

with open('table.json', 'r') as f:
        table = json.load(f)

for k,v in table.items():
    aval.append(v[0])

print(aval)

root = Tk()
root.configure(background='#fdcb6e')
root.wm_title("Periodic table guessing game")
root.geometry("680x450")

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def popup(do=''):
    global score, players
    win = TK.Toplevel()
    if do == '':

        win.wm_title("Game Over!")
        win.configure(background='#fdcb6e')
        
        l = TK.Label(win, text="Hope you had a good time playing!\n Your score is " + str(s), font='Arial 15 bold',
                     bg="#ecf0f1")
        l.grid(row=0, column=0)

        b = ttk.Button(win, text="Play Again..", command=combine_funcs(win.destroy, startGame), width=40)
        b.grid(row=1, column=0)

        q = ttk.Button(win, text="Quit", command=root.destroy , width=40)
        q.grid(row=2, column=0)


def newNo():
    global n
    print('new')
    n = random.randrange(1, 119, 1)
    ques.config(text=str(n))
    message.config(text="")
    hint.config(text="")
    submit.config(state='active')
    e1.config(state='normal')
    e1.delete(0, END)

def submit():
    global s,n,w,tries,aval 
    print(table[str(n)][0])
    if e1.get() == table[str(n)][0]:
        print('correct')
        s+=1
        tries=0
        hint.config(text="")
        message.config(text='Correct!! Keep going.', fg="green")
        message.after(1500, lambda: newNo())


    
    elif e1.get() not in aval:
        w += 1
        tries+=1
        message.config(text='Wrong!! Please enter a valid element.', fg="red")
        if w >= 6:
            hint.config(text='Right answer is '+table[str(n)][0], fg="black")
            message.after(1500, lambda: popup())
            return
        hint.config(text="Hint:\n1. "+table[str(n)][1])
        
        print('wrong!')

    else:
        w += 1
        tries+=1
        message.config(text='Wrong!!', fg="red")
        if w >= 6:
            hint.config(text='Right answer is '+table[str(n)][0], fg="black")
            message.after(1500, lambda: popup())
            return
        if tries == 1:
            if aval.index(e1.get()) < aval.index(table[str(n)][0]):
                hint.config(text = "Hint:\n1. The correct element is on the right of the element entered")

            else:
                hint.config(text = "Hint:\n1. The correct element is on the left of the element entered")                                
                
        elif tries >= 2:
            
            if aval.index(e1.get()) < aval.index(table[str(n)][0]):
                hint.config(text = "Hint:\n1. The correct element is on the right of the element entered"+'\n2. '+table[str(n)][1])

            else:
                hint.config(text = "Hint:\n1. The correct element is on the left of the element entered"+'\n2. '+table[str(n)][1])
    e1.delete(0, END)
    no1.config(text="Score: "+str(s))
    no2.config(text="Wrong: "+str(w))
    print('submit')

def startGame():
    global no1, no2, n, s, w, tries, ques, atom, submit, ans, new, over, e1, start
    tries = 0
    n = 0
    s = 0
    w = 0
    e1.delete(0, END)
    message.config(text="")
    hint.config(text="")
    no1.config(text="Score: "+str(s))
    no2.config(text="Wrong: "+str(w))
    n = random.randrange(1, 119, 1)
    ques.config(text=str(n), font="Comic 40 bold")
    atom.place(x=200,y=50)
    submit.place(x=420, y=400)
    ans.place(x=240, y=400)
    new.place(x=40, y=400)
    over.place(x=580, y=400)
    e1.place(x=320,y=206)
    k.place(x=150,y=200)
    message.place(x=340,y=250, anchor = CENTER)
    hint.place(x=340,y=300, anchor = CENTER)
    ques.place(x=350, y=140, anchor='center')
    no2.place(x=590, y=0)
    print('start')
    start.place_forget()

def ans():
    message.config(text='Right answer is: '+table[str(n)][0],fg='black' )
    hint.config(text="")
    e1.config(state='disabled')
    submit.config(state='disabled')
    print('ans')

atom = Label(root, text="Atomic Number :", font='Comic 30 bold', bg='#fdcb6e')

ques = Label(root, text="1. Type your answer in the textbox provied. \n\n2. Click the submit button to check your answer\n\n3. If your answer is wrong you will be provided with hints.\n\n4. You can also skip the question by clicking the\n 'Generate next' button.\n\n5. If you're too excited to know the answer then you may click the \n'get answer' button.But then you can't attempt it anymore and have\n to click 'Generate next' button.\n\n6. Game ends after 6 wrong attempts", font='Comic 15 bold', bg='#fdcb6e')
ques.place(x=350, y=200, anchor='center')

message = Label(root, text="",font='Comic 15 bold', bg='#fdcb6e')
hint = Label(root, text="",font='Comic 12 bold', bg='#fdcb6e')

k=Label(root, text="Atomic Symbol: ",font='Comic 15 bold', bg='#fdcb6e')

no1 = Label(root, text="How To Play", font='Comic 15 bold', bg="#ecf0f1")
no1.place(x=0, y=0)

no2 = Label(root, text="Rules", font='Comic 15 bold', bg="#ecf0f1")

e1 = Entry(root, width=30)

submit = Button(root, command=submit, text="Submit", bg="#ecf0f1",font='Comic 12 bold')

start = Button(root, command=startGame, text="Start", bg="#ecf0f1",font='Comic 16 bold')
start.place(x=310, y=390)

ans = Button(root, command=ans, text="Get answer", bg="#ecf0f1",font='Comic 12 bold')

new = Button(root, command=newNo, text="Generate new", bg="#ecf0f1",font='Comic 12 bold')

over = Button(root, command=popup, text="Quit", bg="#ecf0f1",font='Comic 12 bold')

root.mainloop()

    
