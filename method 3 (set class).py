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




duplicate = list(set(duplicate))


end = time()


print((end-start)*1000, " ms")
