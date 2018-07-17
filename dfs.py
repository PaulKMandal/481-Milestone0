m = [[0, 0, 0, 1, 1, 0, 0, 1],
     [0, 0, 1, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 1, 1, 0, 0],
     [0, 1, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0]]

start = (0,0)
end = (4,3)
path = []

def dfs(start, end, m):
    o = [(start, None)]
    c = [end]
    
    while o != []:
        X = o.pop(0)

        if X[1] == None:
            x = 1;
        else:
            path.append(X[1]); 

        if X[0] == end:
            path.append(end);
            return path
        

        temp = []
        if X[0][0] > 0:
            if m[X[0][0] - 1][X[0][1]] == 0:
                temp.insert(0, ((X[0][0] - 1, X[0][1]), X[0]))
        if X[0][0] < (len(m) - 1):
            if m[X[0][0] + 1][X[0][1]] == 0:
                temp.insert(0, ((X[0][0] + 1, X[0][1]),X[0]))
        if X[0][1] > 0:
            if m[X[0][0]][X[0][1] - 1] == 0:
                temp.insert(0, ((X[0][0], X[0][1] - 1),X[0]))
        if X[0][1] < (len(m[0]) - 1): 
            if m[X[0][0]][X[0][1] + 1] == 0:
                temp.insert(0, ((X[0][0], X[0][1] + 1),X[0]))
        
        c.insert(0, X)
        for child in temp:
            if (not child[0] in [x[0] for x in c]) and (not child[0] in [x[0] for x in o]):
                o.insert(0, child)

print("The path calculated by the dfs function is: ", dfs(start, end, m))
