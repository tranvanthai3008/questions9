# get input
inputNumberPhone = input("Enter number phone: ")

# Result dictionary

def checkNumber(input):
	input = str(input)
	# Split part of number
	internationalCode = ""
	for char in input:
		if char =="(":
			break
		internationalCode += char

	if internationalCode == "+7":
		print("The phone number from Russian")

	codes = {
	    'Абакан': ['39022'],
	    'Архангельск': ['8182', '818'],
	    'Астрахань': ['8512'],
	    'Барнаул': ['3852'],
	    'Белгород': ['4722'],
	    'Благовещенск': ['4162'],
	    'Брянск': ['4832'],
	    'Владивосток': ['4232'],
	    'Владикавказ': ['8672'],
	    'Владимир': ['492'],
	    'Волгоград': ['8442'],
	    'Вологда': ['8172'],
	    'Воркута': ['82151'],
	    'Воронеж': ['4732'],
	    'Грозный': ['8712'],
	    'Санкт-Петербург': ['812'],
	    'Москва': ['495', '499']
	    }
	try:
		scopeOfCityCode = [input.index("("),input.index(")")]
		cityCode = input[scopeOfCityCode[0]+1:scopeOfCityCode[1]]
		cityName = ""
		for name, code in codes.items():
			if cityCode in code:
				cityName = name
		print(cityName)
	except:
		print("Phone without code")




checkNumber(inputNumberPhone)