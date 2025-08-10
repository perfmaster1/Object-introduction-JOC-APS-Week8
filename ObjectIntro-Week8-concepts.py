#+++==========================================================================================
#
#  Linked List creation exercise
#  Author: Daniel Wroblewski
#  Date: 7/5/2025
#
#  Status: In development
#
#
#+++==========================================================================================

#==========================================================================================
#   Node class definition and methods:
#==========================================================================================
class Node(object):
    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node

#  provided methods:

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next

#==========================================================================================
#   ll_Nodes_Create: Create the linked list structure with inputs of head and list
#   Variables:
#       fitem - the head node
#       llist - the list to create the linked list nodes from
#==========================================================================================
def ll_Nodes_Create(fitem,llist):
    maxindex=len(llist)-1
    i=0
    fitem=Node(llist[i])           # head node
    curitem = fitem
    for istr in llist:
        if i < maxindex:
            i+=1
            curitem2=Node(llist[i])
            curitem.set_next(curitem2)
            curitem=curitem2
    return fitem


#==========================================================================================
#   find_node: Find the node to remove and bypass it within the data structure
#==========================================================================================
def find_node(head=None,remove=None):
    cur_node=head
    prev_node=head
#-------------------------------------------------------------------------
#  If node to remove is head, then change the node head is pointed to: 
#-------------------------------------------------------------------------
    if head.get_data()==remove.get_data() and head is not None:
        newhead=head.next_node
        return newhead 
#--------------------------------------------------
#   Locate the node to remove, if exists: 
#-------------------------------------------------- 
    while cur_node.get_data() != remove.get_data() and cur_node.get_next() is not None:
        prev_node=cur_node
        cur_node=cur_node.get_next() 
#--------------------------------------------------
#  If at end of linked list and did not find the
#    value then no changes to list: 
#--------------------------------------------------
    if cur_node.get_next() is None or head is None:
        return head
    prev_node.next_node=cur_node.get_next()   # cuts out cur_node from the linked list
    return head

#==========================================================================================
#   printnodes: print the nodes starting with the head, sequentially: 
# 
#     Project Parameter: Create a function to print ANY length list, given its head node 
#==========================================================================================
def printnodes(index,mnode,eflag,tstmsg):
    idx=index
    mynode = mnode
    endflag=eflag
    print(tstmsg)
    if mynode is None:
        print("Empty head node")
        return 
#--------------------------------------------------
# is not None and mynode.data is not None:
#--------------------------------------------------
    while mynode.get_data() and not endflag:
        print(mynode.get_data()," --> ",end="")
        mynode=mynode.get_next()
        idx += 1
        if mynode.next_node is None:
            endflag=True
            print(mynode.get_data())
    exit

#==========================================================================================
#    -- end of methods --
#========================================================================================== 

def main():

    nodelist = ["First node","Second node","Third node","Fourth node"]

    if len(list(nodelist)) < 2:
        print("The list is too small it has ",len(nodelist)," items. Ending execution")
        exit(1)

    fnode = ll_Nodes_Create(nodelist[0],nodelist)
     
#--------------------------------------------------
#  now print off the nodes:
#--------------------------------------------------
    idx=1 
    mynode = fnode
    endflag=False
    testmsg="Testing the structure"
#--------------------------------------------------------------
#  Testing status of creation of nodes and the structure: 
#--------------------------------------------------

    printnodes(idx,mynode,endflag,testmsg)

    idx=0
    mynode = fnode
    endflag=False
    testmsg="Function printnodes result:"
    printnodes(idx,mynode,endflag,testmsg)

    remnode=Node(nodelist[2])
    mynode=find_node(mynode,remnode)
    printnodes(idx,mynode,endflag,testmsg)
    exit


main()
