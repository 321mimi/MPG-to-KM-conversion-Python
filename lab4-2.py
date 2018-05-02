# convertGas
# By Michelle Cantin

import math

# The function
def convertGas(conversionType, convert):
    conversion = float((100 * 3.785411784) / (1.609344 * convert))
    conversion = round(conversion,2)
    return conversion

# Prompts
convert = float(input("What is the number to convert? "))
conversionType = int(input("What is the type of conversion? \n0 for MPG to kms, 1 for kms to MPG "))

# Calls the function and prints the result
print(convertGas(conversionType, convert))


