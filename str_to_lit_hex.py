#!/usr/bin/python3

import sys

def hex_lsb(number):
    try:
        # 먼저 숫자를 16진수 문자열로 변환 후 앞에 쓸때 없는 0x 를 제거한다.
        # <feff>254200104122 > <feff>0x3b2f81c4ba > 3b2f81c4ba
        hex_str = number

        # 2자리씩잘라 역순으로 변환 후 합친다.
        # 3b2f81c4ba > ba c4 81 2f 3b > bac4812f3b
        hex_str_lsb = ''.join([hex_str[i-2:i] for i in range(len(hex_str), 0, -2)])

        # 다시 0x 를 붙여 나는 16진수다! 를 알려준다. 그러고 그대로 반환
        #  bac4812f3b > 0xbac4812f3b
        return '0x' + hex_str_lsb

    except ValueError:
        # 에러 처리!
        print('Conversion failed!')


munja = sys.argv[1]

if len(sys.argv) != 2:
    print("Use: ./str+_to_lit_hex.py Text")

long = 0
lit_mun = list(munja)
i = 0
result = ''
num = ''
nums = 0
hex_val = ''

for a in range(len(munja)):
    nums = ord(lit_mun[a])
    hex_val += str(hex(nums))[2:]

print("\n")
for j in range(int(len(hex_val)/16)):
    long = 1
    if (hex_val[i:i+16] != ''):
        num = hex_val[i:i+16]
    result = hex_lsb(num)
    print(result)
    i += 16
if (long == 0):
    num = hex_val[i:i+len(hex_val)]
    result = hex_lsb(num)
    print(result)
print("\n")
