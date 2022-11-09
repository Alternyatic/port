from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
root = Tk()
root.title("Money Converter")
root.resizable(0,0)
c = CurrencyRates()
b = BtcConverter()

money = IntVar()
Label(text="Total Amount",padx=10,font=30).grid(row=0,sticky=W)
et1 = Entry(width=30,font=30,textvariable=money)
et1.grid(row=0,column=1)
choice = StringVar(value="Please choose currency")
Label(text="Choosing currency",padx=10,font=30).grid(row=1,sticky=W)
combo = ttk.Combobox(width=28,font=30,textvariable=choice)
combo["values"]=("€ (EUR)","$ (USD)","£ (GBP)","Ft (HUF)","₹ (INR)","₫ (VND)","RM (MYR)","₣ (CHF)","¥ (CNY)","₩ (KRW)","¥ (JPY)","₿ (BTC)")
combo.grid(row=1,column=1)

Label(text="Converted Total Amount",padx=10,font=30).grid(row=2,sticky=W)
et2 = Entry(width=30,font=30)
et2.grid(row=2,column=1)

def calculate():
    amount=money.get()
    currency=choice.get()
    match currency:
        case "€ (EUR)":
            et2.delete(0,END)
            result = (c.convert('THB', 'EUR', amount),"€ (EUR)")
            et2.insert(0,result)
        case "$ (USD)": 
            et2.delete(0,END)
            result = (c.convert('THB', 'USD', amount),"$ (USD)")
            et2.insert(0,result)  
        case "£ (GBP)":
            et2.delete(0,END)
            result = (c.convert('THB', 'GBP', amount),"£ (GBP)")
            et2.insert(0,result)
        case "Ft (HUF)":
            et2.delete(0,END)
            result = (c.convert('THB', 'HUF', amount),"Ft (HUF)")
            et2.insert(0,result) 
        case "₹ (INR)":
            et2.delete(0,END)
            result = (c.convert('THB', 'INR', amount),"₹ (INR)")
            et2.insert(0,result)    
        case "₫ (VND)":
            et2.delete(0,END)
            result = (c.convert('THB', 'VND', amount),"₫ (VND)")
            et2.insert(0,result)   
        case "RM (MYR)":
            et2.delete(0,END)
            result = (c.convert('THB', 'MYR', amount),"RM (MYR)")
            et2.insert(0,result)       
        case "₣ (CHF)":
            et2.delete(0,END)
            result = (c.convert('THB', 'CHF', amount),"₣ (CHF)")
            et2.insert(0,result)       
        case "¥ (CNY)":
            et2.delete(0,END)
            result = (c.convert('THB', 'CNY', amount),"¥ (CNY)")
            et2.insert(0,result)       
        case "₩ (KRW)":
            et2.delete(0,END)
            result = (c.convert('THB', 'KRW', amount),"₩ (KRW)")
            et2.insert(0,result)       
        case "¥ (JPY)":
            et2.delete(0,END)
            result = (c.convert('THB', 'JPY', amount),"¥ (JPY)")
            et2.insert(0,result)       
        case "₿ (BTC)":
            et2.delete(0,END)
            result = (b.convert_to_btc(amount,'THB'),"₿ (BTC)")
            et2.insert(0,result)                                    
        case _:
            et2.delete(0,END)
            result = "Please enter the amount of money"
            et2.insert(0,result)

def recalculate():
    amount=money.get()
    currency=choice.get()
    match currency:
        case "€ (EUR)":
            et2.delete(0,END)
            result = (c.convert('EUR', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)
        case "$ (USD)": 
            et2.delete(0,END)
            result = (c.convert('USD', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)
        case "£ (GBP)": 
            et2.delete(0,END)
            result = (c.convert('GBP', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)
        case "Ft (HUF)": 
            et2.delete(0,END)
            result = (c.convert('HUF', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)
        case "₹ (INR)": 
            et2.delete(0,END)
            result = (c.convert('INR', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)
        case "₫ (VND)": 
            et2.delete(0,END)
            result = (c.convert('VND', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)
        case "RM (MYR)": 
            et2.delete(0,END)
            result = (c.convert('MYR', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)
        case "₣ (CHF)": 
            et2.delete(0,END)
            result = (c.convert('CHF', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)
        case "¥ (CNY)": 
            et2.delete(0,END)
            result = (c.convert('CNY', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)    
        case "₩ (KRW)": 
            et2.delete(0,END)
            result = (c.convert('KRW', 'THB', amount),"฿ (THB)")
            et2.insert(0,result) 
        case "¥ (JPY)": 
            et2.delete(0,END)
            result = (c.convert('JPY', 'THB', amount),"฿ (THB)")
            et2.insert(0,result)
        case "₿ (BTC)": 
            et2.delete(0,END)
            result = (b.convert_btc_to_cur(amount,'THB'),"฿ (THB)")
            et2.insert(0,result)    
        case _ :
            et2.delete(0,END)
            result = "Please enter the amount of money"
            et2.insert(0,result)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)

Button(text="฿ (THB) to Currency",font=30,width=17,command=calculate,bg="#5b5b5b").grid(row=3,column=0,sticky=W)
Button(text="Currency to  ฿ (THB)",font=30,width=17,command=recalculate,bg="#5b5b5b").grid(row=3,column=1,sticky=W)
Button(text="Delete",font=30,width=8,command=deleteText,bg="#5b5b5b").grid(row=3,column=1,sticky=E)
root.mainloop()