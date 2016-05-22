#
#  Author: Abraham Adberstein
#  Date: May 16, 2016
#

from xor_cipher import xor_cipher
import sys

def get_score(text):
    text = text[1].lower()

    frequency = { 'a': 8.167, 'c': 2.782, 'b': 1.492, 'e': 12.702, 'd': 4.253, 'g': 2.015, 'f': 2.228, 'i': 6.966,
                  'h': 6.094, 'k': 0.772, 'j': 0.153, 'm': 2.406, 'l': 4.025, 'o': 7.507, 'n': 6.749, 'q': 0.095,
                  'p': 1.929, 's': 6.327, 'r': 5.987, 'u': 2.758, 't': 9.056, 'w': 2.361, 'v': 0.978, 'y': 1.974,
                  'x': 0.15,  'z': 0.074}

    frequencyTest = {}
    score = 0

    for key in frequency.keys():
        frequencyTest[key] = float(text.count(key) / len(text))

    for key in frequency.keys():
        num = frequency[key] - frequencyTest[key]
        if (num > 0):
            score += num
        if (num < 0):
            score += abs(num)

    return score

def detect(filename):
    with open(filename, 'r') as p:
        lines = p.readlines()

    scores = []
    totalLines = []

    for line in lines:
        line = line.strip()
        for x in xor_cipher(line):
            totalLines.append(x)

    index = 0

    for text in totalLines:
        score = (index, get_score(text))
        scores.append(score)
        index += 1


    scores = sorted(scores, key=lambda x : x[1] )

    for i in range(0, 100):
        res = scores[i]
        line = totalLines[res[0]]
        print("Score:",res[1], "Character:",line[0], line[1])



def main():
    filename = "detect.txt"
    detect(filename)

if __name__ == "__main__":
    main()
