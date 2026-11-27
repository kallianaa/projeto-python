# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯


class Caneta:
    def __init__(self, cor):
        self.__cor = cor  # atributo privado
        self._cor_tampa = None  # atributo protegido

    @property
    def cor(self):  # getter
        print("Executando o getter...")
        return self.__cor

    @cor.setter
    def cor(self, nova_cor):  # setter
        print("Executando o setter...")
        self.__cor = nova_cor

    @property
    def cor_tampa(self):  # getter
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, nova_cor_tampa):  # setter
        print("Executando o setter da cor da tampa...")
        self._cor_tampa = nova_cor_tampa

caneta = Caneta("Azul")
print(caneta.cor)  # chama o getter
caneta.cor_tampa = "Vermelho"  # chama o setter
print(caneta.cor)  # chama o getter
print(caneta.cor_tampa)  # chama o getter