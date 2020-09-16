import pygame
import random
import time

class display:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    PURPLE = (255, 0, 255)
    BACKGROUND = BLACK

    def __init__(self, width=600, height=600, number_of_elements=100, repeats=True):
        if (number_of_elements > width):
            raise ValueError("Wisplay width must be larger than number of elements")
        self.width = width
        self.height = height
        self.number_of_elements = number_of_elements
        self.div = width//number_of_elements
        self.repeats = repeats
        
        if self.repeats:
            self.array = [random.randint(0, self.height) for _ in range(self.number_of_elements)]
        else:
            self.array = random.sample(range(0,self.height), self.number_of_elements)

    def show(self, p=-1):
        pygame.draw.rect(self.window, self.BACKGROUND, (0, 0, self.width, self.height))
        i, j = 0, 0
        while(i<self.width):
            if self.array[j] != float('inf'):  # cycle sort
                pygame.draw.rect(self.window, (255, 255, 255), (i, 0, self.width//self.number_of_elements, self.array[j]))
            i += self.div
            j += 1
        if (p != -1):
            pygame.draw.rect(self.window, (0, 255, 0), (self.div*p, 0, self.width//self.number_of_elements, self.array[p]))
        pygame.display.update()
        # TODO: add color selection

    def make_window(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        # make wrapper

    def close_window(self):
        pygame.quit()

    def bubble_sort(self):
        random.shuffle(self.array) # TODO: join in algo_init
        self.make_window()  # TODO: put in algo_init

        n  = self.number_of_elements
        while(n):
            for i in range(1, n):
                if self.array[i-1] > self.array[i]:
                    self.array[i-1], self.array[i] = self.array[i], self.array[i-1]
                    self.show(i)
            n -= 1
        self.close_window()
    
    def insertion_sort(self):
        random.shuffle(self.array)
        self.make_window()
        for i in range(1, self.number_of_elements):
            p = i
            while(p > 0 and self.array[p-1] > self.array[p]):
                self.array[p-1], self.array[p] = self.array[p], self.array[p-1]
                self.show(p)
                p -= 1
        self.close_window()

    def bogo_sort(self, optimize=True):
        self.make_window()
        random.shuffle(self.array)

        s_arr = sorted(self.array)

        if optimize:
            n = 0
            while(n < self.number_of_elements):
                copy = self.array[n:]
                random.shuffle(copy)
                self.array[n:] = copy
                # random.shuffle(self.array[n:])
                self.show()
                # self.array[n:] = copy
                if self.array[n] == s_arr[n]:
                    n += 1
        # self.close_window()
        else:
            while(self.array != sorted(self.array)):
                random.shuffle(self.array)
                self.show()
        time.sleep(5)

    def selection_sort(self):
        random.shuffle(self.array)
        self.make_window()
        n = 0
        while n < len(self.array):
            min_index = n
            for i in range(n, self.number_of_elements):
                if self.array[i] < self.array[min_index]:
                    min_index = i
            self.array[n], self.array[min_index] = self.array[min_index], self.array[n]
            self.show()
            n += 1
        self.close_window()

    def cycle_sort(self):
        random.shuffle(self.array)
        self.make_window()
        pos = 0
        i = self.array[pos]
        while pos < len(self.array) - 1:
            changed = False
            counter = 0
            for val in self.array[pos:]:
                if val < i:
                    counter += 1
                    changed = True
            if changed:
                while self.array[pos + counter] == i:  # for duplicates
                    counter += 1
                i, self.array[pos + counter] = self.array[pos + counter], i
                self.array[pos] = float('inf')
            else:
                if self.array[pos + counter] == float('inf'):
                    self.array[pos + counter] = i
                pos += 1
                i = self.array[pos]            
            self.show()

    def pancake_sort(self):
        random.shuffle(self.array)
        self.make_window()
        cur = 0
        length = len(self.array)
        while cur < length:
            min_idx = self.array[cur:].index(min(self.array[cur:])) + cur
            if cur != min_idx:  # or remove +cur and check min_idx != 0
                if min_idx != length - 1:
                    self.array[min_idx:] = reversed(self.array[min_idx:])
                    self.show()
                self.array[cur:] = reversed(self.array[cur:])
                self.show()
            cur += 1

if __name__ == '__main__':
    win = display(number_of_elements=1000, width=1000, height=1000)
    # print(win.array)
    # win.cycle_sort()
    win.pancake_sort()
    # win.selection_sort()
    # win.bogo_sort()
    # win.bubble_sort()
    # win.insertion_sort()