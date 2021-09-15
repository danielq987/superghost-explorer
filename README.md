# superghost-explorer
Explore every possible turn of Superghost with this command line tool, giving guaranteed winning moves and winning percentages for all other moves!

Information about the game can be found here. https://www.wikiwand.com/en/Ghost_(game)

# Usage
Download the files, then run explorer.py. Program runs in your favourite terminal using python. Type help for help.

![image](https://user-images.githubusercontent.com/67433232/133364356-9f8392a8-31f4-479f-a974-d34309dc4af1.png)

After a string is entered, all guaranteed winning moves will be listed. 
Additionally, all non-winning moves will also be listed, with a simple estimate for probability of win.

If the string cannot form another word, then `Bad string` will be outputted.

# About the app
This project stemmed from superghost-tree (https://github.com/danielq987/superghost-tree) as a simple way to look-up information from the large, ~15mB pickle file. Since the tree was already made, this program was fairly simple and simply required traversing the tree to find the optimal moves at each point the user queried for. 

Additionally, you can use this app to try to beat the "perfect AI" of SuperGhost found at https://github.com/danielq987/superghost-computer.

Thanks for checking this out! More information can be found at my blog [here](https://danielq987.github.io/blog/posts/2020/10/15/superghost.html).
