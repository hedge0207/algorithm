def check(nums):
    for num in nums:
        if num > 0:
            return False
    return True

def steadyGene(gene):
    num_chars = {"A": 0, "C": 0, "T": 0, "G": 0}
    num_overed = {}

    n = len(gene)
    for char in gene:
        num_chars[char] += 1
        if num_chars[char] > n // 4:
            if char in num_overed:
                num_overed[char] += 1
            else:
                num_overed[char] = 1

    if len(num_overed) == 0:
        return 0

    ans = n
    st = 0
    for ed in range(n):
        if gene[ed] in num_overed:
            num_overed[gene[ed]] -= 1

        while check(num_overed.values()) and st < ed:
            ans = min(ans, ed - st + 1)
            if gene[st] in num_overed:
                num_overed[gene[st]] += 1
            st += 1
    return ans