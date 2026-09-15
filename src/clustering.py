from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

pedidos = {
    1: (0.5, 4.8),
    2: (2.2, 4.5),
    3: (4.5, -4.8),
    4: (4.8, -5.5),
    5: (5.2, -1.2),
    6: (4.5, -0.8),
    7: (2.0, 1.2),
    8: (1.8, 0.8),
}

coordenadas = list(pedidos.values())

n_zonas = 3
kmeans = KMeans(n_clusters=n_zonas, random_state=42, n_init=10)
zonas = kmeans.fit_predict(coordenadas)

if __name__ == "__main__":
    for pedido_id, zona in zip(pedidos.keys(), zonas):
        print(f"Pedido {pedido_id} -> Zona {zona}")

    plt.figure(figsize=(10, 8))
    cores = ["red", "blue", "green", "orange", "purple"]
    zonas_ja_legendadas = set()
    for (x, y), zona, pedido_id in zip(coordenadas, zonas, pedidos.keys()):
        rotulo = f"Zona {zona}" if zona not in zonas_ja_legendadas else None
        plt.scatter(x, y, color=cores[zona], s=100, label=rotulo)
        plt.annotate(f"Pedido {pedido_id}", (x, y), fontsize=8, xytext=(5, 5), textcoords="offset points")
        zonas_ja_legendadas.add(zona)

    plt.legend()

    plt.title("Pedidos agrupados por zona (K-Means)")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.margins(0.15)
    plt.savefig("outputs_zonas.png")
    print("Gráfico salvo como outputs_zonas.png")