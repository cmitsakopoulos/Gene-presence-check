#User should ensure that strain ID and name file consists of two tab separated columns. ID should be column one(left) and name column two(right).
def idname(idnamefiledirectory):
 NamenIDDict = {}
 with open(idnamefiledirectory, 'r') as file:
     for line in file:
      split_line = line.strip().split("\t")
      id, name = split_line
      NamenIDDict[name] = id
 return NamenIDDict


