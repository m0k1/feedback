from sys import stdin

block_size = 65536

def file_size(filename):
    filename.seek(0,2)
    num = filename.tell()
    filename.seek(0,0)
    return num

def cypher(data,key):
    cyphertext = ''.join([chr(ord(x)^ord(y)) for x,y in zip(data,key)])
    return cyphertext

def file_cypher_with_keyfile(inputfilename,outputfilename,keyfilename):
    try:
        openinputfile = open(inputfilename,'r')
        openoutputfile = open(outputfilename,'w')
        openkeyfile = open(keyfilename,'r')
    except:
        return None
    if file_size(openinputfile) > file_size(openkeyfile):
        return False
    cyphertext = ''
    while True:
        data = openinputfile.read(len(block_size))
        if not data:
            break
        pad = openkeyfile.read(len(data))
        cyphertext += cypher(data,pad)
    openoutputfile.write(cyphertext)
    openkeyfile.close()
    openoutputfile.close()
    openinputfile.close()
    return True

def file_cypher_with_looback(inputfilename,outputfilename):
    try:
        openinputfile = open(inputfilename,'r')
        openoutputfile = open(outputfilename,'w')
    except:
        return None
    cyphertext = ''
    while True:
        data = openinputfile.read(block_size)
        if not data:
            break
        pad = stdin.read(len(data))
        cyphertext += cypher(data,pad)
    openoutputfile.write(cyphertext)
    openoutputfile.close()
    openinputfile.close()
    return True

#EOF