from tkinter import *
wincal=Tk()
wincal.resizable(0,0)#size not changable
wincal.title('Calculator')
def btn_clear():
    global expression
    expression=""
    input_text.set("")

def btn_click(i):
    global expression
    expression=expression+str(i)
    input_text.set(expression)

def btn_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""

expression=""
input_text=StringVar()#accept String
input_frame=Frame(wincal,width=320,height=50,highlightbackground='black',highlightcolor='black',highlightthickness=2)
input_frame.pack(side=TOP)#frame seated at top 
input_field=Entry(input_frame,font=('arial',18,'bold'),textvariable=input_text,width=50,bg='skyblue',justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btns_frame=Frame(wincal,width=320,height=290,bg='grey')
btns_frame.pack()


opbrac=Button(btns_frame,text="(",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('('))
opbrac.grid(row=0,column=0,padx=1,pady=1)


clbrac=Button(btns_frame,text=")",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click(")"))
clbrac.grid(row=0,column=1)

mod=Button(btns_frame,text="%",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('%'))
mod.grid(row=0,column=2)


divide=Button(btns_frame,text="/",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('/'))
divide.grid(row=0,column=3)

seven=Button(btns_frame,text="seven",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('7'))
seven.grid(row=1,column=0)

eight=Button(btns_frame,text="eight",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('8'))
eight.grid(row=1,column=1)

nine=Button(btns_frame,text="nine",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('9'))
nine.grid(row=1,column=2)

mult=Button(btns_frame,text="*",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('*'))
mult.grid(row=1,column=3)

four=Button(btns_frame,text="four",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('4'))
four.grid(row=2,column=0)

five=Button(btns_frame,text="five",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('5'))
five.grid(row=2,column=1)

six=Button(btns_frame,text="six",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('6'))
six.grid(row=2,column=2)

sub=Button(btns_frame,text="-",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('-'))
sub.grid(row=2,column=3)

one=Button(btns_frame,text="one",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('1'))
one.grid(row=3,column=0)


two=Button(btns_frame,text="two",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('2'))
two.grid(row=3,column=1)


three=Button(btns_frame,text="three",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('3'))
three.grid(row=3,column=2)

plus=Button(btns_frame,text="+",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('+'))
plus.grid(row=3,column=3)

zero=Button(btns_frame,text="zero",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('0'))
zero.grid(row=4,column=0)

clear=Button(btns_frame,text="clear",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_clear()).grid(row=4,column=1)

point=Button(btns_frame,text=".",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_click('.'))
point.grid(row=4,column=2)

equal=Button(btns_frame,text="=",width=20,height=2 ,cursor='hand2',fg='white',bg='black',command=lambda:btn_equal())
equal.grid(row=4,column=3)
wincal.mainloop()#run 
