# odprem datoteko
f = open('slovar_mini_unicode.txt', 'r', encoding='utf8')

# preberem vrstice
lines=[]
for line in f:
    lines.append(line)

# locim geslo in zaglavje
kljuci=[]
razlage={}
for line in lines:
    words = line.split("\t")
    geslo = words[0]
    kljuc = words[1]
    razlaga = words[2]
    kljuci.append(kljuc)
    razlage[kljuc] = razlaga

### PISANJE HTML DATOTEKE ###

d = open('slovar.html', 'w', encoding='utf8')

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


for kljuc in sorted(kljuci):
    d.write('<idx:entry>\n<b><idx:orth>%s</idx:orth></b>\n<p>%s</p>\n</idx:entry>\n\n' % (kljuc, razlage[kljuc]))

d.write("""
    </mbp:frameset>
    </body>
</html>  """)

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