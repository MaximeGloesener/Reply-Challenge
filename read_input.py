def read_input(filepath):
    with open(filepath, 'r') as fin:
        D, R, T = map(int, fin.readline().split())
        ressources = []
        for _ in range(R):
            dico = {}
            line = fin.readline().split()
            for i in range(len(line)):
                if line[i].isnumeric(): line[i] = int(line[i])
            if len(line) == 8:
                dico['RI'], dico['RA'], dico['RP'], dico['RW'], dico['RM'], dico['RL'], dico['RU'], dico['RT'], dico['RE'] = line + [None]
            else:
                dico['RI'], dico['RA'], dico['RP'], dico['RW'], dico['RM'], dico['RL'], dico['RU'], dico['RT'], dico['RE'] = line
            ressources.append(dico)
        turns = []
        for _ in range(T):
            dico = {}
            dico['TM'], dico['TX'], dico['TR'],  = map(int, fin.readline().split())
            turns.append(dico)

    return D, R, T, ressources, turns

D, R, T, ressources, turns = read_input('inputs/0-demo.txt')
print(D,R,T)
print(ressources[0])
print(turns[0])