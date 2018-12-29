def enclosing():
  x = 'closed_over'
  def local_fn():
    print(x)
  return local_fn

lf = enclosing()
lf()
print(lf.__closure__)


print("=================Verifying LEGB Rule=========================")

message = 'global'
def enclosing():
    message = 'enclosing'

    def local():  
        global message
        message = 'local'
    
    def local2():  
        nonlocal message
        message = 'test'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)
    local2()
    print('enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)


print("=================Closure Timer=========================")
import time

def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return elapsed

print("=================Raise To Closure=========================")
def raise_to(exp):
  def raise_to_exp(x):
    return pow(x, exp)
  return raise_to_exp