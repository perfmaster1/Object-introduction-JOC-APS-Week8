#
#
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

def main():
    new_node = Node("first node data")
    next_node = Node("second node data", new_node)
    print(next_node.get_data())

    nodelist = ["First node","Second node","Third node","Fourth node"]

    if len(list(nodelist)) < 2:
        print("The list is too small it has ",len(nodelist)," items. Ending execution")
        exit(1)
    
#
#   Building the linked list: 
#    tested ok. 

    for idx, item in enumerate(nodelist):
        if idx == 0:
            headnode = Node(nodelist[idx],nodelist[idx+1])
            curnode = headnode
            print("Head is:", headnode.data,headnode.next_node)
        elif idx == (len(nodelist) - 1):    # last node w/null pointer
            curnode = Node(nodelist[idx])
        else:
            curnode = Node(nodelist[idx],nodelist[idx+1])
        print("Current node is:", curnode.data,curnode.next_node)

#
#  Traversed the linked list structure
#
    curnode=headnode
    idx=0
    while Node.get_next(curnode) is not None:
        print("got one")
        idx += 1
        curnode=Node.get_next(curnode)
        if idx > 6:
            print("exiting - too many")
            exit
    
    #     print("linked list node # ",idx," is ",Node.get_data(curnode))
    #     curnode=Node.get_next(curnode)
    #     idx += 1
    # print("Node structure length is ",idx)



main()
