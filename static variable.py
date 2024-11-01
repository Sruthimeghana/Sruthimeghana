# class Test():
#     x=20
#     def __init__(self):
#         self.y=30
# t = Test()
# t2 = Test()
# print(t.x , t2.y)
# print(t2.y,  t2.x )
# Test.x = 200
# print(t.x)
# t.y = 300
# print(t.x,t.y)
from Tools.scripts.dutree import display


class Test:
    name="sruthi"
    age=25
    course="m.Sc computer science"
    fpercent=79.9
    clgname="SVDC"
    location="kadapa"
    def __init__(self):
        print(self.name)
        print(Test.name)
    def  display(self):
        print(Test.course)
        print(self.clgname)
    def cls_m1(cls):
        print(Test.fpercent)
        print(cls.age)
    def m1(self):
        print(Test.location)
t = Test()
t .display()
t.cls_m1()
t.m1()


