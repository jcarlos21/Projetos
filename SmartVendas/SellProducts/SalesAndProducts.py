class Product:
    def __init__(self, codProduct, qtdEstoque, typo):
        self.codProduct = codProduct
        self.qtdeEstoque = qtdEstoque
        self.typo = typo
        pass


class Sales(Product):
    def __init__(self, dateSale, codProduct, codSeller):
        self.dateSale = dateSale
        self.codProduct = codProduct
        self.codSeller = codSeller
        pass