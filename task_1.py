import networkx as nx
import matplotlib.pyplot as plt

# Граф Харківського метро
metro_graph = nx.Graph()

metro_graph.add_edges_from(
    [
        # Холодногірсько-Заводська лінія
        ("Kholodna Hora", "Pivdennyi Vokzal"),
        ("Pivdennyi Vokzal", "Tsentralnyi Rynok"),
        ("Tsentralnyi Rynok", "Maidan Konstytutsii"),
        ("Maidan Konstytutsii", "Prospekt Haharina"),
        ("Prospekt Haharina", "Sportyvna"),
        ("Sportyvna", "Zavodska"),
        ("Zavodska", "Turboatom"),
        ("Turboatom", "Palats Sportu"),
        ("Palats Sportu", "Armiiska"),
        ("Armiiska", "Maselskoho"),
        ("Maselskoho", "Traktornyi Zavod"),
        ("Traktornyi Zavod", "Industrialna"),

        # Салтівська лінія
        ("Istorychnyi Muzei", "Universytet"),
        ("Universytet", "Yaroslava Mudroho"),
        ("Yaroslava Mudroho", "Kyivska"),
        ("Kyivska", "Akademika Barabashova"),
        ("Akademika Barabashova", "Akademika Pavlova"),
        ("Akademika Pavlova", "Studentska"),
        ("Studentska", "Saltivska"),

        # Олексіївська лінія
        ("Peremoha", "Oleksiivska"),
        ("Oleksiivska", "23 Serpnia"),
        ("23 Serpnia", "Botanichnyi Sad"),
        ("Botanichnyi Sad", "Naukova"),
        ("Naukova", "Derzhprom"),
        ("Derzhprom", "Arkhitektora Beketova"),
        ("Arkhitektora Beketova", "Zakhysnykiv Ukrainy"),
        ("Zakhysnykiv Ukrainy", "Metrobudivnykiv"),

        # Пересадки
        ("Maidan Konstytutsii", "Istorychnyi Muzei"),
        ("Sportyvna", "Metrobudivnykiv"),
        ("Derzhprom", "Universytet"),
    ]
)

# Візуалізація
pos = nx.spring_layout(metro_graph)

nx.draw(
    metro_graph,
    pos,
    with_labels=True,
    font_size=8,
    node_size=700,
    node_color="lightgray",
    font_color="black",
    font_weight="bold",
)

plt.title("Харківське метро")
plt.show()

# Аналіз графа
num_nodes = metro_graph.number_of_nodes()
num_edges = metro_graph.number_of_edges()

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")

degree_dict = dict(metro_graph.degree())
print("\nСтупінь кожної вершини:")
for station, degree in degree_dict.items():
    print(f"{station}: {degree}")
