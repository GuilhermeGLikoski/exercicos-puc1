preco_quilos = float(input("digite o preço do produto(R$): "))
peso_produto = float(input("digite o peso do produto (Kg): "))

valor_venda = preco_quilos * peso_produto

print(f"o preço de venda do produto é R$ {valor_venda:.2f}")
