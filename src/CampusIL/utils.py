import numpy as np
import math

def expect_assert(fn, *args):
  try:
    fn(*args)
  except AssertionError:
    return True
  return False

def squarred_error(y_hat, y):
  return (y-y_hat)**2

def abs_error(y_hat, y):
  return abs(y-y_hat)
