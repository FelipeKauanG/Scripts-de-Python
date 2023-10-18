import hashlib

# Sua senha em texto claro
senha = input("Senha: ")

# Crie um objeto de hash SHA-256
hash_object = hashlib.sha512()

# Converta a senha para bytes (geralmente é necessário em Python 3)
senha_bytes = senha.encode('utf-8')

# Atualize o objeto de hash com a senha em bytes
hash_object.update(senha_bytes)

# Obtenha a representação hexadecimal do hash SHA-256
senha_sha256 = hash_object.hexdigest()

print("Senha SHA-256:", senha_sha256)
