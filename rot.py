def rot(plain, n):
    ct = ''
    for k in plain.lower():
        if k not in 'abcdefghijklmnopqrstuvwxyz':
            ct += k
        else:
            ct += chr((ord(k)-97 + n) % 26 + 97)
    return ct
