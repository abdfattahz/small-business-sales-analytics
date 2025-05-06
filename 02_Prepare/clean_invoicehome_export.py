import pandas as pd
import re

# Load the raw CSV data
file_path = r"\02_Prepare\InvoiceHome-1746512515-40477412865608774113549e4a2.csv"
df_raw = pd.read_csv(file_path, dtype={'Customer': str})

def clean_invoice_data(df):
    cleaned_rows = []

    for _, row in df.iterrows():
        # Safely extract fields
        note_field = str(row.get('Number', '') or '').strip() if pd.notna(row['Number']) else ''
        customer_field = str(row.get('Customer', '') or '').strip() if pd.notna(row['Customer']) else ''
        date_field = row.get('Date') if pd.notna(row.get('Date')) else ''
        total_field = row.get('Total') if pd.notna(row.get('Total')) else ''

        # Determine if customer is a name or phone number
        phone_pattern = re.compile(r'^\+?60\s?\d{1,2}[-\s]?\d{3,4}[-\s]?\d{4}$|^01\d{1}-?\d{7,8}$')
        if phone_pattern.match(customer_field):
            nama_pelanggan = customer_field
        elif customer_field:
            nama_pelanggan = customer_field
        else:
            nama_pelanggan = ''

        # Append cleaned row
        cleaned_rows.append({
            'Tarikh': date_field,
            'Jenis': '',
            'Nama Produk / Servis': '',
            'Kuantiti / Harga': total_field,
            'Nama Pelanggan': nama_pelanggan,
            'Lokasi / Kawasan': '',
            'Nota Tambahan': note_field
        })

    return pd.DataFrame(cleaned_rows)

# Clean and export
cleaned_df = clean_invoice_data(df_raw)
cleaned_df.to_csv(r'\02_Prepare\cleaned_data.csv', index=False)
print("✔ Cleaned CSV saved successfully.")
