"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""

def foo(x):
  if x <= 1:
    return x
  else:
    return (foo(x-1)) + (foo(x-2))

def longest_run(mylist, key):
  count = 0
  max_val = 0
  for i in mylist:
    count = count +1 if i == key else 0
    max_val = max(count, max_val)
  return max_val

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
def longest_run_recursive(mylist, key):
  if len(mylist) == 1:
    return 0
  return (mylist[0] == key) + longest_run_recursive(mylist[1:], key)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


