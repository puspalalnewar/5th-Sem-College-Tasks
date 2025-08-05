#finding area, perimeter of rectangle
# a,b = input("Enter height and breadth of the rectangle (seperated by commas) : ").split(",")
# a,b = float(a),float(b)
# print("Area : {}\nPerimeter : {}".format((a*b),2*(a+b)))

a,b = input("Enter height and breadth of a rectangle (seperated by commas) : ").split(",")
a, b = float(a), float(b)
print(f"Area : {a*b}\nPermimeter : {2 *(a*b)}")