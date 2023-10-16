import pikepdf
import PyPDF2
from PyPDF2 import PdfReader
import io 
from PIL import Image 
import fitz  # PyMuPDF 

def remove_password_from_pdf(file_path, password):
    pdf = pikepdf.open(file_path, password=password)
    pdf.save("decrypted pdf1.pdf")

remove_password_from_pdf('C:/Users/Rohan  Dapurkar/Desktop/New folder (2)/Data Extraction/ICIC Statement.pdf',password='loke1808')


# Open the PDF file
pdf_file = fitz.open('C:/Users/Rohan  Dapurkar/Desktop/New folder (2)/Data Extraction/decrypted pdf1.pdf')
len_pdf = len(pdf_file)
for page_index in range(len_pdf):
            # get the page itself
                print(type(page_index))
                print(page_index)
                page = pdf_file[page_index]
                image_list = page.get_images()
                # printing number of images found in this page
                if image_list:
                    print(
                        f"[+] Found {len(image_list)} images in page {page_index}"
                        )
                else:
                    print("[!] No images found on page", page_index)
                for image_index, img in enumerate(page.get_images(), start=1):
                    # get the XREF of the image
                    xref = img[0]
                    # extract the image bytes
                    base_image = pdf_file.extract_image(xref)
                    image_bytes = base_image["image"]
                    # get the image extension
                    image_ext = base_image["ext"]
                    # load it to PIL
                    image = Image.open(io.BytesIO(image_bytes))

# save it to local disk
                    file_name = f"image{page_index+1}_{image_index}.{image_ext}"


                    image.save(open(file_name, "wb"))  
                    
# Open the PDF file
pdf_file_path = 'C:/Users/Rohan  Dapurkar/Desktop/New folder (2)/Data Extraction/decrypted pdf1.pdf'
pdf_file = open(pdf_file_path, 'rb')
len_pdf = len(pdf_file)

# creating a pdf reader object 
reader = PdfReader(pdf_file_path) 

# printing number of pages in pdf file 
print(len(reader.pages)) 

# getting a specific page from the pdf file 
page = reader.pages[0] 


# extracting text from page 
text = page.extract_text() 
print(text) 
text_file_path = 'file 3.txt'
with open(text_file_path, 'w') as text_file:
    text_file.write(text) 

