import pygame
import random

width = 600
height = 600
window = pygame.display.set_mode((width, height))
arr = random.sample(range(height), width)
i = 0

def show():
    i = 0
    while(i<width):
        pygame.draw.rect(window, (255, 0, 0), (i, 0, 1, arr[i]))
        i+=1
        pygame.display.update()

def bubble_sort(arr, itr=False):
    if(itr):
        show()
    n = len(arr)
    while n:
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
            if (itr):
                show()
        n -= 1
    return arr

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
    bubble_sort(arr, True)

pygame.quit()
