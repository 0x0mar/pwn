import operator
import fixedxor
import re
import string

def try_dec(s, b): # try to decrypt 's' with single-byte 'b'
    data = fixedxor.fixed_xor(s, ("%02x" % b) * len(s))
    return data.decode('hex')

def strip_string(s):
    return ''.join(re.findall('[a-zA-Z]+', s))

def get_letter_freq_order(s):
    freq = {}
    chars = float(len(s))
    for i in range(ord('a'), ord('z') + 1):
        freq[chr(i)] = 0
    for c in s:
        freq[c] += 1
    cipher_freq = {}

    for key, val in freq.items():
        cipher_freq[key] = val / chars * 100.0

    return cipher_freq

def printable(s):
    return all(c in string.printable for c in s)

def freq_score(s):
    if not printable(s):
        return 10**10

    s = strip_string(s.lower()) # preprocess the string for characters only, all in lowercase

    cipher_freq = get_letter_freq_order(s) # get the incidence of each character in percentage

    freqs_eng = {'a': 8.167, 'b':1.492, 'c':2.782, 'd':4.253, 'e':12.702, 'f':2.228,
                 'g':2.015, 'h':6.094, 'i':6.966, 'j':0.153, 'k':0.772, 'l':4.025, 'm':2.406,
                 'n':6.749, 'o':7.507, 'p':1.929, 'q':0.095, 'r':5.987, 's':6.327, 't':9.056,
                 'u':2.758, 'v':0.978, 'w':2.360, 'x':0.150, 'y':1.974, 'z':0.074}

    # difference between actual english and cipher freq: higher is worse
    neg_score = 0
    for key, val in freqs_eng.items():
        neg_score += abs(cipher_freq[key] - val)

    return neg_score

def decrypt(s):
    '''Takes a string of hex-encoded data and attempts to decrypt it.
       The key must be a single byte. Returns the best match (key, decrypted, score).'''
    decrypted = []
    for i in range(0, 256):             # test every possible singular byte as key;
        tmp_dec = try_dec(s, i)  # return the one with the highest frequency
        score = freq_score(tmp_dec)     # score (matches the english alphabet the closest)
        decrypted.append((i, tmp_dec, score))  # (key, decrypted text, score)

    # sort the list
    sorted_dec = sorted(decrypted, key=operator.itemgetter(2))
    #for v in sorted_dec[:20]:
    #    print v

    return sorted_dec[0]

if __name__ == '__main__':
    s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print decrypt(s)
