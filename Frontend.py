import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename
import pandas as pd
from database import init_db, add_assay, get_assays, add_result, get_results

# Initialize the database
init_db()

class AssayApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Assay Management System")

        # Tabs for different sections
        self.tab_control = ttk.Notebook(root)
        self.tab_assays = ttk.Frame(self.tab_control)
        self.tab_results = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_assays, text="Manage Assays")
        self.tab_control.add(self.tab_results, text="Manage Results")
        self.tab_control.pack(expand=1, fill="both")

        # Setup tabs
        self.setup_assay_tab()
        self.setup_results_tab()

    def setup_assay_tab(self):
        # Form to add new assay
        tk.Label(self.tab_assays, text="Name").grid(row=0, column=0)
        tk.Label(self.tab_assays, text="Type").grid(row=1, column=0)
        tk.Label(self.tab_assays, text="Procedure").grid(row=2, column=0)
        tk.Label(self.tab_assays, text="Reagents").grid(row=3, column=0)
        tk.Label(self.tab_assays, text="Expected Outcomes").grid(row=4, column=0)

        self.assay_name_entry = tk.Entry(self.tab_assays)
        self.assay_type_entry = tk.Entry(self.tab_assays)
        self.assay_procedure_entry = tk.Entry(self.tab_assays)
        self.assay_reagents_entry = tk.Entry(self.tab_assays)
        self.assay_outcomes_entry = tk.Entry(self.tab_assays)

        self.assay_name_entry.grid(row=0, column=1)
        self.assay_type_entry.grid(row=1, column=1)
        self.assay_procedure_entry.grid(row=2, column=1)
        self.assay_reagents_entry.grid(row=3, column=1)
        self.assay_outcomes_entry.grid(row=4, column=1)

        tk.Button(self.tab_assays, text="Add Assay", command=self.add_new_assay).grid(row=5, columnspan=2)

        # Display list of assays
        self.assay_listbox = tk.Listbox(self.tab_assays)
        self.assay_listbox.grid(row=6, columnspan=2)

        self.refresh_assay_list()

    def setup_results_tab(self):
        # Form to add new result
        tk.Label(self.tab_results, text="Assay ID").grid(row=0, column=0)
        tk.Label(self.tab_results,text="Measurement").grid(row=1,column=0)