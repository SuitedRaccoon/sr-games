import random

class Carta:
    def __init__(self, id:int, nome:str) -> None:
        self.id = id
        self.nome = nome

    def exibe_info(self):
        print(f"    Carta:  {self.id}")
        print(f"    ID:     {self.nome}")

#instancias
pedra   = Carta(1, "Pedra")
papel   = Carta(2, "Papel")
tesoura = Carta(3, "Tesoura")

CARTAS = {
    1: 'PEDRA',
    2: 'PAPEL',
    3: 'TESOURA'
}

# tabela de quem ganha de quem: chave vence de valor
VITORIAS = {
    1: 3,  # Pedra (1) vence Tesoura (3)
    2: 1,  # Papel (2) vence Pedra (1)
    3: 2,  # Tesoura (3) vence Papel (2)
}

def compara(c1:Carta, c2:Carta) -> str:
    if c1.id == c2.id: return "Empate!"
    if VITORIAS.get(c1.id) == c2.id: return f"{c1.nome} vence {c2.nome}... Vitória!"
    else: return f"{c2.nome} vence {c1.nome}... Derrota."

def escolha_player() -> int:
    print("1 - PEDRA | 2 - PAPEL | 3 - TESOURA")
    escolha:int = int(input("Digite sua escolha: "))
    return escolha

def escolha_cpu() -> int:
    return random.randint(1, 3)

if __name__ == "__main__":
    carta1 = papel
    carta2 = CARTAS.get(escolha_cpu())
    print(f"A CPU escolheu {carta2}")
    print(compara(carta1, carta1))
    print(compara(carta1, carta2))