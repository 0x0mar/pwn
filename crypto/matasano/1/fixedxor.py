def fixed_xor(buf1, buf2):
    '''Takes two hex-encoded buffers and returns their XOR.'''
    a = buf1.decode('hex')
    b = buf2.decode('hex')
    s = ''
    for i, j in zip(a, b):
        s += chr(ord(i) ^ ord(j))
    return s.encode('hex')

if __name__ == '__main__':
    a = fixed_xor('1c0111001f010100061a024b53535009181c', \
                  '686974207468652062756c6c277320657965')

    print a
    print a == '746865206b696420646f6e277420706c6179'
