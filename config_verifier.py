def verify(filepath):
	"""
	Verifies if the config is a valid config file
	returns True if yes and False if no, and error message if no
	Input: filepath of config file
	Output: bool
	Output: error message: None if config is valid and one of the following when config is invalid:
	(Line 2) Line 2 of config should end in / or be an empty string
	(Line 3) Line 3 of config must be a integer number
	(Line 4) Line 4 of config is not turf war, ranked, or league
	"""
	file = open(filepath)
	lines = file.readlines()
	return verify_lines(lines)

def verify_lines(lines):
	"""
	Verifies if the config is a valid config file
	returns True if yes and False if no, and error message if no
	Input: lines from config file
	Output: bool
	Output: error message: None if config is valid and one of the following when config is invalid:
	(Line 2) Line 2 of config should end in / or be an empty string
	(Line 3) Line 3 of config must be a integer number
	(Line 4) Line 4 of config is not turf war, ranked, or league
	"""
	# checks if line 2 is either "" (empty string) or ends in /
	if(lines[1][:-1] != "" and lines[1][-2] != "/"):
		return (False, "(Line 2) Line 2 of config should end in / or be an empty string")
	try:
		time_per_rotation = float(lines[2])
	except ValueError:
		return (False, "(Line 3) Line 3 of config must be a number")
	if(lines[3][:-1].lower() not in ['turf war', 'ranked', 'league']):
		print("verifier: ", lines[3][:-1].lower())
		return (False, "(Line 4) Line 4 of config is not turf war, ranked, or league")
	return True, None
