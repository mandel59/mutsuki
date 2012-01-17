Mutsuki.ttf: Mutsuki.sfd ff_generate.py LICENSE LICENSE.ja
	fontforge -lang=py -script $(word 2, $^) $< $@

