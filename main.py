# odprem datoteko
f = open('slovar_mini_unicode.txt', 'r', encoding='utf-8')

# preberem vrstice
lines = []
for line in f:
    lines.append(line)

podatek = {}
# prva vrstica vsebuje rubrike
first_line = lines[0]
# odstaniti moram znak za novo vrstico
first_line = first_line.replace('\n', '')
rubrike = first_line.split("\t")

# vsaki rubriki naredim prazen slovar
for p in rubrike[1:]:
    podatek[p] = {}

# v vsaki vrstici locim geslo_id in zaglavje
gesla_id = []
for line in lines[1:]:
    words = line.split("\t")
    geslo_id = words[0]
    zaglavje = words[1:]
    gesla_id.append(geslo_id)
    # posamezen element dam na pravo mesto
    for p, v in zip(rubrike[1:], zaglavje):
        podatek[p][geslo_id] = v


### PISANJE HTML DATOTEKE ###

d = open('slovar.html', 'w', encoding='utf-8')

# glava
d.write("""
<html xmlns:math="http://exslt.org/math" xmlns:svg="http://www.w3.org/2000/svg"
xmlns:tl="http://www.kreutzfeldt.de/tl"
xmlns:saxon="http://saxon.sf.net/" xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:cx="http://www.kreutzfeldt.de/mmc/cx"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:mbp="http://www.kreutzfeldt.de/mmc/mbp"
xmlns:mmc="http://www.kreutzfeldt.de/mmc/mmc"
xmlns:idx="http://www.mobipocket.com/idx">
    <head>
	    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    </head>
    <body>
    <mbp:frameset>
    """)

import inflect
p = inflect.engine()

for geslo_id in sorted(gesla_id):
    if podatek["BESEDNA_VRSTA"][geslo_id] == "noun":
        mnozina = p.plural(podatek["GESLO"][geslo_id])
        d.write("<idx:entry>\n<idx:orth><b>%s</b>\n<idx:infl>\n<idx:iform value=\"%s\"/>\n</idx:infl>\n</idx:orth>\n"
                "<p>%s <i style=\"color:#808080\">%s</i> %s</p>\n</idx:entry>\n\n" % (podatek["GESLO"][geslo_id], mnozina, podatek["IZGOVORJAVA"][geslo_id],podatek["BESEDNA_VRSTA"][geslo_id], podatek["RAZLAGA"][geslo_id].replace('"', '')))
    elif podatek["BESEDNA_VRSTA"][geslo_id] == "verb":
        present_participle = p.present_participle(podatek["GESLO"][geslo_id])
        past_participle = podatek["GESLO"][geslo_id] + "ed"
        third_singular = podatek["GESLO"][geslo_id] + "s"
        if podatek["GESLO"][geslo_id][-1] == "e":
            past_participle = podatek["GESLO"][geslo_id] + "d"

        d.write("<idx:entry>\n<idx:orth><b>%s</b>\n<idx:infl>\n"
                "<idx:iform value=\"%s\"/>\n"
                "<idx:iform value=\"%s\"/>\n"
                "<idx:iform value=\"%s\"/>\n"
                "</idx:infl>\n</idx:orth>\n"
                "<p>%s <i style=\"color:#808080\">%s</i> %s</p>\n</idx:entry>\n\n" % (podatek["GESLO"][geslo_id], present_participle, past_participle, third_singular, podatek["IZGOVORJAVA"][geslo_id],podatek["BESEDNA_VRSTA"][geslo_id], podatek["RAZLAGA"][geslo_id].replace('"', '')))
    else:
        d.write("<idx:entry>\n<idx:orth><b>%s</b>\n</idx:orth>\n<p>%s</p>\n</idx:entry>\n\n" % (podatek["GESLO"][geslo_id], podatek["RAZLAGA"][geslo_id].replace('"', '')))

# REP datoteke
d.write("""
    </mbp:frameset>
    </body>
</html>  """)


# # preberem vrstice
# kval_f = open('Kvalifikatorji.txt', 'r', encoding='utf-8')
# kvalifikatorji = []
# for line in kval_f:
#     kvalifikatorji.append(line)
#
# g = open('slovar.html', 'w', encoding='utf-8')
# for i in kvalifikatorji:



### PISANJE OPF DATOTEKE ###

opf = open('slovar.opf', 'w')
opf.write("""
<?xml version="1.0" encoding="utf-8"?>
<package unique-identifier="uid">
	<metadata>
		<dc-metadata xmlns:dc="http://purl.org/metadata/dublin_core" xmlns:oebpackage="http://openebook.org/namespaces/oeb-package/1.0/">
			<dc:Title>Anglesko-slovenski slovar</dc:Title>
			<dc:Language>en-us</dc:Language>
			<dc:Identifier id="uid">9095C522E5</dc:Identifier>
			<dc:Creator>KlemenD</dc:Creator>
			<dc:Subject BASICCode="REF008000">Dictionaries</dc:Subject>
		</dc-metadata>
		<x-metadata>
			<output encoding="utf-8"></output>
			<DictionaryInLanguage>en-us</DictionaryInLanguage>
			<DictionaryOutLanguage>sl</DictionaryOutLanguage>
			<EmbeddedCover>MobipocketSampleBookCover.jpg</EmbeddedCover>
		</x-metadata>
	</metadata>
	<manifest>
		<item id="item1" media-type="text/x-oeb1-document" href="slovar.html"></item>
	</manifest>
	<spine><itemref idref="item1"/></spine>
	<tours></tours>
	<guide></guide>
</package>""")

