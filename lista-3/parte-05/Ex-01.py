entrada = int(input())

num = entrada

mult_bin = 1
binario = 0

while num > 0:
    dig_bin = num % 2
    binario += dig_bin*mult_bin

    num = num // 2
    mult_bin = mult_bin*10

print(binario)