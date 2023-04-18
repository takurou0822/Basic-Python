import string
import sys


alfa = string.ascii_lowercase
Alfa = string.ascii_uppercase


atai = [0]*26

eigo_morau = sys.stdin.read()

for i in eigo_morau:
    for m in range(26):
        if i == alfa[m] or i == Alfa[m]:
            atai[m] += 1

for z in range(26):
    print("{} : {}".format(alfa[z], atai[z]))