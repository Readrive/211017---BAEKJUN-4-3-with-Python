number = int(input("수를 입력하세요"))
n = number
count = 0

while True:
    interger = n // 10
    decimal = n % 10
    plusDecimal = (interger + decimal) % 10
    n = (decimal * 10) + plusDecimal

    count += 1

    if(n == number):
        break

print(count)
