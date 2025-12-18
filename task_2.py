import networkx as nx
from collections import deque

G = nx.Graph()

# Харківське метро
red_line = [
    "Холодна гора", "Південний вокзал", "Центральний ринок", "Майдан Конституції",
    "Проспект Гагаріна", "Спортивна", "Завод ім. Малишева", "Московський проспект",
    "Палац спорту", "Армійська", "Імені О. Масельського", "Тракторний завод", "Індустріальна"
]

blue_line = [
    "Історичний музей", "Університет", "Пушкінська", "Київська",
    "Академіка Барабашова", "Академіка Павлова", "Студентська", "Героїв праці"
]

green_line = [
    "Перемога", "Олексіївська", "23 Серпня", "Ботанічний сад",
    "Наукова", "Держпром", "Архітектора Бекетова", "Захисників України",
    "Метробудівників", "Одеська"
]


def add_line_edges(graph, stations):
    for i in range(len(stations) - 1):
        graph.add_edge(stations[i], stations[i + 1])


add_line_edges(G, red_line)
add_line_edges(G, blue_line)
add_line_edges(G, green_line)

# Пересадки
transfers = [
    ("Університет", "Держпром"),                 # синя <-> зелена
    ("Історичний музей", "Майдан Конституції"),  # синя <-> червона
    ("Спортивна", "Метробудівників"),            # червона <-> зелена
]
G.add_edges_from(transfers)


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))
    return None


def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))
    return None


start_station = "Героїв праці"
end_station = "Індустріальна"

print(f"--- Пошук шляху: {start_station} -> {end_station} ---\n")

dfs_result = dfs_path(G, start_station, end_station)
bfs_result = bfs_path(G, start_station, end_station)

print(f"DFS (у глибину): {dfs_result}")
print(f"Довжина шляху DFS: {len(dfs_result) - 1} переходів")
print("-" * 40)
print(f"BFS (у ширину): {bfs_result}")
print(f"Довжина шляху BFS: {len(bfs_result) - 1} переходів")

shortest = nx.shortest_path(G, start_station, end_station)
print("-" * 40)