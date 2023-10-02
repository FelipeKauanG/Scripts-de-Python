from hashlib import sha512, sha256
print(sha512("abc".encode()).hexdigest())
print(sha256("abc".encode()).hexdigest())
print(2**512)
print(2**256)
