# Data Structures and Sequences

# Tuples
tup = (4, 5, 6)
print(tup)

# In many contexts, the parentheses can be omitted:
tup = 4, 5, 6
print(tup)

# You can convert any sequence or iterator to a tuple by invoking tuple:
print(tuple([4, 0, 2]))
tup = tuple('string')
print(tup)

# Elements can be accessed with square brackets [] as with most other sequence types:
print(tup[0])

# Creating a tuple of tuples:
nested_tup = (4, 5, 6), (7, 8)
print(nested_tup)

# Accessing elements in nested tuples:
print(nested_tup[0])
print(nested_tup[1])

# While the objects stored in a tuple may be mutable themselves, once the tuple is created it’s not possible to modify which object is stored in each slot:
tup = tuple(['foo', [1, 2], True])
# tup[2] = False  # This would give Error

# If an object inside a tuple is mutable, such as a list, you can modify it in place:
tup[1].append(3)
print(tup)

# You can concatenate tuples using the + operator to produce longer tuples:
print((4, None, 'foo') + (6, 0) + ('bar',))

# Multiplying a tuple by an integer, as with lists, has the effect of concatenating that many copies of the tuple:
print(('foo', 'bar') * 4)

# Unpacking tuples
tup = (4, 5, 6)
a, b, c = tup
print(b)

# Even sequences with nested tuples can be unpacked:
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
print(d)

# Using this functionality you can easily swap variable names:
a, b = 1, 2
print(a)
print(b)
b, a = a, b
print(a)
print(b)

# A common use of variable unpacking is iterating over sequences of tuples or lists:
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}')

# There are some situations where you may want to “pluck” a few elements from the beginning of a tuple:
values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a)
print(b)
print(rest)

# Tuple methods
a = (1, 2, 2, 2, 3, 4, 2)
print(a.count(2))

# Lists
a_list = [2, 3, 7, None]
tup = ("foo", "bar", "baz")
b_list = list(tup)
print(b_list)
b_list[1] = "peekaboo"
print(b_list)

# Adding and removing elements
b_list.append("dwarf")
print(b_list)

b_list.insert(1, "red")
print(b_list)

print(b_list.pop(2))
print(b_list)

b_list.append("foo")
print(b_list)
b_list.remove("foo")
print(b_list)

print("dwarf" in b_list)

# Concatenating and combining lists
print([4, None, "foo"] + [7, 8, (2, 3)])
x = [4, None, "foo"]
x.extend([7, 8, (2, 3)])
print(x)

# Sorting
a = [7, 2, 5, 1, 3]
a.sort()
print(a)

b = ["saw", "small", "He", "foxes", "six"]
b.sort(key=len)
print(b)

# Slicing
seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[1:5])
seq[3:5] = [6, 3]
print(seq)

print(seq[:5])
print(seq[3:])

print(seq[-4:])
print(seq[-6:-2])

print(seq[::2])

print(seq[::-1])

# Built-in Sequence Functions

# Enumerate
some_list = ["foo", "bar", "baz"]
for i, value in enumerate(some_list):
    print(i, value)

mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
print(mapping)

# Sorted
print(sorted([7, 1, 2, 6, 0, 3, 2]))
print(sorted("horse race"))

# Zip
seq1 = ["foo", "bar", "baz"]
seq2 = ["one", "two", "three"]
print(list(zip(seq1, seq2)))

print(list(zip(seq1, seq2, range(3))))

pitchers = [("Nolan", "Ryan"), ("Roger", "Clemens"), ("Schilling", "Curt")]
first_names, last_names = zip(*pitchers)
print(first_names)
print(last_names)

# Dict
empty_dict = {}
print(empty_dict)

mapping = dict(zip(range(5), reversed(range(5))))
print(mapping)

d1 = {"a": "some value", "b": [1, 2, 3, 4]}
print(d1)
d1[7] = "an integer"
print(d1)
print(d1["b"])

print("b" in d1)

d1[5] = "some value"
print(d1)
del d1[5]
print(d1)
ret = d1.pop("a")
print(ret)
print(d1)

print(list(d1.keys()))
print(list(d1.values()))

d1.update({"b": "foo", "c": 12})
print(d1)

mapping = dict(zip(range(5), reversed(range(5))))
print(mapping)

