# coding:utf-8
import math

angle = 15
while angle<360:
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))
    tan = math.tan(math.radians(angle))

    print("{}°".format(angle))

    print("sin{} = {}".format(angle,round(sin,2)))
    print("cos{} = {}".format(angle,round(cos,2)))
    print("tan{} = {}\n".format(angle,round(tan,2)))
    
    angle += 15
else:
    print("Finish")