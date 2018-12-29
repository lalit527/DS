def new_decorator(fn):
  def wrapper():
    print("Before Executing")
    fn()
    print("After Executing")
  return wrapper

def fn_needs_decorator():
  print("This function will need Decorator")

# fn_needs_decorator()

fn_needs_decorator = new_decorator(fn_needs_decorator)
fn_needs_decorator()

# Single Line for above FP

@new_decorator
def fn_needs_decorator2():
  print("This function will need Decorator")

fn_needs_decorator2()