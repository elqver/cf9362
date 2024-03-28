def binary_search_last_true(left, right, func):
    mid = (left + right) // 2
    while right - left > 1:
        if func(mid):
            left = mid
        else:
            right = mid
        mid = (left + right) // 2
    return left


def split(tree, weight):
    stack = [next(iter(tree.keys()))]
    weights = {}
    visited = set()
    partitions = 0
    while stack:
        node = stack[-1]
        if node not in visited and node in tree:
            visited.add(node)
            for child in tree[node]:
                if child not in visited:
                    stack.append(child)
            continue
        if node not in tree:
            weights[node] = 1
        else:
            weights[node] = 1 + sum((weights[child] for child in tree[node] if child in weights))
        if weights[node] >= weight:
            partitions += 1
            weights[node] = 0
        stack.pop()

    return partitions


def solution(n, k, graph):
    return binary_search_last_true(1, n, lambda x: (split(graph, x)) > k)


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        graph = {}
        for _ in range(n - 1):
            a, b = map(int, input().split())
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)
        print(solution(n, k, graph))


if __name__ == "__main__":
    main()
