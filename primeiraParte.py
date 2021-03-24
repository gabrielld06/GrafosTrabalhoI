"""

*** ESTE SERÁ O ARQUIVO QUE SERÁ ENVIADO NA PRIMERIA PARTE ***

TODO LIST:
ADEQUAR OS COMENTARIOS (ver ultimo video do professor)
CHECKUP FINAL

"""

class Graph:
  def __init__(self, v, adj, vertexNumber):
    self.v = v
    self.adj = adj
    self.vertexNumber = vertexNumber

class vertex:
  def __init__(self, d, pai, cor):
    self.d = d
    self.pai = pai
    self.cor = cor

def enqueue(Q,v):
    Q.append(v)
    
def dequeue(Q):
    return Q.pop(0)

def bfs(G, s):
    # maior guarda o indice do vertex com maior D do grafo
    maior = s
    G.v[s].d = 0
    G.v[s].pai = None
    G.v[s].cor = 'cinza'
    Q = []
    enqueue(Q,s)
    while(len(Q) != 0):
        u = dequeue(Q)
        for v in G.adj[u]:
            if G.v[v].cor == 'branco':
                G.v[v].cor = 'cinza'
                G.v[v].d = G.v[u].d + 1
                if G.v[v].d > G.v[maior].d :
                    maior = v
                G.v[v].pai = u
                enqueue(Q, v)
        G.v[u].cor = 'preto'
    return maior

def testBfs():
    g = Graph([], [], 7)

    g.v = [vertex(float('inf'), None, 'branco') for i in range(g.vertexNumber)]
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
    
    g.v = [vertex(float('inf'), None, 'branco') for i in range(g.vertexNumber)]
    
    bfs(g, 3)
    assert g.v[0].d == 2
    assert g.v[1].d == 1
    assert g.v[2].d == 2
    assert g.v[3].d == 0
    assert g.v[4].d == 1
    assert g.v[5].d == 1
    assert g.v[6].d == 2
    
    g2 = Graph([], [], 7)

    g2.v = [vertex(float('inf'), None, 'branco') for i in range(g2.vertexNumber)]
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
    
    
def diameter(T):
    # s recebe vertice qualquer de T
    s = 0
    a = bfs(T, s)
    # reset dos atributos para que um novo bfs seja feito
    T.v = [vertex(float('inf'), None, 'branco') for i in range(T.vertexNumber)]
    b = bfs(T, a)
    # apos o bfs o atributo D de cada vertice possui a sua distancia em relação ao vertice a,
    # por isso return T.v[b].d
    return T.v[b].d

def testDiameter():
    assert diameter(Graph([vertex(float('inf'), None, 'branco') for i in range(1)], [[]], 1)) == 0
    assert diameter(Graph([vertex(float('inf'), None, 'branco') for i in range(2)], [[1], [0]], 2)) == 1
    assert diameter(Graph([vertex(float('inf'), None, 'branco') for i in range(3)], [[1], [0, 2], [1]], 3)) == 2
    assert diameter(Graph([vertex(float('inf'), None, 'branco') for i in range(4)], [[1], [0, 3, 2], [1], [1]], 4)) == 2
    assert diameter(Graph([vertex(float('inf'), None, 'branco') for i in range(5)], [[1], [0, 2, 4], [1, 3], [2], [1]], 5)) == 3
    assert diameter(Graph([vertex(float('inf'), None, 'branco') for i in range(6)], [[2], [2, 4, 5], [0, 1], [5], [1], [1, 3]], 6)) == 4
    assert diameter(Graph([vertex(float('inf'), None, 'branco') for i in range(7)], [[1], [0, 6, 5], [5, 3], [2], [6], [1, 2], [1, 4]], 7)) == 5

def runAsserts():
    testBfs()
    testDiameter()

def main():    
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
            print("")
        elif opt == "2":
            print("Executando Algoritimo de Kruskal")
            print("")
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