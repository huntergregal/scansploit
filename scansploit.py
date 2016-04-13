#!/usr/bin/python3
import logging
import sys
import argparse
from pystrich.code128 import Code128Encoder
from pystrich.qrcode import QRCodeEncoder
from pystrich.datamatrix import DataMatrixEncoder
from pystrich.ean13 import EAN13Encoder

parser = argparse.ArgumentParser(description="Tool to embed exploits into barcodes.")

parser.add_argument('-f', '--file', dest='outfile', help='Output file name', required=True)
parser.add_argument('-v', '--verbose', dest='verbose', help='Optional: verbose mode', action='store_true', default=False)
parser.add_argument('-t', '--type', dest='type', help='Specify barcode encoding type (default: code128)', choices=["code128", "qrcode", "dmatrix", "ean13"], default="code128")


ptype = parser.add_mutually_exclusive_group(required=True)
ptype.add_argument('-ps', '--pstring', help='Specify payload string', type=str)
ptype.add_argument('-pf', '--pfile', help='Specify a payload file', type=argparse.FileType('r'))

args = parser.parse_args()
	
def code128(payload):
	if args.verbose:
		logging.getLogger("code128").setLevel(logging.DEBUG)
		logging.getLogger("code128").addHandler(logging.StreamHandler(sys.stdout))

	encoded = Code128Encoder(payload)
	encoded.save(args.outfile)

def qrcode(payload):
	if args.verbose:
		logging.getLogger("qrcode").setLevel(logging.DEBUG)
		logging.getLogger("qrcode").addHandler(logging.StreamHandler(sys.stdout))

	encoded = QRCodeEncoder(payload)
	encoded.save(args.outfile, 3)

def dmatrix(payload): 
	if args.verbose:
		logging.getLogger("datamatrix").setLevel(logging.DEBUG)
		logging.getLogger("datamatrix").addHandler(logging.StreamHandler(sys.stdout))

	encoded = DataMatrixEncoder(payload)
	encoded.save(args.outfile)

def ean13(payload):
	if args.verbose:
		logging.getLogger("ean13").setLevel(logging.DEBUG)
		logging.getLogger("ean13").addHandler(logging.StreamHandler(sys.stdout))

	encoded = DataMatrixEncoder(payload)
	encoded.save(args.outfile)

if __name__ == "__main__":
	if args.pstring:
		payload = args.pstring
	elif args.pfile:
		pfile = args.pfile
		try:
			payload = pfile.read()
		except:
			print("Payload data not ASCII! QUITTING")
			exit()

	if args.type == "code128":
		code128(payload)
	elif args.type == "qrcode":
		qrcode(payload)
	elif args.type == "dmatrix":
		dmatrix(payload)
	elif args.type == "ean13":
		ean13(payload)
	print("Barcode Payload Generated!")
