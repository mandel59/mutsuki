#!/usr/bin/fontforge -lang=py -script
# -*- coding: utf-8 -*-

u"""
ff_generate.py フォント生成スクリプト

使い方: fontforge -script ff_generate.py source output
"""

from __future__ import print_function

import sys
import datetime
import codecs
import fontforge


def font_version(date):
    # type: (date) -> str
    u"与えられた日付に生成されるフォントのバージョンを返す"
    return str(date.year - 2000) + '.' + str((date - datetime.date(date.year, 1, 1)).days)


def generate_font(source_path, dest_path):
    # type: (str, str) -> None
    u"フォントを生成する"
    font = fontforge.open(source_path)
    version = font_version(datetime.date.today())
    font.version = version
    font.sfnt_names += (('Japanese', 'Version', 'Version ' + version),)
    for (language, license_file) in [('English (US)', 'LICENSE'), ('Japanese', 'LICENSE.ja'), ]:
        try:
            license_text = codecs.open(
                license_file, 'r', 'utf-8').read().encode('utf-8')
            font.sfnt_names += ((language, 'License', license_text),)
        except IOError:
            print('cannot open %s' % license_file)
    font.hasvmetrics = True
    font.generate(dest_path, '', ('short-post', 'opentype'))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: fontforge -script ff_generate.py SOURCE_FILE OUTPUT_FILE")
        quit()
    SOURCE_PATH = sys.argv[1]
    DEST_PATH = sys.argv[2]
    generate_font(SOURCE_PATH, DEST_PATH)
