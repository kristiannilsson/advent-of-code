import hashlib

key = "ckczppom"
n = 0
has_found_part_one = False

while True:
    string = key + str(n)
    hash = hashlib.md5(string.encode()).hexdigest()
    if not has_found_part_one and hash[0:5] == "00000":
        print("part 1", n)
        has_found_part_one = True
    if hash[0:6] == "000000":
        print("part 2", n)
        break
    n += 1
