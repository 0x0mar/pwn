import base64
import operator
import hackercodecs
import singlebytexor as sbx
import repeatingxor as rx

def hamming_d(x, y):
    x = x.encode('bin')
    y = y.encode('bin')
    dist = 0
    for i, j in zip(x, y):
        if i != j:
            dist += 1
    return dist

def break_xor(cip):
    e_distances = []
    for KEYSIZE in range(2, 41):
        # 3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second
        #    KEYSIZE worth of bytes, and find the distance between them. Normalize this
        #    this result by dividing by KEYSIZE.
        edit_dist_acc = 0
        NUM_AVG = 15
        for i in range(0, NUM_AVG):
            edit_dist_acc += hamming_d(cip[KEYSIZE*2*i:KEYSIZE*(2*i + 1)],
                                   cip[KEYSIZE*(2*i + 1):KEYSIZE*2*(i+1)])
        avg_edit_dist = (edit_dist_acc) / float(NUM_AVG)
        norm_e_dist = avg_edit_dist / float(KEYSIZE)
        e_distances.append((KEYSIZE, norm_e_dist))
    # 4. The KEYSIZE with the smallest normalized edit distance is probably the key.
    #    You could proceed perhaps with the smallest 2-3 KEYSIZE values.
    sorted_dist = sorted(e_distances, key=operator.itemgetter(1))
    #**DEBUG**
    #for i in sorted_dist:
    #    print i

    for KEYSIZE, norm_edit_dist in sorted_dist[:1]:
        # 5. Now that you probably know the KEYSIZE: break the ciphertext into blocks
        #    of KEYSIZE length. Now transpose the blocks: make a block that is the first
        #    byte of each block, and block that is the second bytes, and so on.
        block_cip = ['' for i in range(0, KEYSIZE)]
        for index, char in enumerate(cip):
            block_cip[index % KEYSIZE] += char
        # 7. Solve each block as if it was single-character XOR.
        key = ''
        for block in block_cip:
            key += chr(sbx.decrypt(block.encode('hex'))[0])
        print "GUESSED KEY:\n " + key
        print "MESSAGE:\n" + rx.rep_xor(cip, key).decode('hex')

if __name__ == '__main__':
    # read in the file
    cip = open('6.txt').read().replace('\r', '').replace('\n', '').strip()
    cip = base64.b64decode(cip)

    break_xor(cip)

