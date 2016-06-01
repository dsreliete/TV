class Televisao():
    """
    Classe Televisão criada em 21/05/16
    """
    
    def __init__(self):
        self.canais = 0
        self.volume = 5
        self.ligada = False

    def ligar(self):
        if self.ligada == False:
            self.ligada = True
            print('TV foi ligada')
        else:
            print('TV já está ligada')

    def desligar(self):
        if self.ligada == True:
            self.ligada = False
            print('TV foi desligada')
        else:
            print('TV já está desligada')

    def mudar_canal(self, canal):
        if self.ligada == True:
            self.canais = canal
            print('canal da TV foi alterado')
        else:
            print('Não é possível mudar canal. A TV está desligada!!!')

    def aumentar_volume(self):
        if self.ligada == True:
            self.volume = self.volume + 6
            print('o volume da tv foi aumentado')
        else:
            print('Não é possível aumentar volume. A TV está desligada!!!')

    def diminuir_volume(self):
        if self.ligada == True:
            self.volume = self.volume - 1
            print('volume da TV foi diminuido')
        else:
            print('Não é possível aumentar volume. A TV está desligada!!!')

    def print(self):
        print('self.ligada = ' + str(self.ligada) + '\n'
              + 'self.canais = ' + str(self.canais) + '\n'
              + 'self.volume = ' + str(self.volume))
        

        
