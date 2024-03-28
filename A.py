def solution():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    median_index = (n // 2 - 1 if n % 2 == 0 else n // 2)
    median = a[median_index]
    print(a[median_index:].count(median))


def main():
    for n in range(int(input())):
        solution()


if __name__ == '__main__':
    main()
