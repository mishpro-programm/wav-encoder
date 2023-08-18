import argparse
import base64
import struct

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--original", help="Encrypted file", type=argparse.FileType('rb'), required=True)
parser.add_argument("-o", "--output", help="Output data file", type=argparse.FileType('wb'), required=True)
args = parser.parse_args()

args.original.read(44)
data_len = struct.unpack("i", args.original.read(4))[0]
data = args.original.read(data_len)
decrypted_data = base64.b16decode(data)
args.output.write(decrypted_data)
args.output.close()
