from app import app
app.run(debug=True, host='0.0.0.0', port=80)


import math
def circle(radius):
    circum = 2 * math.pi * radius
    area =  math.pi * radius ** 2
    return area,circum

a, c = circle(3)
print("Area is " ,round(a))
print("Circumference is ",c)