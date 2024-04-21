
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
        self.back()

    def edit_discount(self):
        discount_id = tk.simpledialog.askstring("Edit Discount", "Enter Discount ID:")
        if discount_id:
            self.discount_id = discount_id
            self.create_discount()  # Reuse the create discount interface for editing

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

        

    def set_description(self, description: str) -> None:
        """Set description."""
        if not validate_description(description):
            raise InputError("Invalid description.")

        Database.execute_and_commit(
            "UPDATE public.discounts SET description = %s WHERE id = %s",
            description, self._discount_id)

    def set_multiplier(self, multiplier: float) -> None:
        """Set multiplier."""
        Database.execute_and_commit(
            "UPDATE public.discounts SET multiplier = %s WHERE id = %s",
            multiplier, self._discount_id)

    def delete(self) -> None:
        """
        Delete the discount from the database.

        After calling you should immediately discard this object. Not doing so
        will cause errors.

        :raises PermissionError: If the current user does not have permission
        """
        # Could cause issues with references, might be best to switch to soft
        # deletion and a cron job
        sql = "DELETE FROM public.discounts WHERE id=%s;"

        ActiveUser.get().raise_without_permission("discount.delete")

        Database.execute_and_commit(sql, self._discount_id)

    def back(self):
        for widget in self.widgets:
            widget.pack_forget()
        self.widgets = []
        # Go back to main menu or previous GUI
        # Example: MainMenuGUI(self.root)

