# Anything with image for CTF checklist
### This checklist is useful when encounter an image file in CTF
- Check the file type using `file <filename>`
- Try open the file to see if it's corrupted or not
- use exiftool to find flag in metadata `exiftool <filename> | grep -iE '{.*}'`. Install with `sudo apt install exiftool`
- use strings command to see if there is flag stored in image binary `strings <filename> | grep -iE '{.*}'`
- if the file is PNG try to run test from this website https://www.shanereilly.net/posts/basic_steganography_and_png_files/ to find any steganography
- upload the file here https://stylesuxx.github.io/steganography/ to see if there is any hidden text
- use binwalk to see if there is another file inside the image `binwalk -D=".*" <filename>`
- use stegctfsolver for steganography `python3 stegctfsolver.py <filename>`. Install with `git clone https://github.com/thepaulbenoit/stegctfsolver`
- use stegsolve to see if the flag is stored on the image `stegsolve.jar`. Download JAR file at http://www.caesum.com/handbook/Stegsolve.jar
- use stegoveritas `stegoveritas <filename>`. Install with `pip3 install stegoveritas`
- use stegseek `stegseek --crack <filename>`
- if steganography has passphrase and stegseek cannot find the passphrase, use stegcracker `stegcracker <filename> /usr/share/wordlists/rockyou.txt`. Install with `pip3 install stegcracker`

\#\#most important is to open the image and look at the image. sometimes the hint/clue/answer is in the picture.
