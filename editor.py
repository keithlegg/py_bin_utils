#!/usr/bin/python



class edit_blob(object):
    def __init_(self):
        filebuffer = [] 

    #def insert(self, input, num, position):

    #def remove(self, num, position):

    #def split(self, num, position):

    #def replace(self, byte, repbyte, start, end):
   
    def read_binfile(self, filepath, encoding='int'):
    	pass 

    def dumpfile(self, bdata, filepath, encoding='int'):
        # encoding 'utf-8'
        # arr = bytearray(string, 'utf-8')

        ba = bytearray(bdata)
 
        nf = open(filepath,'wb')
        if encoding=='int':
            nf.write(struct.pack('%sB'%len(ba), *ba))




