from collections import deque

# 与えられる迷路の設定です
maze = [[".", "#", "#"], [".", ".", "#"], ["#", ".", "#"]]
start = [0, 0]
goal = [2, 1]

# 幅優先探索のためのキュー
queue = deque([start])
# 移動できる方向をまとめておく                            
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
# スタートを探索済みに変える  
maze[start[0]][start[1]] = "#"      

# 幅優先探索開始
while queue:      
    # 現在地の座標を取り出す                                
    x, y = queue.popleft()
    # もしgoalの座標と現在地の座標が一致するなら
    if x == goal[0] and y == goal[1]:  
        # 1を表示してループを抜ける           
        print(1)                                  
        break
    # 右、左、上、下に行けるかどうかを判定する
    for dx, dy in directions:              
        # 現在地を次の地点に進める       
        nx, ny = x + dx, y + dy                   
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == ".":
            # もし次の地点が壁でない、かつ、迷路の外でないならば
            queue.append([nx, ny])                
            # キューに次に地点を追加して、探索済みにマーク
            maze[nx][ny] = "#"     
  
# 全地点を探索し終わったなら迷路を出力
print(maze)                                    