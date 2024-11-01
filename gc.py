# import gc
# print("Python garbage collector is enable or not:", gc.isenabled())
#
# gc.disable()
# print("Python garbage collector is enable or not:", gc.isenabled())
# gc.enable()
# print("Python garbage collector is enable or not:", gc.isenabled())
#
#
#
# import gc
# print("Python garbage collector is enable or not : ", gc.isenabled())
#
# gc.disable()
# print(" python garbage collector is enabled or not :", gc.isenabled())
#
# gc.enable()
# print("python garbarge collector is ebabled or not :",gc.isenabled())
#
# import time
#
# class Test:
#
#     def _init_(self):
#         print("object Initilization...")
#
#     def _del_(self):
#         print("peform the destructor operation..")
#
# t1 = Test()
# t1 = None
# time.sleep(5)
# print("End")
# print(t1)

import sys

class Test:

    def _init_(self):
        print("constructure method")


t1 = Test()
t2 = t1
t3 = t1
t4 = t1
print(sys.getrefcount(t1))
