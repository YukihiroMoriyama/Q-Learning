# coding: utf-8

from agent import Agent
from world import World

def main():
    agent = Agent()
    world = World()

    for i in range(10000):
        update(agent, world)
    print agent.Q


def update(agent, world):
    s1 = world.get_state()
    a = agent.take_action()
    world.set_action(a)
    s2 = world.get_state()
    r = world.get_reward()

    agent.learning(s1, a, s2, r)

if __name__ == '__main__':
    main()
