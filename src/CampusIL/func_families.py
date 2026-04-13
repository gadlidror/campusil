
# Function Family of the form wx + b
class Line():
  def __init__(self, w, b):  # a, b must be numbers
    assert isinstance(w, (int, float)), "a should be a number"
    assert isinstance(b, (int, float)), "b should be a number"

    self._w = w
    self._b = b

  def __str__(self):
    return f'w = {self._w}, b = {self._b}'

  def __call__(self, x):
    return self._w*x + self._b



# Function Family of the form ax^2 + bx + c
class Square():
  def __init__(self, a, b, c):  # a, b, c must be numbers
    assert isinstance(a, (int, float)), "a should be a number"
    assert isinstance(b, (int, float)), "b should be a number"
    assert isinstance(c, (int, float)), "c should be a number"

    self._a = a
    self._b = b
    self._c = c

  def __str__(self):
    return f'a = {self._a}, b = {self._b}, c = {self._c}'

  def __call__(self, x):
    return self._a*x**2 + self._b*x + self._c


# Function Family of a polynom
class Poly():
  def __init__(self, W, b):  # W is a list of parameters, b is a number
    assert isinstance(W, list), "W is a list of parameters"
    assert isinstance(b, (int, float)), "b should be a number"
    assert (isinstance(x, (int, float)) for x in W), "W elements must be numbers"

    self._W = W.copy()  # avois aliasing the input list
    self._W.insert(0, b)    # add the bias term to the list of parameters

  def __str__(self):
    return f'a = {self._W}, b = {self._b}, c = {self._c}'

  def __call__(self, x):
    """
    Compute the polinum when the parameters are 
    W ( a list of parameters), and b, and the input is x.
    W: [a0, a1, a2, ...] כלומר a0*x + a1*x^2 + ...
    b: a number, the bias term
    x: מספר
    """
    result = 0
    for a in reversed(self._W):
        result = result * x + a
    return result + self._b

"""
# Function Family of Loss (error) functions
class Loss():
  def __init__(self, xi, yi):  # a, b, c must be numbers
    assert isinstance(xi, (int, float)), "a should be a number"
    assert isinstance(yi, (int, float)), "b should be a number"

    self._xi = xi
    self._yi = yi

  #def __str__(self):
  #  return f'xi = {self._xi}, yi = {self._yi}'
    def __call__(self, y_real, y_pred):
"""
