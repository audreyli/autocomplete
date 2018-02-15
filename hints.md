6.s04 Hints for Lab 7
=====================
If you are having trouble with this lab, consider the following:

To generate your trie, start with an empty trie (one node representing ""), and add to it by inserting one word a time.

To get children out of your trie, try the following recursive functions:
 - `get_child`, a recursive method which takes in a trie and a prefix and returns the subtrie that designates that prefix.
 - `suffixes`, a recursive method which takes in a trie and returns a string representation of all valid children of the trie. 

To get all valid words, you can combine the two methods: call `get_child` to get the trie starting with your prefix, then call `suffixes` to get all the suffixes from that trie. Combine the suffixes with your prefix to get all the words!

Remember that because of the recursive structure of tries, any child of a trie is also a trie.
