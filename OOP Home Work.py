class Product:
    def __init__(self, name, description, price, size, color):
        self.name = name
        self.description = description
        self.price = price
        self.size = size
        self.color = color
        self.rating = None

    def info(self):
        return f'Product Name : {self.name}, description: {self.description}, size: {self.size}, price is :{self.price}, color :{self.color}, rating: {self.rating}'

    def change_des(self,new_description):
        self.description = new_description
        return self.description

    def new_rating(self, new_rating):
        if 1 <= new_rating <= 10:
            self.rating = new_rating
        else:
            raise ValueError("Rating must be between 1 and 10")
        return self.rating

    def change_price(self, addition , discount):
        self.price = self.price + addition
        self.price = self.price - discount
        return self.price


pants = Product('jeans', 'modern pants 2024', 24 , 'XL', 'blue')
shorts = Product('short', 'very short', 10, 'L', 'blue')

pants.new_rating(6)
shorts.new_rating(9)
pants.change_price(addition=50, discount=0)
shorts.change_price(addition=0, discount= 5)

shorts.change_des('under the knee')
print(shorts.info())
print(pants.info())
print('shorts has 5% discount')