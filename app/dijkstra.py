"""
ダイクストラ法
"""

def dijkstra(edges, num_node):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = [i for i in range(num_node)]     #ノードの名前を0~ノードの数で表す

    while len(node_name) > 0:
        r = node_name[0]

        #最もコストが小さい頂点を探す
        for i in node_name:
            if  node[i] < node[r]:
                r = i   #コストが小さい頂点が見つかると更新

        #最もコストが小さい頂点を取り出す
        min_point = node_name.pop(node_name.index(r))

        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost     #更新

    return node

import heapq

def dijkstra_pq(edges, num_node):
    """ダイクストラ法: ヒープを使用"""
    node = [float('inf')] * num_node
    node[0] = 0  # スタート地点を0で初期化

    # 優先度キュー (コスト, ノード)
    pq = [(0, 0)]

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        # 現在のコストが既知の最短経路より大きい場合はスキップ
        if current_cost > node[current_node]:
            continue

        # 隣接ノードをチェック
        for neighbor, cost in edges[current_node]:
            new_cost = current_cost + cost
            if new_cost < node[neighbor]:
                node[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return node
