import tkinter 
m = tkinter.Tk() 
''' 
widgets are added here 
'''
button=tkinter.Button(m,text='Stop', bg='yellow',  width=10,height=5,activebackground='pink', activeforeground='blue',font=170,command=m.destroy)
button.pack()
m.mainloop()









