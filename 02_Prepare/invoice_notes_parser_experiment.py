import pandas as pd
import re

# Load the raw CSV data
file_path = r'\02_Prepare\InvoiceHome-1746512515-40477412865608774113549e4a2.csv'
df_raw = pd.read_csv(file_path)

# Step-by-step cleaning script
def clean_invoice_data(df):
    # Step 1: Collect cleaned rows in a list instead of concatenating
    cleaned_rows = []

    for _, row in df.iterrows():
        note_field = str(row['Number'])

        # 1. Extract date
        tarikh = row['Date'] if pd.notna(row['Date']) else None

        # 2. Set default values
        jenis = 'Servis'  # default guess
        nama_item = ''
        kuantiti = 1
        harga = row['Total'] if pd.notna(row['Total']) else None
        nama_pelanggan = ''
        lokasi = ''
        nota = note_field.strip()

        # 3. Identify known keywords in note field
        if 'Doorgift' in note_field:
            nama_item = 'Doorgift'
            jenis = 'Produk'
        elif 'Makan Beradap' in note_field:
            nama_item = 'Makan Beradap'
        elif 'Potong Rumput' in note_field:
            nama_item = 'Potong Rumput'
        elif 'COD' in note_field:
            nota += ' (COD info)'

        # 4. Try to extract name
        name_match = re.search(r'(?i)nama[:\s]*([A-Za-z\s]+)', note_field)
        if name_match:
            nama_pelanggan = name_match.group(1).strip()
        else:
            phone_match = re.search(r'(\+?60\s?\d{1,2}[-\s]?\d{3,4}[-\s]?\d{4})', note_field)
            if phone_match:
                nama_pelanggan = phone_match.group(0).strip()

        # 5. Extract location
        location_match = re.search(r'(?i)kampung\s+[A-Za-z\s]+', note_field)
        if location_match:
            lokasi = location_match.group(0).strip()

        # 6. Add cleaned row to the list
        cleaned_rows.append({
            'tarikh': tarikh,
            'jenis': jenis,
            'nama_item': nama_item,
            'kuantiti': kuantiti,
            'harga': harga,
            'nama_pelanggan': nama_pelanggan,
            'lokasi': lokasi,
            'nota': nota
        })

    # Step 2: Convert the list to a DataFrame
    cleaned = pd.DataFrame(cleaned_rows)
    return cleaned

cleaned_df = clean_invoice_data(df_raw)

# Export the cleaned data to CSV
cleaned_df.to_csv(r'\02_Prepare\cleaned_data.csv', index=False)
print("✔ Cleaned CSV saved successfully.")
