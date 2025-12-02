with open("22.txt") as f:
    secrets = map(int, f.readlines())


def generate_secret(secret):
    num = 64 * secret
    secret ^= num
    secret %= 16777216

    num = secret // 32
    secret ^= num
    secret %= 16777216

    num = secret * 2048
    secret ^= num
    secret %= 16777216
    return secret


secret_map = {}
for secret in secrets:
    initial_secret = secret
    for _ in range(2000):
        secret = generate_secret(secret)
    secret_map[initial_secret] = secret
print(secret_map)
print(sum(secret_map.values()))
