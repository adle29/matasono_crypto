
from fixed_xor import fixed_xor
from xor_cipher import hex_to_ascii

def repeated_xor(stringsArray, key):
    #get key as hex
    singleKeyHex = ''.join(['%02x'%(ord(c)) for c in key])
    cipher_lines = []
    print("text: ")
    for string in stringsArray:
        string = ''.join([str(hex(ord(c)))[2:] for c in string])
        #prepare buffer
        length = len(string)
        buff = ( length * singleKeyHex )[:length]
        print(string)

        #xor hexString and buffer
        res = fixed_xor(string, buff)
        cipher_lines.append(res)

    return cipher_lines

def main():
    stringsArray = ["Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"]
    key = "ICE"
    res = repeated_xor(stringsArray, key)
    print("key: ", key)
    print("result: ")
    for line in res:
        print(line)

if __name__ == "__main__":
    main()
