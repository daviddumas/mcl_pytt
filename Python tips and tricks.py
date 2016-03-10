
# coding: utf-8

# # Python tips and tricks
# MCL Tutorial / Spring 2016 / David Dumas <david@dumas.io>
# 
# ## Inspired by / see also
# 
# * R. Hettinger's PyCon 2013 presentation "Transforming code into Beautiful, Idiomatic Python"
# 
#   * [slides](https://speakerdeck.com/pyconslides/transforming-code-into-beautiful-idiomatic-python-by-raymond-hettinger-1)
#   * [video](http://www.youtube.com/watch?v=OSGv2VnC0go)
#   * [notes & code as github repo, by Jeff Paine](https://gist.github.com/JeffPaine/6213790)
# * D. Beazley and B. Jones, _Python Cookbook_, 3ed.  O'Reilly, 2013.
#   * [O'Reilly page](http://shop.oreilly.com/product/0636920027072.do)
#   * [Amazon](http://www.amazon.com/Python-Cookbook-Third-David-Beazley/dp/1449340377)
#   
# ## Warning
# 
# This presentation is about Python 3 (mostly 3.3+).  Most of the tips apply to Python 2, sometimes requiring minor changes to syntax or names.
# 
# However, let's be clear:  Python 3 is the present and the future.  Python 2 is the past.  Use Python 3.
# 
# *Python 2 is the Windows XP of the Python world.*

# ---
# ## Python delivered, free
# 
# * [Sage Math Cloud](cloud.sagemath.com)
# * [PythonAnywhere](https://www.pythonanywhere.com/)
# 
# ## Takeout
# 
# * [Anaconda](https://www.continuum.io/downloads) -- Python + many common scientific libraries, packaged for easy installation on Windows, Mac, Linux.  Easiest way for most users to go to from "zero to python" in a few minutes.
# * [Official installers](https://www.python.org/downloads/) from `python.org`

# ---
# # Use the iterator protocol
# 
# If `range()` and `len()` appear regularly in your code, there is probably a better way!

# In[ ]:

L = ['lion','zebra','bear','asp']

# Don't do this
for i in range(len(L)):
    print(L[i])


# In[ ]:

# Instead, do this
for x in L:
    print(x)


# In[ ]:

# Better yet
zoo = ['lion','zebra','bear','asp']
for animal in zoo:
    print(animal)


# Advantage: **for object in collection** is flexible, expresses intent, avoids need for index variable

# In[ ]:

# works for unordered collections, too
teams = set(['White Sox', 'Cubs','Yankees','Red Sox']) # equivalent to above
teams = { 'White Sox', 'Cubs' ,'Yankees','Red Sox'}
for t in teams:
    print(t)


# ---
# # Aside: `set`, an unordered collection of distinct elements

# In[ ]:

L = [1,2,3,3,3]
set(L)  # set constructed from a list


# In[ ]:

type({})    # empty dict


# In[ ]:

type(set())  # empty set


# In[ ]:

A = {1,2,3,3,999}
B = {4,5,6,6,999}
A | B  # union


# In[ ]:

A & B  # intersection


# In[ ]:

A - B  # difference


# In[ ]:

S = {'alpha', 'gamma'}
S.update( {'beta'} )    # equivalent to S = S | {'beta'}
S


# ---
# # Back to iteration.
# 
# # If you realy need the index: `enumerate`

# In[ ]:

L = ['lion','zebra','bear','asp']

# Ask for it
for i,x in enumerate(L):
    print('Animal with index {} is: {}'.format(i,x))


# ---
# # Iterating over sorted collection:  `sorted`

# In[ ]:

L = ['lion','zebra','bear','asp']

for x in sorted(L):
    print(x)


# ---
# # Custom sort: `key`
# 
# `key` is an optional keyword parameter of sorted, is applied to each element of L before comparisons

# In[ ]:

L = ['lion','zebra','bear','asp']

print('Animals by length of name:')
for x in sorted(L,key=len):
    print(x)

    
print('\nAnimals by number of "e"s:')
num_e = lambda s:s.count('e')
for x in sorted(L,key=num_e):
    print(x)


# ## Also operating on iterables (lists, sets, etc):
# 
# * `all` : cast to boolean and take logical and
# * `any` : cast to boolean and take logical or
# * `min`, `max` : These accept `key`, like `sorted`
# * `sum`

# ---
# # Iterating over dictionaries

# In[ ]:

d = {'a': 1, 'b': 2, 'c': 8675309}

for k in d:    # iterates over KEYS
    print(k)


# In[ ]:

d = {'a': 1, 'b': 2, 'c': 8675309}

for k in d:
    print(d[k])


# If you really want keys and values together: `items()`

# In[ ]:

d = {'a': 1, 'b': 2, 'c': 8675309}

for k,v in d.items():
    print(k,'->',v)


# Related: Testing membership tests **keys**

# In[ ]:

d = {'a': 1, 'b': 2, 'c': 8675309}

8675309 in d


# ---
# # Extended slice syntax

# In[ ]:

L = ['Mathematical','science','is','in','my',
     'opinion','an','indivisible','whole']


# In[ ]:

L[0]  # First element


# In[ ]:

L[-1] # Last element


# In[ ]:

L[:-1] # All elements except the last (drop one from the end)


# In[ ]:

L[2:-1] # Drop two from the start, one from the end


# In[ ]:

L[::2] # Every other element (steps of 2)


# In[ ]:

L[::-1] # Reversed list (steps of -1)


# In[ ]:

L[-2:1:-1] # Reversed list, except first and last elements


# ---
# # Use tuple unpacking

# In[ ]:

f = (34,8812,'Anne Example')  # Maybe this came from a file or database query
age = f[0]
idnum = f[1]
name = f[2]

name


# In[ ]:

# Better
age, idnum, name = (34,8812,'Anne Example')

name


# ---
# # List and generator comprehensions

# In[ ]:

# Squares of integers congruent to 2 mod 7
[ x*x for x in range(100) if x % 7 == 2 ]


# In[ ]:

( x*x for x in range(100) if x % 7 == 2 )


# In[ ]:

# Generate the whole list, then iterate over it
for y in [ x*x for x in range(100) if x % 7 == 2 ]:
    print(y)


# In[ ]:

# Generate elements one by one, run loop body as they are produced
for y in ( x*x for x in range(100) if x % 7 == 2 ):
    print(y)


# Generators are instances.  They can be assigned.  However, they are single-use.

# In[ ]:

G = ( x*x for x in range(100) if x % 7 == 2 )
for x in G:
    print('foo')
for x in G:  # Iteration already ended; will not run
    print('bar')


# A function which creates and returns a list can often be replaced by a generator.
# Statement `yield x` replaces "append x to the list we will later return".

# ---
# # Gems from the `collections` module

# ## `namedtuple`:  creates a class which behaves like a `tuple` (immutable ordered collection), but whose entries have names as well as indices.

# In[ ]:

from collections import namedtuple

PersonDatum = namedtuple('PersonDatum',['age','idnum','name'])

F = PersonDatum(34,8812,'Anne Example')
F


# In[ ]:

print(F.age)
print(F.idnum)
print(F.name)


# Alternative: A dict with keys 'age', 'idnum', 'name'.  *How to choose?*
# 
# * A dict is not a bad choice.
# * Use `namedtuple` when the keys/attributes are **fixed** and will available in a fixed **order**.

# ## `defaultdict`: a dictionary where missing keys are assigned a default value on first use
# 
# Example: quick word length histogram

# In[ ]:

# Instead of this...
counts = {}
L = ['Mathematical','science','is','in','my',
     'opinion','an','indivisible','whole']

for word in L:
    n = len(word)
    if n not in counts:
        counts[n] = 0
    counts[n] += 1

for l,count in counts.items():
    print(count,'words of length',l)


# In[ ]:

# A defaultdict makes it a bit cleaner
from collections import defaultdict
counts = defaultdict(int)
L = ['Mathematical','science','is','in','my',
     'opinion','an','indivisible','whole']

for word in L:
    n = len(word)
    counts[n] += 1

for l,count in counts.items():
    print(count,'words of length',l)


# Passing `int` as the parameter to `defaultdict` means that `int()` is called to generate a new value when an unknown key is accessed.  Since `int()` returns zero, this means the default zero is zero.

# Drop in `defaultdict(list)` and now the same code *groups* words by their length.

# ## Also from `collections`:
# 
# * `OrderedDict` : Dictionary which remembers order in which keys were added, uses this order for iteration
# * `deque` : Like a list, but removing the first element is **not** an expensive operation

# ---
# # Gems from the `itertools` module

# ## built-in, but related: `zip`

# In[ ]:

L = [1,   2,   3,   5,  8, 13 ]
M = ['a', 'b', 'c', 'd']
N = ['foo','bar']
for l,m,n in zip(L,M,N):
    print(l,'-',m,'-',n)


# ## `groupby`
# 
# Take an iterator, return iterators over longest runs in which some quantity is constant

# In[ ]:

from itertools import groupby

L = ['Mathematical','science','is','in','my',
     'opinion','an','indivisible','whole']
for l,words in groupby(L,len):
    print('Found a run of words of length',l,':',list(words))


# ## permutations

# In[ ]:

from itertools import permutations

L = [1,2,3,4]
list(permutations(L))


# In[ ]:

L = [1,2,3,4]
list(permutations(L,2))


# ## combinations

# In[ ]:

from itertools import permutations

L = [1,2,3,4]
list(combinations(L,2))


# # Useful decorators
# 
# Modify a function's behavior.  (They are functions that map functions to functions.)

# ## `functools.lru_cache`

# Suppose you have a function which is expensive, but which will be called many times with the same arguments.

# In[ ]:

# Simple
def long_running(n):
    # expensive computation
    return result


# In[ ]:

# Better, use caching
def long_running(n,cache={}):
    if n in cache:
        return cache[n]
    else:
        # expensive computation
        cache[n] = result
        return result


# In[ ]:

# Cleaner and imposes size limits
from functools import lru_cache

@lru_cache(maxsize=128)
def long_running(n):
    # expensive computation
    return result

long_running(123)  # Will take a long time
long_running(123)  # Will return instantly


# ## Others (OO)
# * `staticmethod` : method with no "self"; can treat asclass as a "bag of functions"
# * `classmethod` : method that gets class (not instance) as first parameter; useful for alternate constructors
# * `property` : zero-parameter method turns into a computed attribute, i.e. `A.foo` instead of `A.foo()`

# # Use keyword arguments for clarity

# In[ ]:

move_data('asd.dat','jkl.dat',True)
# Moved... where?  What's the source?  And what is "True" for?
# Did I just overwrite my priceless data?


# In[ ]:

move_data(source='asd.dat',dest='jkl.dat',overwrite_existing=True)


# # Use context managers for file I/O
# 
# The file is closed on exit from the with-block (e.g. normally or by exception)

# In[ ]:

with open('out.txt','wt') as outfile:
    outfile.write('First line\n')
    risky_operation()  # possible exception terminates program?
    outfile.write('Possible second line\n')


# # Error suppression context manager
# 
# Possibly more readable than a bunch of try...except pass blocks

# In[ ]:

from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove('does_not_exist.dat')


# # Assertions
# 
# Not very popular in the Python community, but can be useful for debugging.  Assertion checking can be disabled with the '-O' command-line parameter.

# In[ ]:

assert True, 'no problem'
assert False, 'big problem'


# Assertions should be reserved for statements that will be true unless a contract has been broken, so that it would not make sense to continue.  Assertions are not for catching routine errors.

# In[ ]:

def handle_everything():
    queue = get_work_queue()
    queue.process_all_events()
    assert queue.is_empty(), 'Queue not empty after process_all_events()"
    cleanup()


# * If the condition shows that an error has occurred, raise an exception
# * If the condition shows that a bug is present, *maybe* check it with an assertion

# In[ ]:



