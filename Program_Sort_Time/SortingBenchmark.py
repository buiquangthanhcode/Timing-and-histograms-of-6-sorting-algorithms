import BubbleSort
import InsertionSort
import CountingSort
import QuickSort
import HeapSort
import RadixSort
import random
from PIL import Image
from tkinter import *
import tkinter as tk
import matplotlib
class App(tk.Tk):
    def chart(self,b,i,c,q,h,r):
        # prepare data
        data = {
            'BubbleSort': b,
            'InsertionSort': i,
            'CoutingSort': c,
            'QuickSort': q,
            'HeapSort': h,
            'RadixSort': r,
            
        }
        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(7, 6), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure,self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas,self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('6 Sort Algorithms')
        axes.set_ylabel('Time')
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

root = Tk()
root.title("Benchmark")
root.geometry("900x600")
listInt = []
for i in range(7):
    listInt.append(0)

            
def window2():
   
    root.destroy()
    window2_main = Tk()
    def end():
        window2_main.destroy()  
        end_main = Tk()
        end_main.title("End")
        end_main.geometry('720x568') 
        bg_end = PhotoImage(file = "4.png")
        labelend = Label( end_main, image = bg_end)
        labelend.place(x = 0, y = 0)
        end_main.mainloop()
      
       
        
        
    window2_main.title("Benchmark")
    window2_main.geometry('900x600')
    def link(a,b,c,d,e,f):
        app = App()
        app.chart(a,b,c,d,e,f);
        app.mainloop()
    def command():
        raw_values=entry.get()
        str1,x1=BubbleSort.main(raw_values)
        Output.insert(END,str1)
        listInt[0]=x1
        Output.insert(END,'\n')
        str2,x2=InsertionSort.main(raw_values)
        Output.insert(END,str2)
        listInt[1]=x2
        Output.insert(END,'\n')
        str3,x3=CountingSort.main(raw_values)
        Output.insert(END,str3)
        listInt[2]=x3
        Output.insert(END,'\n')
        str4,x4=QuickSort.main(raw_values)
        Output.insert(END,str4)
        listInt[3]=x4
        Output.insert(END,'\n')
        str5,x5=HeapSort.main(raw_values)
        Output.insert(END,str5)
        listInt[4]=x5
        Output.insert(END,'\n')
        str6,x6=RadixSort.main(raw_values)
        Output.insert(END,str6)
        listInt[5]=x6
        
    
 
    def listRandom(flag):
        if(flag==1000):
            entry.insert(0,random.sample(range(0, 1001), 1000))
        elif(flag==5000):
            entry.insert(0,random.sample(range(0, 5001), 5000))
        elif(flag==10000):
            entry.insert(0,random.sample(range(0, 10001), 10000))  
        raw_values = entry.get()
        str1,x1=BubbleSort.main(raw_values)
        Output.insert(END,str1)
        listInt[0]=x1
        Output.insert(END,'\n')
        str2,x2=InsertionSort.main(raw_values)
        Output.insert(END,str2)
        listInt[1]=x2
        Output.insert(END,'\n')
        str3,x3=CountingSort.main(raw_values)
        Output.insert(END,str3)
        listInt[2]=x3
        Output.insert(END,'\n')
        str4,x4=QuickSort.main(raw_values)
        Output.insert(END,str4)
        listInt[3]=x4
        Output.insert(END,'\n')
        str5,x5=HeapSort.main(raw_values)
        Output.insert(END,str5)
        listInt[4]=x5
        Output.insert(END,'\n')
        str6,x6=RadixSort.main(raw_values)
        Output.insert(END,str6)
        listInt[5]=x6
    def clear():
        entry.delete(0, 'end')
        Output.delete("1.0","end")
        listInt[0]=0
        listInt[1]=0
        listInt[2]=0
        listInt[3]=0
        listInt[4]=0
        listInt[5]=0
    
    l = Label(text = "PLEASE INPUT LIST (ARRAY) OF INTEGER NUMBER ")   
    l.config(font =("Courier", 14))
    entry = Entry(window2_main)
    button = Button(window2_main, bg='blue',text="Start",command=command)
    buttonEnd = Button(window2_main,bg='red', text="End",command=end)
    buttonClear = Button(window2_main, text="Clear",command=clear)
    button1_1000 = Button(window2_main, text="Random 1-1000",command=lambda:listRandom(1000))
    button1_10000 = Button(window2_main, text="Random 1-5000",command=lambda:listRandom(5000))
    button1_100000 = Button(window2_main, text="Random 1-10000",command=lambda:listRandom(10000))
    buttonLink = Button(window2_main, bg='green', text="Chart",command= lambda:link(listInt[0],listInt[1],listInt[2],listInt[3],listInt[4],listInt[5]))
    l.place(x=235,y=10)
    entry.place(width=890,height=70)
    entry.place(x=5,y=35)
    button.place(width=100, height=45)
    button.place(x=365, y=110)
    buttonLink.place(width=100, height=45)
    buttonLink.place(x=490, y=110)
    buttonClear.place(x=20,y=110)
    buttonEnd.place(x=800,y=8)
    button1_1000.place(x=10, y=310)
    button1_10000.place(x=10, y=410)
    button1_100000.place(x=10, y=510)
    # Execute Tkinte
   
    Output = Text(window2_main, height = 25,
                width = 80,
                bg = "light cyan")
    Output.place(x=122, y=165)
    window2_main.mainloop()

bg = PhotoImage(file = "2.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
a = Button( bg='blue',text="Click This", command=window2)
a.place(x=420,y=470)

root.mainloop()

