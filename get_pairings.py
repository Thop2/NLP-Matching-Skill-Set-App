from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def avg_scores(table):
  result = np.zeros((len(table), len(table[0])))
  for row in range(len(table)):
    for col in range(len(table)):
      result[row][col] = 0.5 * (table[row][col] + table[col][row])
  return result

def get_pairs(table):
  pairings = []

  # Zero out self-pairs
  for row in range(len(table)):
        for col in range(len(table)):
          if row == col:
            table[row][col] = float("-inf")

  # While there are pairings to be made
  while len(pairings) < len(table) // 2:

    # Get the index of the best pairing
    max_index = np.unravel_index(table.argmax(), table.shape)
    pairings.append(max_index)

    # Zero out the people who are taken
    for i in max_index:
      for row in range(len(table)):
        for col in range(len(table)):
          table[row][i] = float("-inf")
          table[i][col] = float("-inf")

  return pairings

def pairings_to_names(pairings, nameList):
  names = []
  for pairing in pairings:
    pair_names = [ nameList[pairing[0]], nameList[pairing[1]] ]
    names.append(pair_names)
  return names

def run(know, want, name_list):
  model = SentenceTransformer('bert-base-nli-mean-tokens')
  know_embeddings = model.encode(know)
  want_embeddings = model.encode(want)
  table = cosine_similarity(
      know_embeddings,
      want_embeddings
  )
  table = avg_scores(table)
  pairings = get_pairs(table)
  names = pairings_to_names(pairings, name_list)
  return names
