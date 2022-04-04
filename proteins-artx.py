import random

AMINO_TABLE = {
    "A": ["Alanine", "Ala"],
    "C": ["Cysteine", "Cys"],
    "D": ["Aspartic acid", "Asp"],
    "E": ["Glutamic acid", "Glu"],
    "F": ["Phenylalanine", "Phe"],
    "G": ["Glycine", "Gly"],
    "H": ["Histidine", "His"],
    "I": ["Isoleucine", "He"],
    "K": ["Lysine", "Lys"],
    "L": ["Leucine", "Leu"],
    "M": ["Methionine", "Met"],
    "N": ["Asparagine", "Asn"],
    "P": ["Proline", "Pro"],
    "Q": ["Glutamine", "Gla"],
    "R": ["Arginine", "Arg"],
    "S": ["Serine", "Ser"],
    "T": ["Threonine", "Thr"],
    "V": ["Valine", "Val"],
    "W": ["Ttryptophan", "Trp"],
    "Y": ["Tyrosine", "Tyr"]
}

database = dict()

class Protein:
    def __init__(self, id, name, long, sequence, tipo):
        self.id = id
        self.name = name
        self.long = long
        self.sequence = sequence
        self.tipo = tipo

def decode(sequenza):
    monomers = sequenza.split()
    chain = []
    for i in range(0,len(monomers)):
        chain.append(AMINO_TABLE[monomers[i]][0])
        if i == len(monomers)-1: print(AMINO_TABLE[monomers[i]][1])
        else: print(AMINO_TABLE[monomers[i]][1]+"-", end="")
    return chain

def do_game(sequence):

    rand_len = random.randint(5,9)
    rand_Start = random.randint(0, len(sequence)-10)
    seq = ""
    for i in range(rand_len): seq += sequence[rand_Start+i] + " "
    seq = seq.rstrip()
    print("Here is a subsequence of this protein:")
    chain = decode(seq)
    print("Guess the full name of at least 3 of the above list of codons")
    i = correct = 0
    while(i<3):
        guess = input().capitalize()
        if guess in chain:
            print("Correct!")
            correct += 1
        else: print("That's not right! Try next one")
        i+=1
    print("You got", correct,"out of 3")

if __name__ == "__main__":

    f = open("pdb_seqres.txt")
    print("####################")
    print("Parsing PDB database")
    while True:

        parse = f.readline()

        if parse == "":
            print("Parsing terminated.", len(database), "entries stored.")
            print("####################")
            print()
            break

        if parse[0] == ">":
            info = parse.split()
            id = info[0][1] + info[0][2] + info[0][3] + info[0][4]
            tipo = info[1].split(":")[1]
            number = int(info[2].split(":")[1])
            name = ""
            for i in range(3, len(info)): name += info[i] + " "
            name = name.rstrip()
            sequence = f.readline()

            if id in database: database[id].long += number
            else: database[id] = Protein(id, name, number, sequence, tipo)


    
    while True:
        print("-------------------------------------------------")
        id = input("Hello! Enter the PBD IDs of a protein (For example enter something like 4D2I, 4CS4, 4CIW, or 4Q4W): ").lower()
        if id == "quit": break
        print("Great! You chose", database[id].name)
        print("Here are some info about it:")
        print("Type:", database[id].tipo)
        print("Length:", database[id].long)
        print()

        do_game(database[id].sequence)
        print()