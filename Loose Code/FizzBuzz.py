# Based on the Fizz Buzz Game and coding challenge.
# See https://en.wikipedia.org/wiki/Fizz_buzz

def fizz_buzz(val):
    if val % 5 == 0 and val % 3 == 0:
        return "FizzBuzz"
    elif val % 3 == 0:
        return "Fizz"
    elif val % 5 == 0:
        return "Buzz"
    else:
        return val

output = []

for i in range(101):
    output.append(fizz_buzz(i))

print(output)
