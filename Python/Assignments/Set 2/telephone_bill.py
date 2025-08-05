# finding telephone bill for MR. X
noOfCalls = int(input("Enter total number of calls made : "))
base = 250
if noOfCalls<=100:
    print("Bill : ",base+noOfCalls*0.1)
elif noOfCalls<=200:
    print("Bill : ",base+100*0.1+(noOfCalls-100)*0.3)
else:
    print("Bill : ",base+100*0.1+100*0.3+(noOfCalls-200)*0.5)
