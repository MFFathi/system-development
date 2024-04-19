
from Databases.Databases import Databases

class BranchReservation(): 

    def Show_All_The_Tables():
        pass

    # Function to check if a table is available at a specific date and time
    def Is_Table_Available(tableNo, dateTime):
        pass

    # Function to add a new table
    def Add_Table(TableNo, NoOfPeople) -> int:
        pass

    # Function to edit the number of people for an existing table
    def Edit_Table(TableNo, NewNoOfPeople) -> int:
        pass

    # Function to delete a table
    def Delete_Table(TableNo:int):
        pass

    # Function to get all reservations for a specific table
    def get_all_reservations_for_table(TableNo):
        pass

    # Function to get all reservations for a specific date
    def get_all_reservations_for_date(date:str):
        pass

    