import singlebytexor as sbx

for l in open('4.txt').readlines():
    s = sbx.decrypt(l.strip())
    if sbx.printable(s[1]):
        print s
