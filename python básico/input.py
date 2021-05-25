# ENTRADA DE DADOS EM PYTHON

# a função input SEMPRE RETORNA UMA STRING
# casting = alterar o tipod a variável

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
anoDeNascimento = 2021 - int(idade)     #fazendo casting da idade

print(f'{nome} tem {idade} anos de idade, então ele nasceu em {anoDeNascimento}')

# Definindo o tipo da variavel no input
altura = float(input('Qual a sua altura? '))
print(f'A altura do {nome} eh {altura:.2f}, {type(altura)}')