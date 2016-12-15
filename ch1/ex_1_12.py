# Problem: You have a sequence of items and you'd like to determine the most requently occurring items in the sequence
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', 'do', 'not', 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', 'you', 'are', 'under'
                                    ]
from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
