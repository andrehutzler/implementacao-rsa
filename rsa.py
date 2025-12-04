from math import gcd

def eh_primo(n: int) -> bool:
    """Retorna True se n for primo, False caso contrário (versão simples)."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = int(n ** 0.5) + 1
    for divisor in range(3, limite, 2):
        if n % divisor == 0:
            return False
    return True

def gerar_primos(inicio: int, fim: int):
    """Gera todos os números primos no intervalo [inicio, fim]."""
    primos = []
    for numero in range(inicio, fim + 1):
        if eh_primo(numero):
            primos.append(numero)
    return primos

def ler_primo(nome_variavel: str) -> int:
    """
    Fica em loop até o usuário digitar um número primo.
    Se o usuário digitar 'ls', lista vários números primos entre 2 e 1000.
    """
    while True:
        entrada = input(
            f"Digite um número PRIMO para {nome_variavel} "
            f"(ou 'ls' para listar primos de 2 até 1000): "
        ).strip().lower()

        if entrada == "ls":
            primos = gerar_primos(2, 1000)
            print(f"\nPrimos entre 2 e 1000 (total: {len(primos)}):")
            for i, p in enumerate(primos, start=1):
                print(f"{p:5}", end=" ")
                if i % 15 == 0:  # quebra linha a cada 15 números
                    print()
            print("\n")
            continue  # volta a pedir o valor de p ou q

        try:
            valor = int(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'ls'.\n")
            continue

        if eh_primo(valor):
            print(f"{nome_variavel} = {valor} é primo!\n")
            return valor
        else:
            print(f"{nome_variavel} = {valor} NÃO é primo. Tente novamente.\n")

def encontrar_d(e: int, phi: int) -> int:
    """
    Encontra d tal que (e * d) % phi == 1.
    Versão bem simples, força bruta.
    """
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    raise ValueError("Não foi possível encontrar d. Verifique e e phi.")

# ------------- ENTRADA DE p e q (COM LOOP + 'ls') -------------

p = ler_primo("p")
q = ler_primo("q")

# ------------- CÁLCULO DE n E phi(n) -------------

n = p * q
phi = (p - 1) * (q - 1)

print(f"p = {p}, q = {q}")
print(f"n  = p * q     = {n}")
print(f"phi(n)        = {phi}")

# ------------- LISTAGEM DE e (COPRIMOS COM phi) -------------

maior_primo = max(p, q)
limite_e = min(maior_primo, 1000)  # não passa de 1000

es_disponiveis = []
for e in range(2, limite_e + 1):   # entre 2 e limite_e
    if gcd(e, phi) == 1:
        es_disponiveis.append(e)

print(f"\nMaior primo entre p e q: {maior_primo}")
print(f"Valores de e possíveis (coprimos de phi(n)) entre 2 e {limite_e}:")
print(es_disponiveis)
print(f"Total de valores possíveis para e nesse intervalo: {len(es_disponiveis)}")

# ------------- USUÁRIO ESCOLHE UM e -------------

while True:
    try:
        e_escolhido = int(input("\nEscolha um valor para e dentre os mostrados acima: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    if e_escolhido in es_disponiveis:
        print(f"e escolhido = {e_escolhido}")
        break
    else:
        print("Esse valor de e NÃO está na lista de valores possíveis. Tente novamente.")

# ------------- CALCULAR d -------------

d = encontrar_d(e_escolhido, phi)
print(f"\nValor de d encontrado: {d}")
print(f"Verificação: (e * d) % phi = {(e_escolhido * d) % phi} (tem que ser 1)")

# ------------- MOSTRAR CHAVES -------------

print("\n--- CHAVES RSA ---")
print(f"Chave pública  (e, n) = ({e_escolhido}, {n})")
print(f"Chave privada  (d, n) = ({d}, {n})")

# ------------- TESTE SIMPLES DE CRIPTOGRAFIA -------------

while True:
    try:
        mensagem = int(input(f"\nDigite uma mensagem (número inteiro entre 0 e {n-1}) para testar a criptografia: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    if 0 <= mensagem < n:
        break
    else:
        print(f"A mensagem precisa estar entre 0 e {n-1}. Tente novamente.")

cifra = pow(mensagem, e_escolhido, n)
mensagem_decifrada = pow(cifra, d, n)

print("\n--- TESTE DE CRIPTOGRAFIA ---")
print(f"Mensagem original  = {mensagem}")
print(f"Mensagem cifrada   = {cifra}")
print(f"Mensagem decifrada = {mensagem_decifrada}")

if mensagem == mensagem_decifrada:
    print("\nSucesso! A implementação básica do RSA está funcionando.")
else:
    print("\nAlgo deu errado, a mensagem decifrada é diferente da original.")
