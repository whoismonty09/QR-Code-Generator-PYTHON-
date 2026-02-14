import qrcode
print("QR Code Generator developed by Monty")
data = input("Enter text or URL: ")

qr = qrcode.make(data)

qr.save("qrcode.png")

print("QR code generated successfully")
