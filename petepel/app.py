import random

class Carta:
    def __init__(self, id:int, nome:str) -> None:
        self.id = id
        self.nome = nome

    def exibe_info(self):
        print(f"    Carta:  {self.id}")
        print(f"    ID:     {self.nome}")

#instancias
CARTAS = {1: Carta(1, "Pedra"), 
          2: Carta(2, "Papel"), 
          3: Carta(3, "Tesoura")}

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

def escolha_player() -> Carta:
    print("1 - PEDRA | 2 - PAPEL | 3 - TESOURA")
    escolha:int = int(input("Digite sua escolha: "))
    return CARTAS[escolha]

def escolha_cpu() -> Carta:
    return CARTAS[random.randint(1, 3)]

def main() -> None:
    carta1:Carta = escolha_player()
    carta2:Carta = escolha_cpu()
    print(f"\nVocê escolheu {carta1.nome}")
    print(f"A CPU escolheu {carta2.nome}\n\n")
    print(compara(carta1, carta2))

if __name__ == "__main__":
    main()