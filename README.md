# Small Business Sales Analytics & Data System (WIP)

This repository documents a real-world data project for a small family-run business in rural Terengganu, Malaysia. The business sells viral food products, kuih raya, doorgifts and services such as lawn mowing and wedding catering.

The original goal was to analyse sales and customer behaviour. However, the business mainly tracks activity using **notebooks and WhatsApp chats**, with no structured database.

Because of this, the project naturally split into two parts:

1. **Analytics project (Ask → Prepare → Process)** - cleaning and structuring whatever historical data exists (from an app called InvoiceHome)
2. **System design (POS + inventory + invoicing)** - designing a simple data system so the business can collect better data going forward

> **Privacy note:**  
> All actual business data (CSV/XLS exports, customer info, real sales) is **not** included in this repo
> Only scripts, schema and documentation are shared

---

## What this project shows (for DA / DE roles)

**Data Analyst skills**

- Framing business questions:
  - Best-selling products and services  
  - Most frequent / repeat customers  
  - Seasonal / monthly sales trends  
  - Product profitability  
  - Geographic demand for lawn mowing services
- Understanding messy source systems (notebooks, WhatsApp, a basic invoice app)
- Planning data collection and analysis steps

**Data Engineer / Analytics Engineer skills**

- Designing a relational schema for sales data (`schema_sales_records.sql`)
- Cleaning and reshaping exported invoice data using **Python + pandas**:
  - Normalising customer names / phone numbers  
  - Parsing unstructured notes into structured fields  
  - Creating a consistent CSV ready for database import   
- Loading cleaned sales data into **MySQL** from Python (`import_cleaned_sales_to_mysql.py`)
- Documenting the real-world constraints that block analysis and motivate building a proper POS / inventory / invoicing system

---

## Tech Stack

- **Python** - data cleaning, parsing and DB loading (pandas, mysql-connector)
- **Excel / Google Sheets** - initial manual data exports and checks
- **MySQL** - database schema and storage for cleaned sales records
- **Git & GitHub** - version control and documentation

---

## Repository structure

```text
01_Ask/
  project_brief.md          # business summary, problem statement, goals
  business_questions.md     # key questions for analysis
  data_sources.md           # current data sources (notebooks, WhatsApp, etc)

02_Prepare/
    clean_invoicehome_export.py        # main cleaning script for InvoiceHome CSV exports 
    invoice_notes_parser_experiment.py # experimental parser for unstructured notes (product type, location, etc)
    dev_log.md                         # simple step log (xls → csv → sheet cleaning → DB setup → import)
