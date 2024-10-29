# Dictionaries
my_dict = {"Ринат": 2006, "Денис": 2000, "Константин": 1998}
print(my_dict)
print(my_dict["Ринат"])
print(my_dict.get("Алексей"))
my_dict.update({"Дарья": 2007, "Яна": 2006})
print(my_dict.pop("Денис"))
print(my_dict)
# Sets
my_set = {2, 3, "str", False, 0.0, 3}
print(my_set)
my_set.add(("int", 5))
my_set.remove(2)
print(my_set)