# Write a program to conver phone number to word

# phone_number = int(input("Enter your phone number : "))
ph_num=input("Enter a phone number: ")

dictionary = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "ninr",
    "0" : "zero",
}
    
print("The phone number in words is: ",{ph_num})

for i in range(len(ph_num)) :
    for j in dictionary :
        if j == ph_num[i]:
            print(dictionary[j], end = " ")
    