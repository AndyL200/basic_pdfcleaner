import pdf2image as p2i
import img2pdf as i2p
import piexif

def pdf_clean(input_file, output_file):
    images = p2i.convert_from_path(input_file, fmt='jpeg', dpi=600)

    clean_image_path = []
    for i, image in enumerate(images):
        filename = f"hashbash{i}pdfimgTemp{i}.jpeg"
        image.save(filename, "JPEG")

        piexif.remove(filename)

        clean_image_path.append(filename)

    with open(output_file, 'wb') as file:
        file.write(i2p.convert(clean_image_path))
