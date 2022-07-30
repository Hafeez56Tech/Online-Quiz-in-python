
## some imports
import random,sys  ## import random mudule
from tkinter import *
from tkinter.ttk import Separator   ## through this we can del any window we want
from tkinter.messagebox import showinfo
from time import time,strftime

## making a window
Window = Tk()     ## creating a root window ## scree
Window.geometry("1000x600")  ## parameters , width and height pixels
Window.resizable(0,0) ## prevents from resizing the window
Window.title("Online Quiz Managment System")    ##our title

## Set an image as icon of app
img=('wm','iconphoto',Window._w,PhotoImage(file='hafeez.png'))   #taking an img as icon of app ##few attribues
Window.tk.call(img)  ## we add our img as icon
Window.config(bg='black')  ## intilizing background as black
i=0 ## initilizing a variable as zero
timeLeft={'min':5,'sec':5} ## 5 mins for quiz and 5 for reading instructions


intro="""1: You have multiple chioce question
        2:  You must to complete with in given time
        3:   At the end you will see their score
        Good luck"""
def timeShow():
    global i,timeLeft
    if(timeLeft['min']==5 and timeLeft['sec']>0):
       note.config(text='you can Start Quiz after  {}  seconds.'.format(timeLeft['sec']))
       timeLeft['sec']-=1

    elif timeLeft['sec']>0:
        submit.config(state=NORMAL)
        instruction.config(text='')
        timeLeft['sec']-=1
        note.config(text='Time left :  {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
    elif timeLeft['min']!=0 and timeLeft['sec']==0:
        timeLeft['min']-=1
        timeLeft['sec']=59
        note.config(text='Time left :  {}min:{}sec'.format(timeLeft['min'],timeLeft['sec']))
    elif (timeLeft['min']==0 and timeLeft['sec']==0):
          print('Time up!')
          result()
    showtime.config(text=strftime('%H:%M:%S'))
    showtime.after(1000,timeShow)

#___________ student___________

def getDetails():
    global name ,roll,mainWindow,Name,Roll
    Name=name.get()
    Roll=roll.get()
    Window.deiconify()
    timeShow()
    mainWindow.destroy()

def attendance():
    global name,roll,mainWindow
    mainWindow=Toplevel(Window)
    mainWindow.geometry("700x500")
    mainWindow.resizable(0,0)
    mainWindow.title('Quiz Managment System [make attendee]')
    mainWindow.tk.call(img)
    mainWindow.config(bg='black')
    #------
    appName=Label(mainWindow,text=title,font=('impact',20,'italic'),
                  justify=CENTER,bg='goldenrod2',fg='white')
    appName.pack(side=TOP,fill=BOTH)
    #---time---
    #showtime=Label(mainWindow,text='',font=20,fg='red',bg='goldenrod2')
    #showtime.place(x=600,y=50)

    #----------Label----
    info=Label(mainWindow,text='Enter Name and Roll  Number',bg='black',fg='goldenrod1',font=('arial',15))
    info.place(x=210,y=200)
    name=Entry(mainWindow,width=30)
    name.place(x=250,y=235)
    roll=Entry(mainWindow,width=30)
    roll.place(x=250,y=260)
    name.insert(END,'  ')
    roll.insert(END,'   ')
    submit=Button(mainWindow,text='config & Start',width=20,bg='goldenrod1',fg='green',command=getDetails)
    submit.place(x=265,y=300)
    mainWindow.mainloop()

#--------quit---
def quit_function():
    answer=showinfo(title="good luck",message="we will contect you soon")
    if(answer=='ok'):
        sys.exit(Window.destroy())
#------desable----
def desableAllButton():
    option1.config(state=DISABLED)
    option2.config(state=DISABLED)
    option3.config(state=DISABLED)
    option4.config(state=DISABLED)
def enableAllButton():
    option1.config(state=NORMAL)
    option2.config(state=NORMAL)
    option3.config(state=NORMAL)
    option4.config(state=NORMAL)
#--------result---
def result():
    global score,Name,Roll
    Window.withdraw()
    top=Toplevel(Window)
    top.tk.call('wm','iconphoto',top._w,PhotoImage(file='hafeez.png'))

    top.geometry('200x100')
    top.resizable(0,0)
    top.title("QUIZ RESULT")
    top.config(bg='blue')
    top.protocol('WM_DELET_WINDOW',quit_function)
    filename=Name+'_'+Roll+'.txt'
    data='\nstudent: '+Name+'\nRoll: '+Roll+'\nScore'+str(score)+'\ncompleted Quiz at:'+strftime('%d%m%y --%H:%M:%S')
    with open(filename,'a') as file:
        file.write(data)

    label=Label(top,text='Quiz over...\nscore:  '+str(score),font=30,fg='white',bg='blue').place(x=50,y=25)
    exitBtn=Button(top,text='Exit',width=10,bg='black',fg='red',command=quit_function).place(x=50,y=70)
    top.mainloop()


#--------questions nd their corresponding answer----
questions={'python is a?': 'human readble',       ## created a dictionary
           'out put 45/5-4 in python ?':'5',
'''i=0
while(i<3):
    print(i," ")
    i++
           ///what is the output/''':'0 1 2',
            '''what  is  the output ?
print("welllcome") [::-1]''':'emoclew',
           'what will print 45%6==0?':'False'}
#------answer---
que=[]          ## list variable
ans=[]
for key,value in questions.items():
    que.append(key)        ## through append our qs andanswers gets separetd
    ans.append(value)
#-------options------
options=[
    ['low level',ans[0],'machine','C++'],         ## created a list
    [ans[1],'12','6','error'],        ## correct ans [1]
    ['012','123',ans[2],'none'],         # correct ans [2]
    ['welcome','w e l c o m e',ans[3],'error'],
    ['7.33','true','7',ans[4]]]

#-------ygygy

currentQ=''        ## by default nothing
queNo=None        ##none
currentA=''       #by default nothing
score=0           ## zero
qn=1        ## for printing number of a question
var=StringVar()
def _next():            ## by using some global variables
    global currentQ,currentA,queNo,score,i,qn
    i=0                      # initializing i equals to zero
    if(len(que)>0):         # till last question is left
        currentQ=random.choice(que)
        print(currentQ)
        q=Label(Window,text='Que. '+str(qn),font=('arial',10)).place(x=20,y=80)
        qn+=1


        #--------
        queNo=que.index(currentQ)
        print(options[queNo])
        currentA=questions[currentQ]
        ###firslty change caption of button
        submit.config(text='Next')
        ## print current question on que label
        queLabel.config(text=currentQ,fg='green',heigh=6)
        ##print option  for question on labels ..... option1,option2
        enableAllButton()
        option1.config(text=options[queNo][0],bg='sky blue',value=options[queNo][0],bd=1,command=answer)
        option2.config(text=options[queNo][1],bg='sky blue',value=options[queNo][1],bd=1,command=answer)
        option3.config(text=options[queNo][2],bg='sky blue',value=options[queNo][2],bd=1,command=answer)
        option4.config(text=options[queNo][3],bg='sky blue',value=options[queNo][3],bd=1,command=answer)
        ## remove question from list which are asked
        que.remove(currentQ)
        ans.remove(currentA)
        options.remove(options[queNo])
    elif(len(que)==0):
        result()

def answer():
    global currentQ,currentA,score

    a=var.get()
    if(currentA==str(a)):
        
        score+=1
        desableAllButton()
    else:
        desableAllButton()
title='''Entry Test For AddmItion Fall 2022
in COMSATS universty'''
appName=Label(Window,text=title,font=('impact',20,'italic'),
              justify=CENTER,bg='goldenrod2',fg='white')
appName.pack(side=TOP,fill=BOTH)                ## ap name label


#------           ### radio button will be created
queLabel=Label(Window,text='',justify=LEFT ,font=25)
queLabel.pack(side=TOP,fill=BOTH)
s= Separator(Window).place(x=0,y=195,relwidth=1)

option1=Radiobutton(Window,text='',bg='black',font=20,width=20,relief=FLAT,
                    indicator=0,value=1,variable=var,bd=0)
option1.place(x=150,y=250)
option2=Radiobutton(Window,text='',bg='black',font=20,width=20,relief=FLAT,
                    indicator=0,value=2,variable=var,bd=0)
option2.place(x=400,y=250)
option3=Radiobutton(Window,text='',bg='black',font=20,width=20,relief=FLAT,
                    indicator=0,value=3,variable=var,bd=0)
option3.place(x=150,y=300)
option4=Radiobutton(Window,text='',bg='black',font=20,width=20,relief=FLAT,
                    indicator=0,value=4,variable=var,bd=0)
option4.place(x=400,y=300)

#instruction         of Quiz----
instruction=Label(Window,text=intro,bg='black',fg='white',
                  font=('calibri',15),justify=LEFT)
instruction.place(x=150,y=200)
#note about Quiz
note=Label(Window,text='',font=('impact',10),bg='black',fg='red')
note.pack(side=BOTTOM)

### Submit button
submit=Button(Window,text='Start Quiz',fg='white',bg='blue',width=15,font=('impact',15),
              state=DISABLED,command=_next)      ## bY default disabled
submit.pack(side=BOTTOM)

##Show current time
showtime=Label(Window,text='',font=20,fg='black',bg='goldenrod2')
showtime.place(x=620,y=50)

##Copyright
copyri8=Label(Window,text="Developed by:  Hafeez Ullah",
              font=('italic',12,'bold'),fg='blue',bg='powder blue',width=25,justify=LEFT)
copyri8.place(x=700,y=580)

if(__name__=="__main__"):
    Window.withdraw()
    attendance()
    Window.mainloop()
              


    
     


    

    
