from PIL import Image
import json
import glob

data = []

#with open('data.json') as json_file:
#
#	data = json.load(json_file)

print(data);

print( "Filväg till mapp med träningsbilder: " )
src = input()

print( glob.glob('{}/*'.format(src)) )

for file in glob.glob( '{}/*'.format(src)):

	print( file )
	print( "Visar bilden klipp, natt eller vänd? (c/n/t)" )
	txt = input()

	while txt != "c" and txt != "n" and txt != "t":

		print("type 'c' or 'n' or 't'")
		txt = input()

	img = Image.open( file )
	img = img.resize( ( 1,1 ) )
	px = img.load()[0,0]

	data.append({
		"r": int(px[0]),
		"g": int(px[1]),
		"b": int(px[2]),
		"t": txt
	});

	with open('data.json', 'w', encoding='utf-8') as json_file:
		json.dump(data, json_file, ensure_ascii=False, indent=4)
