def shortestPathBinaryMatrix(grid):
    # 获取二维数组的行数
    row = len(grid)
    column = len(grid[0])
    if row != column:
        return -1
    # 检查启动和终端是否可通，否则无解
    if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    if row == 1:
        return 1
    # 定义八个方向
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (-1, 0), (-1, -1), (0, -1), (-1, 1)]
    # 把起点加入栈
    stacks = [(0, 0, 1)]
    # 定义备完（防止重复遍历）
    visited_grid = [[0] * column for _ in range(row)]
    visited_grid[0][0] = 1
    # 开始遍历
    while len(stacks) > 0:
        # 取出栈顶元素
        cur_pos_x, cur_pos_y, step = stacks.pop()
        step += 1
        # 八个方向遍历一步
        for dir in directions:
            next_pos_x = cur_pos_x + dir[0]
            next_pos_y = cur_pos_y + dir[1]
            # 检查退出条件
            if next_pos_x == row - 1 and next_pos_y == column - 1:
                return step
            # 检查位置边界
            if next_pos_x < 0 or next_pos_x >= row or next_pos_y < 0 or next_pos_y >= column:
                continue
            # 判断是否可通过
            if grid[next_pos_x][next_pos_y] == 1:
                continue
            # 检查备忘
            if visited_grid[next_pos_x][next_pos_y] > 0:
                if step < visited_grid[next_pos_x][next_pos_y]:
                    stacks.append((next_pos_x, next_pos_y, step))
                    visited_grid[next_pos_x][next_pos_y] = step
                continue
            # 加入队列
            stacks.append((next_pos_x, next_pos_y, step))
            # 添加备忘
            visited_grid[next_pos_x][next_pos_y] = step

    return -1

if __name__ == "__main__":
    print(shortestPathBinaryMatrix([[0]]))
    print(shortestPathBinaryMatrix([[0, 1], [1, 0]]))
    print(shortestPathBinaryMatrix([[0,0,0,0],[1,0,0,1],[0,1,0,0],[0,0,0,0]]))
    print(shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
