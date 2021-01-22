# chongvocab

from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
import random

##########DATA BASE #########################

conn = sqlite3.connect('vocab.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS vocab (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        vocab text,
        meaninging text,
        score int)""")

def insert_vocab(vocab,meaning):
    ID = None
    score = 0
    with conn:
        c.execute("""INSERT INTO vocab VALUES (?,?,?,?)""",
                    (ID,vocab,meaning,score))
    conn.commit()
    print('Data was inserted')

# insert_vocab('cat','แมว')

def view_vocab():
    with conn:
        c.execute("SELECT * FROM vocab")
        vocab = c.fetchall()
        print(vocab)

    return vocab

#############################################

GUI = Tk()
GUI.geometry('600x550+600+200')
GUI.title('โปรแกรมท่องจำคำศัพท์อัจฉริยะ - chongvocab')

FONT1 = ('Angsana New',25)
FONT2 = ('Angsana New',30)

############# NOTEBOOK ######################
Tab = ttk.Notebook(GUI)

T1 =Frame(Tab)
T2 =Frame(Tab)
T3 =Frame(Tab)

Tab.pack(fill=BOTH,expand=1)

Tab.add(T1,text='Add Vocab')
Tab.add(T2,text='All Vocab')
Tab.add(T3,text='Flashcard Vocab')


############## VOCAB ######################
L1 = ttk.Label(T1,text='คำศัพท์',font=FONT2) 
L1.pack()
# L1.place(x=50,y=200)
# L1.grid(row=0,column=0)
v_vocab = StringVar()
E1 = ttk.Entry(T1,textvariable=v_vocab,font=FONT2,width=30)
E1.pack()

############## meaning ######################
L2 = ttk.Label(T1,text='คำแปล',font=FONT2) 
L2.pack()
# L1.place(x=50,y=200)
# L1.grid(row=0,column=0)
v_meaning = StringVar()
E2 = ttk.Entry(T1,textvariable=v_meaning,font=FONT2,width=30)
E2.pack()

###############BUTTON###############
def saveVocab(event=None):
    global addvocab
    vocab = v_vocab.get()
    meaning = v_meaning.get()
    if len(vocab) > 0 and len(meaning) > 0 :
        insert_vocab(vocab,meaning)
        print('V: {} M: {}'.format(vocab,meaning))
        v_vocab.set('')
        v_meaning.set('')
        E1.focus()
        # clear old data
        vocabtable.delete(*vocabtable.get_children())
        
        # update TABLE

        addvocab = view_vocab()
        for v in addvocab:
            vocabtable.insert('','end',value=v)


        print('------------------')
    else :
        messagebox.showinfo('ไม่มีข้อมูล','ต้องมีช่องคำศัพท์และคำแปล หากไม่มีไม่สามารถเซฟได้')

    

B1 = ttk.Button(T1,text='Save Vocab',command=saveVocab)
B1.pack(ipadx=40,ipady=20,pady=20)

E2.bind('<Return>',saveVocab)

############# TAB 2 ###########################3
header = ['ID','Vocab','Meaning','Score']
hdsize = [50,200,250,50]

vocabtable = ttk.Treeview(T2,columns = header,show = 'headings',height=20)
vocabtable.place(x=20,y=50)

for h,s in zip(header,hdsize):
    vocabtable.heading(h,text=h)
    vocabtable.column(h,width=s)

########### Tab 3 ###############################
rv_vocab =StringVar()
rv_vocab.set('--คำศัพท์---')
rv_meaning = StringVar()
rv_meaning.set('--คำแปล---')

R1 = ttk.Label(T3,textvariable=rv_vocab,font=FONT2,foreground='green')
R1.pack(pady=20)

R2 = ttk.Label(T3,textvariable=rv_meaning,font=FONT2)
R2.pack(pady=20)

BRF = Frame(T3)
BRF.pack()

vcurrent = []

def NextButton():
    global vcurrent
    current = random.choice(addvocab)
    vcurrent = current
    rv_vocab.set(current[1])
    rv_meaning.set('--คำแปล---')

def ShowButton():
    rv_meaning.set(vcurrent[2])



BR1 = ttk.Button(BRF,text='Next',command=NextButton)
BR1.grid(row=0,column=0,ipadx=40,ipady=20,padx=10)

BR2 = ttk.Button(BRF,text='Show',command=ShowButton)
BR2.grid(row=0,column=1,ipadx=40,ipady=20,padx=10)



############### initial Program ##################
global addvocab

addvocab = view_vocab()
if len(addvocab) > 0:
    for v in addvocab:
        vocabtable.insert('','end',value=v)
    
  



GUI.mainloop()