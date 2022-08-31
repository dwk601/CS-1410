import random
import statistics
import sys
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


class Walker:
    def __init__(self, name: str, icon: str, color: str, step: int):
        self.name = name
        self.icon = icon
        self.color = color
        self.step = step

    def random_step(self):
        if self.name == 'pa':
            return random.choice([north(), east(), south(), west()])
        elif self.name == 'mi_ma':
            return random.choice([north(), east(), south(), south(), west()])
        else:
            return random.choice([east(), west()])

    def trial(self, length: int):
        '''Execute a trial. Return the scaled position.'''
        x_pos = 0
        y_pos = 0
        for _ in range(length):
            x_delta, y_delta = self.random_step()
            x_pos += x_delta
            y_pos += y_delta
        return (x_pos, y_pos)

    def walk(self, length: int, trials: int):
        '''Perform the specified number of trials.'''
        return [self.trial(length) for _ in range(trials)]

    def plot_dests(self, dests: list):
        '''Go to each destination and stamp the turtle.'''
        for dest in dests:
            (x_pos, y_pos) = dest
            turtle.goto(x_pos * self.step, y_pos * self.step)
            turtle.dot(20, self.color)

    def plot_stats(self, dests: list):
        '''Plot the statistics of the destinations.'''
        x_pos = [dest[0] for dest in dests]
        y_pos = [dest[1] for dest in dests]
        x_mean = statistics.mean(x_pos)
        y_mean = statistics.mean(y_pos)
        x_std = statistics.stdev(x_pos)
        y_std = statistics.stdev(y_pos)
        turtle.goto(x_mean * self.step, y_mean * self.step)
        turtle.dot(20, self.color)
        turtle.goto(x_mean * self.step + x_std * self.step, y_mean * self.step)
        turtle.dot(20, self.color)
        turtle.goto(x_mean * self.step - x_std * self.step, y_mean * self.step)
        turtle.dot(20, self.color)
        turtle.goto(x_mean * self.step, y_mean * self.step + y_std * self.step)
        turtle.dot(20, self.color)
        turtle.goto(x_mean * self.step, y_mean * self.step - y_std * self.step)
        turtle.dot(20, self.color)

    def __str__(self):
        return self.name


class Field:
    def __init__(self, length: int, trials: int, walkers: list):
        self.length = length
        self.trials = trials
        self.walkers = walkers

    def run(self):
        for walker in self.walkers:
            dests = walker.walk(self.length, self.trials)
            walker.plot_dests(dests)
            walker.plot_stats(dests)
            turtle.done()

    def put(self, x, y):
        return self.put(x, y)

    def move(self, x, y):
        return self.move(x, y)

    def get(self, x, y):
        return self.get(x, y)

    def reset(self):
        return self.reset()

    def __str__(self):
        return self.put.__name__ + ' ' + self.move.__name__ + ' ' + self.get.__name__ + ' ' + self.reset.__name__


class Trial:
    def __init__(self, steps, walks, field):
        self.steps = steps
        self.walks = walks
        self.field = field

    def run(self):
        return self.field.put(0, 0)

    def walk(self):
        return self.field.move(0, 0)

    def get(self):
        return self.field.get(0, 0)

    def reset(self):
        return self.field.reset()

    def __str__(self):
        return self.steps + ' ' + self.walks + ' ' + self.field.__str__()


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)


def plot():
    '''Plot the field.'''
    turtle.screensize(canvwidth=1000, canvheight=1000)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-Walker.steps / 2, -Walker.steps / 2)
    turtle.pendown()
    turtle.color('black')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(Walker.steps)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.dot(20, 'red')
    turtle.penup()
    turtle.goto(Walker.steps / 2, Walker.steps / 2)
    turtle.pendown()
    turtle.dot(20, 'blue')
    turtle.penup()
    turtle.goto(Walker.steps / 2, -Walker.steps / 2)
    turtle.pendown()
    turtle.dot(20, 'green')
    turtle.done()


def simulate(steps, walks, field):
    '''Simulate the field.'''
    for _ in range(walks):
        for _ in range(steps):
            field.walk()
        field.get()
        field.reset()


def main():
    '''Main program.'''
    steps = int(sys.argv[1])
    walks = int(sys.argv[2])
    field = Field(steps, walks, [Walker('pa', 'P', 'red', steps), Walker(
        'mi_ma', 'M', 'blue', steps), Walker('ma', 'M', 'green', steps)])
    field.run()
    # plot()
    simulate(steps, walks, field)


if __name__ == '__main__':
    main()
    plot()
    turtle.done()
