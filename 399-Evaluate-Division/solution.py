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
        #graph=dict()
        result=[]
        graph = collections.defaultdict(dict)
        for edge,val in zip(equations,values):
            # 4 possibilities
            #graph[edge[0]],graph[edge[1]]=dict(),dict()
            graph[edge[0]][edge[1]]=val
            graph[edge[0]][edge[0]]=1.0
            graph[edge[1]][edge[0]]=1.0/val
            graph[edge[1]][edge[1]]=1.0

        print graph   
        for q in queries:
            print '======================='+','.join(q)+"="*10
            print 'Result ',self.helper_dfs(graph,q[0],q[1],[])
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
        