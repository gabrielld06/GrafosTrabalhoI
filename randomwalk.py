"""
TODO LIST

ARRUMAR AS FUNÇÕES DE TESTE
LIMPAR O CODIGO
IMPLEMENTAR UMA ESTRUTURA DECENTE QUE CONSIDERE O PESO DA ARESTA (TESTAR O METODO DE TUPLAS SEPARADA DA ADJ)
IMPLEMENTAR O KRUSKAL
IMPLEMENTAR O PRIM

"""

from random import randint

class Graph:
  def __init__(self, V, Adj, vertexNumber):
    self.V = V
    self.Adj = Adj
    self.vertexNumber = vertexNumber

class Vertex:
  def __init__(self, d, pai, cor, visitado):
    self.d = d
    self.pai = pai
    self.cor = cor
    self.visitado = visitado

def enqueue(Q,v):
    Q.append(v)
    
def dequeue(Q):
    v = Q[0]
    Q.pop(0)
    return v

def bfs(G, s):
    # maior guarda o indice do vertex com maior D do grafo
    maior = s
    G.V[s].d = 0
    G.V[s].pai = None
    G.V[s].cor = 'cinza'
    Q = []
    enqueue(Q,s)
    while(len(Q) != 0):
        u = dequeue(Q)
        for v in G.Adj[u]:
            if G.V[v].cor == 'branco':
                G.V[v].cor = 'cinza'
                G.V[v].d = G.V[u].d + 1
                if G.V[v].d > G.V[maior].d :
                    maior = v
                G.V[v].pai = u
                enqueue(Q, v)
        G.V[u].cor = 'preto'
    return maior

# def bfs(G, s): #bfs usando matriz
    # # maior guarda o indice do vertex com maior D do grafo
    # maior = s
    # G.V[s].d = 0
    # G.V[s].pai = None
    # G.V[s].cor = 'cinza'
    # Q = []
    # enqueue(Q,s)
    # while(len(Q) != 0):
        # u = dequeue(Q)
        # for v in range(len(G.Adj[u])):
            # if G.Adj[u][v] > 0 and G.V[v].cor == 'branco':
                # G.V[v].cor = 'cinza'
                # G.V[v].d = G.V[u].d + 1
                # if G.V[v].d > G.V[maior].d :
                    # maior = v
                # G.V[v].pai = u
                # enqueue(Q, v)
        # G.V[u].cor = 'preto'
    # return maior

def testBfs():
    g = Graph([], [], 5)

    g.V = [Vertex(float('inf'), None, 'branco', False) for i in range(5)]
    # g.Adj = [
    #       [1, 2],
    #       [0, 3],
    #       [0, 3],
    #       [1, 2],
    #       []
    #       ]
    
    # considerei usar matriz de adjancencia para o algoritmo de kruskal e prim
    # já que no começo é usado grafos completos e tbm resolveria o problema do peso da aresta
    # mas ao final da execução, ela não é mais tão interessante
    
    g.Adj = [ 
      [0, 1, 1, -1, -1],
      [1, 0, -1, 1, -1],
      [1, -1, 0, 1, -1],
      [-1, 1, 1, 0, -1],
      [-1, -1, -1, -1, 0],
      ]
    bfs(g, 0)
    assert g.V[0].d == 0
    assert g.V[1].d == 1
    assert g.V[2].d == 1
    assert g.V[3].d == 2
    assert g.V[4].d == float('inf')

def diameter(T):
    # s recebe vertice qualquer de T
    s = 0
    a = bfs(T, s)
    # reset dos atributos para que um novo bfs seja feito
    T.V = [Vertex(float('inf'), None, 'branco', T.V[i].visitado) for i in range(T.vertexNumber)]
    b = bfs(T, a)
    # apos o bfs o atributo D de cada vertice possui a sua distancia em relação ao vertice a,
    # por isso return T.V[b].d
    return T.V[b].d

def testDiameter():
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[3], [2], [3, 1], [0, 4, 2], [3]], 5)) == 3
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[4, 2], [4], [0, 3], [2], [0, 1]], 5)) == 4
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[2], [4], [0, 3, 4], [2], [2, 1]], 5)) == 3
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[1, 4], [0], [4, 3], [2], [0, 2]], 5)) == 4
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[4, 3, 2], [4], [0], [0], [0, 1]], 5)) == 3
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[3, 1], [0, 4], [3], [0, 2], [1]], 5)) == 4
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[4], [2, 3], [4, 1], [1], [0, 2]], 5)) == 4
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[2, 1, 4], [0], [0, 3], [2], [0]], 5)) == 3
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[3], [4], [3], [0, 2, 4], [3, 1]], 5)) == 3
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(5)], [[1, 3], [0, 2], [1], [0, 4], [3]], 5)) == 4
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(6)], [[2], [2], [0, 1, 3], [2, 4], [3, 5], [4]], 6)) == 4
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(6)], [[4], [5], [4, 3, 5], [2], [0, 2], [2, 1]], 6)) == 4
    assert diameter(Graph([Vertex(float('inf'), None, 'branco', False) for i in range(4)], [[1], [0, 2], [1, 3], [2]], 4)) == 3
    
def randomwalk(n):
    G = Graph([Vertex(float('inf'), None, 'branco', False) for i in range(n)], [[] for i in range(n)], n)
    
    u = 0
    G.V[u].visitado = True
    edges = 0
    while(edges < n-1):
        v = randint(0, n-1)
        if not G.V[v].visitado:
            G.Adj[u].append(v)
            G.Adj[v].append(u)
            G.V[v].visitado = True
            edges += 1
        u = v
    
    return G

# Funciona no bfs mas nao tem peso
# def createCompleteGraph(n):
#     G = Graph([Vertex(float('inf'), None, 'branco', False) for i in range(n)], [[] for i in range(n)], n)
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 G.Adj[i].append(j)
    
#     return G

# def testCompleteGraph():
#     assert createCompleteGraph(0).Adj == []
#     assert createCompleteGraph(1).Adj == [[]]
#     assert createCompleteGraph(2).Adj == [[1], [0]]
#     assert createCompleteGraph(3).Adj == [[1, 2], [0, 2], [0, 1]]
#     assert createCompleteGraph(4).Adj == [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
#     assert createCompleteGraph(5).Adj == [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]

# bfs nao compativel com isso
def createCompleteGraph(n):
    G = Graph([Vertex(float('inf'), None, 'branco', False) for i in range(n)], [], n)
    for i in range(n):
        for j in range(i+1, n):
            G.Adj.append([i, j, 0])
    
    return G

def testCompleteGraph():
    assert createCompleteGraph(0).Adj == []
    assert createCompleteGraph(1).Adj == []
    assert createCompleteGraph(2).Adj == [[0, 1, 0]]
    assert createCompleteGraph(3).Adj == [[0, 1, 0], [0, 2, 0], [1, 2, 0]]
    assert createCompleteGraph(4).Adj == [[0, 1, 0], [0, 2, 0], [0, 3, 0], [1, 2, 0], [1, 3, 0], [2, 3, 0]]
    assert createCompleteGraph(5).Adj == [[0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0], 
                                          [1, 2, 0], [1, 3, 0], [1, 4, 0], [2, 3, 0], [2, 4, 0], [3, 4, 0]]

def findSet(v, sets):
    for i in sets:
        if v in i:
            return i;

def uniaoFlasco(setU, setV, sets):
    sets.remove(setU)
    sets.remove(setV)
    setU = setU.union(setV)
    sets.append(setU)

# Graph -> [[Tuplas de arestas], W total]
def MSTKruskal(adj, sets):
    A = []
    E = adj
    W = 0
    E.sort(key=lambda x : x[2])
    for (u, v, w) in E:
        setU = findSet(u, sets)
        setV = findSet(v, sets)
        if setU != setV:
            A.append((u, v))
            W += w
            uniaoFlasco(setU, setV, sets)
    return A

def randomkruskal(n):
    G = createCompleteGraph(n)
    for i in G.Adj:
            i[2] = randint(0, 1)
    sets = []
    G.Adj = MSTKruskal(G.Adj, sets)
    return G

def runAsserts():
    #testBfs()
    testDiameter()
   # testCompleteGraph()
   
def criarArvores():
    f = open("arvores.txt", "w")
    for i in range(5):
        arvore = randomwalk(i+3)
        f.write("{} == {}".format(arvore.Adj, diameter(arvore)) + "\n")
    f.close()

def main():
    entradas = [250, 500, 750, 1000, 1250, 1500, 1750, 2000]
    criarArvores()
    opt = ""
    while(opt != "5"):
        print("----- MENU -----")
        print("1 - Random Walk ")
        print("2 - Kruskal TODO")
        print("3 - Prim    TODO")
        print("4 - Run Asserts ")
        print("5 - Exit        ")
        opt = input()
        if opt == "1":
            f = open("randomwalk.txt", "w")
            for i in entradas:
                media = 0
                for j in range(500):
                    media += diameter(randomwalk(i))
                f.write(str(i) + " {0:.3f}".format(media/500.00) + "\n")
            f.close()
        elif opt == "2":
            # not working
            # bfs não é compativel com a lista de adjacencia implementada em createCompleteGraph()
            print("Running Kruskal's Algorithm")
            f = open("randomkruskal.txt", "w")
            for i in entradas:
                media = 0
                for j in range(500):
                    media += diameter(randomkruskal(i))
                f.write(str(i) + " {0:.3f}".format(media/500.00) + "\n")
            f.close()
            print("TODO")
        elif opt == "3":
            print("Running Prim's Algorithm")
            print("TODO")
        elif opt == "4":
            print("Running Asserts")
            print("")
            runAsserts()
        elif opt == "5":
            print("さよなら")
        else:
            print("Opcao nao suportada")
            

if __name__ == "__main__":
    main()