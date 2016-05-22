#
#  Author: Abraham Adberstein
#  Date: May 16, 2016
#

import string
from fixed_xor import fixed_xor

def hex_to_ascii(hexString):
    length = len(hexString)
    groups = int(length / 2)
    extra = length % 2
    asciiString = ""

    for i in range(0, groups):
        pair = hexString[length-i*2-2:length-i*2]
        asciiString += chr(int(pair, 16))

    return asciiString[::-1]

def xor_cipher(hexString):
    #33-126
    lines = []

    singleAsciiCharacters = [chr(c) for c in range(33,126) ]
    length = len(hexString)

    for i in singleAsciiCharacters:
        buff = ( length * str(hex(ord(i))[2:] ) )[:length]
        if (ord(i) >= 97 and ord(i) <= 102):
            buff = (length * str(i))[:length]
        res = fixed_xor(hexString, buff)
        pair = (i, hex_to_ascii(res) )
        lines.append(pair)

    return lines


def main():
    hexString = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print(hexString)
    print(xor_cipher(hexString))

if __name__ == "__main__":
    main()
