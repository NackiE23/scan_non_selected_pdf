from io import BytesIO
from PIL import Image
from pdf2image import convert_from_path
import pytesseract


lang = input("Choose language of your pdf[ukr or eng]: ") or "ukr"
pdf_path = input("Write your path to pdf: ")
output_file_name = input("How to name output txt file?(response) ") or "response"

pages = convert_from_path(pdf_path)
output_file = open(f'{output_file_name}.txt', 'w')

for number, page in enumerate(pages, 1):
    print(f"Page {number} is start scanning!")
    with BytesIO() as f:
        page.save(f, format="jpeg")
        f.seek(0)
        img_page = Image.open(f)
        text = pytesseract.image_to_string(img_page, lang=lang)
        output_file.write(text)

output_file.close()
print(f'Program finished successfully! Your result in {output_file_name}.txt')
