"""
Create a QR code and show it
"""
import qrcode
img = qrcode.make("https://google.com")
img.show()
