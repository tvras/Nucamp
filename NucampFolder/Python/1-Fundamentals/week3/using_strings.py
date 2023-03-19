
my_string = "alpha"

multiline_string = '''Bravo
charlie'''
print(my_string)
print(multiline_string)


print(my_string[0], my_string[3])


print(my_string[0:3])
print(my_string[:2])
print(my_string[2:])


for _ in my_string:
    print(_)


print("pha" in my_string)
print("z" not in my_string) 