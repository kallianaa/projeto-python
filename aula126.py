# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if not self.filmando:
            print(f'A câmera {self.nome} começou a filmar.')
            self.filmando = True
        else:
            print(f'A câmera {self.nome} já está filmando.')

    def parar_filmar(self):
        if self.filmando:
            print(f'A câmera {self.nome} parou de filmar.')
            self.filmando = False
            return True
        else:
            print(f'A câmera {self.nome} não está filmando.')
            return False

    def fotografando(self):
        if self.filmando:
            print(f'A câmera {self.nome} esta fotografando.')
            self.filmando = False
        elif self.parar_filmar():
            print(f'A câmera {self.nome} parou de filmar.')
            self.filmando = False
        else:
            print(f'A câmera {self.nome} não está fotografando.')

# Criando uma instância da classe Camera
camera1 = Camera('Canon')
camera1.filmar()  # A câmera Canon começou a filmar.
camera1.filmar()  # A câmera Canon já está filmando.
camera1.parar_filmar()  # A câmera Canon parou de filmar.
camera1.fotografando()  # A câmera Canon não está fotografando.