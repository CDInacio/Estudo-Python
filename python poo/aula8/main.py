from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

produto1 = Produto('biscoito', 3.00)
produto2 = Produto('refrigerante', 8.50)
produto3 = Produto('batata-frita', 12.99)

carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto3)

carrinho.lista_produtos()
print(f'O total deu R$ {carrinho.soma_total()}')

