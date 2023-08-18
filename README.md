# wav-encoder
This script can encode file into wav file as noise and decode it back
# Pros
• Fast\
• Quality
# Cons
• Non secure\
• The script does not completely mask the file, but adds it to the audio as noise
# Encoder
```
$ python encoder.py -h
usage: encoder.py [-h] -r ORIGINAL [-m MERGE] -o OUTPUT

Hide data into wav file

options:
  -h, --help            show this help message and exit
  -r ORIGINAL, --original ORIGINAL
                        Original file that contains data
  -m MERGE, --merge MERGE
                        File to merge encoded file with
                        (Optional)
  -o OUTPUT, --output OUTPUT
                        Output file
```
\You can encode any file into wav like this:\
```$ python encoder.py --original image.png --output encoded.wav```\
There's file before encoding:\
![Github Logo](https://raw.githubusercontent.com/mishpro-programm/wav-encoder/main/assets/image.png)
\
And there's after decoding:\
![Decoded Image](https://raw.githubusercontent.com/mishpro-programm/wav-encoder/main/assets/decoded.png)
\
As you can see, the images are same\
This is audio, generated by encoder: 
[Audio](https://github.com/mishpro-programm/wav-encoder/raw/main/assets/encoded.wav)
# Decoder
```
$ python decoder.py -h
usage: decoder.py [-h] -r ORIGINAL -o OUTPUT               
options:
  -h, --help            show this help message and exit
  -r ORIGINAL, --original ORIGINAL
                Encrypted file
  -o OUTPUT, --output OUTPUT
                Output data file
```
