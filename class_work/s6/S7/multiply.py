def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


def multiplier_creator(const):
    def inner(n):
        answer = n * const
        return answer
        return multiplier_creator(answer)


doubler = multiplier_creator(2)

print(doubler())
