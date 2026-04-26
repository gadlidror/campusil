import numpy as np
import math

def expect_assert(fn, *args):
  try:
    fn(*args)
  except AssertionError:
    return True
  return False

def _close(a, b, tol=1e-6):
    return abs(float(a) - float(b)) <= tol

def _allclose(a, b, tol=1e-6):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    return bool(np.all(np.abs(a-b) <= tol))

def squarred_error(y_hat, y):
  return (y-y_hat)**2

def abs_error(y_hat, y):
  return abs(y-y_hat)
