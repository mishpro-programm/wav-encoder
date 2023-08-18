from ctypes import Structure, c_char, c_short, c_int
import argparse
import base64

class wav_header(Structure):
    _fields_ = [
        ("chunk_id", c_char * 4),
        ("chunk_size", c_int),
        ("format", c_char * 4),
        ("subchunk1_id", c_char * 4),
        ("subchunk1_size", c_int),
        ("audio_format", c_short),
        ("num_channels", c_short),
        ("sample_rate", c_int),
        ("byterate", c_int),
        ("block_align", c_short),
        ("bits_per_sample", c_short),
        ("subchunk2_id", c_char * 4),
        ("subchunk2_size", c_int)
    ]
parser = argparse.ArgumentParser(description="Hide data into wav file")
parser.add_argument("-r", "--original", help="Original file that contains data", type=argparse.FileType('rb'), required=True)
parser.add_argument("-m", "--merge", help="File to merge encoded file with (Optional)", type=argparse.FileType('rb'), required=False)
parser.add_argument("-o", "--output", help="Output file", type=argparse.FileType('wb'), required=True)
args = parser.parse_args()
origdata = open(args.original.name, 'rb').read()
encoded_data = base64.b16encode(origdata)
encoded_len = len(encoded_data)
if args.merge:
    wavfile = args.merge
    wav = wav_header.from_buffer_copy(wavfile.read(44))
    wav_data = wavfile.read()
    wav_len = len(wav_data)
    encoded_data += b"\x00" * (encoded_len % wav.block_align)
    encoded_len = len(encoded_data)
    wav.chunk_size = 36 + encoded_len + wav_len + 4
    wav.subchunk2_size = wav_len + encoded_len + 4
    encoded_file = args.output
    encoded_file.write(bytes(wav))
    encoded_file.write(bytes(c_int(encoded_len)))
    encoded_file.write(encoded_data)
    encoded_file.write(wav_data)
    wavfile.close()
    encoded_file.close()
else:
    encoded_data += b"\x00" * (encoded_len % 2)
    encoded_len = len(encoded_data)
    wav = wav_header()
    wav.chunk_id = b"RIFF"
    wav.chunk_size = 40 + encoded_len
    wav.format = b"WAVE"
    wav.subchunk1_id = b"fmt "
    wav.subchunk1_size = 16
    wav.audio_format = 1
    wav.num_channels = 1
    wav.sample_rate = 44100
    wav.byterate = wav.sample_rate * 2
    wav.block_align = 2
    wav.bits_per_sample = wav.block_align * 8
    wav.subchunk2_id = b"data"
    wav.subchunk2_size = encoded_len + 4
    encoded_file = args.output
    encoded_file.write(bytes(wav))
    encoded_file.write(bytes(c_int(encoded_len)))
    encoded_file.write(encoded_data)
    encoded_file.close()
