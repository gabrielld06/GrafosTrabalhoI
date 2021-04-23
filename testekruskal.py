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
    
    def add_weighted_edge(self, u, v, w):
        self.adj.append((u, v, w))
    
    def create_complete_graph(self):
        for i in range(self.vertexNumber):
            for j in range(i+1, self.vertexNumber):
                #self.add_weighted_edge(i, j, random())
                self.adj.append((i, j, random()))

#Estrutura para guardar as atributos de um vertice, distancia e cor
class Vertex:
    def __init__(self, d, cor, visitado):
        self.d = d
        self.cor = cor
        self.visitado = visitado
        self.p = self
        self.rank = 0

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

def is_tree(G):
    global verticesVisitados
    G.v = [Vertex(float('inf'), 'branco', False) for i in range(G.vertexNumber)]
    verticesVisitados = 0
    return True if DFSVisit(G, 0) and verticesVisitados == G.vertexNumber else False
    
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

def make_set(x):
    x.p = x
    x.rank = 0

def union(x, y):
    link(x, y)

def link(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1

def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p

def MSTKruskal(G):
    A = [[] for i in range(G.vertexNumber)]

    E = sorted(G.adj, key=lambda x : x[2])
    numArestas = 0
    i = 0
    while numArestas < G.vertexNumber-1:
        u,v,w = E[i]
        i += 1
        setU = find_set(G.v[u])
        setV = find_set(G.v[v])
        if setU != setV:
            A[u].append(v)
            A[v].append(u)
            union(setU, setV)
            numArestas += 1
    return A

def randomkruskal(n):
    G = Graph([Vertex(float('inf'), 'branco', False) for i in range(n)], [], n)
    G.create_complete_graph()
    G.adj = MSTKruskal(G)
    assert is_tree(G)
    return G

assert is_tree(randomkruskal(10))

#A funcao runAsserts faz a chamada das funcoes que realizam os testes automatizados
def runAsserts():
    testBfs()
    testDiameter()
    testIs_tree()

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
                    aaaa = diameter(randomkruskal(i))
                    media += aaaa
                    #print((100*j)/500, "%")
                print("N = ", i, " finalizado em ", time() - tempo_atual)
                f.write(str(i) + " {0:.3f}".format(media/500.00) + "\n")
            print("Kruskal finalizado em ", time() - tempo_total)
            f.close()
        elif opt == "3":
            print("Executando Algoritimo de Prim")
            print("")
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