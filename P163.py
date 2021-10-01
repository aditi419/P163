from tkinter import *
root = Tk()
root.title('Heart Diagnose Report')
root.geometry('600x600')
root.configure(background='#F08080')

question1 = StringVar(value='0')
label1 = Label(root,text='Do you experience shortness of breath during routine activies?')
label1.pack()
question1_r1 = Radiobutton(root,text='Yes',variable=question1,value='yes')
question1_r1.pack()
question1_r2 = Radiobutton(root,text='No',variable=question1,value='no')
question1_r2.pack()

question2 = StringVar(value='0')
label2 = Label(root,text='Do you have swellong in the feet/ankles/legs (shoes feel tighter) or abdomen?')
label2.pack()
question2_r1 = Radiobutton(root,text='Yes',variable=question2,value='yes')
question2_r1.pack()
question2_r2 = Radiobutton(root,text='No',variable=question2,value='no')
question2_r2.pack()

question3 = StringVar(value='0')
label3 = Label(root,text='Do you feel any of these symptoms - confusion,disorientation, or loss of memory?')
label3.pack()
question3_r1 = Radiobutton(root,text='Yes',variable=question3,value='yes')
question3_r1.pack()
question3_r2 = Radiobutton(root,text='No',variable=question3,value='no')
question3_r2.pack()

question4 = StringVar(value='0')
label4 = Label(root,text='Do you experience shortness of breathe while resting/laying down?')
label4.pack()
question4_r1 = Radiobutton(root,text='Yes',variable=question4,value='yes')
question4_r1.pack()
question4_r2 = Radiobutton(root,text='No',variable=question4,value='no')
question4_r2.pack()

question5 = StringVar(value='0')
label5 = Label(root,text='Do you experience persistant wheezing/coughing that produces white or pink blood tinged mucus?')
label5.pack()
question5_r1 = Radiobutton(root,text='Yes',variable=question5,value='yes')
question5_r1.pack()
question5_r2 = Radiobutton(root,text='No',variable=question5,value='no')
question5_r2.pack()

def score():
    score = 0
    if question1.get() == 'yes' :
        score = score + 20
        print(score)
    if question2.get() == 'yes' :
        score = score + 20
        print(score)
    if question3.get() == 'yes' :
        score = score + 20
        print(score)
    if question4.get() == 'yes' :
        score = score + 20
        print(score)
    if question5.get() == 'yes' :
        score = score + 20
        print(score)
        
    if score <= 20:
        messagebox.showinfo('Report',"You don't need to visit a doctor")
    elif score > 20 and score < 60:
        messagebox.showinfo('Report','You might want to visit a doctor')
    else:
        messagebox.showinfo('Report','I strongly advise you to see a doctor')

btn = Button(root,text='click me',command=score)
btn.pack()

root.mainloop()