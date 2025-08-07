# Compare two lists of numbers display "perfect match" if all the elements match, otherwise diplaly the number of mismatches
list_1 = [1, 2, 3, 4]
list_2 = [1,2, 5, 4]
zip_obj = zip(list_1, list_2)

count = 0
mis_match = True

for ele_1, ele_2 in zip_obj :
    if(ele_1 != ele_2) :
        count += 1
        mis_match = False

if mis_match : 
    print("Perfect Match")
else :
    print("No of mismatches : " , count)
