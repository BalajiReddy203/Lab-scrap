import heapq
class priorityQueue:
    def__init__(self):
        self.cities=[]
        def push(self,city,cost):
            heapq.heappush(self.cities,(cost,city))
            def po(self):
                return heapq.heappop(self.cities)[1]
            def isEmpty(self):
                if(self.cities==[]):
                    return True
                else:
                    return False
                def check(self):
                    print(self.cities)
                    class ctNode:
                        def__init__(self,city,distance):
                            self,city=str(city)
                            self.distance=str(distance)
                            romania{}
                            def makedict():
                                file=open("romania.txt",'r')
                                for string in file:
                                    line=string.split(',')
                                    ct1=line[0]
                                    ct2=line[1]
                                    dist=int(line[1])
                                    romania.setdefault(ct1,[]).append(ctNode(ct2,dist))
                                    romania.setdefault(ct2,[]).append(ctNode(ct1,dist))
                                    def makehuristicdict():
                                        h={}
                                        with open("romania_sld.txt",'r')as file:
                                            for line in file:
                                                node=line[0].strip()
                                                sld=int(line[1]).strip())
                                                h[node]=sld
                                                return h
                                            def heuristic(node,values):
                                                return values[node]
                                            def astar(start,end)
                                            path={}
                                            distance={}
                                            q=priorityQueue()
                                            h=makehuristicdict()
                                            q.push(start 10)
                                            distance[start]=0
                                            path[start]=None
                                            expandedList=[]
                                            while(q.isEmpty()=False):
                                                current=q.pop()
                                                expandedList.append(current)
                                                if(current==end):
                                                    break
                                                for new in romania[current]:
                                                    g_cost=distance[current]+int(new.distance)
                                                    #print(new.city,new.distance,"now:"+str(distance[current]),g_cost)
                                                    if(new.city not in distance or g_cost(distance[new,city])):
                                                        distance[new,city]=g_cost
                                                        fcost=g_cost+heuristic(new.city,h)
                                                        #prnt(f_cost)
                                                        q.push(new.city,f_cost)
                                                        path=[new.city]=current
                                                        printoutput(start,end,path,distance,expandedlist)
                                                        def pintoutput(start,end,path,distance,expandedlist)
                                                        finalpath=[]
                                                        i=end
                                                        while(path.get[i}!=None):
                                                            finalpath,append(i)
                                                            i=path[i]
                                                            finalpath,append(start)
                                                            finalpath,reverse()
                                                            print("A-star algorithm for Romania Map")
                                                            print("\t Arad=>B4charest)
                                                                  print("============================")
                                                                  print("List of cities that are Exapnded:"+str(len(expandedlist)))
                                                                  print("============================")
                                                                  print("Cities in final path:"+str(finalpath))
                                                                  print("Total number of cities in final path are:"+str(len(finalpath)))
                                                                  print("Totalcost:"+str(distance[end]))
                                                                  def main()
                                                                  src="Arad"
                                                                  dst="B4charest"
                                                                  makedict()
                                                                  astar(src,dst)
                                                                  if__name__=="__main__":
                                                                  main()
