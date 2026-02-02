from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
import os

png = os.path.join('assets','sample_social_qr_short.png')
pdf = os.path.join('assets','sample_social_qr_short.pdf')

if not os.path.exists(png):
    raise SystemExit('PNG not found: ' + png)

# Create a PDF with page size matching the image pixels (points)
from PIL import Image
img = Image.open(png)
w, h = img.size
c = canvas.Canvas(pdf, pagesize=(w, h))
# draw image at origin to fill page
c.drawImage(png, 0, 0, width=w, height=h)
c.showPage()
c.save()
print('WROTE', pdf)
