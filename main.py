from tkinter import *
from tkinter import LabelFrame
from tkinter import messagebox
import random, os, tempfile, smtplib

if not os.path.exists('bills'):
    os.mkdir('bills')


def clear():
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    bodylotionEntry.delete(0, END)
    facewashEntry.delete(0, END)

    dalEntry.delete(0, END)
    wheatEntry.delete(0, END)
    oilEntry.delete(0, END)
    sugarEntry.delete(0, END)
    teaEntry.delete(0, END)
    riceEntry.delete(0, END)

    pepsiEntry.delete(0, END)
    cococolaEntry.delete(0, END)
    maazaEntry.delete(0, END)
    dewEntry.delete(0, END)
    spriteEntry.delete(0, END)
    frootiEntry.delete(0, END)

    bathsoapEntry.insert(0, 0)
    facecreamEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)
    facewashEntry.insert(0, 0)

    riceEntry.insert(0, 0)
    dalEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    teaEntry.insert(0, 0)

    pepsiEntry.insert(0, 0)
    cococolaEntry.insert(0, 0)
    maazaEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    frootiEntry.insert(0, 0)

    cosmetictaxEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    drinkstaxEntry.delete(0, END)

    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkspriceEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.get(0, END)

    textarea.delete(1.0, END)


def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            reciever_address = recieverEntry.get()
            ob.sendmail(senderEntry.get(), reciever_address, message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent', parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error', 'Something went wrong,Please try again', parent=root1)

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('Send email')
        root1.config(bg='gray20')
        root1.resizable(0, 0)

        senderFrame = LabelFrame(root1, text='Sender', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel = Label(senderFrame, text="Sender's Email", font=('arial', 14, 'bold'), bd=6, bg='gray20',
                            fg='white')
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        receiptFrame = LabelFrame(root1, text='Recipient', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        receiptFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(receiptFrame, text="Email Address", font=('arial', 14, 'bold'), bd=6, bg='gray20',
                              fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(receiptFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(receiptFrame, text="Message", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white', )
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(receiptFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN, width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', '').replace('\t\t\t', '\t\t'))

        sendbutton = Button(root1, text='SEND', font=('arial', 16, 'bold'), width=15, command=send_gmail)
        sendbutton.grid(row=2, column=0, pady=20)

    root1.mainloop()


def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Sucesss', f'Bill Number:{billnumber} saved successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)


# functionality
def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details are required')
    elif cosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and drinkspriceEntry.get() == '':
        messagebox.showerror('Error', 'No products are selected')
    elif cosmeticpriceEntry.get() == '0 RS' and grocerypriceEntry.get() == '0 RS' and drinkspriceEntry.get() == '0 RS':
        messagebox.showerror('Error', 'No products selected')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t  **Welcome Customer**\n')
        textarea.insert(END, f'\nBill Number: {billnumber}')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END, f'\nPhone number: {phoneEntry.get()}')
        textarea.insert(END, '\n------------------------------------------------------------')
        textarea.insert(END, 'Products\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n------------------------------------------------------------')
        if bathsoapEntry.get() != '0':
            textarea.insert(END, f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} rs')
        if hairsprayEntry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} rs')
        if facecreamEntry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} rs')
        if facewashEntry.get() != '0':
            textarea.insert(END, f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} rs')
        if hairgelEntry.get() != '0':
            textarea.insert(END, f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} rs')
        if bodylotionEntry.get() != '0':
            textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} rs')

        # grocery
        if riceEntry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} rs')
        if oilEntry.get() != '0':
            textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} rs')
        if dalEntry.get() != '0':
            textarea.insert(END, f'\nDal\t\t\t{dalEntry.get()}\t\t\t{dalprice} rs')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} rs')
        if sugarEntry.get() != '0':
            textarea.insert(END, f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} rs')
        if teaEntry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} rs')

        # drinks
        if maazaEntry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} rs')
        if pepsiEntry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} rs')
        if spriteEntry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} rs')
        if dewEntry.get() != '0':
            textarea.insert(END, f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} rs')
        if frootiEntry.get() != '0':
            textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} rs')
        if cococolaEntry.get() != '0':
            textarea.insert(END, f'\nCoco Cola\t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} rs')

        textarea.insert(END, '\n------------------------------------------------------------')
        if cosmetictaxEntry.get() != '0.0 RS':
            textarea.insert(END, f'\n Cosmetic Tax\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get() != '0.0 RS':
            textarea.insert(END, f'\n Grocery Tax\t\t\t{grocerytaxEntry.get()}')
        if drinkstaxEntry.get() != '0.0 RS':
            textarea.insert(END, f'\n Cold Drinks Tax\t\t\t{drinkstaxEntry.get()}')

        textarea.insert(END, '\n------------------------------------------------------------')
        textarea.insert(END, f'Total Bill\t\t\t\t{totalbill} Rs')
        save_bill()


def total():
    # cosmetics
    global soapprice, hairsprayprice, facecreamprice, facewashprice, hairgelprice, bodylotionprice
    global riceprice, dalprice, oilprice, sugarprice, teaprice, wheatprice
    global maazaprice, frootiprice, dewprice, pepsiprice, spriteprice, cococolaprice
    global totalbill

    soapprice = int(bathsoapEntry.get()) * 20
    facecreamprice = int(facecreamEntry.get()) * 50
    facewashprice = int(facewashEntry.get()) * 100
    hairsprayprice = int(hairsprayEntry.get()) * 150
    hairgelprice = int(hairgelEntry.get()) * 80
    bodylotionprice = int(bodylotionEntry.get()) * 60

    totalcosmeticprice = soapprice + facecreamprice + facewashprice + hairsprayprice + hairgelprice + bodylotionprice
    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0, str(totalcosmeticprice) + 'RS')
    cosmetictax = totalcosmeticprice * 0.12
    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, str(cosmetictax) + 'RS')

    # grocery
    riceprice = int(riceEntry.get()) * 200
    dalprice = int(dalEntry.get()) * 100
    oilprice = int(oilEntry.get()) * 120
    sugarprice = int(sugarEntry.get()) * 50
    teaprice = int(teaEntry.get()) * 140
    wheatprice = int(wheatEntry.get()) * 80

    totalgroceryprice = riceprice + dalprice + oilprice + sugarprice + teaprice + wheatprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, str(totalgroceryprice) + 'RS')
    grocerytax = totalgroceryprice * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax) + 'RS')

    # drinks
    maazaprice = int(maazaEntry.get()) * 50
    frootiprice = int(frootiEntry.get()) * 20
    dewprice = int(dewEntry.get()) * 30
    pepsiprice = int(pepsiEntry.get()) * 20
    spriteprice = int(spriteEntry.get()) * 45
    cococolaprice = int(cococolaEntry.get()) * 90

    totaldrinksprice = maazaprice + frootiprice + dewprice + pepsiprice + spriteprice + cococolaprice
    drinkstaxEntry.delete(0, END)
    drinkspriceEntry.insert(0, str(totaldrinksprice) + 'RS')
    drinkstax = totaldrinksprice * 0.08
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, str(drinkstax) + 'RS')

    totalbill = totalcosmeticprice + totalgroceryprice + totaldrinksprice + cosmetictax + grocerytax + drinkstax


root = Tk()
root.title('Billing System')
root.geometry('1280x720')
root.iconbitmap('icon.ico')
# main heading
headingLabel = Label(root, text='Retail Billing System', font=('times new roman', 30, 'bold'), bg='gray20', fg='gold',
                     bd=12, relief='groove')
headingLabel.pack(fill=X, pady=10)

# customer details

customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), bg='gray20',
                                    fg='gold', bd=8, relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'), bg='gray20', fg='white')
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billnumberLabel = Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'), bg='gray20',
                        fg='white')
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)
billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_details_frame, text='Search', font=('arial', 12, 'bold'), bd=7, width=10,
                      command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

# products
productsFrame = Frame(root)
productsFrame.pack()

cosmeticFrame = LabelFrame(productsFrame, text='Cosmetics', font=('times new roman', 15, 'bold'), bg='gray20',
                           fg='gold', bd=8, relief=GROOVE)
cosmeticFrame.grid(row=0, column=0)

bathsoapLabel = Label(cosmeticFrame, text='Bath soap', font=('times new roman', 15, 'bold'), bg='gray20',
                      fg='white')
bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
bathsoapEntry = Entry(cosmeticFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1, pady=9, padx=10)
bathsoapEntry.insert(0, 0)

facecreamLabel = Label(cosmeticFrame, text='Face cream', font=('times new roman', 15, 'bold'), bg='gray20',
                       fg='white')
facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
facecreamEntry = Entry(cosmeticFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
facecreamEntry.grid(row=1, column=1, pady=9, padx=10, sticky='w')
facecreamEntry.insert(0, 0)

facewashLabel = Label(cosmeticFrame, text='Face wash', font=('times new roman', 15, 'bold'), bg='gray20',
                      fg='white')
facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
facewashEntry = Entry(cosmeticFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
facewashEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')
facewashEntry.insert(0, 0)

hairsprayLabel = Label(cosmeticFrame, text='Hair spray', font=('times new roman', 15, 'bold'), bg='gray20',
                       fg='white')
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
hairsprayEntry = Entry(cosmeticFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1, pady=9, padx=10, sticky='w')
hairsprayEntry.insert(0, 0)

hairgelLabel = Label(cosmeticFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='gray20',
                     fg='white')
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
hairgelEntry = Entry(cosmeticFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10, sticky='w')
hairgelEntry.insert(0, 0)

bodylotionLabel = Label(cosmeticFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='gray20',
                        fg='white')
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
bodylotionEntry = Entry(cosmeticFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10, sticky='w')
bodylotionEntry.insert(0, 0)

groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('times new roman', 15, 'bold'), bg='gray20',
                          fg='gold', bd=8, relief=GROOVE)
groceryFrame.grid(row=0, column=1)

riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='white')
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
riceEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10)
riceEntry.insert(0, 0)

oilLabel = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), bg='gray20',
                 fg='white')
oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
oilEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
oilEntry.grid(row=1, column=1, pady=9, padx=10, sticky='w')
oilEntry.insert(0, 0)

dalLabel = Label(groceryFrame, text='Dal', font=('times new roman', 15, 'bold'), bg='gray20',
                 fg='white')
dalLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
dalEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
dalEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')
dalEntry.insert(0, 0)

wheatLabel = Label(groceryFrame, text='Wheat', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
wheatLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
wheatEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
wheatEntry.grid(row=3, column=1, pady=9, padx=10, sticky='w')
wheatEntry.insert(0, 0)

sugarLabel = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
sugarLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
sugarEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
sugarEntry.grid(row=4, column=1, pady=9, padx=10, sticky='w')
sugarEntry.insert(0, 0)

teaLabel = Label(groceryFrame, text='Tea', font=('times new roman', 15, 'bold'), bg='gray20',
                 fg='white')
teaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
teaEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
teaEntry.grid(row=5, column=1, pady=9, padx=10, sticky='w')
teaEntry.insert(0, 0)

drinksFrame = LabelFrame(productsFrame, text='Cold Drinks', font=('times new roman', 15, 'bold'), bg='gray20',
                         fg='gold', bd=8, relief=GROOVE)
drinksFrame.grid(row=0, column=2)

maazaLabel = Label(drinksFrame, text='Maaza', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
maazaLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
maazaEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
maazaEntry.grid(row=0, column=1, pady=9, padx=10)
maazaEntry.insert(0, 0)

pepsiLabel = Label(drinksFrame, text='Pepsi', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
pepsiLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
pepsiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
pepsiEntry.grid(row=1, column=1, pady=9, padx=10, sticky='w')
pepsiEntry.insert(0, 0)

spriteLabel = Label(drinksFrame, text='Sprite', font=('times new roman', 15, 'bold'), bg='gray20',
                    fg='white')
spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
spriteEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
spriteEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')
spriteEntry.insert(0, 0)

dewLabel = Label(drinksFrame, text='Dew', font=('times new roman', 15, 'bold'), bg='gray20',
                 fg='white')
dewLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
dewEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
dewEntry.grid(row=3, column=1, pady=9, padx=10, sticky='w')
dewEntry.insert(0, 0)

frootiLabel = Label(drinksFrame, text='Frooti', font=('times new roman', 15, 'bold'), bg='gray20',
                    fg='white')
frootiLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
frootiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
frootiEntry.grid(row=4, column=1, pady=9, padx=10, sticky='w')
frootiEntry.insert(0, 0)

cococolaLabel = Label(drinksFrame, text='Coco Cola', font=('times new roman', 15, 'bold'), bg='gray20',
                      fg='white')
cococolaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
cococolaEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
cococolaEntry.grid(row=5, column=1, pady=9, padx=10, sticky='w')
cococolaEntry.insert(0, 0)

billFrame = Frame(productsFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=5)

billareaLabel = Label(billFrame, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billFrame, height=18, width=60, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# bill menu
billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'), bg='gray20',
                           fg='gold', bd=8, relief=GROOVE)
billmenuFrame.pack()
cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetic price', font=('times new roman', 15, 'bold'), bg='gray20',
                           fg='white')
cosmeticpriceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
cosmeticpriceEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=1, pady=9, padx=10, sticky='w')

grocerypriceLabel = Label(billmenuFrame, text='Grocery price', font=('times new roman', 15, 'bold'), bg='gray20',
                          fg='white')
grocerypriceLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
grocerypriceEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1, pady=9, padx=10, sticky='w')

drinkspriceLabel = Label(billmenuFrame, text='Drinks price', font=('times new roman', 15, 'bold'), bg='gray20',
                         fg='white')
drinkspriceLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
drinkspriceEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
drinkspriceEntry.grid(row=2, column=1, pady=9, padx=10, sticky='w')

# tax
cosmetictaxLabel = Label(billmenuFrame, text='Cosmetic tax', font=('times new roman', 15, 'bold'), bg='gray20',
                         fg='white')
cosmetictaxLabel.grid(row=0, column=2, pady=9, padx=10, sticky='w')
cosmetictaxEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
cosmetictaxEntry.grid(row=0, column=3, pady=9, padx=10, sticky='w')

grocerytaxLabel = Label(billmenuFrame, text='Grocery tax', font=('times new roman', 15, 'bold'), bg='gray20',
                        fg='white')
grocerytaxLabel.grid(row=1, column=2, pady=9, padx=10, sticky='w')
grocerytaxEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
grocerytaxEntry.grid(row=1, column=3, pady=9, padx=10, sticky='w')

drinkstaxLabel = Label(billmenuFrame, text='Cold Drinks price', font=('times new roman', 15, 'bold'), bg='gray20',
                       fg='white')
drinkstaxLabel.grid(row=2, column=2, pady=9, padx=10, sticky='w')
drinkstaxEntry = Entry(billmenuFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
drinkstaxEntry.grid(row=2, column=3, pady=9, padx=10, sticky='w')

# butttons
buttonframe = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonframe.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonframe, text='Total', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                     pady=10, command=total)
totalButton.grid(row=0, column=0, padx=5, pady=20)

billButton = Button(buttonframe, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                    pady=10, command=bill_area)
billButton.grid(row=0, column=1, padx=5, pady=20)

emailButton = Button(buttonframe, text='Emaill', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                     pady=10, command=send_email)
emailButton.grid(row=0, column=2, padx=5, pady=20)

printButton = Button(buttonframe, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                     pady=10, command=print_bill)
printButton.grid(row=0, column=3, padx=5, pady=20)

clearButton = Button(buttonframe, text='Clear', font=('arial', 16, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                     pady=10, command=clear)
clearButton.grid(row=0, column=4, padx=5, pady=20)
root.mainloop()
