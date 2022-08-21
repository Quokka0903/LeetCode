def chk_row(i, j, k, lists):    
    res = 0
    comp = []
    for _ in range(k - j + 1):
        comp.append("1")
    print('comp')
    print(comp)
    print('compare')
    for a in range(i, len(lists)):
        print(lists[a][j:k + 1])
        if lists[a][j:k + 1] != comp:
            break
        else :
            res += k - j + 1
    return res
    
def chk_row_rev(i, j, k, lists):
    res = 0
    comp = []
    for _ in range(k - j + 1):
        comp.append("1")
    print('comp')
    print(comp)
    print('compare')
    for a in range(i, -1, -1):
        print(lists[a][j:k + 1])
        if lists[a][j:k + 1] != comp:
            break
        else :
            res += k - j + 1
    return res

def maximalRectangle(matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        import collections
        
        print('len(matrix)')
        print(len(matrix))
        print('len(matrix[0])')
        print(len(matrix[0]))
        
        
        res = []
        y = 0
        flag = 0
        while True:
            x = 0
            stack = []
            print('flag')
            print(flag)
            print('y, x')
            print(y, x)
            x_flag = 0
            while True:
                if matrix[y][x] == '1':
                    stack.append(x)
                    print('stack')
                    print(stack)
                    print('y, stack[0], stack[-1]')
                    print(y, stack[0], stack[-1])
                    if flag == 0:
                        res.append(chk_row(y, stack[0], stack[-1], matrix))
                    else:
                        res.append(chk_row_rev(y, stack[-1], stack[0], matrix))
                    print('res')
                    print(res)
                else:
                    stack = []                
                
                if x_flag == 0 and x == len(matrix[0]) - 1:
                    x_flag = 1
                    stack = []
                    continue
                
                x = x + 1 if x_flag == 0 else x - 1

                if x < 0:
                    break

            if stack:
                print('y, stack[0], stack[-1]')
                print(y, stack[0], stack[-1])
                res.append(chk_row(y, stack[0], stack[-1], matrix))
                print('res')
                print(res)
            
            if flag == 0 and y == len(matrix) - 1:
                flag = 1
                continue
        
            y = y + 1 if flag == 0 else y - 1
            
            if y < 0:
                break
                
        return res
                

print(max(maximalRectangle([["1","1","1","1","1","1","0","1","1","1","1","1","1","1","1"],\
                        ["1","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],\
                        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],\
                        ["0","1","1","1","1","1","1","0","1","1","1","0","1","1","1"],\
                        ["1","0","0","1","1","1","1","1","1","1","1","0","1","1","1"],\
                        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],\
                        ["1","1","1","0","1","1","1","1","1","1","1","0","1","1","1"],\
                        ["1","1","1","1","0","0","0","1","1","1","1","1","0","1","0"],\
                        ["1","0","1","1","0","0","0","1","1","1","1","0","1","0","1"],\
                        ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1"],\
                        ["1","0","1","1","1","1","1","1","1","1","1","1","1","1","1"],\
                        ["1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],\
                        ["1","1","1","0","0","0","1","0","1","1","1","1","1","1","1"],\
                        ["1","1","1","1","1","1","0","1","1","1","1","1","1","1","1"],\
                        ["1","1","1","1","1","1","1","0","1","1","1","1","1","0","1"]])))