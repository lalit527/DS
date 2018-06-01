import os
import sys

def disk_usage(path):
  total = os.path.getsize(path)
  if os.path.isdir(path):
    for filename in os.listdir(path):
      childpath = os.path.join(path, filename)
      total += disk_usage(childpath)

  print('{0:<7}'.format(total), path)
  return total


sys.setrecursionlimit = 100000000
print(os.path.dirname(os.path.realpath(__file__))) # current file-path
print(disk_usage('/Users/lality/projects/personal/'))
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

# print(get_size('/Users/lality/projects/personal/'))
