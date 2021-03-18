# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:00:37 2021

@author: Gabriel
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

# Crie um grafo G com n vértices
# 2 for each vertex u ∈ G.V
# 3 u.visitado = False
# 4 u = um vértice qualquer de G.V
# 5 u.visitado = True
# 6 while |G.E| < n − 1
# 7 v = um vértice aleatório de G.V
# 8 if v.visitado == False
# 9 Adicione (u, v) em G.E
# 10 v.visitado = True
# 11 u = v
# 12 return G

# Diameter(T )
# 1 s = vértice qualquer de T .V
# 2 a = o vértice com valor máximo de d obtido por BFS(T , s)
# 3 b = o vértice com valor máximo de d obtido por BFS(T , a)
# 4 return A distância entre a e b

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

def testBfs():
    g = Graph([], [], 5)

    g.V = [Vertex(float('inf'), None, 'branco', False) for i in range(5)]
    g.Adj = [
          [1, 2],
          [0, 3],
          [0, 3],
          [1, 2],
          []
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

def main():
    entradas = [250, 500, 750, 1000, 1250, 1500, 1750, 2000]
    
    f = open("randomwalk.txt", "w")
    # testBfs()
    for i in entradas:
        media = 0
        for j in range(500):
            media += diameter(randomwalk(i))
        f.write(str(i) + " {0:.3f}".format(media/500.00) + "\n")
    f.close()
            


if __name__ == "__main__":
    main()