### Data Preparation and Cleaning

1. Saved the original `.xls` file as `.csv`
2. Set the file path for processing
3. Wrote the initial data-processing script
4. Ran the script to generate the first cleaned output
5. Identified and verified the correct data types for each column
6. Performed additional cleaning directly inside Google Sheets
7. Added the `RM` prefix to the output values to match the form input format

   ```
   ="RM" & E4
   ```

### Database Setup

8. Created a new MySQL database
9. Created the `sales_records` table with the required columns

### Data Import Workflow

10. Wrote a Python script to import the cleaned CSV file into MySQL
11. Re-downloaded the cleaned CSV from Sheets because some cells were merged and caused import issues
