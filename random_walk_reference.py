'''A random walk simulation
author: Peter Aldous
'''

import math
import random
import statistics
import subprocess
import sys
import tempfile
import turtle

def north():
    '''Take one step north.'''
    return (0, 1)

def south():
    '''Take one step south.'''
    return (0, -1)

def east():
    '''Take one step east.'''
    return (1, 0)

def west():
    '''Take one step west.'''
    return (-1, 0)

def pa_step():
    '''Take a step in any of the directions with equal probability.'''
    return random.choice([north(), east(), south(), west()])

def mi_ma_step():
    '''Take a step in any of the directions, with south being twice as likely as others.'''
    return random.choice([north(), east(), south(), south(), west()])

def reg_step():
    '''Take a step east or west with equal probability.'''
    return random.choice([east(), west()])

def scale():
    '''A global constant.'''
    return 5

def trial(length, walker):
    '''Execute a trial. Return the scaled position.'''
    x_pos = 0
    y_pos = 0
    for _ in range(length):
        x_delta, y_delta = walker()
        x_pos += x_delta
        y_pos += y_delta
    return (x_pos, y_pos)

def walk(length, trials, walker):
    '''Perform the specified number of trials.'''
    return [trial(length, walker) for _ in range(trials)]

def plot_dests(dests):
    '''Go to each destination and stamp the turtle.'''
    for dest in dests:
        (x_pos, y_pos) = dest
        turtle.goto(x_pos * scale(), y_pos * scale())
        turtle.stamp()

def plot(dest='random_walk.png'):
    '''Perform one experiment of 50 trials of length 100 for each walker. Plot the destinations.'''
    walk_length = 100
    trials = 50
    turtle.Screen().setup(300, 400)
    turtle.speed(0)
    turtle.penup()
    turtle.shapesize(0.5, 0.5)
    turtle.shape('circle')
    turtle.color('black')
    plot_dests(walk(walk_length, trials, pa_step))
    turtle.shape('square')
    turtle.color('green')
    plot_dests(walk(walk_length, trials, mi_ma_step))
    turtle.shape('triangle')
    turtle.color('red')
    plot_dests(walk(walk_length, trials, reg_step))
    save_to_image(dest)

def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to 'random_walk.png'. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        subprocess.run(['gs', '-dSAFER', '-o', dest, '-r200', '-dEPSCrop', '-sDEVICE=png16m', tmp.name], stdout=subprocess.DEVNULL)

def distance(pos):
    '''Compute the euclidean distance of pos from the origin.'''
    (x_pos, y_pos) = pos
    return math.sqrt(x_pos ** 2 + y_pos ** 2)

def simulate(walk_lengths, trials, walker_str):
    '''Perform the specified simulation.'''
    pa_pair = (pa_step, 'Pa')
    mi_ma_pair = (mi_ma_step, 'Mi-Ma')
    reg_pair = (reg_step, 'Reg')
    walkers_lookup = {'Pa': [pa_pair],
                      'Mi-Ma': [mi_ma_pair],
                      'Reg': [reg_pair],
                      'all': [pa_pair, mi_ma_pair, reg_pair]}
    for walker, name in walkers_lookup[walker_str]:
        for walk_length in walk_lengths:
            dests = walk(walk_length, trials, walker)
            distances = list(map(distance, dests))
            print(f'{name} random walk of {walk_length} steps')
            mean = statistics.mean(distances)
            print(f'Mean = {mean:.1f} CV = {statistics.stdev(distances)/mean:.1f}')
            print(f'Max = {max(distances):.1f} Min = {min(distances):.1f}')

def main():
    '''Read parameters from sys.argv, run simulate(), and then run plot().'''
    if len(sys.argv) != 4:
        print('Usage: python3 random_walk.py <walk,lengths> <trials> <walker>')
        return
    (length_str, trial_str, walker_str) = sys.argv[1:]
    lengths = [int(length) for length in length_str.split(',')]
    trials = int(trial_str)
    simulate(lengths, trials, walker_str)
    plot()

if __name__ == '__main__':
    main()
