#!/usr/bin/python3
import sys, os

def get():
    code = ''

    f = open("dump.txt", 'r')

    for line in f:
        if(line[0:1] == " "):
            code += line[10:32]
        if(line[17:18] == "<"):
            code = code.split()
            code = ''.join(code)
            result = [code[i:i+2] for i in range(0, len(code), 2)]
            print(r"\x" + r"\x".join(result))
            print("\n")
            code = ''
        print(line)
    f.close()

if len(sys.argv) != 2:
    print("Use: shellcode Filename or -h")
    sys.exit()

file_path = sys.argv[1]

os.system("objdump -d " + file_path + "> dump.txt")
get()
