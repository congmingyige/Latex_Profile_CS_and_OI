import shutil
import subprocess
from pdf2image import convert_from_path

# Step 1: Copy 'resume-zh_CN.pdf' to '陈冠斌_个人简历_2025年6月毕业_CS.pdf', overwriting if it exists
src_pdf = 'resume-zh_CN.pdf'
dst_pdf = '陈冠斌_个人简历_2025年6月毕业_CS.pdf'

shutil.copyfile(src_pdf, dst_pdf)

# Step 2: Convert each page of the PDF to PNG images
# Ensure you have installed pdf2image and have Poppler installed on your system
images = convert_from_path(dst_pdf)

for i, image in enumerate(images, start=1):
    output_filename = f'陈冠斌_个人简历_2025年6月毕业_CS_Page{i}.png'
    image.save(output_filename, 'PNG')

# Step 3: Execute 'clear_some_personal_informations.py' in the same directory
subprocess.run(['python', 'clear_some_personal_informations.py'])
