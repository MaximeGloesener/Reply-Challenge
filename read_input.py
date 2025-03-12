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

def generate_output(filepath, roadbook):
    with open(filepath, 'w') as fout:

        for t, ressources in roadbook.items():
            if ressources:
                line = f"{t} {len(ressources)}"
                for r in ressources:
                    line += f" {r}"
                line += "\n"
                fout.write(line)