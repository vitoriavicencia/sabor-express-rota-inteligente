from sklearn.cluster import KMeans

# Coordenadas dos pedidos simulados (poderiam vir de um CSV, mas aqui é fixo pra simplificar)
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