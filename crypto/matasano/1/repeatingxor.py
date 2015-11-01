
def rep_xor(mes, key):
    '''Repeated key XOR. Returns the hex-encoded string.'''
    ret = ''
    for a, b in zip(mes, key * (len(mes) / len(key) + 1)):
        ret += chr(ord(a) ^ ord(b))
    return ret.encode('hex')

if __name__ == '__main__':
    mes = "Burning 'em, if you ain't quick and nimble\n" + \
          "I go crazy when I hear a cymbal"
    key = "ICE"
    ciphertext = rep_xor_enc(mes, key)
    cip = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272" + \
          "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    print ciphertext
    print ciphertext == cip
