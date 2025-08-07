# Input a list of strings and convert each of them into upper case using map and lambda function

l = ["abc", " xyz"]

ans = map((lambda x : x.upper()), l)

print(tuple(ans))