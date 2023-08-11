from tkinter import *
window= Tk()
window.title('Test')
window.geometry('300x160')
label = Label(window, 
              text='Test',
              bg='lightyellow',
              width=15,
              font='Helvetica 16 bold italic')
label2 = Label(window, 
              text='Test2',
              bg='lightyellow',
              width=15,
              font='Helvetica 16 bold italic')
#pack()
# label.pack(side=BOTTOM) #包裝定位字元
# label2.pack(side=BOTTOM, pady=5)


#grid()
label.grid(row=0, column=0)
label2.grid(row=1, column=2)

window.mainloop()