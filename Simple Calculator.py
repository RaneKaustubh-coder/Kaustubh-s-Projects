# importing tkinter for GUI for Calculator.
from tkinter import *

# Create Calculator Window.
calculator = Tk()

# GUI application title.
calculator.title('Calculator')

#GUI height and width.
calculator.geometry('400x350')

# This is used to place the Buttons and Display as per the Height and Width of the GUI Window. 
# This is also useful for Auto Adjusting the Buttons and Display as per the user.
# Because of this grid we can use sticky command.
calculator.grid_columnconfigure(0, weight=1)
calculator.grid_columnconfigure(1, weight=1)
calculator.grid_columnconfigure(2, weight=1)
calculator.grid_columnconfigure(3, weight=1)
calculator.grid_rowconfigure(0, weight=1)
calculator.grid_rowconfigure(1, weight=1)
calculator.grid_rowconfigure(2, weight=1)
calculator.grid_rowconfigure(3, weight=1)
calculator.grid_rowconfigure(4, weight=1)
calculator.grid_rowconfigure(5, weight=1)
calculator.grid_rowconfigure(6, weight=1)

# This is a label in the GUI application.
lab = Label(calculator, text = 'Simple Calculator')
lab.grid(row=0, column=0)

# To display which number is clicked on GUI.
display = Entry(calculator, width=50, bg='White')
display.grid(row=1, column=1, columnspan=3, pady=5, sticky='NSEW')

# To display the Button which were used.
def text_update(number):
    display.insert(END,str(number))

# This function is used for the functionality of the Buttons.
def calculate_result():
    try:
        # This eval is responsible for the addition, subtrating, Multiplying and Dividing.
        result = eval(display.get()) 
        display.delete(0, END)  
        display.insert(END, str(result))  
    except Exception:
        display.delete(0, END)
        display.insert(END, "Error")  

def display_button():

        #Creating button
        button_calci1 = {}
        num = ['1','2','3','+']
        # This for loop is used because the numbers must be added to GUI as buttons and in the same format as in the list.
        for i,n in enumerate(num):
            button_calci1[n] = Button(calculator, text= n, command= lambda x = n: text_update(x))
            # Remamber that stiky = 'NSEW' is used for the auto resizing of the buttons on GUI while adjesting the GUI Window .
            button_calci1[n].grid(row = 2, column = i, sticky = 'NSEW')
    
        button_calci2 = {}
        num = ['4','5','6','-']
        # This for loop is used because the numbers must be added to GUI as buttons and in the same format as in the list.
        for i,n in enumerate(num):
            button_calci2[n] = Button(calculator, text= n, command = lambda x = n: text_update(x))
            button_calci2[n].grid(row = 3, column = i, sticky='NSEW')

        button_calci3 = {}
        num = ['7','8','9','*']
        # This for loop is used because the numbers must be added to GUI as buttons and in the same format as in the list.
        for i,n in enumerate(num):
            button_calci3[n] = Button(calculator, text= n, command= lambda x = n: text_update(x))
            button_calci3[n].grid(row = 4, column = i, sticky='NSEW')

        button_calci4 = {}
        num = ['AC','0','C','/']
        # This for loop is used because the numbers must be added to GUI as buttons and in the same format as in the list.
        for i,n in enumerate(num):
            button_calci4[n] = Button(calculator, text= n, command= lambda x = n: text_update(x))
            button_calci4[n].grid(row = 5, column = i, sticky='NSEW')
            if n == 'AC':
                button_calci4[n] = Button(calculator, text= n, command= lambda: display.delete(0,END))
                
            elif n == 'C':
                button_calci4[n] = Button(calculator, text= n, command= lambda: display.delete(len(display.get())-1,END))
                
            else:
                button_calci4[n] = Button(calculator, text= n, command= lambda x = n: text_update(x))

            button_calci4[n].grid(row = 5, column = i, sticky='NSEW')


        button_calci5 = {}
        num = ['=']
        # This for loop is used because the numbers must be added to GUI as buttons and in the same format as in the list.
        for i,n in enumerate(num):
            if n == '=':
                button_calci5[n] = Button(calculator, text= n, command= lambda: calculate_result())
                button_calci5[n].grid(row = 6, column = i, sticky='NSEW')
            else:
                button_calci5[n] = Button(calculator, text=n, command=lambda x=n: text_update(x))
display_button()    
calculator.mainloop()