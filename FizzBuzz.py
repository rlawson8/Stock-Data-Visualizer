import itertools as itt

f = itt.cycle([""] * 2 + ["Fizz"])
b = itt.cycle([""] * 4 + ["Buzz"])
fb = (fizz + buzz for fizz, buzz in zip(f, b))
result = (word or n for word, n in zip(fb, itt.count(1)))
for i in itt.islice(result, 100):
    print(i)