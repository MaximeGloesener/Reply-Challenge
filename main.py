from read_input import read_input, generate_output
from game import Game


filename = '1-demo'

if __name__ == '__main__':
    D, R, T, ressources, turns = read_input(f'inputs/{filename}.txt')
    game = Game(ressources, D)

    for t in range(T):
        game.next_turn(**turns[t])

    roadbook = game.save_dictionary # dico du genre {turn: [RI1, RI2, ...]}
    generate_output(f'outputs/{filename}.txt', roadbook)
