import networkx as nx

G = nx.Graph()
edges_with_weights = []

# --- Харківське метро
# Холодногірсько-заводська (червона)
red_line_edges = [
    ("Холодна гора", "Південний вокзал", 3),
    ("Південний вокзал", "Центральний ринок", 2),
    ("Центральний ринок", "Майдан Конституції", 2),
    ("Майдан Конституції", "Проспект Гагаріна", 3),
    ("Проспект Гагаріна", "Спортивна", 2),
    ("Спортивна", "Завод ім. Малишева", 2),
    ("Завод ім. Малишева", "Турбоатом", 2),
    ("Турбоатом", "Палац спорту", 2),
    ("Палац спорту", "Армійська", 2),
    ("Армійська", "Імені О.С. Масельського", 2),
    ("Імені О.С. Масельського", "Тракторний завод", 2),
    ("Тракторний завод", "Індустріальна", 3),
]

# Салтівська (синя)
blue_line_edges = [
    ("Героїв праці", "Студентська", 2),
    ("Студентська", "Академіка Павлова", 2),
    ("Академіка Павлова", "Академіка Барабашова", 2),
    ("Академіка Барабашова", "Київська", 3),
    ("Київська", "Пушкінська", 3),
    ("Пушкінська", "Університет", 2),
    ("Університет", "Історичний музей", 2),
]

# Олексіївська (зелена)
green_line_edges = [
    ("Перемога", "Олексіївська", 2),
    ("Олексіївська", "23 Серпня", 2),
    ("23 Серпня", "Ботанічний сад", 2),
    ("Ботанічний сад", "Наукова", 2),
    ("Наукова", "Держпром", 2),
    ("Держпром", "Архітектора Бекетова", 2),
    ("Архітектора Бекетова", "Захисників України", 3),
    ("Захисників України", "Метробудівників", 2),
]

# Пересадки
transfers = [
    ("Майдан Конституції", "Історичний музей", 5),  # червона <-> синя
    ("Спортивна", "Метробудівників", 5),           # червона <-> зелена
    ("Університет", "Держпром", 6),                # синя <-> зелена (довгий перехід)
]

edges_with_weights.extend(red_line_edges)
edges_with_weights.extend(blue_line_edges)
edges_with_weights.extend(green_line_edges)
edges_with_weights.extend(transfers)

G.add_weighted_edges_from(edges_with_weights)


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in graph.nodes}
    unvisited = list(graph.nodes)

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])

        if distances[current_node] == float("infinity"):
            break

        unvisited.remove(current_node)

        for neighbor, attributes in graph[current_node].items():
            weight = attributes.get("weight", 1)
            potential_distance = distances[current_node] + weight

            if potential_distance < distances[neighbor]:
                distances[neighbor] = potential_distance
                previous_nodes[neighbor] = current_node

    return distances, previous_nodes


def reconstruct_path(previous_nodes, start, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        if current == start:
            break
        current = previous_nodes[current]
    return path[::-1]


start_station = "Героїв праці"

print("--- Алгоритм Дейкстри (Харківське метро) ---")
print(f"Пошук найкоротших шляхів від станції: {start_station}\n")

shortest_distances, previous = dijkstra(G, start_station)

print(f"{'Цільова станція':<25} | {'Час (хв)':<10} | {'Маршрут'}")
print("-" * 75)

for station in G.nodes:
    if station == start_station:
        continue

    path = reconstruct_path(previous, start_station, station)
    total_time = shortest_distances[station]
    path_str = " -> ".join(path)

    if len(path_str) > 55:
        path_str = path[0] + " -> ... -> " + path[-1]

    print(f"{station:<25} | {total_time:<10} | {path_str}")

# приклад детального маршруту
target = "Індустріальна"
my_path = reconstruct_path(previous, start_station, target)

print(f"\nДетальний маршрут {start_station} -> {target}:")
print(f"Час: {shortest_distances[target]} хв")
print(f"Шлях: {my_path}")
