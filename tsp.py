from itertools import permutations

test_edges = {
    "AB": 10,
    "AC": 2,
    "AD": 6,
    "BC": 11,
    "BD": 4,
    "CD": 3,
}

# Mia's edges in table form are:
#   A	B	C	D	E	F	G	H	I
# A	0.0	3.0	7.9	9.7	8.4	8.1	6.0	2.1	4.4
# B	3.0	0.0	7.1	8.9	7.5	7.2	5.2	3.9	7.2
# C	7.9	7.1	0.0	2.5	0.7	1.6	2.4	5.9	7.8
# D	9.7	8.9	2.5	0.0	2.3	2.3	4.2	6.3	8.2
# E	8.4	7.5	0.7	2.3	0.0	1.6	2.7	5.7	7.7
# F	8.1	7.2	1.6	2.3	1.6	0.0	2.6	4.1	6.1
# G	6.0	5.2	2.4	4.2	2.7	2.6	0.0	4.0	6.0
# H	2.1	3.9	5.9	6.3	5.7	4.1	4.0	0.0	3.6
# I	4.4	7.2	7.8	8.2	7.7	6.1	6.0	3.6	0.0

mias_edges = {
    "AB": 3.0,
    "AC": 7.9,
    "AD": 9.7,
    "AE": 8.4,
    "AF": 8.1,
    "AG": 6.0,
    "AH": 2.1,
    "AI": 4.4,
    "BA": 3.0,
    "BC": 7.1,
    "BD": 8.9,
    "BE": 7.5,
    "BF": 7.2,
    "BG": 5.2,
    "BH": 3.9,
    "BI": 7.2,
    "CA": 7.9,
    "CB": 7.1,
    "CD": 2.5,
    "CE": 0.7,
    "CF": 1.6,
    "CG": 2.4,
    "CH": 5.9,
    "CI": 7.8,
    "DA": 9.7,
    "DB": 8.9,
    "DC": 2.5,
    "DE": 2.3,
    "DF": 2.3,
    "DG": 4.2,
    "DH": 6.3,
    "DI": 8.2,
    "EA": 8.4,
    "EB": 7.5,
    "EC": 0.7,
    "ED": 2.3,
    "EF": 1.6,
    "EG": 2.7,
    "EH": 5.7,
    "EI": 7.7,
    "FA": 8.1,
    "FB": 7.2,
    "FC": 1.6,
    "FD": 2.3,
    "FE": 1.6,
    "FG": 2.6,
    "FH": 4.1,
    "FI": 6.1,
    "GA": 6.0,
    "GB": 5.2,
    "GC": 2.4,
    "GD": 4.2,
    "GE": 2.7,
    "GF": 2.6,
    "GH": 4.0,
    "GI": 6.0,
    "HA": 2.1,
    "HB": 3.9,
    "HC": 5.9,
    "HD": 6.3,
    "HE": 5.7,
    "HF": 4.1,
    "HG": 4.0,
    "HI": 3.6,
    "IA": 4.4,
    "IB": 7.2,
    "IC": 7.8,
    "ID": 8.2,
    "IE": 7.7,
    "IF": 6.1,
    "IG": 6.0,
    "IH": 3.6,
}

edges = mias_edges
# add in any missing reverse paths between pairs
# we need to do the list creation dance to avoid permutation of the keys during execution
for pair in list(edges.keys()):
    edges[pair[1] + pair[0]] = edges[pair]


def length(path: str) -> float:
    total = 0
    for i in range(len(path) - 1):
        edge = path[i : i + 2]
        if edge not in edges:
            # the path is not valid, return a large number
            return 10e10
        total += edges[edge]
    return total


count = 0
shortest = 10e10
best = ""

for p in permutations("BCDEFGHI"):
    count += 1
    trip = "A" + "".join(p) + "A"
    distance = length(trip)
    if distance < shortest:
        shortest = distance
        best = trip
    print(trip, length(trip))

print("\nTotal paths checked:", count)
print("Best path:", best, "with length", shortest)
