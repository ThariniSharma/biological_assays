# biological_assays
---

# *Assay Management System*  
A digital platform for managing chemical, biochemical, and biological assays, designed to simplify experiment tracking, data visualization, and reporting for researchers and laboratory technicians.

---

## *Key Features*  
✅ *Assay Management*  
- Add assays with details like name, type (e.g., Enzyme Assay), procedure, reagents, and expected outcomes.  
- Categorize assays into types for easy organization.  

✅ *Results Tracking*  
- Log experimental results (measurements, concentrations, observations).  
- Automatically track results over time.  

✅ *Data Visualization*  
- View results in tabular format (charts can be added later).  
- Compare multiple trials or assays.  

✅ *Notes & Observations*  
- Add detailed notes and anomalies during experiments.  

✅ *Export Data*  
- Export assay records and results to *CSV* for further analysis.  

---

## *Technologies Used*  
- *Backend*: Python + SQLite (for data storage).  
- *Frontend*: Tkinter (GUI toolkit for Python).  
- *Export*: Pandas (for CSV generation).  

---

## *How to Run*  
1. *Install Python* (if not installed):  
   - Download from [python.org](https://python.org).  
   - Ensure *"Add Python to PATH"* is checked during installation.  

2. *Install Dependencies*:  
   bash
   pip install pandas
   

3. *Run the Application*:  
   bash
   python main.py
   

---

## *Usage*  
1. *Add Assays*:  
   - Navigate to the "Manage Assays" tab.  
   - Fill in assay details (name, type, procedure, etc.).  
   - Click "Add Assay".  

2. *Log Results*:  
   - Go to the "Manage Results" tab.  
   - Enter the assay ID, measurements, and observations.  
   - Click "Add Result".  

3. *Export Data*:  
   - Click "Export to CSV" to save results for analysis.  

---

## *Next Steps*  
- Add *charts/graphs* for visualizing trends (using Matplotlib).  
- Implement *search/filter* functionality for assays.  
- Enable *multi-user support* with login authentication.  

---

## *Contribute*  
Feel free to fork this repository and submit pull requests!  

---
