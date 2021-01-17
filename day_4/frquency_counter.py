"""
passage: this is amazing this is so awesome i am really enjoying learning python and python is so amazing and python is very easy to use
{
    'this': 2
    'is': 2
    'amazing': 1
    'so': 1
}
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

passage = input()
words = passage.split()     # O(n)
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

"""
words = ['this', 'is', 'amazing', 'this', 'is', 'so', 'awesome', 'i', 'am', 'really', 'enjoying', 'learning', 'python', 'and', 
'python', 'is', 'so', 'amazing', 'and', 'python', 'is', 'very', 'easy', 'to', 'use']

freq = {
}

freq[this] = freq.get(this, 0) + 1
           = 0 + 1
           = 1
           = n + 1

"""

print(frequency)
