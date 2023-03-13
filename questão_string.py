'''5) Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;'''

# Solicitando ao usuário para informar a string
string = input("Digite uma string: ")

# Definindo a variável string_reverse como vazio
string_reverse = ""

# criando um loop para percorrer a variável string a partir do último caracter e inserir os caracteres na variável string_invetida.
for i in range (len(string)-1, -1, -1):
    string_reverse += string[i]

# Retornando a string
print("A string invertida é:", string_reverse)