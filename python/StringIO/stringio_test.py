#!/usr/bin/env python

from six import StringIO
from six import print_

output = StringIO()
output.write('First line.\n')
print_('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()
print(contents)

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()
