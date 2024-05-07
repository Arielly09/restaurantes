class Restaurante:
    def __init__(sef,nome,categoria):
        sef.nome = nome
        sef.categoria = categoria
        sef.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praça','Gurmet')
restaurante_pizza = Restaurante ('Pizza','Italiana')


restaurante_pizza = Restaurante()

restaurantes =[restaurante_pizza,restaurante_praca]

print(vars(restaurante_praca))
print(vars(restaurante_pizza))
