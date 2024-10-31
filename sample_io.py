import sys
import struct

with open (sys.argv[1], 'rb') as f:
    #ヘーダー読み込み
    while True:
        line =f.readline()
        print(line)
        if b'end_header' in line:
            break
        if b'vertex ' in line:
            vnum = int(line.split(b' ')[-1]) # 頂点の数
        if b'face ' in line:
            fnum = int(line.split(b' ')[-1]) #面の数
        #頂点を読込み
    for i in range(vnum):
        for j in range(3):
            print( struct.unpack('f',f.read(4))[0],end =' ')
        print("")
    
    #面を読み込み
    for i in range(fnum):
        n = struct.unpack('B',f.read(1))[0]
        for j in range(n):
            print(struct.unpack('i',f.read(4))[0],end=' ')
        print("")    