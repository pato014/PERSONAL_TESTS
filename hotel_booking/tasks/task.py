import pandas
from pdf_code import generate_invoice

df = pandas.read_csv("articles.csv", dtype={"id": str})


class Product:
    def __init__(self, product_id):
        self.product_id = product_id
        self.name = df.loc[df["id"] == self.product_id, "name"].squeeze()

    def buy(self):
        in_stock = df.loc[df["id"] == self.product_id, "in stock"].squeeze()
        df.loc[df["id"] == self.product_id, "in stock"] = in_stock - 1
        df.to_csv("articles.csv", index=False)

    def in_stock(self):
        availibility = df.loc[df["id"] == self.product_id, "in stock"].squeeze()
        if availibility > 0:
            return True
        else:
            return False


class Invoice:
    def __init__(self, product_id):
        self.product_id = product_id

    def generate_pdf(self):
        article = df.loc[df["id"] == self.product_id, "name"].squeeze()
        price = df.loc[df["id"] == self.product_id, "price"].squeeze()
        generate_invoice(article, price)


print(df)
product_id = input("please enter product id: ")
product = Product(product_id)
if product.in_stock():
    product.buy()
    invoice = Invoice(product_id)
    invoice.generate_pdf()
else:
    print("not in stock")
