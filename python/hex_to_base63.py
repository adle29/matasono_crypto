#
#  Author: Abraham Adberstein
#  Date: May 16, 2016
#

base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1','2', '3', '4','5','6','7','8','9','+', '\\']

def hex_to_base64(hexString):
    #hexString to binary string
    binDic = {
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'a': "1010",
        'b': "1011",
        'c': "1100",
        'd': "1101",
        'e': "1110",
        'f': "1111"
    }

    binaryString = ''.join([ binDic[c] for c in hexString ])
    length = len(binaryString)

    #take every 6 bits
    base64String = ''
    groups = int(length/6)
    extra = length%6

    #convert every six bits to int and then correlate to base64 characters
    for i in range(0, groups):
        section = binaryString[length-i*6-6:length-i*6]
        base64String += base64[ int(section, 2) ]

    if (extra>0):
        base64String += base64[ int(binaryString[:extra], 2) ]

    return base64String[::-1]

def main():
    hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hexString)
    result = hex_to_base64(hexString)
    print(result)


if __name__ == '__main__':
    main()
