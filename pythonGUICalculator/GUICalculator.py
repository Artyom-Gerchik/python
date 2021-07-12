import tkinter
import tkmacosx
import tkinter.font as font
from tkinter import messagebox

mainWindow = tkinter.Tk()
mainWindow.geometry("120x210")  # 30 pixels on top label (disabled)
mainWindow.resizable(0, 0)
mainWindow.configure(bg='black')
mainWindow.overrideredirect(1)  # top border controlled by me right now

mainLabel = tkinter.Label(mainWindow, bg='black', fg='white', text='0')
mainLabel.place(x=0, y=30)
mainLabel.configure(text="0")

global dotInserted
dotInserted = 0  # 0 - not inserted yet. 1 - inserted yet.

global firstNum
global secondNum
global result

global plusOperation
plusOperation = 0  # 0 - no. 1 - yes.

global minusOperation
minusOperation = 0  # 0 - no. 1 - yes.

global multiplyOperation
multiplyOperation = 0  # 0 - no. 1 - yes.

global divisionOperation
divisionOperation = 0  # 0 - no. 1 - yes.

global solved
solved = 0  # 0 - no. 1 - yes.


def changeValue(input):
    global dotInserted
    global solved

    if solved == 1 and input == '.':
        mainLabel.configure(text='0')
        solved = 0
    if solved == 1:
        mainLabel.configure(text=input)
        solved = 0
    else:
        if input == '.':
            if dotInserted == 0:
                if str(mainLabel.cget("text")) == '0' and input != '.':
                    mainLabel.configure(text=input)
                    dotInserted = 1
                else:
                    tempText = mainLabel.cget("text")
                    tempOutput = str(tempText) + str(input)
                    mainLabel.configure(text=tempOutput)
                    dotInserted = 1
        else:
            if str(mainLabel.cget("text")) == '0' and input != '.':
                mainLabel.configure(text=input)

            else:
                tempText = mainLabel.cget("text")
                tempOutput = str(tempText) + str(input)
                mainLabel.configure(text=tempOutput)


def clearLabel():
    global dotInserted
    mainLabel.configure(text='0')
    dotInserted = 0


def handlePlus():
    global firstNum
    global plusOperation

    if minusOperation == 0 and divisionOperation == 0 and multiplyOperation == 0:
        firstNum = float(mainLabel.cget("text"))
        plusOperation = 1
        clearLabel()


def handleMinus():
    global firstNum
    global minusOperation

    if plusOperation == 0 and divisionOperation == 0 and multiplyOperation == 0:
        firstNum = float(mainLabel.cget("text"))
        minusOperation = 1
        clearLabel()


def handleMultiply():
    global firstNum
    global multiplyOperation

    if plusOperation == 0 and minusOperation == 0 and divisionOperation == 0:
        firstNum = float(mainLabel.cget("text"))
        multiplyOperation = 1
        clearLabel()


def handleDivision():
    global firstNum
    global divisionOperation

    if plusOperation == 0 and minusOperation == 0 and multiplyOperation == 0:
        firstNum = float(mainLabel.cget("text"))
        divisionOperation = 1
        clearLabel()


def solve():
    global firstNum
    global secondNum
    global result

    global plusOperation
    global minusOperation
    global multiplyOperation
    global divisionOperation

    global solved

    if plusOperation == 1:
        secondNum = float(mainLabel.cget("text"))
        result = firstNum + secondNum

        if (float(result) - int(result)) != 0:  # if result int - preventing .0 at the end
            mainLabel.configure(text=str(result))
        else:
            mainLabel.configure(text=str(int(result)))

    if minusOperation == 1:
        secondNum = float(mainLabel.cget("text"))
        result = firstNum - secondNum
        if (float(result) - int(result)) != 0:  # if result int - preventing .0 at the end
            mainLabel.configure(text=str(result))
        else:
            mainLabel.configure(text=str(int(result)))

    if multiplyOperation == 1:
        secondNum = float(mainLabel.cget("text"))
        result = firstNum * secondNum
        if (float(result) - int(result)) != 0:  # if result int - preventing .0 at the end
            mainLabel.configure(text=str(result))
        else:
            mainLabel.configure(text=str(int(result)))

    if divisionOperation == 1:
        secondNum = float(mainLabel.cget("text"))
        if secondNum == 0:
            messagebox.showinfo(title='Info Box', message='Division By Zero', icon='warning')
        else:
            result = firstNum / secondNum
            if (float(result) - int(result)) != 0:  # if result int - preventing .0 at the end
                mainLabel.configure(text=str(result))
            else:
                mainLabel.configure(text=str(int(result)))

    firstNum = 0
    secondNum = 0
    result = 0

    plusOperation = 0
    minusOperation = 0
    multiplyOperation = 0
    divisionOperation = 0

    solved = 1


def changeSign():
    tempNum = float(mainLabel.cget("text"))
    if (float(tempNum) - int(tempNum)) == 0:
        tempNum = int(tempNum)

    if tempNum < 0:
        mainLabel.configure(text=str(abs(tempNum)))
    else:
        mainLabel.configure(text=str(-tempNum))


def handlePercent():
    tempNum = float(mainLabel.cget("text"))
    tempNum /= 100

    if (float(tempNum) - int(tempNum)) == 0:
        tempNum = int(tempNum)

    mainLabel.configure(text=str(tempNum))


buttonFont = font.Font(family='Terminal', size=10, weight='bold')
buttonExit = tkmacosx.Button(mainWindow, text='✕', font=buttonFont, anchor='center', height=15, width=15, fg='#740000',
                             bg='#ff5f56', activebackground='#be4741', activeforeground='#740000',
                             borderless=1, focuscolor='', command=lambda: mainWindow.destroy())
buttonExit.place(x=0, y=0)

buttonDot = tkmacosx.Button(mainWindow, text='.', height=30, width=30, fg='white', bg='gray',
                            activebackground='lightgray', borderless=1, focuscolor='',
                            command=lambda: changeValue('.'))
buttonDot.place(x=60, y=180)

button0 = tkmacosx.Button(mainWindow, text='0', anchor='w', height=30, width=60, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(0))
button0.place(x=0, y=180)

button1 = tkmacosx.Button(mainWindow, text='1', height=30, width=30, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(1))
button1.place(x=0, y=150)

button2 = tkmacosx.Button(mainWindow, text='2', height=30, width=30, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(2))
button2.place(x=30, y=150)

button3 = tkmacosx.Button(mainWindow, text='3', height=30, width=30, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(3))
button3.place(x=60, y=150)

button4 = tkmacosx.Button(mainWindow, text='4', height=30, width=30, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(4))
button4.place(x=0, y=120)

button5 = tkmacosx.Button(mainWindow, text='5', height=30, width=30, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(5))
button5.place(x=30, y=120)

button6 = tkmacosx.Button(mainWindow, text='6', height=30, width=30, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(6))
button6.place(x=60, y=120)

button7 = tkmacosx.Button(mainWindow, text='7', height=30, width=30, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(7))
button7.place(x=0, y=90)

button8 = tkmacosx.Button(mainWindow, text='8', height=30, width=30, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(8))
button8.place(x=30, y=90)

button9 = tkmacosx.Button(mainWindow, text='9', height=30, width=30, fg='white', bg='gray',
                          activebackground='lightgray', borderless=1, focuscolor='',
                          command=lambda: changeValue(9))
button9.place(x=60, y=90)

buttonClear = tkmacosx.Button(mainWindow, text='C', height=30, width=30, fg='black', bg='lightgray',
                              activebackground='#F0F5F0', activeforeground='black',
                              borderless=1, focuscolor='', command=lambda: clearLabel())
buttonClear.place(x=0, y=60)

buttonPlus = tkmacosx.Button(mainWindow, text='+', height=30, width=30, fg='white', bg='orange',
                             activebackground='#FFD27E', borderless=1, focuscolor='',
                             command=lambda: handlePlus())
buttonPlus.place(x=90, y=150)

buttonMinus = tkmacosx.Button(mainWindow, text='-', height=30, width=30, fg='white', bg='orange',
                              activebackground='#FFD27E', borderless=1, focuscolor='',
                              command=lambda: handleMinus())
buttonMinus.place(x=90, y=120)

buttonMultiply = tkmacosx.Button(mainWindow, text='x', height=30, width=30, fg='white', bg='orange',
                                 activebackground='#FFD27E',
                                 borderless=1, focuscolor='', command=lambda: handleMultiply())
buttonMultiply.place(x=90, y=90)

buttonDivide = tkmacosx.Button(mainWindow, text='÷', height=30, width=30, fg='white', bg='orange',
                               activebackground='#FFD27E', borderless=1, focuscolor='',
                               command=lambda: handleDivision())
buttonDivide.place(x=90, y=60)

buttonEquals = tkmacosx.Button(mainWindow, text='=', height=30, width=30, fg='white', bg='orange',
                               activebackground='#FFD27E', borderless=1, focuscolor='',
                               command=lambda: solve())
buttonEquals.place(x=90, y=180)

buttonChangeSign = tkmacosx.Button(mainWindow, text='+/-', height=30, width=30, fg='black', bg='lightgray',
                                   activebackground='#F0F5F0', activeforeground='black',
                                   borderless=1, focuscolor='', command=lambda: changeSign())
buttonChangeSign.place(x=30, y=60)

buttonPercent = tkmacosx.Button(mainWindow, text='%', height=30, width=30, fg='black', bg='lightgray',
                                activebackground='#F0F5F0', activeforeground='black',
                                borderless=1, focuscolor='', command=lambda: handlePercent())
buttonPercent.place(x=60, y=60)

mainWindow.mainloop()
