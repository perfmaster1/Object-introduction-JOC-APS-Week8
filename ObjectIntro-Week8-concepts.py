#
#  Linked List creation exercise
#  Author: Daniel Wroblewski
#  Date: 7/5/2025
#
#  Status: In development
#
#
#

class Node(object):
    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next

def printnodes(index,mnode,eflag,tstmsg):
    idx=index
    mynode = mnode
    endflag=eflag
    print(tstmsg)
#    while mynode.next_node:  # is not None and mynode.data is not None:
    while mynode.get_data() and not endflag:
        print(mynode.get_data()," --> ",end="")
        mynode=mynode.get_next()
        idx += 1
        if mynode.next_node is None:
            endflag=True
            print(mynode.get_data())
    exit


def main():
    new_node = Node("first node data")
    next_node = Node("second node data", new_node)
    nodelist = ["First node","Second node","Third node","Fourth node"]

    if len(list(nodelist)) < 2:
        print("The list is too small it has ",len(nodelist)," items. Ending execution")
        exit(1)
    
#
#  New attempt 7/9/2025
#   Building dnode")
    dnode = Node(nodelist[0])
    dnode.set_next(nodelist[2])

    newnode=Node(nodelist[2])
    Node.set_next(dnode,newnode)

    mynode=dnode.get_next()
    newnode3=Node(nodelist[3])
    Node.set_next(mynode,newnode3)
    mynode2=mynode.get_next()
#
#  more efficient attempt: 
#
    fnode = Node(nodelist[0])
    newnode2 =  Node(nodelist[1])
    fnode.set_next(newnode2)
    
    cur2node=newnode2
    new2node =  Node(nodelist[2])
    cur2node.set_next(new2node)

    cur2node=new2node
    new2node =  Node(nodelist[3])
    cur2node.set_next(new2node)
#
#  now print off the nodes:
#
    idx=1 
    mynode = fnode
    endflag=False
    testmsg="Testing the structure"
#
#  Testing status of creation of nodes and the structure: 
#
#    while mynode.next_node:  # is not None and mynode.data is not None:
    printnodes(idx,mynode,endflag,testmsg)
# 
# Project Parameter: Create a function to print ANY length list, given its head node and test
#             
#    print("Function printnodes")
    idx=0
    mynode = fnode
    endflag=False
    testmsg="Function printnodes result:"
    printnodes(idx,mynode,endflag,testmsg)
    exit


main()
