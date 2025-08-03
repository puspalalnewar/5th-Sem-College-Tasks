# finding average of three decimal numbers
a = float(input("Please enter num_1 floating-point number: "))
b = float(input("Please enter num_2 floating-point number: "))
c = float(input("Please enter num_3 floating-point number: "))

# a,b,c = input("Enter three numbers seperated by commas : ").split(",")
# a,b,c = float(a),float(b),float(c)
print("Average of {}, {} and {} is : {}".format(a,b,c,(a+b+c)/3))