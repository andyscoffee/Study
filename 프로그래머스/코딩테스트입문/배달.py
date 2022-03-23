# Summer/Winter Coding(~2018) 배달 (난이도 2)
import heapq


def solution(N, road, K):
    answer = 0
    m = len(road)
    graph = [[] for _ in range(N+1)]
    distance = [int(1e9)]*(N+1)
    for r in road:
        a, b, c = r[0], r[1], r[2]
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijk(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    dijk(1)
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
      [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
      3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
