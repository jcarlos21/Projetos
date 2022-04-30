class Product:
    def __init__(self, codProduct, qtdStock):
        self.codProduct = codProduct
        self.qtdStock = qtdStock
        pass


class Sales(Product):
    def __init__(self, dateSale, codProduct, codSeller):
        self.dateSale = dateSale
        self.codProduct = codProduct
        self.codSeller = codSeller
        pass
