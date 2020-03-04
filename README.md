# gy-grasklippare

## Utveckling
Alla ändringar kommer bli pushade till Github. Vi använder sedan SSH för att ansluta till raspberry pi:en och synca ner den nya versionen. 

Docs till gpioZero:
https://gpiozero.readthedocs.io/en/stable/api_input.html

## Checklista

TODO: Gör en lista med allt vi ska göra...???

## Dependencies

*pygame
*Pillow
*gpiozero

10.152.135.69

## GPIO Karta

3V3	SVP			1	2	5V Relä
				3	4	
				5	6	
GPIO 4	SVS		7	8	
GND		SVG		9	10	
				11	12	
				13	14	GND		SHG
				15	16	GPIO 23 SHS
3v3 SHP			17	18	
				19	20	
				21	22	
				23	24	
				25	26	
				27	28	
				29	30	
GPIO 6	MK		31	32	
GPIO 13	MHOO	33	34	
GPIO 19	MH+		35	36	GPIO 16 MVOO
GPIO 26	MH-		37	38	GPIO 20 MV+
GND - Relä 		39	40	GPIO 21 MV-

## Vid ny installation

mkdir gy-grasklippare

cd gy-grasklippare

git clone https://github.com/olliverpersson/gy-grasklippare.git

python3 -m venv venv

pip3 install -r requirements.txt

THAT'S IT!!