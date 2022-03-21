from cgitb import text
from tkinter import *
import random
from tokenize import Number
from tkinter import messagebox
root= Tk()
# create our matches
matches=['A','A','B','B','C','C','D','D','E','E','F','F','G','G','H','H','I','I','J','J' ]
random.shuffle(matches)

count=0
answer_list=[]
answer_dictionary={}
#create button Frame
my_frame=Frame(root)
my_frame.pack(pady=10)

#funiction of click buttons

def button_click(p,num):

 global count, answer_dictionary,answer_list
 if p["text"]==' ' and count<2:
     p["text"]=matches[num]
     #adding num to list
     answer_list.append(num)
     #adding button and num to answer dictionary
     answer_dictionary[p]=matches[num]
     #increasing our counter
     count=count+1
 if len(answer_list)==2:
     if matches[answer_list[0]]==matches[answer_list[1]] and matches[answer_list[0]]!='*' and matches[answer_list[1]]!='*':
         matches[answer_list[0]] ='*' 
         matches[answer_list[1]]='*'
         my_label.config(text="match!")
         
         for key in answer_dictionary:
             key["text"]= '*'
             key["state"]="disabled"
         count=0
         answer_list=[]
         answer_dictionary={}
     else:
         my_label.config(text="wrong!")
         count=0
         answer_list=[]
         #popping a message
         messagebox.showinfo("incorrect")
         #buttons to alphabets
         for key in answer_dictionary:
             key["text"]=" "
         answer_dictionary={}

#define buttons
p0=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p0,0) )
p1=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p1,1) )
p2=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p2,2) )
p3=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p3,3) )
p4=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p4,4) )
p5=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p5,5) )
p6=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p6,6) )
p7=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p7,7) )
p8=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p8,8) )
p9=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p9,9) )
p10=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p10,10) )
p11=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p11,11) )
p12=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p12,12) )
p13=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p13,13) )
p14=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p14,14) )
p15=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p15,15) )
p16=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p16,16) )
p17=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p17,17) )
p18=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p18,18) )
p19=Button(my_frame,text=' ',font=("helvetica",20),height=3,width=6,command=lambda:button_click(p19,19) )

#grid buttons
p0.grid(row=0,column=0)
p1.grid(row=0,column=1)
p2.grid(row=0,column=2)
p3.grid(row=0,column=3)
p4.grid(row=0,column=4)

p5.grid(row=1,column=0)
p6.grid(row=1,column=1)
p7.grid(row=1,column=2)
p8.grid(row=1,column=3)
p9.grid(row=1,column=4)

p10.grid(row=2,column=0)
p11.grid(row=2,column=1)
p12.grid(row=2,column=2)
p13.grid(row=2,column=3)
p14.grid(row=2,column=4)

p15.grid(row=3,column=0)
p16.grid(row=3,column=1)
p17.grid(row=3,column=2)
p18.grid(row=3,column=3)
p19.grid(row=3,column=4)

my_label=Label(root,text="")
my_label.pack(pady=20)
root.mainloop()



