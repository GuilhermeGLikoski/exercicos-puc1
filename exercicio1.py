from datetime import datetime

#pega o ano em que estamos direto do sistema
ano_atual = datetime.now().year
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade =  ano_atual - ano_nascimento
print(f"Sua idade neste ano será ou já é: {idade} anos.")
