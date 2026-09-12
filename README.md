# sabor-express-rota-inteligente

## 1. Descrição do problema e objetivos
A Sabor Express é uma pequena empresa de delivery de alimentos que enfrenta grandes desafios para gerenciar suas entregas, especialmente nos horários de pico (almoço e jantar). Atualmente, as rotas são definidas manualmente pelos entregadores, com base apenas na experiência, o que causa atrasos, maior gasto com combustível e insatisfação dos clientes. O objetivo deste projeto é resolver esse problema criando uma solução baseada em algoritmos de Inteligência Artificial, capaz de sugerir as melhores rotas de entrega.

## 2. Escopo da solução
- **Grafo**: a cidade será representada como um grafo, onde bairros são nós e ruas são arestas com peso (distância).
- **A\***: algoritmo usado para encontrar o caminho mais curto entre a loja e os pontos de entrega.
- **K-Means**: usado para agrupar pedidos próximos em zonas, dividindo o trabalho entre entregadores.