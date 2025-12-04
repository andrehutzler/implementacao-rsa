# Valores primos escolhidos 
p = 11
q = 13

# Módulo n = p * q
n = p * q

# phi(n) = (p - 1) * (q - 1)
phi = (p - 1) * (q - 1)

# e tem que ser coprimo de phi(n)
e = 7

print("p =", p)
print("q =", q)
print("n (modulo) =", n)
print("phi(n) =", phi)
print("e (expoente publico) =", e)

# Encontrar d tal que: (e * d) % phi == 1
# Ou seja, d é o inverso multiplicativo de e módulo phi(n)
d = None
for candidato_d in range(1, phi):
    if (e * candidato_d) % phi == 1:
        d = candidato_d
        break

print("d (expoente privado) =", d)

# Só pra garantir que achamos o d certo:
print("e * d mod phi(n) =", (e * d) % phi)  # tem que dar 1

# Vamos testar agora:

# Escolhemos uma mensagem M em forma de número, com 0 <= M < n
mensagem_original = 9

# Criptografia: c = m^e mod n
cifra = pow(mensagem_original, e, n)

# Decriptação: m' = c^d mod n
mensagem_decifrada = pow(cifra, d, n)

print("Mensagem original =", mensagem_original)
print("Mensagem cifrada  =", cifra)
print("Mensagem decifrada =", mensagem_decifrada)

