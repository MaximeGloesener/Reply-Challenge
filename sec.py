from read_input import read_input, generate_output
from game import Game

filenames = ['0-demo', '1-thunberg', '2-attenborough', '4-maathai', '6-earle', '8-shiva']

if __name__ == '__main__':
    for filename in filenames:
        D, R, T, ressources, turns = read_input(f'inputs/{filename}.txt')
        game = Game(ressources, D)

        for t in range(T):
            game.next_turn(**turns[t])

        print("Profit total", game.profit_tot)
        roadbook = game.save_dictionary # dico du genre {turn: [RI1, RI2, ...]}
        generate_output(f'outputs/{filename}.txt', roadbook)
