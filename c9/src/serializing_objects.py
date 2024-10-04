import pickle

some_data = [
    "a list", "containing", 5, "items",
    {"including": ["str", "int", "dict"]}
    ]

with open("pickled_list", 'wb') as file:
    pickle.dump(some_data, file)
