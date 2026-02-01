number = 0

while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)
else:
    print('no longer less than 5')