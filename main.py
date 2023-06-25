def getTalk(type="shout"):
    # Мы определяем функции прямо здесь
    def shout(word="да"):
        return word.capitalize() + "!"

    def whisper(word="да"):
        return word.lower() + "...";

    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    else:
        return whisper

talk = getTalk()
print(talk)
print(talk())
print(getTalk("whisper")())


def doSomethingBefore(func):
    print("Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал")
    print(func())

talk = getTalk()
doSomethingBefore(talk)
# выведет:
# Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал
# Да!