import unittest
from unittest.mock import patch
from datetime import datetime
from tkinter import messagebox

from EventManagement import EventManagementPage

class TestEventManagementPage(unittest.TestCase):
    def setUp(self):
        self.app = EventManagementPage()

    def tearDown(self):
        self.app.destroy()

    def test_submit_button_clicked_valid_input(self):
        with patch.object(messagebox, 'showinfo') as mock_showinfo:
            self.app.submit_button_clicked("Test Event", "Test Description", "2024-04-25", "12:00", "15:00", "Birthday", "1234567890", "Karim@gmail.com", "123 Test St", "Accept")
            mock_showinfo.assert_called_once_with("Success", "Data has been inserted successfully.")

    def test_submit_button_clicked_missing_fields(self):
        with patch.object(messagebox, 'showerror') as mock_showerror:
            self.app.submit_button_clicked("", "Test Description", "2024-04-25", "12:00", "15:00", "Birthday", "1234567890", "Karim@example.com", "123 Test St", "Accept")
            mock_showerror.assert_called_once_with("Error", "All fields must be filled.")

    def test_submit_button_clicked_invalid_date_format(self):
        with patch.object(messagebox, 'showerror') as mock_showerror:
            self.app.submit_button_clicked("Test Event", "Test Description", "25-04-2024", "12:00", "15:00", "Birthday", "1234567890", "Karim@example.com", "123 Test St", "Accept")
            mock_showerror.assert_called_once_with("Error", "Invalid date format, it must be in this format YYYY-MM-DD.")

    def test_submit_button_clicked_invalid_time_format(self):
        with patch.object(messagebox, 'showerror') as mock_showerror:
            self.app.submit_button_clicked("Test Event", "Test Description", "2024-04-25", "12:00 PM", "3:00 PM", "Birthday", "1234567890", "Karim@example.com", "123 Test St", "Accept")
            mock_showerror.assert_called_once_with("Error", "Invalid time format, it must be in this format HH:MM.")

    def test_submit_button_clicked_past_date(self):
        with patch.object(messagebox, 'showerror') as mock_showerror:
            yesterday = datetime.now().date() - timedelta(days=1)
            self.app.submit_button_clicked("Test Event", "Test Description", str(yesterday), "12:00", "15:00", "Birthday", "1234567890", "Karim@example.com", "123 Test St", "Accept")
            mock_showerror.assert_called_once_with("Error", "Date of Event must be after the current date.")

if __name__ == "__main__":
    unittest.main()
