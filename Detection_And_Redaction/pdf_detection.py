import os
import fitz  # PyMuPDF (for digital PDFs)
import pytesseract  # OCR for scanned PDFs in image format
from pdf2image import convert_from_path  # Converts PDF pages to images for OCR
from PIL import Image  # Image processing for OCR

file_path='../Data/generated_pdf/'
doc_list=os.listdir(file_path)

class TextExtraction():
    def __init__(self,path):
        self.path=path
        self.extracted_text =""
    def text_extraction(self):
        #path=os.path.join(file_path,doc_list[0])
        doc=fitz.open(self.path)

        for page_num in range(len(doc)):
            page=doc[page_num]
            text=page.get_text() #pymupdf function to get text
            if text.strip():
                self.extracted_text+=text+'\n'
            else:
                images=convert_from_path(self.path,first_page=page_num+1,last_page=page_num+1)
                ocr_text = pytesseract.image_to_string(images[0])
                self.extracted_text += ocr_text + '\n'
            '''
            num_page+1 because, mupdf process page from 0 to n whereas for 
            pdf2image,page starts from 1.Hence the adjustment.Also last_page also 
            is num_page+1 becuase, we want to process only 1 page at a time.Hence only the 
            cureent page is converted.'''


        return self.extracted_text


if __name__=="__main__" :
    path = os.path.join(file_path, doc_list[0])
    extractor=TextExtraction(path)
    print(extractor.text_extraction())













