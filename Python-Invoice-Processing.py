#created by https://github.com/Anna-portfolio

import pdfplumber
import re
import openpyxl

#get paths
pdf_path = "Musterrechnung.pdf"
excel_path = "Rechnung_Daten.xlsx"

#get values from .pdf using regex
with pdfplumber.open(pdf_path) as pdf:
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

kunde_pattern = re.compile(r"Kunde:\s*(.+)")
rechnungsnr_pattern = re.compile(r"Rechnungsnummer:\s*([A-Z0-9/]+)")
faelligkeit_pattern = re.compile(r"Fälligkeitsdatum:\s*([0-9]{2}\.[0-9]{2}\.[0-9]{4})")
gesamt_pattern = re.compile(r"Gesamtbetrag\s+([\d\.\,]+)")
waehrung_pattern = re.compile(r"Währung:\s*([A-Z]+)")

kunde = kunde_pattern.search(text).group(1).strip() if kunde_pattern.search(text) else None
rechnungsnummer = rechnungsnr_pattern.search(text).group(1).strip() if rechnungsnr_pattern.search(text) else None
faelligkeitsdatum = faelligkeit_pattern.search(text).group(1).strip() if faelligkeit_pattern.search(text) else None
gesamtbetrag = gesamt_pattern.search(text).group(1).strip() if gesamt_pattern.search(text) else None
waehrung = waehrung_pattern.search(text).group(1).strip() if waehrung_pattern.search(text) else None

print("Kunde:", kunde)
print("Rechnungsnummer:", rechnungsnummer)
print("Fälligkeitsdatum:", faelligkeitsdatum)
print("Gesamtbetrag:", gesamtbetrag)
print("Währung:", waehrung)

#get .xlsx, create a table and fill in with data
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Rechnungsdaten"

headers = ["Kunde", "Rechnungsnummer", "Fälligkeitsdatum", "Gesamtbetrag", "Währung"]
ws.append(headers)

row = [kunde, rechnungsnummer, faelligkeitsdatum, gesamtbetrag, waehrung]
ws.append(row)


wb.save(excel_path)

print("Data printed to: ", excel_path)