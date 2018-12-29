def escape_unicode(f):
  print(f)
  def wrap(*args, **kwargs):
    print(args)
    print(kwargs)
    x = f(*args, **kwargs)
    return ascii(x)
  return wrap

@escape_unicode
def northern_city():
  return 'Tromsø'

print(northern_city())