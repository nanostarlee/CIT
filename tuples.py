animals = ("dogs", "cats", "cows", "sheep")
animals = "dogs", "cats", "cows", "sheep"

print(type(animals))


tuple_with_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tuple_with_tuples[0][0]) 
print(tuple_with_tuples[1][1]) 
print(tuple_with_tuples[2][2]) 

my_tuple = (("Python", "C++", "C#"), ("1,5,8"), "Ford", ["Apple", "Banana", "Oranges"])

for item in my_tuple:
    if isinstance(item, tuple) or isinstance(item, list):
        for x in item:
            print(x)
    else:
        print(item)

python = ('P', 'y', 't', 'h', 'o', 'n')

print("" .join(python))
