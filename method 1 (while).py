from time import time


duplicate = []
count = 0
count2 = 0
while(count<1_000):
    while(count2<5):
        duplicate.append(count)
        count2+=1
    count+=1
    count2 = 0


start = time()


i = 0
while i < len(duplicate):
    j = i + 1
    while j < len(duplicate):
        if duplicate[i] == duplicate[j]:
            del duplicate[j]
        else:
            j += 1
    i += 1


end = time()


print((end-start)*1000, " ms")
