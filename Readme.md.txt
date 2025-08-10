Object-Introduction and Linked List Demo

Programming Tasks:

1. Using Python, copy and the base code including the node class and run it to verify that
    'second node data" is observed

2. Create a list of 4 numbers/strings & print them out. Create this code initially in the main 
    function.

    Expected output similar to:  Fourth node --> Third node --> Second node --> First node

3. Create a function to print any length list, given its head node. Test the function to 
    prove it works by printing the list of 4 nodes.

4. After printing t he list in main, remove a node and print the remaining nodes

5. Next, add a new element & print your list.

RECOMMENDED:

* COnsider using an extra Node as a loop variable when printing:

     Node n = next_node
     while n != null:
        print(n.get_data(), "->")
        n = n.get_next()

* When removing a node, you will need to have access to the nodes before and after
    the one to be deleted. 