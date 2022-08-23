import requests
import json

def get_data(api):
	"""
	Generic API caller.
	Input: api (string) API handle
	Output: response-json (dict) if status OK else None
	Predecessor here https://www.educative.io/answers/how-to-make-api-calls-in-python
	"""
	response = requests.get(f"{api}")
	if response.status_code == 200:
		print("sucessfully fetched the data")
		return response.json()
	else:
		print(f"Hello person, there's a {response.status_code} error with your request")
		

def get_schedules(mode):
	"""
	Specific API caller hardcoded with schedules API from splatoon2.ink
	Extracts current stages for requested mode
	Error checking of input done at earlier stage.
	Input: mode: either 'turf war', 'ranked', or 'league'
	Output: 2-tuple (stage_a, stage_b)
	"""
	mode_translation_dict = {'turf war':'regular', 'ranked':'gachi', 'league':'league'}
	response = get_data("https://splatoon2.ink/data/schedules.json")
	return (response[mode_translation_dict[mode]][0]['stage_a']['name'], response[mode_translation_dict[mode]][0]['stage_b']['name'])
	