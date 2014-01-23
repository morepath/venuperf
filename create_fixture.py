import shutil
import os
import sys

try:
    amount = int(sys.argv[1])
except (ValueError, IndexError):
    print "Usage: create_fixture.py <amount_of_modules>"
    sys.exit(1)

if os.path.isdir('fixture'):
    shutil.rmtree('fixture')

os.mkdir('fixture')

with open('fixture/__init__.py', 'w') as f:
    f.write("# init")

shutil.copy('dec.py', 'fixture/dec.py')

for i in range(amount):
    shutil.copy('module.py', 'fixture/module%04d.py' % i)

print "fixture package set up with %s modules" % amount
