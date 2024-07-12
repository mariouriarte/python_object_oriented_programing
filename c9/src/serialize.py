import pickle

some_data = [
    "a list", "containing", 5, "items",
    {"including": ["str", "int", "dict"]}
]
with open("pickled_list", 'wb') as file:
    pickle.dump(some_data, file)

with open("pickled_list", 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
