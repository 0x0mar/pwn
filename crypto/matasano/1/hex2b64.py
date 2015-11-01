import base64

def hex2b64(s):
    return base64.b64encode(s.decode('hex'))

if __name__ == '__main__':
   print hex2b64('49276d206b696c6c696e6720796f757220627261696e206c'  + \
                 '696b65206120706f69736f6e6f7573206d757368726f6f6d')
