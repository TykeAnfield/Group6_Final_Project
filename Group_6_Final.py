'''
Tyke Anfield
last revision 11-10-22
version 4
Bag calculator
'''
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image
import math


#===============================================Window Class========================

class Windows(tk.Tk):
  
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    self.title('Batch Calculator')
    container = tk.Frame(self, height=400, width=600)
    container.pack(side="top", fill="both", expand=True)

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
      label = tk.Label(self, text="First Material Needed", border=3)
      label.grid(row=0, column=0, 
      columnspan=5, 
      pady=10, padx=250, 
      ipady=5, ipadx=5,
      sticky="")
      label.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)

      self.PRODUCTS = []
      self.list = list
      self.list = tk.Listbox(self, 
      width=50, 
      height=15,
      background="lightblue",
      border=3
      )
      self.list.grid(row=1, column=0, columnspan=3,
      pady=10, padx=10, 
      ipady=5, ipadx=5,
      sticky="nsew")
      

      self.PRODUCTS = [
      ("MATERIAL NUMBER", "MATERIAL NAME", "MATERIAL WEIGHT(kg)"),
      (1019680, "Protein Hydrolysate", "weight varies by drum"),
      (1019716, "Lactose", 25),
      (1019740, "Sucrose Bakers Special", 22.67),
      (1019753, "Malto Dextrin", 22.67),
      (1019788, "Corn Syrup Solids", 22.68),
      (1019895, "Malto Dextrin", 22.68),
      (1019921, "Corn Syrup Solids", 22.68),
      (1020329, "Milk Protein Isolate", 15),
      (1020356, "Soy Protein Isolate", 20),
      (1020369, "Milk High heat", 25),
      (1020370, "Starch", 22.7),
      (1020372, "Starch Waxy Rice", 25),
      (1020465, "Dextrose Anhydrose", 25),
      (1020523, "Starch Waxy Pregelantinized", 25),
      (1134853, "Whey Protein Isolate Hydrolyzed", 14.99),
      (1182347, "Milk Protein Partial Hydrolysate", 25),
      (1189912, "Malto Dextrin Identity Preserved", 22.68),
      (1190076, "Corn Syrup Solids", 25),
      (1275288, "Whey Protein 80%", 20),
      (1216239, "Milk Protein Conc.", 20),
      (2005725, "Caseinate Calcium", 20),
      (2005726, "Caseinate Sodium Pwd 60 Mesh", 20),
      (2029078, "Exp Cocoa", 22.68),
      (2049037, "Corn Sryup Solids", 22.68),
      (2064148, "Milk Protein Hydro", 25)
      ]
  
      for self.item in self.PRODUCTS:
        self.list.insert(END, self.item)

    #Label
      self.nttLabel = tk.Label(self, 
      text="How many NTTs",
      background="lightblue"
      )
      self.nttLabel.grid(row=2, column=1, sticky="nsew")
    #Spinbox
      self.ntts = tk.Spinbox(self, 
      from_=int(0), 
      to=int(10)
      )
      self.ntts.grid(row=2, column=2)
    #Label
      self.showsplitLabel = tk.Label(self, 
      text="needed per NTT",
      background="lightblue"
      )
      self.showsplitLabel.grid(row=3, column=1, sticky="nsew")


    #Label
      self.bulkLabel = tk.Label(self, 
      text="Enter amount needed",
      background="lightblue"
      )
      self.bulkLabel.grid(row=4, column=1, sticky="nsew")
    #Entry
      self.bulk = tk.Entry(self)
      self.bulk.grid(row=4, column=2, sticky="nsew")
    #Label
      self.bagsNeededLabel = tk.Label(self, 
      text="Bags needed",
      background="lightblue"
      )
      self.bagsNeededLabel.grid(row=7, column=1, sticky="nsew")
    #Label for rounded 
      self.roundedLabel = tk.Label(self, text="Rounded amount", background="lightblue")
      self.roundedLabel.grid(row=6, column=1, sticky="nsew")

      def clicker():
          for self.bagWeight in self.list.curselection():
                #sets the last value in tuple as bagWeight
                self.bagWeight = self.list.get(self.bagWeight)[2]  

                # Calculates bags needed for batch by dividing the whole amount by the bag weight
                self.bagsNeeded = float(self.bulk.get()) / self.bagWeight
                self.bagsNeededAmount = tk.Label(self, 
                text=round(self.bagsNeeded)
                )
                self.bagsNeededAmount.grid(row=7, column=2, sticky="nsew")

                # splits the bags between the NTTs 
                self.split = int(round(self.bagsNeeded)) / int(self.ntts.get())
                self.showsplit = tk.Label(self, 
                text=round(self.split)
                )
                self.showsplit.grid(row=3, column=2, sticky="nsew")

                #Rounds the batch total amount
                self.rounded = self.bagsNeeded * float(self.bagWeight.get)
                self.showRounded = tk.Label(self, 
                            text=round(self.rounded))
                self.showRounded.grid(row=6, column=2)
                  

      def clear():
        self.bagsNeededAmount.destroy()
        self.showsplit.destroy()
        self.showRounded.destroy()
        
      #Clear Button
      self.clearButton = tk.Button(self,
      text="Clear",
      command=clear)
      self.clearButton.grid(row=4, column=3, padx=10, pady=5,)

      #Calculate Button
      self.calButton = tk.Button(self, 
      text="Calculate", 
      command=clicker
      )
      self.calButton.grid(row=3, column=3, sticky="nsew")
          

    # We use the switch_window_button in order to call the show_frame() method as a lambda function
      switch_window_button = tk.Button(self, 
        text="Go to the Second material", 
        command=lambda: controller.show_frame(SidePage)
        )
      switch_window_button.grid(row=5, column=3, sticky="nsew")


#==================================================Second Class==========================================

class SidePage(tk.Frame):
    def __init__(self, parent, controller, ):
      tk.Frame.__init__(self, parent, )
      label = tk.Label(self, text="Second Material Needed")
      label.grid(row=0, column=0, columnspan=5, sticky="nsew")

      self.PRODUCTS = []
      self.list = list
      self.list = tk.Listbox(self, 
      width=50, 
      height=15
      )
      self.list.grid(row=1, column=0, sticky="nsew")

      self.PRODUCTS = [
      ("MATERIAL NUMBER", "MATERIAL NAME", "MATERIAL WEIGHT(kg)"),
      (1019680, "Protein Hydrolysate", "weight varies by drum"),
      (1019716, "Lactose", 25),
      (1019740, "Sucrose Bakers Special", 22.67),
      (1019753, "Malto Dextrin", 22.67),
      (1019788, "Corn Syrup Solids", 22.68),
      (1019895, "Malto Dextrin", 22.68),
      (1019921, "Corn Syrup Solids", 22.68),
      (1020329, "Milk Protein Isolate", 15),
      (1020356, "Soy Protein Isolate", 20),
      (1020369, "Milk High heat", 25),
      (1020370, "Starch", 22.7),
      (1020372, "Starch Waxy Rice", 25),
      (1020465, "Dextrose Anhydrose", 25),
      (1020523, "Starch Waxy Pregelantinized", 25),
      (1134853, "Whey Protein Isolate Hydrolyzed", 14.99),
      (1182347, "Milk Protein Partial Hydrolysate", 25),
      (1189912, "Malto Dextrin Identity Preserved", 22.68),
      (1190076, "Corn Syrup Solids", 25),
      (1275288, "Whey Protein 80%", 20),
      (1216239, "Milk Protein Conc.", 20),
      (2005725, "Caseinate Calcium", 20),
      (2005726, "Caseinate Sodium Pwd 60 Mesh", 20),
      (2029078, "Exp Cocoa", 22.68),
      (2049037, "Corn Sryup Solids", 22.68),
      (2064148, "Milk Protein Hydro", 25)
      ]
  
      for item in self.PRODUCTS:
        self.list.insert(END, item)

    #Label
      nttLabel = tk.Label(self, 
      text="How many NTTs"
      )
      nttLabel.grid(row=1, column=1, sticky="nsew")
    #Spinbox
      ntts = tk.Spinbox(self, 
      from_=int(0), 
      to=int(10)
      )
      ntts.grid(row=1, column=2)
    #Label
      showsplitLabel = tk.Label(self, 
      text="needed per NTT"
      )
      showsplitLabel.grid(row=2, column=1, sticky="nsew")


    #Label
      bulkLabel = tk.Label(self, 
      text="Enter amount needed"
      )
      bulkLabel.grid(row=3, column=1, sticky="nsew")
    #Entry
      bulk = tk.Entry(self)
      bulk.grid(row=3, column=2, sticky="nsew")
    #Label
      show1 = tk.Label(self, 
      text="Bags needed"
      )
      show1.grid(row=4, column=1, sticky="nsew")

      def clicker():
          for i in self.list.curselection():
                
                i = self.list.get(i)[2]  

                bagsNeeded = int(bulk.get()) / i

                show = tk.Label(self, 
                text=bagsNeeded
                )
                show.grid(row=4, column=2, sticky="nsew")
      
                split = int(bagsNeeded) / int(ntts.get())

                showsplit = tk.Label(self, 
                text=split
                )
                showsplit.grid(row=2, column=2, sticky="nsew")

      calButton = tk.Button(self, 
      text="Calculate", 
      command=clicker
      )
      calButton.grid(row=4, column=4, sticky="nsew")

      switch_window_button = tk.Button(
            self,
            text="Go to the Third material",
            command=lambda: controller.show_frame(CompletionScreen),
        )
      switch_window_button.grid(row=5, column=5, sticky="nsew")
    
  
#==========================================Third Class===============================

class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Third Material Needed")
        label.grid(row=0, column=0, columnspan=5, sticky="nsew")


      
        self.PRODUCTS = []
        self.list = list
        self.list = tk.Listbox(self, 
        width=50, 
        height=15
        )
        self.list.grid(row=1, column=0, sticky="nsew")

        self.PRODUCTS = [
        ("MATERIAL NUMBER", "MATERIAL NAME", "MATERIAL WEIGHT(kg)"),
        (1019680, "Protein Hydrolysate", "weight varies by drum"),
        (1019716, "Lactose", 25),
        (1019740, "Sucrose Bakers Special", 22.67),
        (1019753, "Malto Dextrin", 22.67),
        (1019788, "Corn Syrup Solids", 22.68),
        (1019895, "Malto Dextrin", 22.68),
        (1019921, "Corn Syrup Solids", 22.68),
        (1020329, "Milk Protein Isolate", 15),
        (1020356, "Soy Protein Isolate", 20),
        (1020369, "Milk High heat", 25),
        (1020370, "Starch", 22.7),
        (1020372, "Starch Waxy Rice", 25),
        (1020465, "Dextrose Anhydrose", 25),
        (1020523, "Starch Waxy Pregelantinized", 25),
        (1134853, "Whey Protein Isolate Hydrolyzed", 14.99),
        (1182347, "Milk Protein Partial Hydrolysate", 25),
        (1189912, "Malto Dextrin Identity Preserved", 22.68),
        (1190076, "Corn Syrup Solids", 25),
        (1275288, "Whey Protein 80%", 20),
        (1216239, "Milk Protein Conc.", 20),
        (2005725, "Caseinate Calcium", 20),
        (2005726, "Caseinate Sodium Pwd 60 Mesh", 20),
        (2029078, "Exp Cocoa", 22.68),
        (2049037, "Corn Sryup Solids", 22.68),
        (2064148, "Milk Protein Hydro", 25)
        ]
    
        for item in self.PRODUCTS:
          self.list.insert(END, item)

      #Label
        nttLabel = tk.Label(self, 
        text="How many NTTs"
        )
        nttLabel.grid(row=1, column=1, sticky="nsew")
      #Spinbox
        ntts = tk.Spinbox(self, 
        from_=int(0), 
        to=int(10)
        )
        ntts.grid(row=1, column=2)
      #Label
        showsplitLabel = tk.Label(self, 
        text="needed per NTT"
        )
        showsplitLabel.grid(row=2, column=1, sticky="nsew")


      #Label
        bulkLabel = tk.Label(self, 
        text="Enter amount needed"
        )
        bulkLabel.grid(row=3, column=1, sticky="nsew")
      #Entry
        bulk = tk.Entry(self)
        bulk.grid(row=3, column=2, sticky="nsew")
      #Label
        show1 = tk.Label(self, 
        text="Bags needed"
        )
        show1.grid(row=4, column=1, sticky="nsew")

        def clicker():
            for i in self.list.curselection():
                  
                  i = self.list.get(i)[2]  

                  bagsNeeded = int(bulk.get()) / i

                  show = tk.Label(self, 
                  text=bagsNeeded
                  )
                  show.grid(row=4, column=2, sticky="nsew")
        
                  split = int(bagsNeeded) / int(ntts.get())

                  showsplit = tk.Label(self, 
                  text=split
                  )
                  showsplit.grid(row=2, column=2, sticky="nsew")

        calButton = tk.Button(self, 
        text="Calculate", 
        command=clicker
        )
        calButton.grid(row=4, column=4, sticky="nsew")


        switch_window_button = ttk.Button(
              self, 
              text="Return to First material", 
              command=lambda: controller.show_frame(MainPage)
          )
        switch_window_button.grid(row=5, column=5, sticky="nsew")





if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()
      
