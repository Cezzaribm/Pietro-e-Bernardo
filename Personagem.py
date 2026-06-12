class Personagem:
    def __init__(self, nome: str, vida: int):
        self.nome = nome
        self.vida = vida

    def tomar_dano(valor: int):
        self.vida = self.vida - valor_recebido


class Mago(Personagem):
    def __init__(self, nome: str, vida: int, mana: float):
        super().__init__(nome, vida)
        self.mana = mana
    
    def __str__():
        return f"Mago: {self.nome}. Vida: {self.vida}. Mana: {self.mana}."

    def __add__(self, valor: float):
        return self.mana + valor

    def __sub__(self, valor: float):
        if (self.mana - valor) > 0: 
            return self.mana - valor
        elif (self.mana - valor) < 0:
            return f"Mana não pode ser menor que 0"

    def __mul__(self, fator: float):
        return self.mana * fator

    def __truediv__(self, valor: float):
        return self.mana / valor


class Barbaro(Personagem):
    def __init__(self, nome: str, vida: int, stamina: float):
        super().__init__(nome, vida)
        self.stamina = stamina
        self.furia = True

    def __str__(self):
        return f"Bárbaro: {self.nome}. Vida: {self.vida}. Stamina: {self.stamina}"

    def __add__(self, valor: float):
        if not self.furia:
            return self.stamina + valor
        else: 
            (self.stamina + valor) * self.furia

    def __sub__(self, valor: float):      
        self.stamina - valor
        if self.stamina < 0:
            if not self.furia:
                self.furia = True
                self.stamina = 5.0
            else:
                self.stamina = 0.0
        return self.stamina

    def __mul__(self, fator: float):
        self.stamina * fator
        if self.furia:
            self.vida += 5.0 
        return self.stamina

    def __truediv__(self, valor: float):
        return self.stamina / valor

tipo = input("Mago ou Bárbaro?")
nome = input("Nome do seu personagem:")
vida = int(input("Vida do personagem:"))

print("1: Tomar poção simples")
print("2: Tomar poção especial")
print("3: Ataque básico")
print("4: Ataque básico")
opcao = input("O que você deseja fazer")

if tipo == Mago:
    if opcao == 1: 
        print(mana )

