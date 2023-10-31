from sys import argv
fName = argv[1]
f=open(fName)
enckey = {}
enckey['a'] ='a'
enckey['b'] ='n'
enckey['c'] ='b'
enckey['d'] ='o'
enckey['e'] ='c'
enckey['f'] ='p'
enckey['g'] ='d'
enckey['h'] ='q'
enckey['i'] ='e'
enckey['j'] ='r'
enckey['k'] ='f'
enckey['l'] ='s'
enckey['m'] ='g'
enckey['n'] ='t'
enckey['o'] ='h'
enckey['p'] ='u'
enckey['q'] ='i'
enckey['r'] ='v'
enckey['s'] ='j'
enckey['t'] ='w'
enckey['u'] ='k'
enckey['v'] ='x'
enckey['w'] ='l'
enckey['x'] ='y'
enckey['y'] ='m'
enckey['z'] ='z'
newstring = ""
#enckey = dict(zip(enckey.values(), enckey.keys()))
ef = open("encrypted_"+fName,"w")
Rchar = f.read(1)
while Rchar:
    Rchar = Rchar.lower()
    #transchar = enckey.get(Rchar +"",Rchar +"")
    if Rchar in enckey:
        transchar = enckey[Rchar]
    else:
        transchar = Rchar
    #print(transchar)
    newstring = newstring + transchar
    Rchar = f.read(1)
ef.write(newstring)
ef.close()
