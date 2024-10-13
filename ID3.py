from node import Node
import math

#Remove "class" from features?
#We want to know what labels are being used. Binary? MOre than 2?


#Returns the attribute that gives the most information gain
def get_optimal_attribute(examples, attributes, labels):
  entropy_results = []
  total_samples = len(examples)
  for attribute in attributes:
    print("ATTRIBUTE: " + attribute)
    #Finding attr possibilities
    attribute_possiblities = []
    for e in examples:
      attribute_possiblities.append(e[attribute])
    attribute_possiblities = list(set(attribute_possiblities)) # Removing dups




    entropy = 0

    examples_split_by_attr = {} #dict.fromkeys(attribute_possiblities, []) #examples split by attribute possibilities
    for p in attribute_possiblities:
      examples_split_by_attr[p] = []
    for e in examples:
      examples_split_by_attr[e[attribute]].append(e)

    for subgroup in examples_split_by_attr:
      subgroup_entropy = 0
      for label in labels:
        curr_count = 0
        for e in examples_split_by_attr[subgroup]:
          if (e['Class'] == label):
            curr_count += 1
        if (curr_count != 0):
          print("Curr count: " + str(curr_count))
          subgroup_entropy += -(curr_count / len(examples_split_by_attr[subgroup])) * math.log2(curr_count / len(examples_split_by_attr[subgroup]))
          print("SG: " + str(subgroup_entropy))
      print((len(examples_split_by_attr[subgroup]) / total_samples))
      entropy += subgroup_entropy * (len(examples_split_by_attr[subgroup]) / total_samples)
    print("*************")
    entropy_results.append(entropy)

  print(entropy_results)
  min_index = 0 # index of minimum entropy
  for i in range(len(entropy_results)):
    if entropy_results[i] < entropy_results[min_index]:
      min_index = i

  return attributes[min_index]


def ID3_recurse(examples, attributes, default):
  t = Node()

  #Getting list of labels
  labels = []
  for e in examples:
    labels.append(e['Class'])
  labels = list(set(labels)) # removing duplicates
  
  #Setting label to most common class
  label_counts = dict.fromkeys(labels, 0)
  for e in examples:
    label_counts[e['Class']] += 1

  frequent_label = labels[0]
  for key in label_counts:
    if label_counts[key] > label_counts[frequent_label]:
      frequent_label = key

  t.label = frequent_label

  #Checking stopping conditions:
  if (label_counts[frequent_label] == len(examples)):
    #Perfectly uniform; no need to split
    return t
  if (attributes == []):
    return t

  #Finding feature to split on
  optimal_attribute = get_optimal_attribute(examples, attributes, labels)
  print(optimal_attribute)
  print("---------")
  #Getting list of optimal feature possibilities
  feature_possibilities = []
  print(attributes)
  for e in examples:
    feature_possibilities.append(e[optimal_attribute])
  feature_possibilities = list(set(feature_possibilities)) # Removing duplicates

  #Removing optimal feature from attribute list
  attributes.remove(optimal_attribute)

  for possibility in feature_possibilities:
    #Want to add child to node
    select_examples = []
    for e in examples:
      if e[optimal_attribute] == possibility:
        select_examples.append(e)
    new_child = ID3_recurse(select_examples, attributes, default)
    #t.children.update({possibility, new_child})
    t.children[possibility] = new_child

  return t

def ID3(examples, default): 
  attributes = list(examples[0].keys())
  attributes.remove('Class')
  return ID3_recurse(examples, attributes, default)



  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  return t

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  num_correct = 0
  for example in examples:
    curr_node = node
    while curr_node.children != {}:
      curr_node = current_node.children[example[current_node.feature]]
    prediction = curr_node.label
    if prediction == example['class']:
      num_correct += 1

  return (num_correct / len(examples))
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''