class RajuStores():
   gloceries = "rice","blackgrams","redgrams","flour items"
   beauty = "facial creams", "hair growth ","under eye creams "
   clothes= tuple["cotton", "slik ", "banaras","soft slik"]
   juices = "lemon","pineapple","grapes juice", "kiwi juice"
   fwatches_price  = 56.6,78.9,66,90.4
   discount_rates = 50-70
   def __init__(self):
      print(self.gloceries)
      print(RajuStores.discount_rates)
   def display(self):
       print(RajuStores.beauty)
       print(self.discount_rates)
   def cls_name(cls_name):
       print(cls_name.clothes)
       print(RajuStores.discount_rates)
   def static_m1(self):
       print(RajuStores.juices)
   def m2(self):
       print(RajuStores.fwatches_price)



s =RajuStores()
s.display()
s.cls_name()
s.static_m1()
s.m2()



