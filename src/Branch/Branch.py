from tkinter import *
from tkinter import ttk
from tkcalendar import *

from Login.Login import Login

root = Tk()
root.geometry("500x320")
root.title("Horizon Restaurant Management System")

class Branch():
    
    def __init__(self):
        
         system_name= ttk.Label(root,text="Horizon Restaurant Management System", font=("Arial",18))
         select_branch_label = ttk.Label(root,text="Select Branch",font=("Arial",14))
         
         #List Of Existing Branches:
         birmingham = "Birmingham"
         bristol = "Bristol"
         cardiff = "Cardiff"
         glasgow = "Glasgow"
         london = "London"
         manchester = "Manchester"
         nottingham = "Nottingham"
         
         birmingham_button = ttk.Button(root,text="Birmingham",command=lambda:Login(widgets, birmingham,root),width=40)
         bristol_button = ttk.Button(root,text="Bristol",command=lambda:Login(widgets, bristol,root),width=40)
         cardiff_button = ttk.Button(root,text="Cardiff",command=lambda:Login(widgets, cardiff,root),width=40)
         glasgow_button = ttk.Button(root,text="Glasgow",command=lambda:Login(widgets, glasgow,root),width=40)
         london_button = ttk.Button(root,text="London",command=lambda:Login(widgets, london,root),width=40)
         manchester_button = ttk.Button(root,text="Manchester",command=lambda:Login(widgets, manchester,root),width=40)
         nottingham_button = ttk.Button(root,text="Nottingham",command=lambda:Login(widgets, nottingham,root),width=40)
         
         system_name.pack()
         select_branch_label.pack()
         
         birmingham_button.pack()
         bristol_button.pack()
         cardiff_button.pack()
         glasgow_button.pack()
         london_button.pack()
         manchester_button.pack()
         nottingham_button.pack()
         
         #Packs the widgets into a list to be passed onto the next class/function that may be called:
         widgets = [system_name,
                    select_branch_label,
                    birmingham_button,
                    bristol_button,
                    cardiff_button,
                    glasgow_button,
                    london_button,
                    manchester_button,
                    nottingham_button]
         
        
         root.mainloop()

