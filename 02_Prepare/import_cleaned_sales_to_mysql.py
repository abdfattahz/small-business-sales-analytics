import pandas as pd
import mysql.connector
from datetime import datetime

# Load your cleaned CSV
df = pd.read_csv(r"\02_Prepare\cleaned_cleaned_data.csv")

# Convert date strings to proper date objects if needed
df['Tarikh'] = pd.to_datetime(df['Tarikh'], dayfirst=True, errors='coerce').dt.date
df['Timestamp'] = pd.to_datetime(df['Timestamp'], dayfirst=True, errors='coerce').dt.date

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='YOUR_PASSWORD_HERE',
    database='iroh_business_db'
)
cursor = conn.cursor()

# Insert data row by row
for _, row in df.iterrows():
    sql = """
        INSERT INTO sales_records (
            timestamp, tarikh, jenis, nama_produk_servis,
            kuantiti_harga, nama_pelanggan,
            lokasi_kawasan, nota_tambahan
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = tuple(None if pd.isna(val) else val for val in (
        row['Timestamp'],
        row['Tarikh'],
        row['Jenis'],
        row['Nama Produk / Servis'],
        row['Kuantiti / Harga'],
        row['Nama Pelanggan'],
        row['Lokasi / Kawasan'],
        row['Nota Tambahan']
    ))

    cursor.execute(sql, values)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("✔ Data successfully imported to MySQL.")
