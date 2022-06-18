import math


def find_insert_index(access_set):
    valid_count = 0
    for index in range(len(access_set)):
        if access_set[index][0] == 1:
            valid_count += 1
    return valid_count


class CacheStructure:
    def __init__(self, cache_size, block_size, set_degree):
        self.cacheSize = int(cache_size)
        self.blockSize = int(block_size)
        self.setDegree = int(set_degree)
        self.missCount = 0
        self.hitCount = 0
        self.blockNum = int(self.cacheSize/self.blockSize)
        self.setNum = int(self.blockNum/self.setDegree)
        self.address = []
        for i in range(self.setNum):
            self.address.append([])
        for i in range(self.setNum):
            for j in range(self.setDegree):
                self.address[i].append([0, 0])

    def show_structure(self):
        print(self.blockNum)
        print(self.setNum)

    def show_miss_rate(self):
        print("cache size: " + str(self.cacheSize) + ",block size: " + str(self.blockSize) + ",n way: " + str(self.setDegree))
        # print("miss : " + str(self.missCount))
        # print("hit : " + str(self.hitCount))
        print(self.missCount / (self.missCount + self.hitCount))

    def access_address(self, address):
        access_memory_block = math.floor(address/self.blockSize)
        # print("access_memory_block = " + str(access_memory_block))
        access_set = access_memory_block % self.setNum
        # print("tag = " + str(math.floor(access_memory_block / self.setNum)))  # tag * block num = memory block
        # print("access_set = " + str(access_set))

        done = False
        interation = 0
        # print("set content : ")
        # print(self.address[access_set])
        for cache_block in self.address[access_set]:
            # print("cache block : ")
            # print(cache_block)
            if cache_block[0] == 1:  # valid
                if cache_block[1] == math.floor(access_memory_block/self.setNum):  # check if tag is the same
                    # pop the cache block
                    pop_cache = self.address[access_set].pop(interation)
                    # push the popped cache block back
                    self.address[access_set].insert(find_insert_index(self.address[access_set]), pop_cache)
                    self.hitCount += 1  # cache hit
                    # print("hit")
                    done = True
                    break

            elif cache_block[0] == 0:  # invalid
                cache_block[0] = 1  # set this cache block valid
                cache_block[1] = math.floor(access_memory_block/self.setNum)
                self.missCount += 1  # cache miss
                # print("miss 1")
                done = True
                break
            interation += 1

        if not done:
            self.address[access_set].pop(0)
            self.address[access_set].append([1, math.floor(access_memory_block/self.setNum)])
            self.missCount += 1
            # print("miss 2")

        return
