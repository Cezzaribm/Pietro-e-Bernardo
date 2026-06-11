class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def tomar_dano(valor: int):
        self.vida = self.vida - valor_recebido

    
class Mago(Personagem):
    def __init__(self, nome, vida, mana):
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
    def __init__(self, nome, vida, stamina):
        super().__init__(nome, vida)
        self.stamina = stamina

    def __str__(self):
        return f"Bárbaro: {self.nome}. Vida: {self.vida}. Stamina: {self.stamina}"

    def __add__(self, valor: float):
        return 

    def __sub__(self, valor: float):
        return 

    def __mul__(self, fator: float):
        return

    def __truediv__(self, valor: float):
        return