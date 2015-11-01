import singlebytexor as sbx

for l in open('4.txt').readlines():
    # try to decrypt every single 'ciphertext'
    s = sbx.decrypt(l.strip())

    # if it yields an interesting (i.e. printable) result, display it.
    if sbx.printable(s[1]):
        print s
