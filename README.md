# Spellcheck
An experiment with autocorrect. Prunes the search space
of possible corrections with a few heuristics.
You can test this with the following command:

    python3 tester.py [dictionary.txt]

Where `dictionary.txt` is a file of newline
separated words.

- If we assume that a single letter was mistyped,
we only try to replace it with letters physically
close to it on a QWERTY keyboard.
- If we try to add a single letter, we search for
matches through a prefix tree, and prune when
we know no valid word could be formed.

These approaches drastically cut down the search
space and can potentially be improved to search
a broader set of nodes. This remains as future
work.

Example:

![Autocorrection](https://github.com/jessrenteria/autocorrect/blob/master/media/example.png)
