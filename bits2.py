def countPairs(arr, N):
    # Get the maximum element
    maxm = max(arr)
    i = 0
    k = 0

    # Array to store count of bits
    # of all elements upto maxm
    bitscount = [0 for i in range(maxm + 1)]

    i = 1

    # Store the set bits
    # for powers of 2
    while i <= maxm:
        bitscount[i] = 1
        i *= 2

    # Compute the set bits for
    # the remaining elements
    for i in range(1, maxm + 1):
        if (bitscount[i] == 1):
            k = i
        if (bitscount[i] == 0):
            bitscount[i] = (bitscount[k] +
                            bitscount[i - k])
    print(bitscount)

    # Store the frequency
    # of respective counts
    # of set bits
    setbits = dict()

    for i in range(N):
        if bitscount[arr[i]] in setbits:
            setbits[bitscount[arr[i]]] += 1
        else:
            setbits[bitscount[arr[i]]] = 1

    ans = 0
    print(setbits)
    for it in setbits.values():
        ans += it * (it - 1) // 2

    return ans


# Driver Code
if __name__ == '__main__':
    N = 8
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    print(countPairs(arr, N))