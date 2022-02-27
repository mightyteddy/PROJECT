def ignite(n):
    result = 0
    if n == 0:
        return 1
    else:
        for i in range(n):
            result += ignite(i) * ignite(n - i  - 1)
    return result

print(ignite(16 ))