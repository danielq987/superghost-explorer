from treeClasses import Graph, Node, Edge # tree elements
from string import ascii_lowercase
import json
import time
import pickle

filepath = "tree.p"

def loadTree(filepath):
  """loads the already constructed tree from a .p file specified by filepath"""
  return pickle.load(open(filepath, "rb"))

def main():
  startTime = time.time()
  print(f">> Loading tree from {filepath}, ", end='')
  tree = loadTree(filepath)
  print(f"took {round(time.time() - startTime, 2)} seconds.")

  print("Explore the SuperGhost Tree! Type help for help.")
  # opens the file
  with open("explorerhelp.txt", "r") as f:
    helptext = f.read()
  # main loop
  while True:
    line = input(">> ")
    # empty line
    if line == "":
      continue

    # exit the program
    elif line == "exit":
      print("cya bich")
      break

    # help text
    elif line == "help" or line == "h":
      print(helptext)

    # word query
    elif line[0] == "-":
      word = line[1:].strip()
      turn = len(word) % 2 + 1
      print(f"\n  Player {turn}'s Turn")
      a = tree.getNode(word)

      # string not found in tree - bad string
      if type(a) == int:
        print("    Bad string - no moves possible.")
        continue
      children = tree.getChildren(a)

      # the string is a word
      if len(children) == 0:
        print(f"    {word} is a word! Player {a.getWinner()} wins.\n")
        continue

      # finds winning moves
      winning = []
      notwinning = []
      for i in children:
        if i.getWinner() == turn:
          winning.append(i.getName())
        else:
          notwinning.append(i)
      if len(winning) == 0:
        print(f"    No winning moves for Player {turn}.")
      else:
        print(f"  Winning moves for Player {turn}:")
        for i in winning:
          print(f" -->{i}")
      print("")

      # lists all possible not winning moves and approximate win percentage against a human
      print("  All other possible moves and winning percentages:")
      notword = []
      word = []
      if len(notwinning) == 0:
        print("No other possible words.")
      else:
        for child in notwinning:
          subchildren = tree.getChildren(child)
          leng = len(subchildren)
          if leng != 0:
            winningCount = 0
            for subchild in subchildren:
              if subchild.getWinner() == turn:
                winningCount += 1
            notword.append((winningCount/leng, child.getName()))
          else:
            word.append(child.getName())

        notword.sort(reverse=True)
        for i in notword:
          print(f"    {i[1]} --> ~{round(i[0] * 100, 2)}%")
        for i in word:
          print(f"    {i} is a word, don't play it.")
      print("")
    # invalid line
    else:
      print("  Invalid command. Type help for help.")
          
if __name__ == "__main__":
  main()