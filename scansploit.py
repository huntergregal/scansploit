#!/usr/bin/python3
import logging
import sys
import argparse
from pystrich.code128 import Code128Encoder
from pystrich.qrcode import QRCodeEncoder
from pystrich.datamatrix import DataMatrixEncoder
from pystrich.ean13 import EAN13Encoder

#ARGS
parser = argparse.ArgumentParser(description="Tool to embed exploits into barcodes.")
#Cusstom outfile
parser.add_argument('-f', '--file', dest='outfile', help='Optional output file name', default=None)
#Choose barcode type from CLI
parser.add_argument('-b', '--barcode', dest='type', help='Use standard barcode type',  default=None)
parser.add_argument('-q', '--qrcode', dest='type', help='Use QRcode type',  default=None)
parser.add_argument('-d', '--datamatrix', help='Use datamatrix type',  default=None)
parser.add_argument('-e', '--ean13', help='Use EAN13 type',  default=None)
#Specify Payload String
parser.add_argument('-p', '--payload', help='Specify a payload string',  default=None)
#parse
args = parser.parse_args()

if __name__ == "__main__":
    
    if not
    choice = input("""
        What type of code would you like to generate? 
        1) Barcode (code128)
        2) QRcode
        3) DataMatrix
        4) EAN13
        Choice: """)

    if choice == "1":
        logging.getLogger("code128").setLevel(logging.DEBUG)
        logging.getLogger("code128").addHandler(logging.StreamHandler(sys.stdout))

        encoded = Code128Encoder(DATA)
        encoded.save("barcode.png")

    elif choice == "2":
        logging.getLogger("qrcode").setLevel(logging.DEBUG)
        logging.getLogger("qrcode").addHandler(logging.StreamHandler(sys.stdout))

        encoded = QRCodeEncoder(DATA)
        encoded.save("qrcode.png", 3)
    
    elif choice == "3":
        logging.getLogger("datamatrix").setLevel(logging.DEBUG)
        logging.getLogger("datamatrix").addHandler(logging.StreamHandler(sys.stdout))

        encoded = DataMatrixEncoder(DATA)
        encoded.save("datamatrix.png")

    elif choice == "4":
        logging.getLogger("ean13").setLevel(logging.DEBUG)
        logging.getLogger("ean13").addHandler(logging.StreamHandler(sys.stdout))

        encoded = DataMatrixEncoder(DATA)
        encoded.save("ean13.png")
