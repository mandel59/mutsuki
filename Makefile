all: Mutsuki.ttf Mutsuki.woff Mutsuki.woff2

clean:
	rm -f Mutsuki.ttf Mutsuki.woff Mutsuki.woff2

.PHONY: all clean

Mutsuki.ttf: Mutsuki.sfd ff_generate.py LICENSE LICENSE.ja
	fontforge -lang=py -script $(word 2, $^) $< $@

Mutsuki.woff: Mutsuki.sfd ff_generate.py LICENSE LICENSE.ja
	fontforge -lang=py -script $(word 2, $^) $< $@

Mutsuki.woff2: Mutsuki.ttf
	woff2_compress $<
