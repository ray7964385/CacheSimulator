import cacheStructure

file = open("trace.txt", "r")  # open file
fileContent = file.readlines()  # read file
# print(fileContent)
addressToBeAccess = []  # list to store address to be access
for line in fileContent:  # read the file line by line
    mulValue = 16 ** 7
    decValue = 0
    for char in line[2:10]:
        asciiDifference = ord(char) - ord("A")  # ascii code convert
        if 0 <= asciiDifference <= 5:
            decValue += (10 + asciiDifference) * mulValue
        else:
            decValue += int(char) * mulValue
        mulValue /= 16
    # print(decValue)
    addressToBeAccess.append(decValue)  # put decimal address into list
file.close()

'''
# cache configure
cacheSizeList = [131072, 262144, 524288, 1048576]
blockSizeList = [16]
nWayList = [1, 2, 4, 8]

for cacheSize in cacheSizeList:
    for blockSize in blockSizeList:
        for n in nWayList:
            currentCache = cacheStructure.CacheStructure(cacheSize, blockSize, n)
            for address in addressToBeAccess:
                currentCache.access_address(address)
            currentCache.show_miss_rate()

# cache configure
cacheSizeList = [524288, 1048576]
blockSizeList = [8, 16, 32, 64]
nWayList = [1, 2, 4, 8]

for cacheSize in cacheSizeList:
    for blockSize in blockSizeList:
        for n in nWayList:
            currentCache = cacheStructure.CacheStructure(cacheSize, blockSize, n)
            for address in addressToBeAccess:
                currentCache.access_address(address)
            currentCache.show_miss_rate()
'''

# demo
cacheSizeList = [65536]
blockSizeList = [16]
nWayList = [1, 2, 4, 8]

for cacheSize in cacheSizeList:
    for blockSize in blockSizeList:
        for n in nWayList:
            currentCache = cacheStructure.CacheStructure(cacheSize, blockSize, n)
            for address in addressToBeAccess:
                currentCache.access_address(address)
            currentCache.show_miss_rate()
