def counting_bits(n: int) -> list[int]:
    lookup_table = [0] * (n+1)
    for num in range(n+1):
        binary_repn = decimal_to_binary(num)
        num_of_ones = count_ones(binary_repn)
        lookup_table[num] = num_of_ones
    return lookup_table

def decimal_to_binary(n: int) -> list[int]:
    binary = []
    while n > 0:
        quotient, remainder = divmod(n, 2)
        n = quotient
        binary.append(remainder)
    return binary[::-1]

def count_ones(binary_repn:list[int]) -> int:
    return binary_repn.count(1)