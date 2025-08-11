#+++====================================================================================================================+++
#
#  Linked List creation / management 
#  Author: Daniel Wroblewski
#  Date: 7/5/2025
#
#     Project Requirements: Create a function to print ANY length list, given its head node
#                             (assumes the linked list is created)
#                           REMOVE a random element/node and print the remaining nodes
#                           INSERT a random element/node and print the resulting nodes 
#  Status: In development
#  Last updated: 8/10/2025
#
#+++====================================================================================================================+++

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
#    -- End of Node class definition and methods --
#========================================================================================== 

#==========================================================================================
#   ll_Nodes_Create: Create the linked list structure with inputs of head and list. Return
#     the head node. 
#
#     - Empty list input is guarded against. 
#
#   Variables:
#       fitem - the head node
#       llist - the list to create the linked list nodes from
#
#   Return: the count of the number of nodes / items created
#==========================================================================================
def ll_Nodes_Create(llist):
    maxindex=len(llist)-1
    firstItem=None
    i=0
    if maxindex < 0:
        print("!!!!! ERROR: No head value provided - unable to create a linked list !!!!!")
        fitem = None
    else: 
        firstItem=Node(llist[i])           # head node - first item
        curitem = firstItem
        for istr in llist:
            if i < maxindex:
                i+=1
                curitem2=Node(llist[i])
                curitem.set_next(curitem2)
                curitem=curitem2
        i+=1                                 #initial i element was 0
    return firstItem,i

#=================================================================================================
#   maxIndexCheck: Check for requested index handling greater than maximum node index created
#=================================================================================================
def maxIndexCheck(maxindx,rm_index):
    if rm_index > maxindx:
        print("!!!!! ERROR: Index of node ",rm_index," is greater than max node index ",maxindx," unable to remove the node does not exist, skipping !!!!!")
        return True
    return False   

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

#=================================================================================================================
#   find_node_insert: Find the node to insert AFTER, and insert a new node in the node structure 
#=================================================================================================================
def find_node_insert(mode="x",head=None,insert=None,prevVal=""):
    mode=mode.lower()
    if mode not in ["h","1","l","e"]:
        print("\n<<<<< CONDITION: Invalid mode \"",mode,"\" requested, mode not implemented, no action taken >>>>>",sep='')
        return head
    
    if insert is None:
        print("!!!!! ERROR: Empty insert value found or not specified, insert not performed - skipping !!!!!\n")
        return head  

    if head == None:
        print("!!!!! ERROR: Invalid head found or not specified, insert not performed - skipping !!!!!\n")
        return head 
    
    rootNode=head                              # anchor point for the operation
    newNode=Node(insert)                       # all modes need a new node added     
    if mode == "h":                            # a new head is requested, replacing the old head
        print("Inserting/replacing the head node\n")
        newNode.next_node=rootNode
        print("\nA new head was created for this linked list. The old head is: ",rootNode.get_data())
        print("   The new head and next relationships are ",newNode.get_data(),newNode.next_node.get_data())
        return newNode

    if mode == "1":                             # add list[1] mode is requested, keep the rest of the nodes
        print("\nA new Node 1 item will be created for this linked list. The old head and Node 1 is: ",rootNode.data,rootNode.next_node.get_data())
        newNode2=rootNode.get_next()            # next_node
        newNode.next_node=rootNode.get_next()   # next_node
        rootNode.next_node=newNode
        node2=newNode.get_next()
        print("   The new Head, Node 1 & 2 is ",rootNode.get_data(), newNode.get_data(),node2.get_data())
        return rootNode
    
    if mode == "l":                             # a new LAST NODE is requested
        print("\nA new End Node item called ",insert," will be created for this linked list.")
        newNode2=rootNode.get_next()
        while newNode2.next_node is not None:
            newNode2=newNode2.get_next()        # cycle through nodes until last node in Linked List
        newNode2.set_next(newNode)
        return rootNode        

    if mode == "e":                            # add list item at specified position is requested, keep the rest of the nodes
        print("\nA new Node item called ",insert," will be inserted after the ",prevVal," value for this linked list.")
        newNode2=rootNode.get_next()           # next_node
        while newNode2.get_data() != prevVal:
            newNode2=newNode2.get_next()        # cycle through nodes until the node-before-insert value is found
        nextNodeBkup = newNode2.next_node
        newNode2.next_node = newNode
        newNode.next_node = nextNodeBkup
        return rootNode 
       
    return


#==========================================================================================
#   printnodes: print the nodes starting with the head, sequentially: 
#==========================================================================================
def printnodes(index,mnode,eflag,tstmsg):
    idx=index
    mynode = mnode
    endflag=eflag
    print(tstmsg)
    if mynode.next_node is None:
        print("   Head node: ",mynode.get_data()," is the only node\n")
        endflag=True
        print("   Node List: ",mynode.get_data(),"\n")
        return       
    if mynode is None:
        print("\n   Empty head node\n")
        return 
#--------------------------------------------------
# is not None and mynode.data is not None:
#--------------------------------------------------
    while mynode.get_data() and not endflag:
        print("    ",mynode.get_data()," --> ",end="")
        mynode=mynode.get_next()
        idx += 1
        if mynode.next_node is None:
            endflag=True
            print("    ",mynode.get_data())
#    print("\n")
    exit

#==========================================================================================
#    -- End of functions for Node Class --
#========================================================================================== 

def main():
#--------------------------------------------------------------
#   List input follows: 
#--------------------------------------------------------------
    nodelist = ["First node","Second node","Third node","Fourth node"]
#    nodelist = []
#    nodelist = ["First node"]
#--------------------------------------------------------------
#   End of inputs
#--------------------------------------------------------------

    inodes=0
    listcount=len(nodelist)
    maxindex=len(nodelist)-1
    print("\n\n  <<<<<<<<<<<<<<<<<<< START OF RESULTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    fnode,inodes = ll_Nodes_Create(nodelist)
    if fnode is None:
        print("\n!!!!!ERROR: Linked list could not be created as no head node created. ",len(list(nodelist)),"nodes creation possible !!!!! ")
        print("Ending execution\n")
        return(-1)
    print("     Node count created: ",inodes," list count: ",len(nodelist))
    if inodes != listcount:
        print(" !!!!!ERROR: Not all nodes created, exiting !!!!!\n")
        return(-1) 
    
#--------------------------------------------------------------
#  Testing status of creation of nodes and the structure: 
#--------------------------------------------------------------

    idx=0
    mynode = fnode         # save the original fnode value
    endflag=False
    testmsg="\n |==============================================================================|>>>\n  Initial Node print list result: "
    printnodes(idx,mynode,endflag,testmsg)
    print(" |==============================================================================|>>>\n")

#--------------------------------------------------------------
#   Is remnode index out of bounds? If yex cannot remove it...
#--------------------------------------------------------------

    rm_index=2
    print("  Attempting to remove node ",rm_index+1," \n")
    if not maxIndexCheck(maxindex,rm_index):
        remnode=Node(nodelist[rm_index])
        mynode=find_node(mynode,remnode)



    mynode = find_node_insert("h",mynode,"Xth Node","")

    mynode = find_node_insert("1",mynode,"Ath Node","")

    mynode = find_node_insert("l",mynode,"TheEndOfAllNodes","")   

    mynode = find_node_insert("e",mynode,"TheSecondThirdNode","Second node")   

    mynode = find_node_insert("X",mynode,"ThePhantomNode","")   

    testmsg="\n |==============================================================================|>>>\n   Node print list result after all operations completed: "
    printnodes(idx,mynode,endflag,testmsg)
    print(" |==============================================================================|>>>\n")
    exit


main()
