
def expect_assert(fn, *args):
  try:
    fn(*args)
  except AssertionError:
    return True
  return False
