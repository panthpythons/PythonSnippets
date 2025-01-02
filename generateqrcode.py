#Importing the qrcode library
#[pip install qrcode[pil] ]

import qrcode

data = "https://www.youtube.com/@panthpythons"

qr = qrcode.make(data)

qr.save("panthpythons_qr.png")

print("QR is generated successfully")


