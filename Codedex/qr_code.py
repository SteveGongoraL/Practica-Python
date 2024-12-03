#Generar QR Code.

import qrcode

w_link = input("¿Cual link quieres convertir a QR?:\n")
nombre = input("¿Con cual nombre lo quieres guardar?:\n")
qr = qrcode.QRCode(version =1, box_size=5, border=5)

qr.add_data(w_link)
qr.make()

img = qr.make_image(fill_color = "black", back_color = "white")
img.save(nombre+".png")
