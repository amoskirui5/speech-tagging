
import os
import sys
from tkinter import *
class Application:

    def __init__(self, master):


        frame = Frame(master, width=500, height=400, bd =2 )
        frame.pack()

        self.frame1 = Frame(frame, relief = 'flat', bd =2 )
        self.frame1 .pack(fill= X)
      
        #frame1
        self.heading_lbl = Label(self.frame1, text = "Input Kipsigis text",font='times')
        self.heading_lbl.grid (row = 1, column=0, sticky=W)

        #createframe 2
        self.frame2 = Frame(frame, relief = 'flat', bd =2 )
        self.frame2.pack(fill =X)

        self.userquestion_txt = Text(self.frame2, width=60, height=5, wrap= WORD, font='times',insertborderwidth=3)
        self.userquestion_txt.grid(row = 3, column = 1 , columnspan = 3, sticky = W )

              #create frame 3
        self.frame3 = Frame(frame, relief = 'flat', bd =2 )
        self.frame3.pack(fill = X)


        Button(self.frame3, text='POS-Tag', command = self.reveal,font='times').pack(side=LEFT,padx=5)
        Button(self.frame3, text='Clear', command = self.clear_all_text,font='times').pack(side=RIGHT,padx=5)
            
          #create frame 4
        self.frame4 = Frame(frame, relief = 'flat', bd=2 )
        self.frame4.pack(fill=X)

        self.frame4_lbl1 = Label(self.frame4, text= "Output",font='times' )
        self.frame4_lbl1.grid(row=0, column=0, sticky=W)
   
        self.partofspeech_txt=Text(self.frame4,width=45,height=18,wrap=WORD,fg='dark green',font='Times'  )
        self.partofspeech_txt.grid(row=1,columnspan=2,sticky=W)
      


    def clear_all_text(self):
            #clearAllText
        self.userquestion_txt.delete(0.0, END)
        self.partofspeech_txt.delete(0.0, END)


    def reveal(self):
        fileobj = open('kipsigis.data','w')
        try:

            texttoparse = self.userquestion_txt.get(0.0, END)
            fileobj.write(texttoparse)
        except:
            self.partofspeech_txt.insert(END, 'failed to save file !')
        fileobj.close()
        contents = "mbt -s kipsigis.data.settings -t "+'kipsigis.data'
         #contents = "Mbt -s nergen.settings -t "+'syst001 .txt'
        if contents !=" ":

            message= " There is text to parse "+ contents
            try:
                message = os.popen(contents).read()


            except:
                message = "Failed to execute kipsigis.data.settings"
        else:
            message="There is no text to parse"
        self.partofspeech_txt.delete(0.0, END)
        self.partofspeech_txt.insert(0.0, message)

root = Tk()
root.geometry("500x600")
root.title ("KIPSIGIS PART OF SPEECH" )
root.option_add('*font', ('Helvetica', 9, 'bold'))

app = Application(root)
root.mainloop()