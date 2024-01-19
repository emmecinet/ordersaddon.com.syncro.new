import time
import threading
import tkinter as tk
import smtplib

from ClassOrdersAddonSyncro import OrdersAddonSyncro
from ClassOrders import Orders

def buttonOrders():
    text1.delete("1.0","end")
    text1.insert("end",time.strftime("%d/%m/%Y %H:%M:%S")+"\n")
    text1.insert("end","==> Download ORDINI avviato...\n")
    order = Orders.get()
    text1.insert("end",order)    
    text1.insert("end","==> Download ORDINI completato!\n")

#Form
form = tk.Tk()
form.geometry("600x400")
form.title(OrdersAddonSyncro.get_configuration().get('general','app_name'))
form.resizable(False,False)
#form.configure(background="white")

label1 = tk.Label(form,text="Importazione")
label1.place(x=0,y=10,width=100,height=35)

button_orders = tk.Button(form, text="ORDINI")
button_orders['command']=buttonOrders
button_orders.place(x=10,y=40,width=100,height=35)

label3 = tk.Label(form,text="Risultato")
label3.place(x=-10,y=90,width=100,height=35)

text1 = tk.Text(form, width=55, height = 10, bg = "white", border= 1)
text1.place(x=10,y=120,width=560,height=230)

if __name__ == "__main__":
    form.mainloop()

    
    
