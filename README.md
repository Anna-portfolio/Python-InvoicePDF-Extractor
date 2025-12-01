# Python-InvoicePDF-Extractor
created by Anna Dudek @Anna-portfolio<br><br>
A Python script that extracts structured data from German invoices (PDF). The script uses pdfplumber for text extraction and regex patterns to identify key fields:<br><br>

Customer (Kunde)<br>
Invoice number (Rechnungsnummer)<br>
Due date (Fälligkeitsdatum)<br>
Currency (Währung)<br>
Total amount (Gesamtbetrag)<br><br>

Extracted values are automatically exported to an Excel file using openpyxl.<br>
The solution supports German invoice formats with typical European number and date notations (e.g., 6.545,00 for amounts, 07.05.2025 for dates).
