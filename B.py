def get_max_subarray_sum(arr):
    max_sum = 0
    current_sum = 0
    for i in range(len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    f = get_max_subarray_sum(a)
    print(
        ((2 ** k - 1) * f + sum(a)) % (10 ** 9 + 7)
    )


def main():
    for n in range(int(input())):
        solution()


if __name__ == '__main__':
    main()
