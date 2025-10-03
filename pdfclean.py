import pdf2image as p2i
import img2pdf as i2p
import piexif
import os
import sys

def pdf_clean(input_file, output_file):
    images = p2i.convert_from_path(input_file, fmt='jpeg', dpi=300)

    clean_image_path = []
    for i, image in enumerate(images):
        filename = f"hashbash{input_file}pdfimgTemp{i}.jpeg"
        if not os.path.isfile(filename):
            image.save(filename, "JPEG")
            piexif.remove(filename)

        clean_image_path.append(filename)

    with open(output_file, 'wb') as file:
        file.write(i2p.convert(clean_image_path))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdfclean.py inputfile.pdf outputfile.pdf")
        sys.exit(1)

        input_pdf = str(sys.argv[1])
        output_pdf = str(sys.argv[2])
        pdf_clean(input_pdf, output_pdf)