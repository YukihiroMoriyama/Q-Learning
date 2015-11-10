# coding: utf-8

import random

class Agent:
    def __init__(self):
        self.Q = [[0 for i in range(2)] for j in range(5)]
        self.learning_rate = 0.1 # 学習率
        self.gamma = 0.99 # 割引率

    def take_action(self):
        return random.randint(0, 1)

    def learning(self, s1, a, s2, r):
        before = (1 - self.learning_rate) * self.Q[s1][a]
        after = self.learning_rate * (r + self.gamma * self.getMaxQ(s2))
        self.Q[s1][a] = before + after

    def get_maxQ(self, s):
        q1 = self.Q[s][0]
        q2 = self.Q[s][1]
        if (q1 > q2):
            return q1
        return q2
