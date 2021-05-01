def age_assignment(*args, **kwargs):
    data = {}
    for letter, age in kwargs.items():
        for name in args:
            if name not in data:
                data[name] = {}
            if name.startswith(letter):
                data[name] = age
    return data


print(age_assignment("Peter", "George", G=26, P=19))