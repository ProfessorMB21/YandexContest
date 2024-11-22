# Chain hashing
# First line contains the size of the hash table m
# The second line contains the number of requests n
# There are four types of requests
#   add `string`
#   del `string`
#   find `string`
#   check i

from sys import stdin

hash_size = int(input())
total_reqs = int(input())

hash_table = [[] for _ in range(hash_size)]

def chain_hash(table: list):
    for line in stdin:
        cmd, word = line.split()
        if cmd == "check":
            index = int(word)
        else:
            index, mul = 0, 1
            for ch in word:
                index = (index + ord(ch) * mul) % 1000000007
                mul *= 263
            index %= hash_size
        if cmd == "add":
            if word not in table[index]:
                table[index].insert(0, word)
        elif cmd == "del":
            if word in table[index]:
                table[index].remove(word)
        elif cmd == "find":
            print(["no", "yes"][word in table[index]])
        elif cmd == "check":
            print(*table[index])


for i in range(total_reqs):
    chain_hash(hash_table)

