'''
Created on Apr 21, 2018
By Ben Mackenzie

Program specifications

I. Purpose of the program and any information pertaining to its description
This program is intended to explore text compression using the Huffman Algorithm
and reinforce concepts related to building and traversing trees and using
other data structures.

II. Input
A string that will be compressed using the Huffman Algorithm.

III. Output
The first output for this project is a header representing the character-by-character 
encoding of the string's constituents using the Huffman Algorithm.  
The second is a compressed representation of the input text using the Huffman Codes generated.
The third is a decompression of the compressed representation, which should match the original string.

IV. Bugs or Implemented Test Cases; and, any theoretical follow-up including assignment questions to be turned in for grading
The character-by-character encoding was first tested on a set of sample characters and frequencies, along with the methods
supporting the encoding and representation (including the header method).
A full test of the functionality described in section III constitutes the bulk of the project.


1.  PRE-LAB QUESTIONS

a)  Header Format:
char1:code1,char2,code2,char3:code3... 

See "part1header.txt" for implementation of the header method.

b)  Proof of optimality of Huffman Code

The Huffman Code produces an optimal prefix code if it creates trees representing the code that have
a minimum external path length.  Here I will prove that the Huffman Code produces trees that satisfy 
this condition using induction.

Lemma

    For any Huffman Tree with at least two letters, the two letters with the lowest frequency are set as
    the left and right children of a node V whose value is the sum of their frequencies, at a depth
    that is at least as deep as any other node in the tree.

Proof

    Base Case
    n = 2 where n represents the number of letters encoded.  With only two letters, the tree necessarily
    satisfies the condition of having the minimum external path length.  Only two trees are possible, with
    identical weighted path lengths for the two letter nodes.
    
    Induction Hypothesis
    We start by assuming a Huffman tree T encoding n letters that satisfies the conditions for optimality with 
    leaf V having the lowest frequency and most depth.
    
    Induction Step
    We can obtain a second Huffman tree T' by 'replacing' node V in T with V', the parent node of l1 and l2 where
    f|l1| + f|l2| = f|V|.  Because T is optimal and V has the lowest depth and frequency in T, l1 and l2 also 
    have the lowest depth and frequency in T' and T' is also optimal (min external path length).  
    
    Therefore, the Huffman code produces optimal prefix code.
    
c)  Linear Performance for Symbols Sorted by Frequency

If the symbols are sorted by frequency, the algorithm can avoid the nlogn complexity associated with most
sorting.  With this step out of the picture, the algorithm has to build the tree and traverse the tree n times
where n is the number of characters being encoded.  This leaves us with a linear performance for the 
Huffman Algorithm on pre-sorted lists.  
'''

import sys
from node import Node

def header(code):
    '''
    Takes in a vector of characters and Huffman Coddes
    a header displaying the Huffman Codes of all the characters.
    '''
    header = ''
    for pair in code:
        if pair[0] == "\n":
            pair[0] = "\\n"   
        if pair[0] == " ":
            pair[0] = "space"
        header += pair[0] + ":" + pair[1] + ","
    return header[0:-1]
    

def nodeSort(lyst):
    '''
    Takes in a list of sublists with each sublist containing a character and a frequency
    and returns a new list composed of nodes with character and frequency stored
    as object data members.
    '''
    out = []
    for item in lyst:
        if not isinstance(item, Node):
            item = Node(item[1], item[0])
        out.append(item)
        if len(lyst) == 0:
            print("The list is empty.")  
        i = len(out) - 1
        prev = i - 1
        while item.freq <= out[prev].freq and prev >= 0:
            out[prev], out[i] = out[i], out[prev]
            i -= 1    
            prev -= 1
    return out         

def buildTree(lyst):
    '''
    Takes in a list of nodes sorted in nondecreasing order with each node 
    containing a character and its frequency.  
    Returns a Hoffman tree.
    '''
    if len(lyst) == 1:
        return lyst[0]    
    else:
        n1, n2 = lyst[0], lyst[1]
        root = Node(n1.freq + n2.freq)
        root.left, root.right = n1, n2
        n1.parent, n2.parent = root, root
        lyst.append(root)
        return buildTree(nodeSort(lyst[2::]))
    
def encode(string, vector):
    cyphertext = []
    for char in string:
        for sublist in vector:
            if char == ' ':
                char = 'space'
            elif char == '\n':
                char = '\\n'
            if char == sublist[0]: 
                codedChar = sublist[1]
                cyphertext.append(codedChar)
    return ('').join(cyphertext)    

def getFrequencies(string):
    frequencies = {}
    lyst = []
    for char in string:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1
    for key in frequencies:
        lyst.append([key, frequencies[key]])
    return lyst

def decode(header, code):
    table = {}
    for item in header.split(','):
        codePair = item.split(':')
        table[codePair[1]] = codePair[0]
    root = Node()
    probe = root
    path = ''
    decoded = ''
    i = 0
    while i < len(code):
        codeval = code[i]
        child = Node()
        if codeval == '0':
            probe.left = child
            path += '0'
        if codeval == '1':
            probe.right = child
            path += '1'
        child.parent = probe
        probe = child
        i += 1
        for entry in table:
            if path in table:
                if table[path] == 'space':
                    decodedChar = ' '
                elif table[path] == '\\n':
                    decodedChar = '\n'
                else:
                    decodedChar = table[path]
                leaf = Node()
                if probe.left:
                    probe.right = leaf
                else:
                    probe.left = leaf
                leaf.parent = probe
                leaf.char = decodedChar
                decoded += decodedChar
                probe = root
                path = ''
    return decoded
            
def codeVector(tree):
    '''
    Takes in a Huffman Tree and outputs a vector of coded pairs
    where they first item is the character and the second item is the Huffman Code.
    '''
    code = []
    def recur(root, path):
        if root.left != None:
            root.left.path = path + '0'
            #print("left")
            recur(root.left, root.left.path)
        if root.right != None:
            #print("right")
            root.right.path = path + '1'
            recur(root.right, root.right.path)
        if root.right == None and root.left == None:
            code.append([root.char, root.path])
    recur(tree, tree.path)
    return code


def driver():
    
    #PART 1
    sys.stdout = open("part1header.txt", "w")
    Part1Characters = [["colon", 100], ["space", 605], ["newline", 100], ["comma", 705], ["0", 431], ["1", 242], ["2", 176], ["3", 59], ["4", 185], ["5", 250], ["6", 174], ["7", 199], ["8", 205], ["9", 217]] 
    T = (buildTree(nodeSort(Part1Characters)))
    vector = codeVector(T)
    print("Part 1 Header with Huffman Codes:")
    print(header(vector))
    
    #PART 2 - TEXT COMPRESSION
    inFile = open("in.txt", "r")
    parsed = inFile.readlines()
    #generates a maping of characters to their frequency in the input string
    frequencies = getFrequencies(parsed[0])
    #creates nodes with frequency and character stored as data members and sorts non-decreasing
    sort3d = nodeSort(frequencies)
    #builds a tree from the sorted nodes
    T = buildTree(sort3d)
    #creates a vector of [character, Huffman Code] sublists within a larger list
    cyphered = codeVector(T)
    cypher = header(cyphered)
    #compresses the input string into Huffman Code using the cypher Vector
    code = encode(parsed[0], cyphered) #spaces being eliminated
    #writes the compressed text to a file
    sys.stdout = open("compressed.txt", "w")
    print(str(len(cyphered)))
    print(cypher)
    print(code)
    
    #PART 2 - TEXT DECOMPRESSION
    sys.stdout = open("decompressed.txt", "w")
    inFile = open("compressed.txt", "r")
    parsed = inFile.readlines()
    table = parsed[1].strip()
    tablelength = int(parsed[0].strip())
    compressed = parsed[2].strip()
    decompressed = decode(table, compressed)
    print("Decompressed Text:")
    print(decompressed)
    
if __name__ == '__main__':
    driver()