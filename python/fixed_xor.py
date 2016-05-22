#
#  Author: Abraham Adberstein
#  Date: May 16, 2016
#

def fixed_xor(b1, b2):
    length = len(b1)
    result = ''
    for i in range(0, length):
        result += str(hex(int(b1[i],16)^int(b2[i],16)) )[2:]

    return result

def main():
    buffer1 = "1c0111001f010100061a024b53535009181c"
    buffer2 = "686974207468652062756c6c277320657965"
    result = fixed_xor(buffer1, buffer2)

    print("buffer1:", buffer1)
    print("buffer2:",buffer2)
    print("result: ", result)

if __name__ == "__main__":
  main()
