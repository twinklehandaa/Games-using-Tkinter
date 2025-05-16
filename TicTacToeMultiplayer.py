from tkinter import *
import tkinter.messagebox as msg
# window
root= Tk()
root.title('TIC-TAC-TOE')

digits = [1,2,3,4,5,6,7,8,9]
mark = '' 
count = 0
panels = ["panel"]*10
def win(panels,sign):
    return ((panels[1] == panels[2] == panels [3] == sign)
            or (panels[1] == panels[4] == panels [7] == sign)
            or (panels[1] == panels[5] == panels [9] == sign)
            or (panels[2] == panels[5] == panels [8] == sign)
            or (panels[3] == panels[6] == panels [9] == sign)
            or (panels[3] == panels[5] == panels [7] == sign)
            or (panels[4] == panels[5] == panels [6] == sign) 
            or (panels[7] == panels[8] == panels [9] == sign))
def checker(digit):
    global count, mark, digits, panels, button1, button2, button3, button4, button5, button6, button7, button8, button9, msg, root

    if digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        panels[digit] = mark
        count += 1
        sign = mark

        if digit == 1:
            button1.config(text=mark)
        elif digit == 2:
            button2.config(text=mark)
        elif digit == 3:
            button3.config(text=mark)
        elif digit == 4:
            button4.config(text=mark)
        elif digit == 5:
            button5.config(text=mark)
        elif digit == 6:
            button6.config(text=mark)
        elif digit == 7:
            button7.config(text=mark)
        elif digit == 8:
            button8.config(text=mark)
        elif digit == 9:
            button9.config(text=mark)

        if win(panels, sign):
            if sign == 'X':
                msg.showinfo("Result", "Player1 wins")
            elif sign == 'O':
                msg.showinfo("Result", "Player2 wins")
            root.destroy()

    if count > 8 and not win(panels, 'X') and not win(panels, 'O'):
        msg.showinfo("Result", "Match Tied")
        root.destroy()
Label(root,text="player1 : X",font="times 15").grid(row=0,column=1)
Label(root,text="player2 : O",font="times 15").grid(row=0,column=2)

button1=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(1))
button1.grid(row=1,column=1)
button2=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda:checker(2))
button2.grid(row=1,column=2)

button3=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(3))
button3.grid(row=1,column=3)
button4=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(4))
button4.grid(row=2,column=1)

button5=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(5))
button5.grid(row=2,column=2)
button6=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(6))
button6.grid(row=2,column=3)

button7=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(7))
button7.grid(row=3,column=1)
button8=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(8))
button8.grid(row=3,column=2)

button9=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(9))
button9.grid(row=3,column=3)


root.mainloop()
