from tkinter import *

# main window

window = Tk()
window.title('BMI Calculator')
window.minsize(400,500)
window.iconbitmap(r'C:\Users\Marie\Desktop\BMI\pythonProject\bmi_icon.ico')
window.config(bg='#000')

# function replace comma by dot
def comma_dot(input):
    x = input.replace(',', '.')
    return float(x)

# function calculation
def calculation():
    kg = str(input_w.get())
    kg_float = comma_dot(kg)
    cm = str(input_h.get())
    m_float = comma_dot(cm)/100
    result = round(kg_float/(m_float*m_float), 1)
    label_result['text'] = result
    if result <= 18.5:
        label_result['fg'] = '#fce764'
    elif result > 18.5 and result <25:
        label_result['fg'] = '#86e26c'
    elif result >= 25 and result < 30:
        label_result['fg'] = '#ff9466'
    elif result >= 30:
        label_result['fg'] = '#f96769'

# function table reset
def reset():
    input_w.delete(0, END)
    input_h.delete(0, END)
    label_result['text'] = ''
    input_w.focus()


# label YOUR WEIGHT IN KG
label_w = Label(window, text='Your weight in Kg:', bg=window.cget('bg'), fg='white', font=('Calibri', 15))
label_w.place(x=110, y=20)

# field KG
input_w = Entry(font=('Calibri', 15), justify='center', width=11)
input_w.focus()
input_w.place(x=130, y=60)

# label YOUR HEIGHT IN CM
label_h = Label(window, text='Your height in cm:', fg='white', bg=window.cget('bg'), font=('Calibri', 15))
label_h.place(x=112, y=110)

# field CM
input_h = Entry(font=('Calibry', 15), justify='center', width=10)
input_h.place(x=130, y=150)

# button CALCULATE BMI
button_bmi = Button(window, text='Calculate BMI', font=('Calibry', 15), bg='#ff89aa', width=12, command=calculation)
button_bmi.place(x=40, y=190)

# button RESET
button_r = Button(window, text='Reset', font=('Calibry', 15), bg='#b1ff77', width=12, command=reset)
button_r.place(x=200, y=190)

# label YOUR BMI:
label_bmi = Label(window, text='Your BMI:', fg='white', bg=window.cget('bg'), font=('Calibri', 20))
label_bmi.place(x=100, y=250)

# label RESULT
label_result = Label(window, text='', fg='white', bg=window.cget('bg'), font=('Calibri', 20))
label_result.place(x=220, y=250)

# info
label_a = Label(window, text='bellow 18.5\tUnderweight', fg='#fce764', bg=window.cget('bg'), font=('Calibri', 13, 'bold'))
label_a.place(x=80, y=320)

label_b = Label(window, text='18.6 - 24.9\tHealthy Weight', fg='#86e26c', bg=window.cget('bg'), font=('Calibri', 13, 'bold'))
label_b.place(x=80, y=350)

label_c = Label(window, text='20.0 - 29.9\tOverweight', fg='#ff9466', bg=window.cget('bg'), font=('Calibri', 13, 'bold'))
label_c.place(x=80, y=380)

label_d = Label(window, text='30.0 and Above\tObesity', fg='#f96769', bg=window.cget('bg'), font=('Calibri', 13, 'bold'))
label_d.place(x=80, y=410)

window.mainloop()