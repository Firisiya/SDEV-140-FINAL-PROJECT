# Program name: Pizzanet
# Author: Firisiya Chiomadzi
# Date: 5/15/2022
# Summary: This is an abbplication that enables restaurant workers to function in their pizza selling business.

from tkinter import *
from tkinter import filedialog,messagebox
import random
import time

#Functions
#Defining of all the functions

#The function reset/clears all items to the default to be ready for new items to be added.
def reset():
    textReceipt.delete(1.0,END)
    e_garlicFingers.set('0')
    e_grandmaPie.set('0')
    e_greekStyle.set('0')
    e_grilled.set('0')
    e_pepperoni.set('0')
    e_rubirosa.set('0')
    e_sicilian.set('0')
    e_stromboli.set('0')

    e_beer.set('0')
    e_coffee.set('0')
    e_coldDrinks.set('0')
    e_tea.set('0')
    e_milk.set('0')
    e_vanilla.set('0')
    e_water.set('0')
    e_whiskey.set('0')
    # Disables any user to use the function.
    textgarlicFingers.config(state=DISABLED)
    textgrandmaPie.config(state=DISABLED)
    textgreekStyle.config(state=DISABLED)
    textgrilled.config(state=DISABLED)
    textrubirosa.config(state=DISABLED)
    textsicilian.config(state=DISABLED)
    textstromboli.config(state=DISABLED)

    textbeer.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textcoldDrinks.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textmilk.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textwater.config(state=DISABLED)
    textwhiskey.config(state=DISABLED)

    #Sets all the check buttons of pizza and drink items to 0 as a default when not in use.
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    
# Variables corresponding to the pizza and ddrink items will not show any values
#   when not in use.
    costofPizzavar.set('')
    costofDrinksvar.set('')
    subTotalvar.set('')
    serviceTaxvar.set('')
    totalCostvar.set('')
    
#Enables the user to exit the function appropriately.
def iExit():
    iExit =messagebox.askyesno("Exit Pizza Ordering System", "Confirm f you want to Exit")
    if iExit > 0:
        root.destroy()
        return
    
# The function will save your receipt and give you confirmation that your receipt has been saved if
#    there are items selected only and thr button will not funtion if no item is selected.
def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo("Information","Your bill is Saved Successfully!")

#Function will generate a receipt of all the items purchased and bill number, the date, month and year of purchase.
def receipt():
    global billnumber,date
    if costofPizzavar.get() != "" or costofDrinksVar.get() != "":
        textReceipt.delete(1.0,END)#A condition to delete the items not required and be ready for new item entries.
        x=random.randint(100,10000)
        billnumber="BILL" + str(x)
        date=time.strftime("%d/%m/%Y")
        textReceipt.insert(END,"Receipt Ref:\t\t"+billnumber+"\t\t"+date+"\n")
        textReceipt.insert(END,"*******************************************************************************\n")
        textReceipt.insert(END,"Items:\t\t Cost of Items($)\n")
        textReceipt.insert(END,"*******************************************************************************\n")
        if e_garlicFingers.get()!= 0:# A condition to select new items and delete unwanted text.
            textReceipt.insert(END,f"Garlic Fingers\t\t\t{int(e_garlicFingers.get()) * 4.25}\n")

        if e_grandmaPie.get()!= 0:
            textReceipt.insert(END,f"Grandma Pie\t\t\t{int(e_grandmaPie.get()) * 5.99}\n")

        if e_greekStyle.get()!= 0:
            textReceipt.insert(END,f"Greek Style\t\t\t{int(e_greekStyle.get()) * 6.72}\n")

        if e_grilled.get()!= 0: 
            textReceipt.insert(END,f"Grilled\t\t\t{int(e_grilled.get()) * 8.31}\n")

        if e_pepperoni.get()!= 0:
            textReceipt.insert(END,f"Pepperoni\t\t\t{int(e_pepperoni.get()) * 7.99}\n")

        if e_rubirosa.get()!= 0:
            textReceipt.insert(END,f"Rubirosa\t\t\t{int(e_rubirosa.get()) * 1.99}\n")

        if e_sicilian.get()!= 0:
            textReceipt.insert(END,f"Sicilian\t\t\t{int(e_sicilian.get()) * 13.52}\n")

        if e_stromboli.get()!= 0:
            textReceipt.insert(END,f"Stromboli\t\t\t{int(e_stromboli.get()) * 9.62}\n")

        if e_beer.get()!= 0:
            textReceipt.insert(END,f"Beer\t\t\t{int(e_beer.get()) * 1.99}\n")

        if e_coffee.get()!= 0:
            textReceipt.insert(END,f"Coffee\t\t\t{int(e_coffee.get()) * 1.20}\n")

        if e_coldDrinks.get()!= 0:
            textReceipt.insert(END,f"Cold Drinks\t\t\t{int(e_coldDrinks.get()) * 3.29}\n")

        if e_tea.get() != 0:
            textReceipt.insert(END,f"Tea\t\t\t{int(e_tea.get()) * 4.23}\n")

        if e_milk.get() != 0:
            textReceipt.insert(END, f"Milk\t\t\t{int(e_milk.get()) * 2.99}\n")

        if e_vanilla.get() != "0":
            textReceipt.insert(END,f"Vanilla\t\t\t{int(e_vanilla.get()) * 1.00}\n")

        if e_water.get()!= 0:
            textReceipt.insert(END,f"Water\t\t\t{int(e_water.get()) * 2.42}\n")

        if e_whiskey.get() != 0:
            textReceipt.insert(END,f"Whiskey\t\t\t{int(e_whiskey.get()) * 1.89}\n")
            
        textReceipt.insert(END, "*******************************************************************************\n")
        if costofPizzavar.get()!= "0":
            textReceipt.insert(END, f"Cost of Pizza\t\t\t{priceofPizza}\n\n")   
        if costofPizzavar.get()!= "0":
            textReceipt.insert(END,f"Cost of Drinks\t\t\t{priceofDrinks}\n\n")

        textReceipt.insert(END, f"Sub Total\t\t\t{subTotalofItems}\n\n")
        textReceipt.insert(END, f"Service Tax\t\t\t{1.82}\n\n")
        textReceipt.insert(END, f"Total Cost\t\t\t{subTotalofItems+1.82}\n\n")
        textReceipt.insert(END,"*******************************************************************************\n")
    else:
        messagebox.showerror("ERROR","No Item is Selected")

#The Function will produce total cost comprising of pizza and drink items, subtotals, and serviceTax.
def totalcost():
    global priceofPizza,priceofDrinks,subTotalofItems
    if var1.get()!=0 or var2.get() !=0 or var3.get() !=0 or var4.get()!=0 or var5.get() !=0 or var6.get() !=0 or \
        var7.get()!=0 or var8.get() !=0 or var9.get() !=0 or var10.get()!=0 or var11.get() !=0 or var12.get() !=0 or \
        var13.get()!=0 or var14.get() !=0 or var15.get() !=0 or var16.get()!=0:

        item1 = float(e_garlicFingers.get())
        item2 = float(e_grandmaPie.get())
        item3 = float(e_greekStyle.get())
        item4 = float(e_grilled.get())
        item5 = float(e_pepperoni.get())
        item6 = float(e_rubirosa.get())
        item7 = float(e_sicilian.get())
        item8 = float(e_stromboli.get())
        
        item9 = float(e_beer.get())
        item10 = float(e_coffee.get())
        item11 = float(e_coldDrinks.get())
        item12 = float(e_tea.get())
        item13 = float(e_milk.get())
        item14 = float(e_vanilla.get())
        item15 = float(e_water.get())
        item16 = float(e_whiskey.get())

        # Prices of pizza and drinks to be chosen by the customer
        # If no item is selected there must send an error message to say, "No item is selected".
        priceofPizza=(item1 * 4.25) + (item12 * 5.99) + (item3 * 6.72) + (item4 * 8.31) + (item5 * 7.99) \
                  + (item6 * 11.99) + (item7 * 13.52) + (item8 * 9.62)

        priceofDrinks=(item9 * 1.99) + (item10 * 1.20) + (item11 * 3.29) + (item12 * 4.23) + (item13 * 2.99) \
                   + (item14 * 1.02) + (item15 * 2.42) + (item16 * 1.89)


        costofPizzavar.set (priceofPizza)
        costofDrinksvar.set (priceofDrinks)

        subTotalofItems=priceofPizza + priceofDrinks
        subTotalvar.set(subTotalofItems)

        serviceTaxvar.set("1.82")

        totalCost=subTotalofItems + (1.82)
        totalCostvar.set (totalCost)

    else:
        messagebox.showerror("ERROR", "No Item is Selected")
        
        #Calling and defining constant and fixed conditions of pizza and drink items to be deleted when not in use,
        #and to appear when called.
def garlicFingers():
    if var1.get()==1:
        textgarlicFingers.config(state=NORMAL)
        textgarlicFingers.delete(0,END)
        textgarlicFingers.focus()
    else:
        textgarlicFingers.config(state=DISABLED)
        e_garlicFingers.set(0)

def grandmaPie():
    if var2.get()== 1:
        textgrandmaPie.config(state=NORMAL)
        textgrandmaPie.delete(0,END)
        textgrandmaPie.focus()
    else:
        textgrandmaPie.config(state=DISABLED)
        e_grandmaPie.set(0)

def greekStyle():
    if var3.get()== 1:
        textgreekStyle.config(state=NORMAL)
        textgreekStyle.delete(0,END)
        textgreekStyle.focus()
    else:
        textgreekStyle.config(state=DISABLED)
        e_greekStyle.set(0)

def grilled():
    if var4.get()== 1:
        textgrilled.config(state=NORMAL)
        textgrilled.delete(0,END)
        textgrilled.focus()
    elif var4.get() == 0:
        textgrilled.config(state=DISABLED)
        e_grilled.set(0)

def pepperoni():
    if var5.get()== 1:
        textpepperoni.config(state=NORMAL)
        textpepperoni.delete(0,END)
        textpepperoni.focus()
    elif var5.get() == 0:
        textpepperoni.config(state=DISABLED)
        e_pepperoni.set(0)

def rubirosa():
    if var6.get()== 1:
        textrubirosa.config(state=NORMAL)
        textrubirosa.delete(0,END)
        textrubirosa.focus()
    elif var6.get() == 0:
        textrubirosa.config(state=DISABLED)
        e_rubirosa.set()

def sicilian():
    if var7.get()== 1:
        textsicilian.config(state=NORMAL)
        textsicilian.delete(0,END)
        textsicilian.focus()
    elif var7.get() == 0:
        textsicilian.config(state=DISABLED)
        e_sicilian.set(0)

def stromboli():
    if var8.get()== 1:
        textstromboli.config(state=NORMAL)
        textstromboli.delete(0,END)
        textstromboli.focus()
    elif var8.get() == 0:
        textstromboli.config(state=DISABLED)
        e_stromboli.set(0)

def beer():
    if var9.get()== 1:
        textbeer.config(state=NORMAL)
        textbeer.delete(0,END)
        textbeer.focus()
    elif var9.get() == 0:
        textbeer.config(state=DISABLED)
        e_beer.set(0)

def coffee():
    if var10.get()== 1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    elif var10.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set(0)

def coldDrinks():
    if var11.get()== 1:
        textcoldDrinks.config(state=NORMAL)
        textcoldDrinks.delete(0,END)
        textcoldDrinks.focus()
    elif var11.get() == 0:
        textcoldDrinks.config(state=DISABLED)
        e_coldDrinks.set(0)

def tea():
    if var12.get()== 1:
        texttea.config(state=NORMAL)
        texttea.delete(0,END)
        texttea.focus()
    elif var12.get() == 0:
        texttea.config(state=DISABLED)
        e_tea.set(0)

def milk():
    if var13.get()== 1:
        textmilk.config(state=NORMAL)
        textmilk.delete(0,END)
        textmilk.focus()
    elif var13.get() == 0:
        textmilk.config(state=DISABLED)
        e_milk.set(0)

def vanilla():
    if var14.get()== 1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    elif var14.get() == 0:
        textvanilla.config(state=DISABLED)
        e_vanilla.set(0)

def water():
    if var15.get()== 1:
        textwater.config(state=NORMAL)
        textwater.delete(0,END)
        textwater.focus()
    elif var15.get() == 0:
        textwater.config(state=DISABLED)
        e_water.set(0)

def whiskey():
    if var16.get()== 1:
        textwhiskey.config(state=NORMAL)
        textwhiskey.delete(0,END)
        textwhiskey.focus()
    elif var16.get() == 0:
        textwhiskey.config(state=DISABLED)
        e_whiskey.set(0)

root=Tk()

#Fixed Size window
root.geometry("1270x690+0+0")

root.resizable(0,0)

root.title("Pizzanet Ordering System created by Felicia")


root.config(bg="green4")

topFrame=Frame(root,bd=10,relief=RIDGE,bg="green4")
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text="Pizzanet Ordering System",font=("arial",30,"bold"),fg="yellow",bd=9,bg="green4",width=51)
labelTitle.grid(row=0,column=0)

#Frames available on the pizza ordering app: 

menuFrame=Frame(root,bd=8,relief=RIDGE,bg="green4")
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg="green4",pady=20)
costFrame.pack(side=BOTTOM)

pizzaFrame=LabelFrame(menuFrame,text="Pizza",font=("arial",19,"bold"),bd=10,relief=RIDGE,fg="green4")
pizzaFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text="Drinks",font=("arial",19,"bold"),bd=10,relief=RIDGE,fg="green4")
drinksFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='green4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='green4')
calculatorFrame.pack()

receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='green4')
receiptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='green4')
buttonFrame.pack()

#Variables: 
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

#Defining of Entry fields for pizza items
e_garlicFingers = StringVar()
e_grandmaPie = StringVar()
e_greekStyle = StringVar()
e_grilled = StringVar()
e_pepperoni = StringVar()
e_rubirosa = StringVar()
e_sicilian = StringVar()
e_stromboli = StringVar()

#Defining of Entry fields for drink items
e_beer = StringVar()
e_coffee = StringVar()
e_coldDrinks = StringVar()
e_tea = StringVar()
e_milk = StringVar()
e_vanilla = StringVar()
e_water = StringVar()
e_whiskey = StringVar()

#Setting of entry fields for pizzas to '0' as the starting point if there is no activitiy.
e_garlicFingers.set(0)
e_grandmaPie.set(0)
e_greekStyle.set(0)
e_grilled.set(0)
e_pepperoni.set(0)
e_rubirosa.set(0)
e_sicilian.set(0)
e_stromboli.set(0)

#Setting of entry fields for drinks to '0' as the starting point if there is no activitiy.
e_beer.set(0)
e_coffee.set(0)
e_coldDrinks.set(0)
e_tea.set(0)
e_milk.set(0)
e_vanilla.set(0)
e_water.set(0)
e_whiskey.set(0)

#Defining of variable as stated below
costofPizzavar = StringVar()
costofDrinksvar = StringVar()
subTotalvar= StringVar()
serviceTaxvar= StringVar()
totalCostvar= StringVar()

#Pizza: The types of pizza to be provided by the restaurant and the checkbuttons on the left to
#       indicate which items have been ordered and are to be send for production.

garlicFingers=Checkbutton(pizzaFrame,text="Garlic Fingers",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var1,
                          command=garlicFingers)
garlicFingers.grid(row=0,column=0,sticky=W)

grandmaPie=Checkbutton(pizzaFrame,text="Grandma Pie",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var2,
                       command=grandmaPie)
grandmaPie.grid(row=1,column=0,sticky=W)

greekStyle=Checkbutton(pizzaFrame,text="Greek Style",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var3,
                       command=greekStyle)
greekStyle.grid(row=2,column=0,sticky=W)

grilled=Checkbutton(pizzaFrame,text="Grilled",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var4,
                    command=grilled)
grilled.grid(row=3,column=0,sticky=W)

pepperoni=Checkbutton(pizzaFrame,text="Pepperoni",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var5,
                      command=pepperoni)
pepperoni.grid(row=4,column=0,sticky=W)

rubirosa=Checkbutton(pizzaFrame,text="Rubirosa",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var6,
                     command=rubirosa)
rubirosa.grid(row=5,column=0,sticky=W)

sicilian=Checkbutton(pizzaFrame,text="Sicilian",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var7,
                     command=sicilian)
sicilian.grid(row=6,column=0,sticky=W)

stromboli=Checkbutton(pizzaFrame,text="Stromboli",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var8,
                      command=stromboli)
stromboli.grid(row=7,column=0,sticky=W)

#Entry Fields for Pizza items on the right of the pizzas to indicate how many have been ordered.

textgarlicFingers=Entry(pizzaFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_garlicFingers)
textgarlicFingers.grid(row=0,column=1)

textgrandmaPie=Entry(pizzaFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_grandmaPie)
textgrandmaPie.grid(row=1,column=1)

textgreekStyle=Entry(pizzaFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_greekStyle)
textgreekStyle.grid(row=2,column=1)

textgrilled=Entry(pizzaFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_grilled)
textgrilled.grid(row=3,column=1)

textpepperoni=Entry(pizzaFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_pepperoni)
textpepperoni.grid(row=4,column=1)

textrubirosa=Entry(pizzaFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_rubirosa)
textrubirosa.grid(row=5,column=1)

textsicilian=Entry(pizzaFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_sicilian)
textsicilian.grid(row=6,column=1)

textstromboli=Entry(pizzaFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_stromboli)
textstromboli.grid(row=7,column=1)

#Drinks: These are the drinks checkbuttons on the left for the drinks that will be sold by
#        the restaurant to go aloing with the pizzas.

beer=Checkbutton(drinksFrame,text="Beer",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var9,
                 command=beer)
beer.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text="Coffee",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var10,
                   command=coffee)
coffee.grid(row=1,column=0,sticky=W)

coldDrinks=Checkbutton(drinksFrame,text="Cold Drinks",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var11,
                       command=coldDrinks)
coldDrinks.grid(row=2,column=0,sticky=W)

tea=Checkbutton(drinksFrame,text="Tea",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var12,
                command=tea)
tea.grid(row=3,column=0,sticky=W)

milk=Checkbutton(drinksFrame,text="Milk",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var13,
                 command=milk)
milk.grid(row=4,column=0,sticky=W)

vanilla=Checkbutton(drinksFrame,text="Vanilla",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var14,
                    command=vanilla)
vanilla.grid(row=5,column=0,sticky=W)

water=Checkbutton(drinksFrame,text="Water",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var15,
                  command=water)
water.grid(row=6,column=0,sticky=W)

whiskey=Checkbutton(drinksFrame,text="Whiskey",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var16,
                    command=whiskey)
whiskey.grid(row=7,column=0,sticky=W)

#Entry Fields for drink items to indicate how many have been ordered.

textbeer=Entry(drinksFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_beer)
textbeer.grid(row=0,column=1)

textcoffee=Entry(drinksFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

textcoldDrinks=Entry(drinksFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_coldDrinks)
textcoldDrinks.grid(row=2,column=1)

texttea=Entry(drinksFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_tea)
texttea.grid(row=3,column=1)

textmilk=Entry(drinksFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_milk)
textmilk.grid(row=4,column=1)

textvanilla=Entry(drinksFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=5,column=1)

textwater=Entry(drinksFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_water)
textwater.grid(row=6,column=1)

textwhiskey=Entry(drinksFrame,font=("arial",18,"bold"),bd=7,width=10,state=DISABLED,textvariable=e_whiskey)
textwhiskey.grid(row=7,column=1)

#costlabels and entry fields for the Cost of pizza and drinks, subTotal, ServiceTax and TotalCost and
#       when clicked will produce the desired results and are set to read-only so that no one will be able
#        to make any changes

labelCostofPizza=Label(costFrame,text="Cost of Pizza",font=("arial",16,"bold"),bg="green4",fg="white")
labelCostofPizza.grid(row=0,column=0)

textCostofPizza=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=12,state="readonly",textvariable=costofPizzavar)
textCostofPizza.grid(row=0,column=1,padx=25)

labelcostofDrinks=Label(costFrame,text="Cost of Drinks",font=("arial",16,"bold"),bg="green4",fg="white")
labelcostofDrinks.grid(row=1,column=0)

textcostofDrinks=Entry(costFrame,font=("arial",16,"bold"),bd=6,width=12,state="readonly",textvariable=costofDrinksvar)
textcostofDrinks.grid(row=1,column=1,padx=25)

labelsubTotal=Label(costFrame,text="Sub Total",font=("arial",16,"bold"),bg="green4",fg="white")
labelsubTotal.grid(row=0,column=2)

textsubTotal=Entry(costFrame,font=("arial",18,"bold"),bd=6,width=12,state="readonly",textvariable=subTotalvar)
textsubTotal.grid(row=0,column=3,padx=25)

labelserviceTax=Label(costFrame,text="Service Tax",font=("arial",16,"bold"),bg="green4",fg="white")
labelserviceTax.grid(row=1,column=2)

textserviceTax=Entry(costFrame,font=("arial",18,"bold"),bd=6,width=12,state="readonly",textvariable=serviceTaxvar)
textserviceTax.grid(row=1,column=3,padx=25)

labeltotalCost=Label(costFrame,text="Total Cost",font=("arial",16,"bold"),bg="green4",fg="white")
labeltotalCost.grid(row=2,column=2)

texttotalCost=Entry(costFrame,font=("arial",18,"bold"),bd=6,width=12,state="readonly",textvariable=totalCostvar)
texttotalCost.grid(row=2,column=3,padx=25)

# Buttons for the Total, Receipt, Save, Send and Reset buttons below the calculator and when clicked will
#       produce the desired results.

buttonTotal=Button(buttonFrame,text="Total",font=("arial",14,"bold"),fg="white",bg="green4",bd=3,padx=13,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text="Receipt",font=("arial",14,"bold"),fg="white",bg="green4",bd=3,padx=13,
                     command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave=Button(buttonFrame, text="Save",font=("arial",14,"bold"),fg="white",bg="green4",bd=3,padx=13,
                  command=save)
buttonSave.grid(row=0,column=2)

buttonReset=Button(buttonFrame,text="Reset",font=("arial",14,"bold"),fg="white",bg="green4",bd=3,padx=13,
                   command=reset)
buttonReset.grid(row=0,column=3)

buttonExit=Button(buttonFrame,text="Exit",font=("arial",14,"bold"),fg="white",bg="green4",bd=3,padx=13,
                  command=iExit)
buttonExit.grid(row=0,column=4)

#Textarea for receipt: This is the frame on the right and below the calculator that will
#       show the receipt of the ordered items.
                    
textReceipt=Text(receiptFrame,font=("arial",12,"bold"),bd=3,width=53,height=14)
textReceipt.grid(row=0,column=0)

#Calculator: Entry fields, defining and calling of all the buttons on the calculator and its properties to functionality.
#When clicked and called will produce the desired results
operator="" 
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

# Function will clear everything when called ready for the new items to be added
def clear():
    global operator
    operator=""
    calculatorField.delete(0,END)

# Function will produce the desired results when called, addittion, substraction, multiplication and division of numbers.
def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=""
    
calculatorField=Entry(calculatorFrame,font=("arial",16,"bold"),width=40,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button1=Button(calculatorFrame,text="1",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
               command=lambda:buttonClick("1"))
button1.grid(row=1,column=0)
                    
button2=Button(calculatorFrame,text="2",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
               command=lambda:buttonClick("2"))
button2.grid(row=1,column=1)

button3=Button(calculatorFrame,text="3",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
               command=lambda:buttonClick("3"))
button3.grid(row=1,column=2)

buttonAdd=Button(calculatorFrame,text="+",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
                 command=lambda:buttonClick("+"))
buttonAdd.grid(row=1,column=3)

button4=Button(calculatorFrame,text="4",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
               command=lambda:buttonClick("4"))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text="5",font=("arial",16,"bold"),fg="green4",bg="white",bd=6,width=8,
               command=lambda:buttonClick("5"))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text="6",font=("arial",16,"bold"),fg="green4",bg="white",bd=6,width=8,
               command=lambda: buttonClick("6"))
button6.grid(row=2,column=2)

buttonSubtract=Button(calculatorFrame,text="-",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
                      command=lambda:buttonClick("-"))
buttonSubtract.grid(row=2, column=3)

button7=Button(calculatorFrame,text="7",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
               command=lambda:buttonClick("7"))
button7.grid(row=3,column=0)

button8=Button(calculatorFrame,text="8",font=("arial",16,"bold"),fg="green4",bg="white",bd=6,width=8,
               command=lambda: buttonClick("8"))
button8.grid(row=3,column=1)

button9=Button(calculatorFrame, text="9",font=("arial",16,"bold"),fg="green4",bg="white",bd=6,width=8,
               command=lambda:buttonClick("9"))
button9.grid(row=3,column=2)

buttonMultiply=Button(calculatorFrame,text="*",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
                      command=lambda:buttonClick("*"))
buttonMultiply.grid(row=3,column=3)

buttonAnswer=Button(calculatorFrame,text="Ans",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
                    command=answer)
buttonAnswer.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text="Clear",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
                   command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text="0",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
               command=lambda: buttonClick("0"))
button0.grid(row=4,column=2)

buttonDivide=Button(calculatorFrame, text="/",font=("arial",16,"bold"),fg="yellow",bg="green4",bd=6,width=8,
                    command=lambda: buttonClick("/"))
buttonDivide.grid(row=4,column=3)

root.mainloop()
