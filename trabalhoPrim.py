# Gabriel Lima Dias RA115892
# José Rafael Silva Hermoso RA112685
from collections import deque
from random import randint, random
from time import time

#Estrutura para guardar um grafo, contendo uma lista de vertices, de adj e a quantidade de vertices
class Graph:
    def __init__(self, v, adj, vertexNumber):
        self.v = v
        self.adj = adj
        self.vertexNumber = vertexNumber
    
    #Preenche a lista de adj do grafo, criando um grafo completo com numero de vertices igual a vertexNumber 
    def create_complete_graph(self):
        for i in range(self.vertexNumber):
            for j in range(i+1, self.vertexNumber):
                self.adj.append((i, j, random()))
    
    #Preenche a matriz de adj do grafo, criando um grafo completo com numero de vertices igual a vertexNumber 
    def create_complete_graph_prim(self, matrix):
        for i in range(self.vertexNumber):
            for j in range(i+1, self.vertexNumber):
                num = random()
                matrix[i][j] = num
                matrix[j][i] = num

#Estrutura para guardar as atributos de um vertice, distancia e cor
class Vertex:
    def __init__(self, d, cor, visitado, index=0):
        self.d = d
        self.cor = cor
        self.visitado = visitado
        self.p = self
        self.rank = 0
        self.chave = float('inf')
        self.pai = None
        self.index = index

#A funcao enqueue enfileira o elemento v na fila Q, tal procedimento feito em tempo linear
def enqueue(Q,v):
    Q.append(v)

#A funcao dequeue retira o elemento mais a esquerda da fila e o retorna, caso a fila não seja vazia
def dequeue(Q):
    if len(Q) != 0:
        return Q.popleft()

#A funcao bfs, realiza a busca em largura no grafo G, comecando pelo vertice s. Ao final o atributo
#d de cada vertice sera equivalente a menor distancia em relacao a s e a funcao retornara o vertice com 
#a maior distancia calculada.
def bfs(G, s):
    # maior guarda o indice do vertex com maior D do grafo até o momento
    G.v = [Vertex(float('inf'), 'branco', False) for i in range(G.vertexNumber)]
    maior = s
    G.v[s].d = 0
    G.v[s].cor = 'cinza'
    Q = deque([])
    enqueue(Q,s)
    while(len(Q) != 0):
        u = dequeue(Q)
        for v in G.adj[u]:
            if G.v[v].cor == 'branco':
                G.v[v].cor = 'cinza'
                G.v[v].d = G.v[u].d + 1
                if G.v[v].d > G.v[maior].d :
                    maior = v
                enqueue(Q, v)
        G.v[u].cor = 'preto'
    return maior

#A funcao testeBfs realiza os testes automatizados do bfs
def testBfs():
    g = Graph([], [], 7)
    g.adj = [
          [1],
          [0, 2, 3, 6],
          [1],
          [1, 4, 5],
          [3],
          [3],
          [1]
          ]

    bfs(g, 0)
    assert g.v[0].d == 0
    assert g.v[1].d == 1
    assert g.v[2].d == 2
    assert g.v[3].d == 2
    assert g.v[4].d == 3
    assert g.v[5].d == 3
    assert g.v[6].d == 2
    
    bfs(g, 3)
    assert g.v[0].d == 2
    assert g.v[1].d == 1
    assert g.v[2].d == 2
    assert g.v[3].d == 0
    assert g.v[4].d == 1
    assert g.v[5].d == 1
    assert g.v[6].d == 2
    
    g2 = Graph([], [], 7)
    g2.adj = [
          [1, 2],
          [0, 3, 5],
          [0, 4],
          [1, 5],
          [1, 2, 5],
          [3, 4],
          []
          ]
    
    bfs(g2, 0)
    assert g2.v[0].d == 0
    assert g2.v[1].d == 1
    assert g2.v[2].d == 1
    assert g2.v[3].d == 2
    assert g2.v[4].d == 2
    assert g2.v[5].d == 2
    assert g2.v[6].d == float('inf')
    
#A funcao diameter calcula o diametro da arvore T
def diameter(T):
    #T.v = [vertex(float('inf'), 'branco', False) for i in range(T.vertexNumber)]
    # s recebe vertice qualquer de T
    s = 0 
    a = bfs(T, s)
    # reset dos atributos para que um novo bfs seja feito
    #T.v = [vertex(float('inf'), 'branco', False) for i in range(T.vertexNumber)]
    b = bfs(T, a)
    # apos o bfs o atributo D de cada vertice possui a sua distancia em relação ao vertice a,
    # por isso return T.v[b].d
    return T.v[b].d

#A funcao testDiameter realiza os testes automatizados da funcao diameter 
def testDiameter(): 
    assert diameter(Graph([], [[]], 1)) == 0
    assert diameter(Graph([], [[1], [0]], 2)) == 1
    assert diameter(Graph([], [[1], [0, 2], [1]], 3)) == 2
    assert diameter(Graph([], [[1], [0, 3, 2], [1], [1]], 4)) == 2
    assert diameter(Graph([], [[1], [0, 2, 4], [1, 3], [2], [1]], 5)) == 3
    assert diameter(Graph([], [[2], [2, 4, 5], [0, 1], [5], [1], [1, 3]], 6)) == 4
    assert diameter(Graph([], [[1], [0, 6, 5], [5, 3], [2], [6], [1, 2], [1, 4]], 7)) == 5

#A funcao is_tree verifica se o grafo G é uma arvore, checando se o grafo possui ciclos e é conexo
def is_tree(G):
    global verticesVisitados
    G.v = [Vertex(float('inf'), 'branco', False) for i in range(G.vertexNumber)]
    verticesVisitados = 0
    return True if DFSVisit(G, 0) and verticesVisitados == G.vertexNumber else False

#O DFSVisit é uma funcao auxiliar de is_tree responsavel por visitar os vertices do grafo, retornando False se encontrar um ciclo ou True caso nao encontre    
def DFSVisit(G, u):
    global verticesVisitados
    G.v[u].cor = "cinza"
    retorno = True
    for v in G.adj[u]:
        if G.v[v].cor == "branco":
            retorno = DFSVisit(G, v)
        elif G.v[v].cor == "preto":
            retorno = False
    G.v[u].cor = "preto"
    verticesVisitados += 1
    return retorno

#A funcao testIs_tree realiza os testes automatizados da funcao is_tree 
def testIs_tree(): 
    assert is_tree(Graph([], [[]], 1))
    assert is_tree(Graph([], [[1], [0]], 2))
    assert is_tree(Graph([], [[1], [0, 2], [1]], 3))
    assert is_tree(Graph([], [[1], [0, 3, 2], [1], [1]], 4))
    assert is_tree(Graph([], [[1], [0, 2, 4], [1, 3], [2], [1]], 5))
    assert is_tree(Graph([], [[2], [2, 4, 5], [0, 1], [5], [1], [1, 3]], 6))
    assert is_tree(Graph([], [[1], [0, 6, 5], [5, 3], [2], [6], [1, 2], [1, 4]], 7))
    assert not is_tree(Graph([], [[1, 2], [0], [0, 3], [2, 4, 5], [3, 5, 6, 7], [3, 4, 6], [4, 5, 7], [6, 4]], 8))
    assert not is_tree(Graph([], [[1, 3], [4], [4, 5], [1], [3], [5]], 6))

#A funcao randomwalk cria um grafo com N vertices e adiciona elementos em sua lista de adj. Tal grafo sera testado se atende as propriedades de ser uma arvore
def randomwalk(n):
    G = Graph([Vertex(float('inf'), 'branco', False) for i in range(n)], [[] for i in range(n)], n)
    
    u = 0
    G.v[u].visitado = True
    edges = 0
    while(edges < n-1):
        v = randint(0, n-1)
        if not G.v[v].visitado:
            G.adj[u].append(v)
            G.adj[v].append(u)
            G.v[v].visitado = True
            edges += 1
        u = v
    
    assert is_tree(G)
    return G

#O union faz a uniao entre os conjuntos do vertice x e y
def union(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1

#A funcao testUnion realiza os testes automatizados da funcao union
def testUnion():
    g = Graph([Vertex(float('inf'), 'branco', False) for i in range(6)], [], 6)

    union(find_set(g.v[0]), find_set(g.v[1]))
    assert find_set(g.v[0]) == find_set(g.v[1]) 

    union(find_set(g.v[3]), find_set(g.v[4]))
    assert find_set(g.v[3]) == find_set(g.v[4])

    union(find_set(g.v[1]), find_set(g.v[4]))
    assert find_set(g.v[1]) == find_set(g.v[4])

    union(find_set(g.v[1]), find_set(g.v[5]))
    assert find_set(g.v[1]) == find_set(g.v[5])

#O find_set busca o conjunto do vertice x
def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p

#A funcao testFindset realiza os testes automatizados da funcao find_set
def testFindSet():
    g = Graph([Vertex(float('inf'), 'branco', False) for i in range(5)], [], 5)
    assert find_set(g.v[0]) == g.v[0] 
    assert find_set(g.v[1]) == g.v[1] 
    union(g.v[2], g.v[3])
    assert find_set(g.v[2]) == find_set(g.v[3])
    assert g.v[3].rank == 1
    assert g.v[2].rank == 0
    assert not find_set(g.v[1]) == find_set(g.v[2])
    assert not find_set(g.v[3]) == find_set(g.v[4])

#O MSTKruskal encontra uma arvore geradora minima do grafo G usando o algoritimo de Kruskal
def MSTKruskal(G):
    A = [[] for i in range(G.vertexNumber)]
    
    G.adj.sort(key = lambda x : x[2])

    numArestas = 0
    i = 0
    while numArestas < G.vertexNumber-1:
        u,v,w = G.adj[i]
        i += 1
        setU = find_set(G.v[u])
        setV = find_set(G.v[v])
        if setU != setV:
            A[u].append(v)
            A[v].append(u)
            union(setU, setV)
            numArestas += 1
    return A

#A funcao testKruskal realiza os testes automatizados da funcao MSTKruskal
def testKruskal():
    
    g = Graph([Vertex(float('inf'), 'branco', False) for i in range(9)],
    [(0, 1, 4),
    (0, 7, 8),
    (1, 2, 8),
    (1, 7, 11),
    (2, 3, 7),
    (2, 8, 2),
    (2, 5, 4),
    (3, 4, 9),
    (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1),
    (6, 8, 5),
    (7, 8, 7)
    ] , 9)
    
    assert MSTKruskal(g) == [[1, 7], [0], [8, 5, 3], [2, 4], [3], [6, 2], [7, 5], [6, 0], [2]]

    g1 = Graph([Vertex(float('inf'), 'branco', False) for i in range(5)],
    [(0, 1, 15),
    (0, 2, 10),
    (1, 2, 1),
    (2, 3, 3),
    (1, 3, 5),
    (3, 4, 20)
    ],5)
    
    assert MSTKruskal(g1) == [[2], [2], [1, 3, 0], [2, 4], [3]]

    g2 = Graph([Vertex(float('inf'), 'branco', False) for i in range(4)],
    [(0, 1, 1),
    (0, 2, 10),
    (0, 3, 1),
    (1, 2, 1),
    (1, 3, 10),
    (2, 3, 1)
    ],4)

    assert MSTKruskal(g2) == [[1, 3], [0, 2], [1], [0]]

#A funcao randomKruskal gera uma arvore de tamnho n utilizando o algoritimo do Kruskal
def randomkruskal(n):
    G = Graph([Vertex(float('inf'), 'branco', False) for i in range(n)], [], n)
    G.create_complete_graph()
    G.adj = MSTKruskal(G)
    assert is_tree(G)
    return G

# Retorna o vertice, se existir, com a menor chave do array Q e o remove do array
def extract_min(Q, G):
    if not Q: return None
    indexMin = 0
    chaveMin = 2147483647 #Valor maximo de inteiro ((2^31)-1)
    for i in range(len(Q)):
        if G.v[Q[i]].chave < chaveMin:
            indexMin = i
            chaveMin = G.v[Q[i]].chave
    
    Q[indexMin], Q[len(Q)-1] = Q[len(Q)-1], Q[indexMin]
    
    return G.v[Q.pop()]

#A funcao testExtractMin realiza os testes automatizados da funcao testExtractMin
def testExtractMin():
    G = Graph([Vertex(float('inf'), 'branco', False) for i in range(4)], [], 4)
    G.v[0].chave = 2
    G.v[1].chave = 3
    G.v[2].chave = 1
    G.v[3].chave = 0
    Q = [i for i in range(4)]
    
    assert extract_min(Q, G) == G.v[3]
    assert extract_min(Q, G) == G.v[2]
    assert extract_min(Q, G) == G.v[0]
    assert extract_min(Q, G) == G.v[1]
    assert extract_min(Q, G) == None

#A função prim encontra uma arvore geradora minima do grafo G usando o algoritimo de Prim
def prim(G, matrix):
    G.v[0].chave = 0
    G.v[0].pai = None
    
    Q = [i for i in range(G.vertexNumber)]
    
    for i in range(G.vertexNumber):
        u = extract_min(Q, G)

        if u.pai != None:
            G.adj[u.pai.index].append(u.index)
            G.adj[u.index].append(u.pai.index)

        for v in Q:
            vertex = G.v[v]
            w = matrix[u.index][v]
            if w < G.v[vertex.index].chave:
                G.v[vertex.index].pai = u
                G.v[vertex.index].chave = w

#A funcao testPrim realiza os testes automatizados da funcao prim
def testPrim():
    
    g = Graph([Vertex(float('inf'), 'branco', False, i) for i in range(9)], [[] for i in range(9)], 9)
    
    matrix = [[float('inf'), 4, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 8, float('inf')],
     [4, float('inf'), 8, float('inf'), float('inf'), float('inf'), float('inf'), 11, float('inf')],
     [float('inf'), 8, float('inf'), 7, float('inf'), 4, float('inf'), float('inf'), 2],
     [float('inf'), float('inf'), 7, float('inf'), 9, 14, float('inf'), float('inf'), float('inf')],
     [float('inf'), float('inf'), float('inf'), 9, float('inf'), 10, float('inf'), float('inf'), float('inf')],
     [float('inf'), float('inf'), 4, 14, 10, float('inf'), 2, float('inf'), float('inf')],
     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), 1, 6],
      [8, 11, float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf'), 7],
      [float('inf'), float('inf'), 2, float('inf'), float('inf'), float('inf'), 6, 7, float('inf')]]
    prim(g, matrix)
    assert g.adj == [[1, 7], [0], [5, 8, 3], [2, 4], [3], [6, 2], [7, 5], [0, 6], [2]]

    g1 = Graph([Vertex(float('inf'), 'branco', False, i) for i in range(5)],
               [[] for i in range(5)], 5)
    
    matrix = [[float('inf'), 15, 10, float('inf'), float('inf')],
                [15, float('inf'), 1, 5, float('inf')],
                [10, 1, float('inf'), 3, float('inf')],
                [float('inf'), 5, 3, float('inf'), 20],
                [float('inf'), float('inf'), float('inf'), 20, float('inf')]]
    prim(g1, matrix)
    assert g1.adj == [[2], [2], [0, 1, 3], [2, 4], [3]]
    
    g2 = Graph([Vertex(float('inf'), 'branco', False, i) for i in range(4)],
    [[] for i in range(4)],4)
    
    matrix = [[float('inf'), 1, 10, 1],
                [1, float('inf'), 1, 10],
                [10, 1, float('inf'), 1],
                [1, 10, 1, float('inf')]]
    prim(g2, matrix)
    assert g2.adj == [[3, 1], [0], [3], [0, 2]]


def randomPrim(n):
    G = Graph([Vertex(float('inf'), 'branco', False, i) for i in range(n)], [[] for j in range(n)], n)
    matrix = [[1 for i in range(n)] for j in range(n)]
    G.create_complete_graph_prim(matrix)
    prim(G, matrix)
    assert is_tree(G)
    return G

#A funcao runAsserts faz a chamada das funcoes que realizam os testes automatizados
def runAsserts():
    testBfs()
    testDiameter()
    testIs_tree()
    testUnion()
    testFindSet()
    testKruskal()
    testPrim()
    testExtractMin()

#Um menu com as opcoes de interacao com o usuario, a opcao 4 executa os asserts para a funcao diameter 
def main():
    entradas = [250, 500, 750, 1000, 1250, 1500, 1750, 2000]
    opt = ""
    while(opt != "5"):
        print("----- MENU -----")
        print("1 - Random Walk ")
        print("2 - Kruskal     ")
        print("3 - Prim        ")
        print("4 - Run Asserts ")
        print("5 - Exit        ")
        opt = input()
        if opt == "1":
            print("Executando Random Walk")
            f = open("randomwalk.txt", "w")
            tempo_total = time()
            for i in entradas:
                media = 0
                tempo_atual = time()
                for j in range(500):
                    media += diameter(randomwalk(i))
                print("N = ", i, " finalizado em ", time() - tempo_atual)
                f.write(str(i) + " {0:.3f}".format(media/500.00) + "\n")
            print("Random walk finalizado em ", time() - tempo_total)
            f.close()
        elif opt == "2":
            print("Executando Algoritimo de Kruskal")
            f = open("randomkruskal.txt", "w")
            tempo_total = time()
            for i in entradas:
                print("Executando ", i)
                media = 0
                tempo_atual = time()
                for j in range(500):
                    media += diameter(randomkruskal(i))
                print("N = ", i, " finalizado em ", time() - tempo_atual)
                f.write(str(i) + " {0:.3f}".format(media/500.00) + "\n")
            print("Kruskal finalizado em ", time() - tempo_total)
            f.close()
        elif opt == "3":
            print("Executando Algoritimo de Prim")
            f = open("randomprim.txt", "w")
            tempo_total = time()
            for i in entradas:
                print("Executando ", i)
                media = 0
                tempo_atual = time()
                for j in range(500):
                    media += diameter(randomPrim(i))
                print("N = ", i, " finalizado em ", time() - tempo_atual)
                f.write(str(i) + " {0:.3f}".format(media/500.00) + "\n")
            print("Prim finalizado em ", time() - tempo_total)
            f.close()
        elif opt == "4":
            print("Executando testes")
            runAsserts()
            print("Todos os testes passaram com sucesso\n")
        elif opt == "5":
            print("")
        else:
            print("Opcao nao suportada")

if __name__ == "__main__":
    main()