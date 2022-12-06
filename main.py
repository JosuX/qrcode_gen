import qrcode
data = "https://i.ibb.co/M8cZYKt/yellow.jpg"
img = qrcode.make(data)
img.save('yellowQR.png')
