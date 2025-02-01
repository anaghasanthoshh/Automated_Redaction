import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os
import pdfkit


df=pd.read_csv('data.csv')


#function to generate documents using the data
def html_document_generator():
 # Load Jinja2 Template
 #first lets create html templates
 env = Environment(loader=FileSystemLoader('.'))
 template = env.get_template("template.html")
 global output_dir_html
 output_dir_html = 'generated_html'
 os.makedirs(output_dir_html,exist_ok=True)
# Render HTML with the Data
 for x,y in df.iterrows():
  html_content = template.render(y)
  html_file_path=f"{output_dir_html}/generated_html_{x}.html"
  #Save as html File in output directory
  with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

  #conveting html to pdf
  output_dir_pdf = 'generated_pdf'
  os.makedirs(output_dir_pdf, exist_ok=True)
  pdf_file_path=f"{output_dir_pdf}/generated_pdf_{x}.pdf"
  pdfkit.from_file(html_file_path,pdf_file_path)
  print(f"Document{x} generated successfully!")






