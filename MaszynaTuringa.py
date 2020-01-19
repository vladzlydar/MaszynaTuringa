import time
from tkinter import *

root = Tk()

root.title("Maszyna Turinga")

global tape
global head
global currentState

head = 0
tape = []
slowo = StringVar()

stanPoczatkowy = "q0"
stanAkceptujacy = "qA"

def onCiagEntered(event):
    global  tape
    global  currentState
    global head
    k = 0
    finishLabel.grid_forget()
    tape = ["#"] * 2 + list(slowo.get()) + ["#"] * 2
    head = len(tape) - 1
    currentState = "q0"
    for i in tapeFrame.winfo_children():
        i.destroy()
    tapeFrame.update()
    for i in range(len(tape)):
        if str(tape[i]) not in ["0", "1", "#"]:
            tape[i] = "#"
    for i in range(len(tape)):
        if str(tape[i]) in ["0","1","#"]:
            Label(tapeFrame, text = tape[i], font= 25, fg = "black",  bg="white").pack(expand =True ,fill = "x", side= LEFT)
            tapeFrame.grid_columnconfigure(i, weight=1)
            tapeFrame.grid_rowconfigure(1, weight=1)
            tapeFrame.update()
    head = head - k
    tapeFrame.winfo_children()[head]["bg"] = "orange"
    wskaznikStan["text"] = currentState
    wskaznikStan.update()

tapeFrame = Frame(root, bg="black", height="50")
navigationButtonsFrame = Frame(root, height="50")
statusAndInputFrame = Frame(root, height="50")
nextButton = Button(navigationButtonsFrame, text="Next Step")
autoButton = Button(navigationButtonsFrame, text="AutoRun")
labelStan = Label(statusAndInputFrame,text="AKTUALNY STAN MASZYNY ->")
wskaznikStan = Label(statusAndInputFrame,  bg= "red",  fg = "black", width=3, font="bold")
poleCiagu = Entry(statusAndInputFrame, textvariable = slowo)
finishLabel = Label(navigationButtonsFrame, text = "Work Finished")
labelInput = Label(statusAndInputFrame, text= "Ciag do analizy:")

statusAndInputFrame.grid(row = 0, column = 0)
tapeFrame.grid(row=1, column = 0, sticky= "nswe")
navigationButtonsFrame.grid(row = 2, column = 0)

labelStan.grid(row = 0,column = 0, sticky = "w")
wskaznikStan.grid(row = 0, column = 1 , sticky = "w")
labelInput.grid(row = 0, column = 2, sticky = "e",  padx= (30,0))
poleCiagu.grid(row = 0,column = 3, sticky= "e")
nextButton.grid(row = 0 , column = 0, padx=(0,150))
autoButton.grid(row = 0 , column = 2, padx=(150,0))

poleCiagu.bind('<Return>',onCiagEntered)

tabelaPrzejsc = {
    ("q0", "0"): ("q1", "1", "L"),
    ("q0", "1"): ("q2", "0", "L"),
    ("q0", "#"): ("q0", "#", "L"),
    ("q1", "0"): ("q3", "1", "L"),
    ("q1", "1"): ("q4", "0", "L"),
    ("q1", "#"): ("qA", "1", "L"),
    ("q2", "0"): ("q5", "0", "L"),
    ("q2", "1"): ("q6", "1", "L"),
    ("q2", "#"): ("q4", "0", "L"),
    ("q3", "0"): ("q3", "0", "L"),
    ("q3", "1"): ("q3", "1", "L"),
    ("q3", "#"): ("qA", "#", "L"),
    ("q4", "0"): ("q3", "1", "L"),
    ("q4", "1"): ("q4", "0", "L"),
    ("q4", "#"): ("qA", "1", "L"),
    ("q5", "0"): ("q3", "1", "L"),
    ("q5", "1"): ("q5", "0", "L"),
    ("q5", "#"): ("qA", "1", "L"),
    ("q6", "0"): ("q3", "1", "L"),
    ("q6", "1"): ("q6", "0", "L"),
    ("q6", "#"): ("qA", "1", "L")
}
currentState = stanPoczatkowy

def nextStep(event):
    global currentState
    global head
    global tape
    if not(currentState=="qA"):
        currentState, tape[head], head_d = tabelaPrzejsc[currentState,tape[head]]
        wskaznikStan["text"] = currentState
        wskaznikStan.update()
        tapeFrame.winfo_children()[head]["bg"] = "white"
        tapeFrame.winfo_children()[head]["text"] = tape[head]
        tapeFrame.update()
        # print(tape)
        # print(" "*2+" "*5*head +"^")
        if head_d == "L":
            head-=1
        else:
            head+=1
        tapeFrame.winfo_children()[head]["bg"] = "orange"
    else:
        finishLabel.grid(row =0, column =1)

def autoRun(event):
    while not(currentState=="qA"):
        nextStep(event)
        tapeFrame.update()
        time.sleep(0.5)
    finishLabel.grid(row=0, column=1)

nextButton.bind('<Button-1>', nextStep)
autoButton.bind('<Button-1>', autoRun)

root.mainloop()
