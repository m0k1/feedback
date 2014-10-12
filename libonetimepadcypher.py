blocksize = 65536

def filesize(filename):
    filename.seek(0,2)
    num = filename.tell()
    filename.seek(0,0)
    return num
def cypher(data,key):
    cyphertext = ''.join([chr(ord(x)^ord(y)) for x,y in zip(data,key)])
    return cyphertext
def filecypher_keyfile(inputfilename,outputfilename,keyfilename):
    try:
        inputfile = open(inputfilename,'r')
        outputfile = open(outputfilename,'w')
        keyfile = open(keyfilename,'r')
    except:
        return False
    if filesize(inputfile) > filesize(keyfile):
        return False
    cyphertext = ''
    while True:
        data = inputfile.read(len(blocksize))
        if not data:
            break
        pad = keyfile.read(len(data))
        cyphertext += cypher(data,pad)
    outputfile.write(cyphertext)
    keyfile.close()
    outputfile.close()
    inputfile.close()
    return True
