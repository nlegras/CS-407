def encode(input_string):

	output_string = ""
	
	if input_string == "":
		return output_string
	
	else:
		tmp = input_string[0]
		count = 0	

		for i in input_string:
			if i == tmp:
				count = count + 1
			else:
				output_string = output_string + tmp + str(count)
				count = 1
			tmp = i
		output_string = output_string + tmp + str(count)

		return output_string
