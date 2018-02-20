#Sources for All problem sets:
'''
Books:
Datata structres, algorithms, and applications in Java by Sartaj Sahni.
Data Structures and Algorithms Made Easy in Java. 
Introduction to Algorithms Third Edition by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivet, and Clifford Stein
60 Tips on Object Oriented Programming by Ganesh
https://www.youtube.com/watch?v=jXAHLqQthKw
https://www.youtube.com/watch?v=zIjfhVPRZCg&t=155s
https://www.youtube.com/watch?v=7JwsxXbYSNA&t=173s'''
'''Problem 6'''
import re

'''Creating the Node'''
#strands  =  the DNA strands that will be stored or "strings"
class Node:
    
    def __init__(self, strands=None):
        self.strands = None #storing strand in last node
        self.childnodes = {} # Maps an edge with character


'''Creating the Trie'''     
class Trie:

    def __init__(self):
        self.root = Node() #Defining first that the root is a node
        
    '''This Function inserts a DNA strand or (string) into the tree'''
    def insert(self, strands):
        current_node = self.root
        for input_strand in strands:
        #if the input_strand (strand that is being inserted/deleted/searched) is not in the current node that its traversing then it will call it as a clas node and add it to the dictionary. 

            if not input_strand in current_node.childnodes:
                current_node.childnodes[input_strand] = Node()
            current_node = current_node.childnodes[input_strand]
        current_node.strands=strands #marker for end node for a strand
    '''def getx(self,x):
        return x'''
    '''This function gets all the strands or strings in the trie into one list'''
    def _get_all(self,root_node):
        Every_DNA = [] #Created list to print out each strand
        for key, node in root_node.childnodes.items() :
            if node.strands is not None:
                Every_DNA.append(node.strands)
            #call again with current node
            Every_DNA+= self._get_all(node)
        
        return Every_DNA

    '''This Function helps delete a strand by first checking if the node is a leaf so it does not intefere with any of the other strands'''
    def _delete(self, current_node, strands):
       for key, node in current_node.childnodes.items() :
        #Checking if node is a leaf
         if node.strands is not None and strands==node.strands:
             node.strands=None
         self._delete(node,strands)
        
    '''This function actually deletes the strand'''
    def delete(self,strands):
        self._delete(self.root,strands)


  
    '''This Function returns the strand if its in the trie'''
    def search(self, strands):
        x = self.childSearch(strands)
        if x and x.strands is not None: #It has reached the last node
            print ("Search Strand Found")
        else:
            print ("Search Strand Not Found")

   
    '''This returns if there is any strand in the Trie with the given prefix that was typed in the input'''
    def startsWith(self, prefix):
        if self.childSearch(prefix) is not None:
            print ("Strand starting with prefix is found")
        else:
            print ("Strand starting with prefix is not found")
        

    '''This function actually searches for what ever was inputted or what ever you are looking for'''
    def childSearch(self, strands):
        current_node = self.root
        for input_strand in strands:
            if input_strand in current_node.childnodes:
                current_node = current_node.childnodes[input_strand]
            else:
                return None

        return current_node
    
    '''Displays all all the strands stored'''
    def display(self):
        return self._get_all(self.root)


  
    
    trie = Trie()
    #Calling functions comment out the rest of them if you only want to focus on 1 or two, Sorry I could not put restrictions on for the DNA. I completely forgot untill the last minute and tried making a code below for it and it just turned into a mess. Each one of them are explained in the commented section below
    trie.insert("ACGTTAAAAAG")
    trie.insert("GGGGTTACCCCCT")
    trie.insert("GGGTTTGGGAACCGC")
    
    trie.search("g")
    trie.search("ACGTTAAAAG")
    
    trie.startsWith("ACG")
    trie.startsWith("GT")
    print  (trie.display())
    trie.delete("GGGTTTGGGAACCGC")
    print  (trie.display())
    trie.search("GGGTTTGGGAACCGC"")


# I tried to make it only input ACGT a shorter way but this didn't work on python 3 I guess, apparently it only works for older versions of python
'''def isValid(inputString):
    pattern = re.compile('[A|C|G|T]+')
    if not pattern.match(inputString):
        print("Input is not valid format (ACGT)")
        return None
    else:
        print("valid")
        return True'''
    
 
#There were just a lot of errors while making this
'''    
def menu():
  choice = 0
  
  trie = Trie()
  while True:
     print("Main Choice: Choose 1 of 5 choices")
     print("Choose 0 QUIT")
     print("Choose 1 INSERT")
     print("Choose 2 SEARCH")
     print("Choose 3 DELETE")
     print("Choose 4 DISPLAY")
     print("Choose 5 SEARCH Starts with..")

     choice = int(input ("Please make a choice: "))
     if choice == 0:
            break
     if choice == 1:
        inputString=input("Enter the string to insert : ")
        trie.insert(inputString)
        break
     elif choice == 2:
        inputString=input("Enter the string to search : ") 
        trie.search(inputString)
        break
     elif choice == 3:
        inputString=input("Enter the string to delete : ") 
        trie.delete(inputString)
        break
     elif choice == 4:
        inputString=input("Enter the string to search prefix : ") 
        trie.display (inputString)
        break
     elif choice == 5:
        inputString=input("Enter the string to search prefix : ") 
        trie.startsWith (inputString)
        break
     else:
        print("I don't understand your choice.")
     
    
    
if __name__ == "__main__":
    menu()'''




