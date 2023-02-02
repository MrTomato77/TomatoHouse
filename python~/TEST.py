def minInRange(lst, start):
    for i in range(len(lst[start:])):
        minimum = i
        for j in range(i+1, len(lst)):
            if lst[minimum] > lst[j]:
                minimum = j
                return minimum

lst = [1,3,5,4,0,2,3,8]
Answer = minInRange(lst, 2)
print(lst)
print("index :", Answer)