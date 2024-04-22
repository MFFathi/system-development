import tkinter as tk
from tkinter import messagebox
import random


class Payment:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment Details")

        self.first_name_var = tk.StringVar()
        self.sur_name_var = tk.StringVar()
        self.card_number_var = tk.StringVar()
        self.cvv_var = tk.StringVar()
        self.balance_var = tk.StringVar()

        tk.Label(root, text="First Name").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.first_name_var).grid(row=0, column=1)

        tk.Label(root, text="Surname").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.sur_name_var).grid(row=1, column=1)

        tk.Label(root, text="Card Number").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.card_number_var).grid(row=2, column=1)

        tk.Label(root, text="CVV (Security Code)").grid(row=3, column=0)
        tk.Entry(root, textvariable=self.cvv_var).grid(row=3, column=1)

        tk.Label(root, text="Balance Amount").grid(row=4, column=0)
        tk.Entry(root, textvariable=self.balance_var).grid(row=4, column=1)

        tk.Button(root, text="Submit Payment", command=self.submit_form).grid(row=5, columnspan=2)

    def submit_form(self):
        if not all([self.first_name_var.get(), self.sur_name_var.get(), self.card_number_var.get(), self.cvv_var.get(),
                    self.balance_var.get()]):
            messagebox.showerror("Error", "All fields are required.")
            return

        if len(self.card_number_var.get()) != 16 or not self.card_number_var.get().isdigit():
            messagebox.showerror("Error", "Invalid card number. It must be 16 digits.")
            return

        if len(self.cvv_var.get()) != 3 or not self.cvv_var.get().isdigit():
            messagebox.showerror("Error", "Invalid CVV. It must be 3 digits.")
            return

        if random.choice([True, False]):
            messagebox.showinfo("Success", "Payment submitted successfully!")
        else:
            messagebox.showerror("Failure", "Payment processing failed. Please try again later.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Payment(root)
    root.mainloop()
