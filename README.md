# huffman-coding
Lossless data compression algorithm using optimal prefix codes.


Purpose

    This program is intended to explore text compression using the Huffman Algorithm
    and reinforce concepts related to building and traversing trees and using
    other data structures.

Input

    A string that will be compressed using the Huffman Algorithm.

Output

    A compressed representation of the input text using the Huffman Codes generated and
    a decompression of the compressed representation, which should match the original string.

Bugs or Implemented Test Cases; and, any theoretical follow-up 
    
    The character-by-character encoding was first tested on a set of sample characters and frequencies, along with the methods
    supporting the encoding and representation (including the header method).
    A full test of the functionality described in section III constitutes the bulk of the project.


Proof of optimality of Huffman Code

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
    
Linear Performance for Symbols Sorted by Frequency

    If the symbols are sorted by frequency, the algorithm can avoid the nlogn complexity associated with most
    sorting.  With this step out of the picture, the algorithm has to build the tree and traverse the tree n times
    where n is the number of characters being encoded.  This leaves us with a linear performance for the 
    Huffman Algorithm on pre-sorted lists.
    
    Ben Mackenzie
    Apr 21, 2018
