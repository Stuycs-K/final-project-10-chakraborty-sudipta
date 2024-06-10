# Work Log

## Sudipta Chakraborty

### 6/3/24 - 6/4/24

Did premliminary research on the topic and possible implementations. Settled on creating an implementation of the Solitaire Cipher, with an encoder, decoder, and a cracker (if possible) to accompany it.

### 6/5/24
Setup initial project directory structure. It seems that a cracker won't be possible for this, as the insecurity of the cipher comes from a bias that shows up, rather than something like frequency analysis.

### 6/6/24
Continued work on the encoder, keystream generation, deck keying, and general purpose functions for moving the deck around.
This was around the day when I started having issues with uploading my work to github, so commits from here on out were 
either delayed or did not show up on github and had to be transferred between my laptop and desktop instead. Contacted github support.

### 6/7/24
Finished work on the deck movement, and implemented the usage of a modified Solitaire process to turn a key phrase into a keyed deck.
Additionally implemented the first parts of the encoding process.

### 6/8/24 - 6/9/24
Finally received a response from github support regarding not being able to commit on
my account, and uploaded work after some time spent unifying the code between my laptop
and my desktop. This time was mostly spent tying everything up, creating the demonstration
for the cipher itself, and other final stuff.

### References Used
[Explanation used for Solitaire Cipher](https://www.schneier.com/academic/solitaire/)
<br> *This was the reference mostly used throughout the project, since it comes from the creator himself.*

[Paul Crowley's analysis of Solitaire Cipher](http://www.ciphergoth.org/crypto/solitaire/)

