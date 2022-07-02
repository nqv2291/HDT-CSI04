from collections import Counter
def get_president(ballot_list):
# find duplicate tuples in list
    valid = []
    [valid.append(x) for x in ballot_list if x not in valid]
    # print(valid)
    V = []
    for i in range(0,len(valid)):
        V.append(valid[i][1])
    # print(V)
    winner = Counter(V).most_common(2)
    print(winner)


    
# Test case & sample output
get_president([(1, 2), (1, 3), (1, 4), (2, 2), (5, 1), (5, 1), (5, 3)])
