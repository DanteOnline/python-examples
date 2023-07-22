def get_names():
    tmp_names = []
    names = ['leo', 'pavel', 'kate']
    for name in names:
        tmp_names.append(name)
        print(tmp_names)
        yield name.title()


# for name in get_names():
#     print(name)

result = get_names()
print(next(result))
print(next(result))
print(next(result))