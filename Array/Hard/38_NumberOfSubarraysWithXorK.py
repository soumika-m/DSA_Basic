"""
Find number of subarrays with xor K
"""

def findSubarrayWithXorK(arr, k):
    """ T(C) -> O(N^2), S(C) -> O(1) """

    n = len(arr)

    count = 0

    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor = xor ^ arr[j]

            if xor == k:
                count = count + 1
        
    return count


def findSubarrayWithXorKOptimal(arr, k):
    """ T(C) -> O(N), S(C) -> O(N) """

    n = len(arr)
    count = 0
    # using prefix xor and hashmap
    xor = 0
    # hashmap store xor and it's count
    hmap = {}
    # add 0, and count as 1, incase we get xor as k, we will be able to count that as well
    hmap[xor] = 1
    # using formula x^k = XoR => (x^K) ^ K = XoR ^ K => ||x = XoR ^ K||
    for i in range(n):
        # this is acting as XR
        xor = xor ^ arr[i]

        # find if x present in map, take count
        x = xor ^ k

        # calculate count of subarray, if x in hmap
        count += hmap.get(x, 0)
        
        # add xor and it's count in hmap, if already exist increase count
        hmap[xor] = hmap.get(xor, 0) + 1

    return count


if __name__ == "__main__":
    arr = [4,2,2,6,4]
    k = 6
    print(arr, k)
    print(findSubarrayWithXorK(arr, k))
    print(findSubarrayWithXorKOptimal(arr, k))
