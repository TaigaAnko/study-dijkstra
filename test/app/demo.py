from app.dijkstra import dijkstra, dijkstra_pq

def test_dijkstra():
    Edges = [
        [[1, 4], [2, 3]],             
        [[2, 1], [3, 1], [4, 5]],   
        [[5, 2]],                       
        [[4, 3]],                       
        [[6, 2]],                       
        [[4, 1], [6, 4]],             
        []                                
        ]
    opt_node = dijkstra(Edges, 7)
    assert opt_node == [0, 4, 3, 5, 6, 5, 8]
    
def test_dijkstra_pq():
    Edges = [
        [[1, 4], [2, 3]],             
        [[2, 1], [3, 1], [4, 5]],   
        [[5, 2]],                       
        [[4, 3]],                       
        [[6, 2]],                       
        [[4, 1], [6, 4]],             
        []                                
        ]
    opt_node = dijkstra_pq(Edges, 7)
    assert opt_node == [0, 4, 3, 5, 6, 5, 8]