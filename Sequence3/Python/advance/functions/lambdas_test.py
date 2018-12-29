def test():
  scientists = ['Marie Curie', 'Albert Einstien', 'Niels Bohr']
  return sorted(scientists, key=lambda name: name.split()[-1])