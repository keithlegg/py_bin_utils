#!/usr/bin/python

import struct 




class bin_blob(object):
    def __init_(self):
        pass 

    
    #def insert(self, input, num, position):

    #def remove(self, num, position):
    
    #def split(self, num, position):


    def int_seq(self, start=0, size=1024):
        bdata = []
        if start==0:
            for b in range(size):
                bdata.append(b)
        else:
            for b in range(size):
                bdata.append(b)

        return bdata  

    def dumpfile(self, bdata, filepath, encoding='int'):
        
        # optional encoding ('utf-8',etc)
        #arr = bytearray(string, 'utf-8')
        
        # optional header 

        ba = bytearray(bdata)
 
        nf = open(filepath,'wb')
        if encoding=='int':
            nf.write(struct.pack('%sB'%len(ba), *ba))





def test(filename):
    b = bin_blob()
    seq = b.int_seq(100)
    b.dumpfile(seq, filename)



test('foo.bin')