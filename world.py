# coding: utf-8

class World:
    def __init__(self):
        self.position = 0

    def set_action(self, a):
        if (a == 0): # Left
            self.position = self.position - 1
        if (a == 1): # Right
            self.position = self.position + 1
        if (self.position < 0):
            self.position = 0

    def get_state(self):
        return self.position

    def get_reward(self):
        if (self.position == 4):
            self.position = 0
            return 1
        return 0
