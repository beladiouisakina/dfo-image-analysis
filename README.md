
## Code walkthrough

1. **Setup:** `RUNS = 5` repeats the experiment five times per starting image. `FILES` lists the five input images. Each image is loaded with `mpimg.imread`, and its width and height are read from the array shape.
2. **Initialise the swarm:** 30 flies are created, each a pair `[x, y]` at a random position inside the image.
3. **Main loop (1000 iterations):** every iteration redraws the current image, then updates the swarm. At iterations 250, 500, 750 and 900 the image is replaced with a different one, so the swarm has to find the new bright spot.
4. **Fitness:** each fly's score is the pixel value under it, `img[y][x]`. The code assumes greyscale images, so a higher value means a brighter pixel.
5. **Pick the leader:** the fly with the highest score becomes `best`.
6. **Move the flies:** every fly except the leader either (a) with 5% probability jumps to a random position (the disturbance that keeps the swarm exploring), or (b) otherwise moves a random fraction of the distance toward the leader on both axes.
7. **Draw:** flies are drawn as red circles and the leader as a larger green circle, with a short pause so the animation is visible.
8. **Report:** after 1000 iterations the best final position `(x, y)` and its brightness are printed.

## Acknowledgements

- The Dispersive Flies Optimisation algorithm was introduced by Dr Mohammad Majid al-Rifaie: *Dispersive Flies Optimisation*, Proceedings of the Federated Conference on Computer Science and Information Systems (FedCSIS), 2014.
- This project was developed for the Natural Computing module at the University of Greenwich, starting from starter code and task descriptions provided by Dr al-Rifaie. I extended it myself, including the multi-image switching experiment and the animation.
