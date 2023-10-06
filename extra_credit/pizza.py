import tkinter
import tkinter.messagebox
class MyGUI:
    def __init__(self):
        self._main_window = tkinter.Tk()
        self._main_window.geometry('500x500')
        self._main_window.title("Order Pizza")
        
        self._top_frame = tkinter.Frame(self._main_window)
        self._top_frame.pack(side='top')

        self._bottom_frame = tkinter.Frame(self._main_window)
        self._bottom_frame.pack(side='bottom')

        self._order_pizza_lable = tkinter.Label(self._main_window, text ='Pizza Order')
        self._order_pizza_lable.pack(padx=2, pady=2, ipadx=4, ipady=4)

        #enter name label
        self._enter_name_label = tkinter.Label(self._main_window, text='Enter your name: ')
        self._enter_name_label.pack(padx=3, pady=3)

        #enter name entry
        self._name = tkinter.Entry(self._main_window, width=20)
        self._name.pack(padx=5, pady=5)

        #pick crust
        self._crust_label = tkinter.Label(self._main_window, text='Pick your pizza curst')
        self._crust_label.pack()
        self._crust_var = tkinter.IntVar()
        
        #thin crust
        self._thin = tkinter.Radiobutton(self._main_window, text='Thin', variable=self._crust_var, value=1)
        #regular curst
        self._regular_curst = tkinter.Radiobutton(self._main_window, text='Regular', variable=self._crust_var, value=2)
        #deep dish crust
        self._deep_dish = tkinter.Radiobutton(self._main_window, text='Deep Dish', variable=self._crust_var, value=3)

        self._thin.pack()
        self._regular_curst.pack()
        self._deep_dish.pack()
        #self._crust_var.set(0)

        #pick sauce
        self._sauce_label = tkinter.Label(self._main_window, text='Pick your pizza sauce')
        self._sauce_label.pack()
        self._sauce_var = tkinter.IntVar()

        #regular
        self._regular_sauce = tkinter.Radiobutton(self._main_window, text='Regular', variable=self._sauce_var, value=1)
        #bbq
        self._bbq_sauce = tkinter.Radiobutton(self._main_window, text='BBQ', variable=self._sauce_var, value=2)
        #alfredo
        self._alfredo_sauce = tkinter.Radiobutton(self._main_window, text='Alfredo', variable=self._sauce_var, value=3)

        self._regular_sauce.pack()
        self._bbq_sauce.pack()
        self._alfredo_sauce.pack()
        #self._sauce_var.set(0)
        

        #topping
        self._topping_label = tkinter.Label(self._main_window, text='Pick your pizza topping')
        self._topping_label.pack()
        
        self._pepperoni_var = tkinter.IntVar()
        self._olives_var = tkinter.IntVar()
        self._mushroom_var = tkinter.IntVar()
        #pepperoni
        self._pepperoni = tkinter.Checkbutton(self._main_window, text='Pepperoni', variable=self._pepperoni_var)
        self._pepperoni_var.set(0)
        #olives
        self._olives = tkinter.Checkbutton(self._main_window, text='Olives', variable=self._olives_var)
        self._olives_var.set(0)
        #mushroom
        self._mushroom = tkinter.Checkbutton(self._main_window, text='Mushroom', variable=self._mushroom_var)
        self._mushroom_var.set(0)

        self._pepperoni.pack()
        self._olives.pack()
        self._mushroom.pack()
        
        #pick size

        #pick sauce
        self._size_label = tkinter.Label(self._main_window, text='Pick your pizza size')
        self._size_label.pack()
        self._size_var = tkinter.IntVar()

        #regular
        self._regular_size = tkinter.Radiobutton(self._main_window, text='Medium', variable=self._size_var, value=1)
        #bbq
        self._small_size = tkinter.Radiobutton(self._main_window, text='Small', variable=self._size_var, value=2)
        #alfredo
        self._large_size = tkinter.Radiobutton(self._main_window, text='Large', variable=self._size_var, value=3)

        self._regular_size.pack()
        self._small_size.pack()
        self._large_size.pack()
        #self._size_var.set(0)


        self._order_button = tkinter.Button(self._main_window, text='Order', command=self.cal_order)
        self._order_button.pack(ipadx=5, ipady=5)

        
        tkinter.mainloop()
    
    def cal_order(self):
        
        base_price = 10
        if self._size_var.get() == 1: #medium size
            base_price += 1.5
        elif self._size_var.get() == 3: #large size
            base_price += 3
        
        if self._pepperoni_var.get() == 1:
            base_price += 0.5
        if self._olives_var.get() == 1:
            base_price += 0.5
        if self._mushroom_var.get() == 1:
            base_price += 0.5
        
        

        
        if len(self._name.get()) == 0:
            tkinter.messagebox.showerror("Enter name", "Name cannot be blank")
        elif self._name.get().isnumeric():
            tkinter.messagebox.showerror("Enter valid name", "Name cannot be a number")
        
        elif self._crust_var.get() == 0:
            tkinter.messagebox.showerror("Select your pizza crurst", "You must select crust")
        elif self._sauce_var.get() == 0:
            tkinter.messagebox.showerror("Select your pizza sauce", "You must select crust")
        elif self._size_var.get() == 0:
            tkinter.messagebox.showerror("Select your pizza size", "You must select size")
        else:
            tkinter.messagebox.showinfo("Order received", f"Thank you {self._name.get()} for your order\nYour total: ${base_price}")
    


    
