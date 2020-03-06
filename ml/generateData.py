from PIL import Image
import json
import glob

data = []

#with open('data.json') as json_file:
#
#	data = json.load(json_file)

print("Kompilerar data från bilder, lägg bilderna i en mapp och döp dem till vad de ska klassifiseras som. [typ].[index].JPG ex t.5.jpg")
print("ENDAST BILDFILER I MAPPEN")
print("SE TILL ATT EN FIL SOM HETER data.json FINNS I DENNA MAP, KOMMER SKRIVAS ÖVER")

print( "Filväg till mapp med träningsbilder: " )
src = input()

print( glob.glob('{}/*'.format(src)) )

for file in glob.glob( '{}/*'.format(src)):

	print( file )

	img = Image.open( file )
	img = img.resize( ( 1,1 ) )

	px = img.load()[0,0]

	data.append({
		"r": int(px[0]),
		"g": int(px[1]),
		"b": int(px[2]),
		"t": file.split("/")[-1].split(".")[0]
	});

	with open('data.json', 'w', encoding='utf-8') as json_file:
		json.dump(data, json_file, ensure_ascii=False, indent=4)
