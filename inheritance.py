class Product:
    def __init__(self,title,price):
     self.title=title
     self.price=price
    def apply_discount(self,percent):
     discount=self.price*percent/100
     self.price-=discount
milk=Product("Milk",200)
milk.apply_discount(10)

print(milk.price)


class Product:
    def __init__(self,title,price):
      self.title=title
      self.price=price
    def apply_discount(self,percent):
      discount=self.price*percent/100
      self.price-=discount
class Ebook(Product):
 def __init__(self, title, price,pages):
        super().__init__(title, price)
        self.pages=pages
book=Ebook("Python",45.98,878)
book.apply_discount(50)
print(book.price)



class Product:
    def __init__(self,title,price):
      self.title=title
      self.price=price
    def apply_discount(self,percent):
      discount=self.price*percent/100
      self.price-=discount
class Ebook(Product):
 def __init__(self, title, price,pages):
        super().__init__(title, price)
        self.pages=pages
class Cart:
   def __init__(self):
      self.products=[]
      def add_product(self,product):
         self.products.append(product)
         def total_products(self):
            return len(self.products)
         def subtotal(self):
            total=0
            for product in self.products:
               total+=product.price
               return total
            cart=Cart()
            cart.add_product(Product("banana",56.667))
            cart.add_product(Product("milk",5.67))
            cart.add_product(Ebook("Python",77.67))
            print(cart.subtotal())

