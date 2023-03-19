# numbers_set = {1,2,3,3}    #duplicate values are removed
# numbers_set = {1,2,3,4,[5,6]}    #cannot use list in a set
# numbers_set = {1,2,3,4,(5,6)} #tuples are okay to use

#print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}

""" abcd = ""

for word in words_set:
    abcd += word
print(abcd)
 """

""" if "Alpha" in words_set:
    print("Alpha is in set")
else:
    print("Alpha not in set") """

words_set.add("Delta")
words_set.discard("Alpha")
print(words_set)