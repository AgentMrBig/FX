from __future__ import print_function
import os
import neat
import visualize

import numpy as np
import pandas as pd
from datetime import datetime
import json
import finnhub_data as fin

import matplotlib.pyplot as plt

#===== START FOREX DATA
usdjpy_1 = fin.getFXCandles(fin.API_TOKEN, fin.USDJPY, fin.setDateTimestamp('Jan 01, 2010'), fin.setDateTimestamp('Nov 04, 2020'), '30', 'csv')

print(usdjpy_1.head(20))
# df = pd.read_json(usdjpy_1)
# df_f = fin.formatMarketData(usdjpy_1)
# dfnn = usdjpy_1[['o','h','l','c','t']]
# df_c = df_f['c']

# moving averages

# short_ema = df_c.ewm(span=2, adjust = False).mean()

# long_ema = df_c.ewm(span=7, adjust = False).mean()

# df_f['slow'] = short_ema
# df_f['fast'] = long_ema

# df_n = df_f[['o','h','l','c']]

# df_o = df_f[['o']]
# df_h = df_f[['h']]
# df_l = df_f[['l']]
# df_c = df_f[['c']]

# print(df_f.tail())
# print(df_c[0].values)
#===== END FOREX DATA




# 2-input XOR inputs and expected outputs.
# fx_inputs = [df_o[0], df_h[0], df_l[0], df_c[0]]
# fx_outputs = [ df_o[1], df_h[1], df_l[1], df_c[1]]


# def eval_genomes(genomes, config):
#     for genome_id, genome in genomes:
#         genome.fitness = 4.0
#         net = neat.nn.FeedForwardNetwork.create(genome, config)
#         for xi, xo in zip(xor_inputs, xor_outputs):
#             output = net.activate(xi)
#             genome.fitness -= (output[0] - xo[0]) ** 2


# def run(config_file):
#     # Load configuration.
#     config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                          neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                          config_file)

#     # Create the population, which is the top-level object for a NEAT run.
#     p = neat.Population(config)

#     # Add a stdout reporter to show progress in the terminal.
#     p.add_reporter(neat.StdOutReporter(True))
#     stats = neat.StatisticsReporter()
#     p.add_reporter(stats)
#     p.add_reporter(neat.Checkpointer(5))

#     # Run for up to 300 generations.
#     winner = p.run(eval_genomes, 300)

#     # Display the winning genome.
#     print('\nBest genome:\n{!s}'.format(winner))

#     # Show output of the most fit genome against training data.
#     print('\nOutput:')
#     winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
#     for xi, xo in zip(xor_inputs, xor_outputs):
#         output = winner_net.activate(xi)
#         print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))

#     node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
#     visualize.draw_net(config, winner, True, node_names=node_names)
#     visualize.plot_stats(stats, ylog=False, view=True)
#     visualize.plot_species(stats, view=True)

#     p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
#     p.run(eval_genomes, 10)


# if __name__ == '__main__':
#     # Determine path to configuration file. This path manipulation is
#     # here so that the script will run successfully regardless of the
#     # current working directory.
#     local_dir = os.path.dirname(__file__)
#     config_path = os.path.join(local_dir, 'config-feedforward.txt')
#     run(config_path)