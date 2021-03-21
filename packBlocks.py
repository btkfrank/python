def canFit(blocks, w, h):
    temp = w
    for block in blocks:
        temp -= block
        if temp < 0:
            h -= 1
            temp = w - block
    return h > 0
    
def packBlocks(blocks, height):
    l, r = min(blocks), sum(blocks)
    while l + 1 < r:
        mid = (l + r) // 2
        if canFit(blocks, mid, height):
            r = mid
        else:
            l = mid
    if canFit(blocks, l, height):
        return l
    if canFit(blocks, r, height):
        return r
    return -1
    
print(packBlocks([1,3,1,3,3], 2))
print(packBlocks([9,6,5,7,1,6,2,6,10,3], 7))
print(packBlocks([1,2,3,4,5,6,7,8,9,10], 5))