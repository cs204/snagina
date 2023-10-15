def camel_to_snake(camel, sep='_'):
	snake_register = ''
	for i in camel:
		if i.isupper():
			snake_register += sep + i.lower()
		else:
			snake_register += i
	print(snake_register.lstrip(sep))
camel_register = input("Верблюжий стиль: ")
camel_to_snake(camel_register, '_')
