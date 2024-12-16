import qrcode

# Data to encode
data = "I love GFG!"

# Create QR code object
qr = qrcode.QRCode()

# Add data to the QR code
qr.add_data(data)

# Generate the QR code
qr.make()

# Create an image from the QR code
img = qr.make_image()

img.save('mk.png')