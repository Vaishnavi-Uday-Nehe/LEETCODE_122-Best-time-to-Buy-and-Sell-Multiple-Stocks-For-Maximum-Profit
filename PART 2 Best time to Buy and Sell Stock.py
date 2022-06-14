def stocks(arr,size):
    profit = 0
    for i in range (1,size):
        if arr[i] > arr[i-1]:
            profit += (arr[i] - arr[i-1])
    return profit


arr = [5,2,6,1,4,7,3,6]
size = len(arr)
print("PROFIT IS: ", stocks(arr,size))

#codebyVaishnaviUdayNehe