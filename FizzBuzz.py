import itertools as itt

isFizz = itt.cycle([""] * 2 + ["Fizz"])
isBuzz = itt.cycle([""] * 4 + ["Buzz"])
isFizzBuzz = (fizz + buzz for fizz, buzz in zip(isFizz, isBuzz))
result = (word or n for word, n in zip(isFizzBuzz, itt.count(1)))
for i in itt.islice(result, 100):
    print(i)