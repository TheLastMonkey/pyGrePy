from pygrepy import pygrepy

rex="qwerty.+"
path="~/rockyou.txt"
ops="-E"

my_list=pygrepy(ops,rex,path)
for i in my_list:
    print(i)