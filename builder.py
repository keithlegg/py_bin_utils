#!/usr/bin/python

import struct 




class binary_blob(object):
    def __init_(self):
        pass 

    #def insert(self, input, num, position):

    #def remove(self, num, position):
    
    #def split(self, num, position):


    def int_seq(self, size=1024):
        bdata = []
        for b in range(size):
            bdata.append(b)
        return bdata  

    def dumpfile(self, bdata, filepath, encoding='int'):
        # encoding 'utf-8'
        # arr = bytearray(string, 'utf-8')

        ba = bytearray(bdata)
 
        nf = open(filepath,'wb')
        if encoding=='int':
            nf.write(struct.pack('%sB'%len(ba), *ba))




b = binary_blob()
seq = b.int_seq(100)
b.dumpfile(seq, 'foo.bin')



