import tkinter as tk
from tkinter import ttk, messagebox
from fpdf import FPDF
import datetime
import os
from PIL import Image, ImageTk
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure


class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'Bill Invoice', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

class BillGeneratorApp:
    def __init__(self, master, mongo_uri, db_name, collection_name, name):
        self.master = master
        self.master.title("Bill Master")
        self.master.geometry("800x600")
        
        current_dir = os.getcwd()
        logo_path = os.path.join(current_dir, 'images/application_logo.png')
        image = Image.open(logo_path)
        logo = ImageTk.PhotoImage(image)
        self.master.iconphoto(False, logo)

        self.name = name
        
        try:
            self.client = MongoClient(mongo_uri)
            self.client.server_info()  # This to raise an exception if connection fails die to Invalid URI
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
        except (ConnectionFailure, OperationFailure) as e:
            print(f"Error connecting to MongoDB: {e}")
            messagebox.showerror("Database Error", "Failed to connect to the database. Please check your connection and try again.")
            self.master.destroy()
            return

        self.bills = []
        self.load_bills()

        self.create_main_page()

    def create_main_page(self):
        self.clear_window()

        ttk.Label(self.master, text=f"Welcome, {self.name}!", font=("Helvetica", 16)).pack(pady=10)

        self.tree = ttk.Treeview(self.master, columns=("Date", "Customer", "Total"), show="headings")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Customer", text="Customer")
        self.tree.heading("Total", text="Total")
        self.tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.populate_bills_table()

        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="View Bill", command=self.view_selected_bill).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Print Bill", command=self.print_selected_bill).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="New Bill", command=self.create_new_bill).pack(side=tk.LEFT, padx=5)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def populate_bills_table(self):
        for bill in self.bills:
            self.tree.insert("", "end", values=(bill['date'], bill['customer_info']['Name'], f"${bill['total_sum']:.2f}"))

    def view_selected_bill(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a bill to view.")
            return

        selected_bill = self.bills[self.tree.index(selected_item[0])]
        self.display_bill(selected_bill, editable=False)

    def print_selected_bill(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a bill to print.")
            return

        selected_bill = self.bills[self.tree.index(selected_item[0])]
        filename = f"bill_{selected_bill['customer_info']['Name'].replace(' ', '_')}.pdf"
        self.generate_beautiful_pdf(selected_bill['customer_info'], selected_bill['products'], selected_bill['total_sum'], filename)
        messagebox.showinfo("Success", f"PDF bill generated: {filename}")
        os.startfile(filename)

    def create_new_bill(self):
        self.display_bill(None, editable=True)

    def display_bill(self, bill=None, editable=True):
        self.clear_window()

        self.customer_frame = ttk.LabelFrame(self.master, text="Customer Information")
        self.customer_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(self.customer_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.customer_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.customer_frame, text="Phone:").grid(row=0, column=2, padx=5, pady=5)
        self.phone_entry = ttk.Entry(self.customer_frame)
        self.phone_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.customer_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = ttk.Entry(self.customer_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        if bill:
            self.name_entry.insert(0, bill['customer_info']['Name'])
            self.phone_entry.insert(0, bill['customer_info']['Phone'])
            self.email_entry.insert(0, bill['customer_info']['Email'])

        self.table_frame = ttk.LabelFrame(self.master, text="Product Table")
        self.table_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(self.table_frame, columns=("Product", "Quantity", "Amount", "Total"), show="headings")
        self.tree.heading("Product", text="Product")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Total", text="Total")
        self.tree.pack(fill="both", expand=True)

        if bill:
            for product in bill['products']:
                self.tree.insert("", "end", values=(product['name'], product['quantity'], f"${product['price']:.2f}", f"${product['total']:.2f}"))

        self.total_frame = ttk.Frame(self.master)
        self.total_frame.pack(padx=10, pady=10, fill="x")

        self.total_label = ttk.Label(self.total_frame, text=f"Total Sum: ${bill['total_sum']:.2f}" if bill else "Total Sum: $0.00")
        self.total_label.pack(side="right")
        
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=10)

        if editable:
            self.product_frame = ttk.LabelFrame(self.master, text="Product Entry")
            self.product_frame.pack(padx=10, pady=10, fill="x")

            ttk.Label(self.product_frame, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
            self.product_entry = ttk.Entry(self.product_frame)
            self.product_entry.grid(row=0, column=1, padx=5, pady=5)

            ttk.Label(self.product_frame, text="Quantity:").grid(row=0, column=2, padx=5, pady=5)
            self.quantity_entry = ttk.Entry(self.product_frame)
            self.quantity_entry.grid(row=0, column=3, padx=5, pady=5)

            ttk.Label(self.product_frame, text="Amount:").grid(row=0, column=4, padx=5, pady=5)
            self.amount_entry = ttk.Entry(self.product_frame)
            self.amount_entry.grid(row=0, column=5, padx=5, pady=5)

            ttk.Button(self.product_frame, text="Add Product", command=self.add_product).grid(row=1, column=2, columnspan=2, pady=10)

            ttk.Button(button_frame, text="Save Bill", command=self.save_bill).pack(side=tk.LEFT, padx=5)
        else:
            for widget in self.customer_frame.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.config(state='readonly')

        ttk.Button(button_frame, text="Back to Main", command=self.create_main_page).pack(side=tk.LEFT, padx=5)

    def add_product(self):
        product = self.product_entry.get()
        quantity = int(self.quantity_entry.get())
        amount = float(self.amount_entry.get())
        total = quantity * amount

        self.tree.insert("", "end", values=(product, quantity, f"${amount:.2f}", f"${total:.2f}"))

        self.update_total()
        self.clear_product_entries()

    def update_total(self):
        total_sum = sum(float(self.tree.item(item)["values"][3][1:]) for item in self.tree.get_children())
        self.total_label.config(text=f"Total Sum: ${total_sum:.2f}")

    def clear_product_entries(self):
        self.product_entry.delete(0, "end")
        self.quantity_entry.delete(0, "end")
        self.amount_entry.delete(0, "end")

    def save_bill(self):
        customer_info = {
            "Name": self.name_entry.get(),
            "Phone": self.phone_entry.get(),
            "Email": self.email_entry.get()
        }

        if not all(customer_info.values()):
            messagebox.showerror("Error", "Please fill in all customer information.")
            return

        products = []
        for item in self.tree.get_children():
            values = self.tree.item(item)["values"]
            products.append({
                "name": values[0],
                "quantity": int(values[1]),
                "price": float(values[2][1:]),
                "total": float(values[3][1:])
            })

        total_sum = sum(product['total'] for product in products)

        bill = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "customer_info": customer_info,
            "products": products,
            "total_sum": total_sum
        }

        try:
            # Insert the bill into MongoDB
            result = self.collection.insert_one(bill)
            bill['_id'] = result.inserted_id  # MongoDB-generated ID to the bill
            self.bills.append(bill)
            messagebox.showinfo("Success", "Bill saved successfully!")
            self.create_main_page()
        except Exception as e:
            print(f"Error saving bill: {e}")
            messagebox.showerror("Error", "Failed to save the bill. Please try again.")

    def generate_beautiful_pdf(self, customer_info, products, total_sum, filename='beautiful_bill.pdf'):
        pdf = PDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("helvetica", size=12)

        pdf.set_fill_color(200, 220, 255)
        pdf.cell(0, 10, "Customer Information", 0, 1, 'L', 1)
        pdf.ln(5)
        for key, value in customer_info.items():
            pdf.cell(40, 10, f"{key}:", 0)
            pdf.cell(0, 10, value, 0, 1)
        pdf.ln(10)

        pdf.set_fill_color(220, 220, 220)
        pdf.cell(0, 10, "Product Details", 0, 1, 'L', 1)
        pdf.ln(5)

        col_width = pdf.w / 4.5
        pdf.set_font("helvetica", 'B', 12)
        pdf.cell(col_width, 10, "Product", 1, 0, 'C')
        pdf.cell(col_width, 10, "Quantity", 1, 0, 'C')
        pdf.cell(col_width, 10, "Unit Price", 1, 0, 'C')
        pdf.cell(col_width, 10, "Total", 1, 1, 'C')

        pdf.set_font("helvetica", size=12)
        for product in products:
            pdf.cell(col_width, 10, product['name'], 1)
            pdf.cell(col_width, 10, str(product['quantity']), 1)
            pdf.cell(col_width, 10, f"${product['price']:.2f}", 1)
            pdf.cell(col_width, 10, f"${product['total']:.2f}", 1, 1)
        pdf.ln(10)
        pdf.set_font("helvetica", 'B', 14)
        pdf.cell(0, 10, f"Total Sum: ${total_sum:.2f}", 0, 1, 'R')

        pdf.ln(20)
        pdf.set_font("helvetica", size=10)
        pdf.cell(0, 10, f"Date: {datetime.date.today().strftime('%B %d, %Y')}", 0, 1)
        pdf.cell(0, 10, f"Invoice Number: INV-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}", 0, 1)

        pdf.output(filename)

    def load_bills(self):
        try:
            cursor = self.collection.find()
            self.bills = list(cursor)
        except Exception as e:
            print(f"Error loading bills: {e}")
            self.bills = []
            messagebox.showwarning("Data Loading Error", "Failed to load existing bills. You can still create new bills.")
