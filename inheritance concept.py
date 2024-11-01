
class Stock:
  Stock_id=1
  Quantity=1
  datetime="2.3.2024"
class product:
         def __init__(self,Stock_id,Quantity,datetime):
             self.Stock_id = Stock_id
             self.Quantity = Quantity
             self.datetime = datetime

         def method(self):
             print("Enter Stock_id:", self.Stock_id)
             print("Enter Quantity:", self.Quantity)
             print("Enter datetime:", self.datetime)

c = product(Stock.Stock_id, Stock.Quantity, Stock.datetime)
c.method()




