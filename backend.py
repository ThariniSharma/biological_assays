import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect("assays.db")
    cursor = conn.cursor()
    
    # Create table for assays
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assays (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            procedure TEXT,
            reagents TEXT,
            expected_outcomes TEXT
        )
    """)
    
    # Create table for results
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assay_id INTEGER,
            measurement REAL,
            concentration REAL,
            observations TEXT,
            date TEXT,
            FOREIGN KEY (assay_id) REFERENCES assays(id)
        )
    """)
    
    conn.commit()
    conn.close()

# Add a new assay
def add_assay(name, assay_type, procedure, reagents, expected_outcomes):
    conn = sqlite3.connect("assays.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO assays (name, type, procedure, reagents, expected_outcomes)
        VALUES (?, ?, ?, ?, ?)
    """, (name, assay_type, procedure, reagents, expected_outcomes))
    conn.commit()
    conn.close()

# Get all assays
def get_assays():
    conn = sqlite3.connect("assays.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assays")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Add a new result
def add_result(assay_id, measurement, concentration, observations, date):
    conn = sqlite3.connect("assays.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO results (assay_id, measurement, concentration, observations, date)
        VALUES (?, ?, ?, ?, ?)
    """, (assay_id, measurement, concentration, observations, date))
    conn.commit()
    conn.close()

# Get results for a specific assay
def get_results(assay_id):
    conn = sqlite3.connect("assays.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM results WHERE assay_id=?", (assay_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows