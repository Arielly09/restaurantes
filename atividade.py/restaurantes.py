class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome}  |  {restaurante.categororia}  |  {restaurante.ativo}')


restaurante_praca = Restaurante('Praça','Gurmet')
restaurante_pizza = Restaurante ('Pizza','Italiana')

Restaurante.listar_restaurantes()

