# for this i have taken geeks for geeks website as a result of qr scan
#save this file name as qr(optional).py(must)
# first  pip install pyqrcode & pip install pypng
# import QR code from pyqrcode package
import pyqrcode
import png
from pyqrcode import QRCode
#string which represents the QR code
s="www.geeksforgeeks.org"

#generate qr code
url=pyqrcode.create(s)

#create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale=9)

#create and save the png file naming "gfgqr.png"
url.png("gfgqr.png", scale=7)
