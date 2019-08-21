all: mutsuki kana

mutsuki: Mutsuki.ttf Mutsuki.woff Mutsuki.woff2
kana: Mutsuki-kana.ttf Mutsuki-kana.woff Mutsuki-kana.woff2

clean:
	rm -f Mutsuki.ttf Mutsuki.woff Mutsuki.woff2

.PHONY: all mutsuki kana clean

Mutsuki.ttf: Mutsuki.sfd ff_generate.py LICENSE LICENSE.ja
	fontforge -lang=py -script ff_generate.py Mutsuki.sfd $@

Mutsuki.woff: Mutsuki.sfd ff_generate.py LICENSE LICENSE.ja
	fontforge -lang=py -script ff_generate.py Mutsuki.sfd $@

Mutsuki.woff2: Mutsuki.ttf
	woff2_compress Mutsuki.ttf

Mutsuki-kana.sfd: Mutsuki.sfd mutsuki-kana.pl
	perl mutsuki-kana.pl Mutsuki.sfd > $@

Mutsuki-kana.ttf: Mutsuki-kana.sfd ff_generate.py LICENSE LICENSE.ja
	fontforge -lang=py -script ff_generate.py Mutsuki-kana.sfd $@

Mutsuki-kana.woff: Mutsuki-kana.sfd ff_generate.py LICENSE LICENSE.ja
	fontforge -lang=py -script ff_generate.py Mutsuki-kana.sfd $@

Mutsuki-kana.woff2: Mutsuki-kana.ttf
	woff2_compress Mutsuki-kana.ttf
