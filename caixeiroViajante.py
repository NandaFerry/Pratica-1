class CaixeiroViajante:

    def __init__(self, vertices):
        self.visited = [0 for x in range(vertices)] #Mapa de visita de vertices
        self.nodes = vertices 
        self.visited[0] = 1 #Marca o vertice inicial como visitado
        self.sequence = []
    
    def start(self, graph, currentPosition, count, aresta, total):
        if(count == self.nodes and graph[currentPosition][0] > 0): #Checa a quantidade de viagens com a quantidade de vertices
            total = min(total, aresta + graph[currentPosition][0]) #Se aresta for o menor valor, o armazena 
            return total
        for i in range(0, self.nodes): # Recursão que vai testar todos os caminhos possíveis, a fim de achar o menor percurso
            if(self.visited[i] == 0 and graph[currentPosition][i] > 0):
                self.visited[i] = 1
                total = self.start(graph, i, count + 1, aresta + graph[currentPosition][i], total)
                self.visited[i] = 0            
        return total 
