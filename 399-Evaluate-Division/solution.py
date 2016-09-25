class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.right=None
        sefl.left=None

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        result=[]
        graph = collections.defaultdict(dict)
        for (d0,d1),val in zip(equations,values):
            graph[d0][d1]=val
            graph[d0][d0]=1.0
            graph[d1][d0]=1.0/val
            graph[d1][d1]=1.0

        print graph   
        for q in queries:
            result.append(self.helper_dfs(graph,q[0],q[1],[]))
        
        return result
            
            
    def helper_dfs(self, graph, start, end, path):
        if start not in graph or end not in graph:
            return -1.0
        if graph.has_key(start) and end in graph[start]:
            return graph[start][end]
        for node in graph[start]:
            if node not in path:
                next_val=self.helper_dfs(graph,node,end,path+[node])
                print 'node ',node, 'next_val ',next_val
                if next_val!=-1:
                    return graph[start][node]*next_val
        return -1.0
        
        

        