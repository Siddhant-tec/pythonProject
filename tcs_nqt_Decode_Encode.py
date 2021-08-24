class Encrypt:
    def __init__(self, encode, decode):
        self.encode = encode
        self.decode = decode

    def encoder(self):
        encoded = list()
        for values in encode:
            encoded.append(chr((ord(values)) + 5))
        print(''.join(encoded))

    def decoder(self):
        decoded = list()
        for values2 in decode:
            decoded.append(chr((ord(values2)) - 5))
        print(''.join(decoded))


encode = input()
decode = input()
enc = Encrypt(encode, decode)
enc.encoder()
enc.decoder()
