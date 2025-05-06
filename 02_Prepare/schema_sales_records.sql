-- Create database
CREATE DATABASE iroh_business_db;
USE iroh_business_db;

-- Create sales_records tables
CREATE TABLE sales_records(
	id INT AUTO_INCREMENT PRIMARY KEY,
	timestamp DATE,
    tarikh DATE,
	jenis VARCHAR(50),
	nama_produk_servis VARCHAR(255),
	kuantiti_harga DECIMAL(10,2),
	nama_pelanggan VARCHAR(100),
	lokasi_kawasan VARCHAR(100),
	nota_tambahan TEXT
);

SELECT *
FROM sales_records;