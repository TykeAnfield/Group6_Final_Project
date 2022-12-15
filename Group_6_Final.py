'''
Tyke Anfield
last revision 11-10-22
version 4
Bag calculator
'''
import tkinter as tk
from tkinter import ttk
from tkinter import *



#===============================================Window Class========================

class Windows(tk.Tk):
  
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    self.title('Batch Calculator')
    container = tk.Frame(self, height=400, width=200)
    container.pack(side="top", fill="both", expand=True)
    self.geometry('600x400+600+300')
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = {}
       
    for F in (MainPage, SidePage, CompletionScreen):
      frame = F(container, self,)
      
      self.frames[F] = frame
      frame.grid(row=0, column=0, sticky="nsew")

      # Using a method to switch frames
    self.show_frame(MainPage)

  def show_frame(self, cont):
    frame = self.frames[cont]
    # raises the current frame to the top
    frame.tkraise()


#=========================================First Class==============================

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent, 
      background="lightblue",
      border=10)
      self.label = tk.Label(self, text="Lactose, Sucrose, Malto, ect.", border=3)
      self.label.grid(row=0, column=0, 
      columnspan=5, 
      pady=10, padx=20, 
      ipady=5, ipadx=5,
      )
      self.label.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)

      self.PRODUCTS = []
      self.list = list
      self.list = tk.Listbox(self, 
      width=75, 
      height=15,
      background="lightblue",
      border=3
      )
      self.list.grid(row=1, column=0, columnspan=10,
      pady=10, padx=10, 
      ipady=5, ipadx=5,
      sticky="nsew")
      

      self.PRODUCTS = [
      ("MATERIAL NUMBER", "MATERIAL NAME", "MATERIAL WEIGHT(kg)"),
      (1019716, "Lactose", 25),
      (1019740, "Sucrose Bakers Special", 22.67),
      (1019753, "Malto Dextrin", 22.67),
      (1019895, "Malto Dextrin", 22.68),
      (1020465, "Dextrose Anhydrose", 25),
      (1189912, "Malto Dextrin Identity Preserved", 22.68),
      ]
  
      for self.item in self.PRODUCTS:
        self.list.insert(END, self.item)

    #Label
      self.nttLabel = tk.Label(self, 
      text="How many NTTs",
      background="lightblue"
      )
      self.nttLabel.grid(row=3, column=1, sticky="nsew")
    #Spinbox
      self.ntts = tk.Spinbox(self, 
      from_=int(0), 
      to=int(10)
      )
      self.ntts.grid(row=3, column=2)
    #Label
      self.showsplitLabel = tk.Label(self, 
      text="needed per NTT",
      background="lightblue"
      )
      self.showsplitLabel.grid(row=4, column=1, sticky="nsew")


    #Label
      self.bulkLabel = tk.Label(self, 
      text="Enter amount needed",
      background="lightblue"
      )
      self.bulkLabel.grid(row=5, column=1, sticky="nsew")
    #Entry
      self.bulk = tk.Entry(self)
      self.bulk.grid(row=5, column=2, sticky="nsew")
    #Label
      self.showbags = tk.Label(self, 
      text="Bags needed",
      background="lightblue"
      )
      self.showbags.grid(row=7, column=1, sticky="nsew")
    #Label
      self.roundedLabel = tk.Label(self, text="Rounded amount", background="lightblue")
      self.roundedLabel.grid(row=6, column=1, sticky="nsew")
      self.materialLabel = tk.Label(self, text="Material selected", background="lightblue")
      self.materialLabel.grid(row=2, column=1)
      def clicker():
          for self.i in self.list.curselection():
                self.i = self.list.get(self.i)[2]
                
                
                

                self.bagsNeeded = int(self.bulk.get()) / self.i
            
                self.showneeded = tk.Label(self, 
                text=round(self.bagsNeeded)
                )
                self.showneeded.grid(row=7, column=2, sticky="nsew")
      
                self.split = int(self.bagsNeeded) / int(self.ntts.get())

                self.showsplit = tk.Label(self, 
                text=round(self.split)
                )
                self.showsplit.grid(row=4, column=2, sticky="nsew")

                self.rounded = round(self.bagsNeeded) * self.i
                self.rounded = tk.Label(self, 
                                  text=round(self.rounded))
                self.rounded.grid(row=6, column=2)

                for self.i in self.list.curselection():
                  self.i = self.list.get(self.i)
                  self.showmaterial = tk.Label(self, text=self.i)
                  self.showmaterial.grid(row=2, column=2)
                return self.split, self.showsplit
      def clear():
        self.showmaterial.destroy()
        self.showneeded.destroy()
        self.showsplit.destroy()
        self.rounded.destroy()
        
      self.clearButton = tk.Button(self,
                    text="Clear",
                    command=clear)
      self.clearButton.grid(row=7, column=3, padx=10, pady=5,)
      self.calButton = tk.Button(self, 
      text="Calculate", 
      command=clicker,
      )
      self.calButton.grid(row=5, column=3,
                          padx=10, pady=5, sticky="nsew")
          

    # We use the switch_window_button in order to call the show_frame() method as a lambda function
      switch_window_button = tk.Button(self, 
        text="Go to the Second material", 
        command=lambda: controller.show_frame(SidePage)
        )
      switch_window_button.grid(row=6, column=3, padx=10, pady=5, sticky="nsew")


#==================================================Second Class==========================================

class SidePage(tk.Frame):
    def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent,
      background="lightblue",
      border=10)
      label = tk.Label(self, text="Corn Syrup Solids, Starch", border=3)
      label.grid(row=0, column=0, 
      columnspan=5, 
      pady=10, padx=20, 
      ipady=5, ipadx=5,
      )
      label.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)

      self.PRODUCTS = []
      self.list = list
      self.list = tk.Listbox(self,
      width=75, 
      height=15,
      background="lightblue",
      border=3
      )
      self.list.grid(row=1, column=0, columnspan=10, 
      pady=10, padx=10, 
      ipady=5, ipadx=5,
      sticky="nsew")

      self.PRODUCTS = [
      ("MATERIAL NUMBER", "MATERIAL NAME", "MATERIAL WEIGHT(kg)"),
      (1019788, "Corn Syrup Solids", 22.68),
      (1019921, "Corn Syrup Solids", 22.68),
      (1020370, "Starch", 22.7),
      (1020372, "Starch Waxy Rice", 25),
      (1020523, "Starch Waxy Pregelantinized", 25),
      (1190076, "Corn Syrup Solids", 25),
      (2049037, "Corn Sryup Solids", 22.68),
      ]
  
      for item in self.PRODUCTS:
        self.list.insert(END, item)

   #Label
      self.nttLabel = tk.Label(self, 
      text="How many NTTs",
      background="lightblue"
      )
      self.nttLabel.grid(row=3, column=1, sticky="nsew")
    #Spinbox
      self.ntts = tk.Spinbox(self, 
      from_=int(0), 
      to=int(10)
      )
      self.ntts.grid(row=3, column=2)
    #Label
      self.showsplitLabel = tk.Label(self, 
      text="needed per NTT",
      background="lightblue"
      )
      self.showsplitLabel.grid(row=4, column=1, sticky="nsew")


    #Label
      self.bulkLabel = tk.Label(self, 
      text="Enter amount needed",
      background="lightblue"
      )
      self.bulkLabel.grid(row=5, column=1, sticky="nsew")
    #Entry
      self.bulk = tk.Entry(self)
      self.bulk.grid(row=5, column=2, sticky="nsew")
    #Label
      self.showbags = tk.Label(self, 
      text="Bags needed",
      background="lightblue"
      )
      self.showbags.grid(row=7, column=1, sticky="nsew")
    #Label
      self.roundedLabel = tk.Label(self, text="Rounded amount", background="lightblue")
      self.roundedLabel.grid(row=6, column=1, sticky="nsew")
      self.materialLabel = tk.Label(self, text="Material selected", background="lightblue")
      self.materialLabel.grid(row=2, column=1)


      def clicker():
          for self.i in self.list.curselection():
                self.i = self.list.get(self.i)[2]  

                self.bagsNeeded = int(self.bulk.get()) / self.i
            
                self.showneeded = tk.Label(self, 
                text=round(self.bagsNeeded)
                )
                self.showneeded.grid(row=7, column=2, sticky="nsew")
      
                self.split = int(self.bagsNeeded) / int(self.ntts.get())

                self.showsplit = tk.Label(self, 
                text=round(self.split)
                )
                self.showsplit.grid(row=4, column=2, sticky="nsew")

                self.rounded = round(self.bagsNeeded) * self.i
                self.rounded = tk.Label(self, 
                                  text=round(self.rounded))
                self.rounded.grid(row=6, column=2)

                for self.i in self.list.curselection():
                  self.i = self.list.get(self.i)
                  self.showmaterial = tk.Label(self, text=self.i)
                  self.showmaterial.grid(row=2, column=2)

                return self.split, self.showsplit

      def clear():
        self.showmaterial.destroy()
        self.showneeded.destroy()
        self.showsplit.destroy()
        self.rounded.destroy()
        
      self.clearButton = tk.Button(self,
                    text="Clear",
                    command=clear)
      self.clearButton.grid(row=7, column=3, padx=10, pady=5,)
      self.calButton = tk.Button(self, 
      text="Calculate", 
      command=clicker,
      )
      self.calButton.grid(row=5, column=3,
                          padx=10, pady=5, sticky="nsew")

      switch_window_button = tk.Button(
            self,
            text="Go to the Third material",
            command=lambda: controller.show_frame(CompletionScreen),
        )
      switch_window_button.grid(row=6, column=3, padx=10, pady=5, sticky="nsew")
    
  
#==========================================Third Class===============================

class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
      tk.Frame.__init__(
          self, parent, 
          background="lightblue",
          border=10)
      label = tk.Label(self, text="Proteins", border=3)
      label.grid(row=0, column=0, columnspan=5, 
        pady=10, padx=20, 
        ipady=5, ipadx=5,
        )
      label.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)


      
      self.PRODUCTS = []
      self.list = list
      self.list = tk.Listbox(self, 
        width=75, 
        height=15,
        background="lightblue",
        border=3
      )
      self.list.grid(row=1, column=0, columnspan=10,
      pady=10, padx=10, 
      ipady=5, ipadx=5,
       sticky="nsew")

      self.PRODUCTS = [
      ("MATERIAL NUMBER", "MATERIAL NAME", "MATERIAL WEIGHT(kg)"),
      (1020329, "Milk Protein Isolate", 15),
      (1020356, "Soy Protein Isolate", 20),
      (1134853, "Whey Protein Isolate Hydrolyzed", 14.99),
      (1182347, "Milk Protein Partial Hydrolysate", 25),
      (1275288, "Whey Protein 80%", 20),
      (1216239, "Milk Protein Conc.", 20),
      (2064148, "Milk Protein Hydro", 25)
      ]
  
      for item in self.PRODUCTS:
        self.list.insert(END, item)

  #Label
      self.nttLabel = tk.Label(self, 
      text="How many NTTs",
      background="lightblue"
      )
      self.nttLabel.grid(row=3, column=1, sticky="nsew")
    #Spinbox
      self.ntts = tk.Spinbox(self, 
      from_=int(0), 
      to=int(10)
      )
      self.ntts.grid(row=3, column=2)
    #Label
      self.showsplitLabel = tk.Label(self, 
      text="needed per NTT",
      background="lightblue"
      )
      self.showsplitLabel.grid(row=4, column=1, sticky="nsew")


    #Label
      self.bulkLabel = tk.Label(self, 
      text="Enter amount needed",
      background="lightblue"
      )
      self.bulkLabel.grid(row=5, column=1, sticky="nsew")
    #Entry
      self.bulk = tk.Entry(self)
      self.bulk.grid(row=5, column=2, sticky="nsew")
    #Label
      self.showbags = tk.Label(self, 
      text="Bags needed",
      background="lightblue"
      )
      self.showbags.grid(row=7, column=1, sticky="nsew")
    #Label
      self.roundedLabel = tk.Label(self, text="Rounded amount", background="lightblue")
      self.roundedLabel.grid(row=6, column=1, sticky="nsew")
      self.materialLabel = tk.Label(self, text="Material selected", background="lightblue")
      self.materialLabel.grid(row=2, column=1)

      def clicker():
        for self.i in self.list.curselection():
              self.i = self.list.get(self.i)[2]  

              self.bagsNeeded = int(self.bulk.get()) / self.i
          
              self.showneeded = tk.Label(self, 
              text=round(self.bagsNeeded)
              )
              self.showneeded.grid(row=7, column=2, sticky="nsew")
    
              self.split = int(self.bagsNeeded) / int(self.ntts.get())

              self.showsplit = tk.Label(self, 
              text=round(self.split)
              )
              self.showsplit.grid(row=4, column=2, sticky="nsew")

              self.rounded = round(self.bagsNeeded) * self.i
              self.rounded = tk.Label(self, 
                                text=round(self.rounded))
              self.rounded.grid(row=6, column=2)

              for self.i in self.list.curselection():
                  self.i = self.list.get(self.i)
                  self.showmaterial = tk.Label(self, text=self.i)
                  self.showmaterial.grid(row=2, column=2)

              return self.split, self.showsplit


      def clear():
        self.showmaterial.destroy()
        self.showneeded.destroy()
        self.showsplit.destroy()
        self.rounded.destroy()
        
      self.clearButton = tk.Button(self,
                    text="Clear",
                    command=clear)
      self.clearButton.grid(row=7, column=3, padx=10,     pady=5,)
      self.calButton = tk.Button(self, 
      text="Calculate", 
      command=clicker,
      )
      self.calButton.grid(row=5, column=3,
                          padx=10, pady=5, sticky="nsew")

      switch_window_button = ttk.Button(
              self, 
              text="Return to First material", 
              command=lambda: controller.show_frame(MainPage)
          )
      switch_window_button.grid(row=6, column=3, padx=10, pady=5, sticky="nsew")




if __name__ == "__main__":
    app = Windows()
    app.mainloop()
      
