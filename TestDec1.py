def person(name="Вася"):
    return name.capitalize() + "!"
print(person())

scream = person
print(scream() + "!!")

del person
try:
    print(person())
except NameError as e:
    print(e)
print(scream())