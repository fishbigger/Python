def toRoman(num):
    decimals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X','IX', 'V', 'IV', 'I']
    result = ''
    for i in range(0, len(decimals)):
        while(num % decimals[i] < num):
            result = str(result) + romans[i]
            num -= decimals[i]
    return(result)
def fromRoman(let):
    decimals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X','IX', 'V', 'IV', 'I']
    result = 0
    return(result)
print(fromRoman('IX'))
