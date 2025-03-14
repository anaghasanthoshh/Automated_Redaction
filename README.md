🔒 PII Redaction Tool for PDFs

Automatically detect and redact personally identifiable information (PII) in PDF documents.
This tool permanently removes sensitive data (names, emails, phone numbers, etc.) while keeping the original document structure intact.

✅ Useful for:
✔ Legal & Compliance Teams (e.g., GDPR, HIPAA compliance)
✔ Businesses Handling Confidential Documents
✔ Developers Automating Document Redaction



Initial installation:
1.pip install all the requirements in requirements.txt

Document Generation steps(for testing):
1.Create a basic html template with place holders for the data(template.html)
2.Now render the data to the template,create html files and then convert them to pdf.
Note:For pdfkit to work,install wkhtmltopdf from
https://wkhtmltopdf.org/downloads.html
