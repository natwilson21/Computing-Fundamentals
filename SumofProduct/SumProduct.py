#Question 2
import math
myList1 = [1,2,3,4,5]
myList2 = [4,8,2,6]

def sumProduct(curList, inMode = 0):
    sum = 0
    product = 1
    if inMode == 0:
        for k in range(0, len(curList)):
            sum = sum + curList[k]
            minVal = min(curList)
        return(f'This is the sum: {sum} \nThis is the minumum: {minVal}')
    else:
        for k in range(0, len(curList)):
            product = product * curList[k]
            maxVal = max(curList)
        return(f'This is the product: {product} \nThis is the maximum: {maxVal}')

print(sumProduct(myList1, 0))
print(sumProduct(myList2, 1))
print(sumProduct(myList2))
