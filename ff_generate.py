# ff_generate.py
# Usage: fontforge -script ff_generate.py source output

from __future__ import print_function

import sys
import datetime
import codecs
import fontforge

argvs = sys.argv
argc = len(argvs)

if (argc != 3):
  print("Usage: fontforge -script ff_generate.py source_file output_file")
  quit()

[source_file, output_file] = argvs[1:]

f = fontforge.open(source_file)

today = datetime.date.today()
version = str(today.year - 2000) + '.' + str((today - datetime.date(today.year, 1, 1)).days)
f.version = version
f.sfnt_names += (('Japanese', 'Version', 'Version ' + version),)
for (language, license_file) in [('English (US)', 'LICENSE'), ('Japanese', 'LICENSE.ja'),]:
  try:
    license = codecs.open(license_file, 'r', 'utf-8').read().encode('utf-8')
    f.sfnt_names += ((language, 'License', license),)
  except IOError, (errno, strerror):
    print('cannot open %s' % license_file)

f.hasvmetrics = True

f.generate(output_file, '', ('short-post','opentype'))
