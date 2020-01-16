from tkinter import *
import parser
w=5         #width of button
h=2         #height of button
border=0    #border of button
root = Tk()
root.title('Caculator')

print('History of operations:')

#get user input to text field
i=0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1

#get user inputs of operations
def get_operation(operator):
    global i
    op_len = len(operator)
    display.insert(i,operator)
    i+=op_len

#resets to normal display
def reset():
    display.config(bg='White',fg='Black')

#clear screen
def clearAll():
    display.delete(0,END)

#backspace
def delete():
    disp_str= display.get()
    clearAll()
    display.insert(0,disp_str[:-1]) #OR display.delete(len(disp_str)-1,END)

#calculate sequence
def answer():
    string= display.get()
    result = 'Error'
    try:
        a = parser.expr(string).compile()
        result = eval(a)
        clearAll()
        display.config(bg='Green',fg='White')
        display.insert(0,result)
        display.after(300,reset)
        
    except Exception:
        clearAll()
        display.config(bg='Red',fg='White')
        display.insert(0,'Error')
        display.after(300,reset)
    print(string + ' = ' + str(result))

#adding input field
display = Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)
root.bind('<Return>', lambda _: answer()) #enter to claculate answer

#adding number buttons
Button(root,text='1',width=w, command = lambda :get_variables(1), bd=border,height=h).grid(row=2,column=0)
Button(root,text='2',width=w, command = lambda :get_variables(2), bd=border,height=h).grid(row=2,column=1)
Button(root,text='3', width=w, command = lambda :get_variables(3), bd=border,height=h).grid(row=2,column=2)

Button(root,text='4', width=w, command = lambda :get_variables(4), bd=border,height=h).grid(row=3,column=0)
Button(root,text='5', width=w, command = lambda :get_variables(5), bd=border,height=h).grid(row=3,column=1)
Button(root,text='6', width=w, command = lambda :get_variables(6), bd=border,height=h).grid(row=3,column=2)

Button(root,text='7', width=w, command = lambda :get_variables(7), bd=border,height=h).grid(row=4,column=0)
Button(root,text='8', width=w, command = lambda :get_variables(8), bd=border,height=h).grid(row=4,column=1)
Button(root,text='9', width=w, command = lambda :get_variables(9), bd=border,height=h).grid(row=4,column=2)

#adding operator buttons
Button(root, text='AC\n©Vasu', width=w, command=lambda :clearAll(), bd=border,height=h).grid(row=5,column=0)
Button(root, text='0', width=w, command = lambda :get_variables(0), bd=border,height=h).grid(row=5,column=1)
Button(root, text='=', width=w, command=lambda : answer(), bd=border,height=h).grid(row=5,column=2)

Button(root, text='+', width=w, command=lambda : get_operation('+'), bg='#FF9500',fg='White', bd=border,height=h).grid(row=2,column=3)
Button(root, text='-', width=w, command=lambda : get_operation('-'), bg='#FF9500',fg='White', bd=border,height=h).grid(row=3,column=3)
Button(root, text='x', width=w, command=lambda : get_operation('*'), bg='#FF9500',fg='White', bd=border,height=h).grid(row=4,column=3)
Button(root, text='/', width=w, command=lambda : get_operation('/'), bg='#FF9500',fg='White', bd=border,height=h).grid(row=5,column=3)

#adding new operations
Button(root, text='pi', width=w, command=lambda : get_operation('3.14'), bg='Grey',fg='White',bd=border,height=h).grid(row=2,column=4)
Button(root, text='%', width=w, command=lambda : get_operation('%'), bg='Grey',fg='White',bd=border,height=h).grid(row=3,column=4)
Button(root, text='(', width=w, command=lambda : get_operation('('), bg='Grey',fg='White',bd=border,height=h).grid(row=4,column=4)
Button(root, text='exp', width=w, command=lambda : get_operation('**'), bg='Grey',fg='White',bd=border,height=h).grid(row=5,column=4)

Button(root, text='del', width=w, command=lambda :delete(), bg='Grey',fg='White',bd=border,height=h).grid(row=2,column=5)
Button(root, text='sqrt', width=w, command=lambda : get_operation('**0.5'), bg='Grey',fg='White',bd=border,height=h).grid(row=3,column=5)
Button(root, text=')', width=w, command=lambda : get_operation(')'), bg='Grey',fg='White',bd=border,height=h).grid(row=4,column=5)
Button(root, text='^2', width=w, command=lambda : get_operation('**2'), bg='Grey',fg='White',bd=border,height=h).grid(row=5,column=5)

root.mainloop()