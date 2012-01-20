all: Mutsuki.ttf Mutsuki.woff

Mutsuki.ttf: Mutsuki.sfd ff_generate.py LICENSE LICENSE.ja
	fontforge -lang=py -script $(word 2, $^) $< $@

Mutsuki.woff: Mutsuki.sfd ff_generate.py LICENSE LICENSE.ja
	fontforge -lang=py -script $(word 2, $^) $< $@


