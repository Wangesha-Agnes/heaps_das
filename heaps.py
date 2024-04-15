import heapq
li = [12,10,8,5,4,19,9,3,2,1]
heapq.heapify(li)
print(li)


print (heapq.heappop(li))


heapq.heappush(li, 6)
print(li)

largeElement = heapq.nlargest(1,li)[0]
print(largeElement)