# Developed for the Natural Computing module, University of Greenwich.
# Based on starter code by Dr Mohammad Majid al-Rifaie.
# Algorithm: Dispersive Flies Optimisation, M. M. al-Rifaie (FedCSIS, 2014).


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
#import numpy as np

RUNS = 5
FILES = ['input1.png','input images/input2.png', 'input images/input3.png', 'input images/input4.png', 'input images/input5.png']


for name in FILES:
    img = mpimg.imread(name)
    imgW = len(img[0])
    imgH = len(img)
    print('****', name, '(****)')
    for run in range(RUNS):
       print('RUN:', run + 1, 'of', RUNS)

       flies = []
       for n in range(30):
          x = random.randint(0, imgW - 1)
          y = random.randint(0, imgH - 1)
          flies.append([x, y])
       plt.ion()
       for i in range(1000):
          if i == 250:
             img = mpimg.imread(FILES[1])
             print('Image switched to input 2 <3')
          if i == 500:
             img = mpimg.imread(FILES[2])
             print('Image switched to input 3')
          if i == 750:
             img = mpimg.imread(FILES[3])
             print('Image switched to input 4 <3')
          if i == 900:
             img = mpimg.imread(FILES[4])
             print('Image switched to input 5')
          plt.imshow(img, cmap='gray') # SHOW IMAGE
          scores = []
          for fly in flies:
             scores.append(img[int(fly[1])][int(fly[0])])

          best = scores.index(max(scores))
          for n in range (len(flies)):
             if n == best:
                continue
             if random.random() < 0.05:
                flies[n] = [random.randint(0, imgW - 1), random.randint(0, imgH - 1)]
                continue
             for d in range(2):
                flies[n][d] = flies[n][d] + random.random()*(flies[best][d] - flies[n][d])
             scores.append(img[int(fly[1])][int(fly[0])])
          for fly in flies:
             plt.gca().add_patch(plt.Circle((fly[0], fly[1]), 5, color='red'))
          plt.gca().add_patch(plt.Circle((flies[best][0], flies[best][1]), 8, color='lime'))  # Step C

          print('Best fly:', best, 'at', flies[best], 'brightness', scores[best])  # Step D
          scores = [img[int(fly[1])][int(fly[0])] for fly in flies]
          best = scores.index(max(scores))
          plt.pause(0.1)
          plt.clf()
       print('best final position (x,y):', (int(flies[best][0]), int(flies[best][1])), 'Brightness:', scores[best])  # MOVED: indented so it prints after every run

plt.ioff()
plt.show()
