import sys
import datetime
import codecs
import fontforge
argvs = sys.argv
argc = len(argvs)
if (argc != 3):
  quit()
f = fontforge.open(argvs[1])
today = datetime.date.today()
version = str(today.year - 2000) + '.' + str((today - datetime.date(today.year, 1, 1)).days)
f.version = version
f.sfnt_names = f.sfnt_names + (('Japanese', 'Version', 'Version ' + version),)
for x in [('English (US)', 'LICENSE'), ('Japanese', 'LICENSE.ja'),]:
  try:
    license = codecs.open(x[1], 'r', 'utf-8').read().encode('utf-8')
    f.sfnt_names = f.sfnt_names + ((x[0], 'License', license),)
  except IOError, (errno, strerror):
    print 'cannot open ' + x[1]

f.generate(argvs[2], '', ('short-post','opentype'))

