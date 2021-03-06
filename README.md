# Self-Pilot X Wing Programme
Can the force be with AI to destroy death star by deep learning?
Supervised machine learning to self-pilot X-wing and travel back and forth in the battlefront.

Model developed using Tensorflow.

This repo is cross-post in STEEMIT platform by author Jimsparkle

### TL;DR
The AI has been provided with only 1 hour of video of actual game play together with the corresponding keypress, and trains by tensorflow for 8 hours to pilot a X-Wing just by itself.

The AI achieves satisfactory result in preventing plane crash accident, while lacking capacity to deal effective demage to Imperial tie fighter.


**Entry to battle**

![Entry to battle](https://thumbs.gfycat.com/OnlyVengefulGelada-size_restricted.gif)

**Manoeuvre and auto balancing**

![Manoeuvre](https://thumbs.gfycat.com/HorribleFixedEidolonhelvum-size_restricted.gif)

**Evading Tie fighter from behind**

![Evade](https://thumbs.gfycat.com/PastWelcomeArcherfish-size_restricted.gif)

**Video highlight**

https://www.youtube.com/watch?v=NMZph_X9e8o

# Model and data:
The programme records the frame and the keypress from the game (around 10fps). The dataset is then processed by convolution neural network (see the network structure below).

Each frame is resized to 300 x 179.

I only use 1 hour to play this game to record some training data therefore the training set is rather small. This partially explain why the AI is not able to deal effective demage (my bad gaming skill also counts, I guess...).

![network](https://i.imgur.com/zshydnH.png)

# Issue
This game is a monster in consuming GPU and CPU power thus game and python crashed constantly. This made the data collecting process extremely hard, leading to failed initialization of cuDNN.

Therefore, compromise in underclocking GPU directly delayed AI/model reaction in real time.


# Some Citation:
#### Idea and model are inspired and originated by Sentdex self-driving programme.(https://github.com/sentdex/pygta5/)

Screen capture code is developed by Frannecklp

Key input tracking code is developed by Box Of Hats (https://github.com/Box-Of-Hats )
