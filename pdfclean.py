import pdf2image as p2i
import img2pdf as i2p
import piexif
import os
import sys

def pdf_clean(input_file, output_file):
    #if(os.path.isfile("cleaned/" + output_file)):
        #return
    images = p2i.convert_from_path(input_file, fmt='jpeg', dpi=100)
    ifile = os.path.basename(input_file)
    ofile = os.path.basename(output_file)
    clean_image_path = []
    for i, image in enumerate(images):
        output_path = os.path.join("hash", "hashbash")
        
        file_temp = f"{ifile}pdfimgTemp{i}.jpeg"
        file_path = os.path.join(output_path, file_temp)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        image.save(file_path, "JPEG")
        piexif.remove(file_path)

        clean_image_path.append(file_path)
        print("cleaning...")
    fin_path = os.path.join("cleaned", ofile)
    os.makedirs("cleaned", exist_ok=True)
    with open(fin_path, "wb") as file:
        file.write(i2p.convert(clean_image_path))
    return
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdfclean.py input output")
        sys.exit(1)
        
    input_pdf = str(sys.argv[1])
    output_pdf = str(sys.argv[2])
    pdf_clean(input_pdf, output_pdf)
