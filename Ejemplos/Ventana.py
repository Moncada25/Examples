import tkinter
import time

def minimizar():
    root.iconify()#minimizar
    time.sleep(5)#tiempo transcurrido seg
    root.deiconify()#maximizar
   


root = tkinter.Tk()
boton = tkinter.Button(root, text="Minimizar", command=minimizar)
boton2 = tkinter.Button(root, text="Saludar", command="Hola mundo")
boton2.pack()
boton.pack()
root.geometry("600x300+400+400")
root.title("Hola xd")
root.mainloop()
