def getlength(querydir):
 with open(querydir) as file:
    data = file.readlines()
    sequence = "".join(line.strip() for line in data if not line.startswith(">")).replace("\n", "")
    name = data[0].split(" ")
    sequencelength = len(sequence)
    queryname = name[1]
    return queryname, sequencelength

