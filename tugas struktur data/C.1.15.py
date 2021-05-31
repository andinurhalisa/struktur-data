from typing import List

def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)

data1 = [4, 87, 23, 44, 1]
data2 = [4, 9, 4, 2, 15, 27]

print(areDistinct(data1))
print(areDistinct(data2))
