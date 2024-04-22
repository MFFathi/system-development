
import sys
sys.path.append(r'C:\Users\User\Desktop\System Development\System-Development\src\Discounts')
sys.path.append(r'C:\Users\User\Desktop\System Development\System-Development\src\Databases')

from tkinter import *
from tkcalendar import *
import tkinter as tk
from tkinter import ttk, messagebox
#from Discounts.Discounts import Discount
#from Discounts.utils import validate_description
#from Discounts.utils import validate_description
from Databases.Databases import Databases

class Discount:
    
    def __init__(self, root):
        pass


    def createDiscount(description, multiplier):

        # Create discount in the database
        database = Databases.getDatabase("Bristol")
        cursor = database.cursor()

        cursor.execute(
            "INSERT INTO discounts (description, multiplier) VALUES (%s, %s)",
            (description, multiplier)
        )
        database.commit()
        cursor.close()

        messagebox.showinfo("Success", "Discount created successfully")

    def edit_discount(newDiscountInfo, branch):
        discount_id = tk.simpledialog.askstring("Edit Discount", "Enter Discount ID:")

    def delete_discount(self):
        discount_id = tk.simpledialog.askstring("Delete Discount", "Enter Discount ID:")
        if discount_id:
            # Delete the discount from the database
            discount = Discount(discount_id)
            discount.delete()
            messagebox.showinfo("Success", "Discount deleted successfully")
            
    """Class for mananging specfic discounts."""

    def _init_(self, discount_id: str) -> None:
        """Don't call outside of BranchDiscounts."""
        self._discount_id = discount_id

    def get_id(self):
        """Get ID."""
        return self._discount_id

    def get_description():
        database = Databases.getDatabase("Bristol")
        """Get description."""
        mycursor = database.cursor()
        mycursor.execute("SELECT description FROM discounts")
        description = mycursor.fetchall()
        #return discount
        #for x in description:print(x)
        return description



    def get_multiplier(description):
        database = Databases.getDatabase("Bristol")
        """Get description."""
        mycursor = database.cursor()
        sql = "SELECT multiplier FROM discounts where description = %s"
        val = (description,)
        mycursor.execute(sql,val)
        multiplier = mycursor.fetchall()
        #return discount
        #for x in multiplier:print(x)
        #multiplier_dec = multiplier[0]
        #return float(multiplier)
        return multiplier


    def set_description(original, description: str) -> None:
        """Set description."""
        database = Databases.getDatabase("Bristol")
        mycursor = database.cursor()
        sql = "UPDATE discounts SET description = %s WHERE description = %s"
        val = (description,original,)
        mycursor.execute(sql,val)
        Databases.bristol_db.commit()

    def set_multiplier(original, multiplier: float) -> None:
        """Set multiplier."""
        database = Databases.getDatabase("Bristol")
        mycursor = database.cursor()
        sql = "UPDATE discounts SET multiplier = %s WHERE description = %s"
        val = (multiplier,original,)
        mycursor.execute(sql,val)
        Databases.bristol_db.commit()

    def delete(description,multiplier) -> None:
        """
        Delete the discount from the database.
        """
        database = Databases.getDatabase("Bristol")
        mycursor = database.cursor()
        sql = "DELETE FROM discounts WHERE multiplier = %s AND description = %s"
        val = (multiplier,description,)
        mycursor.execute(sql,val)
        Databases.bristol_db.commit()


    def back(self):
        for widget in self.widgets:
            widget.pack_forget()
        self.widgets = []
        # Go back to main menu or previous GUI
        # Example: MainMenuGUI(self.root)

