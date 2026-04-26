import numpy as np
<<<<<<< HEAD
<<<<<<< HEAD
=======
import math
>>>>>>> 95fd60708e045ca4de71da43c13ae344f9cc4d05
=======
import math
>>>>>>> 95fd60708e045ca4de71da43c13ae344f9cc4d05

def expect_assert(fn, *args):
  try:
    fn(*args)
  except AssertionError:
    return True
  return False

<<<<<<< HEAD
<<<<<<< HEAD

def _close(a, b, tol=1e-6):
    return abs(float(a) - float(b)) <= tol

def _allclose(a, b, tol=1e-6):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    return bool(np.all(np.abs(a-b) <= tol))
=======
=======
>>>>>>> 95fd60708e045ca4de71da43c13ae344f9cc4d05
def squarred_error(y_hat, y):
  return (y-y_hat)**2

def abs_error(y_hat, y):
  return abs(y-y_hat)
<<<<<<< HEAD
>>>>>>> 95fd60708e045ca4de71da43c13ae344f9cc4d05
=======
>>>>>>> 95fd60708e045ca4de71da43c13ae344f9cc4d05
