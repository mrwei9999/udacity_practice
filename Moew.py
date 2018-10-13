#PYTHON
print("數線上線段排列順序為:\n x -> y -> z")
x1 = int(input("x1"))
x2 = int(input("x2"))
y1 = int(input("y1"))
y2 = int(input("y2"))
z1 = int(input("z1"))
z2 = int(input("z2"))
if x2 >= y1:
     One = (y2 - x1)
     if y2 >= z1:
          Two = One + (z2 - y2)
elif x2 >= z1:
     Two = (z2 - x1)
elif not(x2 >= y1) and not(y2 >= z1) and not(x2 >= z1):
     Two = (x2 - x1) + (y2 - y1)+ (z2 - z1)
print(Two)
