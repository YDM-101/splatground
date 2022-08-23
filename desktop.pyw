import splatoon_api_caller
import config_verifier
import bg_switch
import time
import os
import subprocess

def load_image_paths(stage_a, stage_b, bg_directory):
	"""
	Loads image paths from the image directories with desktop bg images
	Input: stage_a: name of stage a
	Input: stage_b: name of stage b
	Input: bg_directory: the directory that contains each of the folders that contains the images. Must end with "/" or be empty string
	Output: image_paths_a: list containing all the image paths in the folder with name stage_a, None if folder does not exist
	Output: image_paths_b: list containing all the image paths in the folder with name stage_b, None if folder does not exist
	Output: ERROR: error code, 0 if OK, 1 if folder not found, 2 if folder has no images

	"""
	# get the images of each stage
	ERROR = 0
	try:
		image_paths_a = os.listdir(bg_directory + stage_a)
	except FileNotFoundError:
		os.system("osascript -e 'tell application \"Terminal\" to display alert \"Splatground: Desktop images folder named %s not found\"'"%(stage_a))
		ERROR = 1
	try:
		image_paths_b = os.listdir(bg_directory + stage_b)
	except FileNotFoundError:
		os.system("osascript -e 'tell application \"Terminal\" to display alert \"Splatground: Desktop images folder named %s not found\"'"%(stage_b))
		ERROR = 1
	# send an error message if no images in stage
	if(len(image_paths_a) == 0):
		os.system("osascript -e 'tell application \"Terminal\" to display alert \"Splatground: Desktop images folder named %s has no images\"'"%(stage_a))
		ERROR = 2
	if(len(image_paths_b) == 0):
		os.system("osascript -e 'tell application \"Terminal\" to display alert \"Splatground: Desktop images folder named %s has no images\"'"%(stage_b))
		ERROR = 2
	# remove hidden files
	image_paths_a = [x for x in image_paths_a if x[0] != '.']
	image_paths_b = [x for x in image_paths_b if x[0] != '.']
	return (image_paths_a, image_paths_b, ERROR)



def rotate_stages(stage_a, stage_b, bg_directory, rotation_speed):
	"""
	Rotates stages until a new time shows up
	stage_a: name of stage a
	stage_b: name of stage b
	bg_directory: the directory that contains each of the folders that contains the images. Must end with "/" or be empty string
	rotation_speed: speed of rotating through images
	"""
	current_time = int((time.time() - 10) // 7200) # get the current time. Note: this has been changed to get the time 10 seconds ago to allow the API to finish refreshing
	stage_names = [stage_a, stage_b]
	image_paths_a, image_paths_b, ERROR = load_image_paths(stage_a, stage_b, bg_directory)
	ERROR_COUNTDOWN = 5 # 5 times the rotation speed
	stage_indices = [0, 0]
	current_stage = 0
	while(True):
		if(ERROR != 0 and ERROR_COUNTDOWN <= 0):
			# retry loading image paths
			image_paths_a, image_paths_b, ERROR = load_image_paths(stage_a, stage_b, bg_directory)
			ERROR_COUNTDOWN = 5
		elif(ERROR != 0):
			ERROR_COUNTDOWN -= 1
		if(ERROR == 0):
			# choose a stage and change the background
			image_paths = [image_paths_a, image_paths_b] # packaging the image paths and names, moved from above to remove referencing bug
			image_paths_len = [len(image_paths_a), len(image_paths_b)]
			current_background_image_name = image_paths[current_stage][stage_indices[current_stage]%image_paths_len[current_stage]]
			bg_path = bg_directory + stage_names[current_stage] + "/" + current_background_image_name
			bg_switch.change_background(bg_path)
			stage_indices[current_stage] += 1
			current_stage = 1 - current_stage
		time_left_in_hour = 7200 - time.time() % 7200 + 10 # 10 is buffer 
		rotation_speed_adjusted = min(rotation_speed, time_left_in_hour)
		time.sleep(rotation_speed_adjusted)
		if(int((time.time() - 10) // 7200) != current_time):
			subprocess.call(['/usr/bin/killall', 'Dock'])
			break

# read the config file
config = open("config.txt", 'r')
lines = config.readlines()
if(lines[3][-1] != '\n'):
	lines[3] = lines[3] + '\n'

# error-check config file and send error message to UI
verification_result = config_verifier.verify_lines(lines)
if(verification_result[0] == False):
	os.system("osascript -e 'tell application \"Terminal\" to display alert \"Splatground: %s\"'"%(verification_result[1]))

bg_directory = lines[1][:-1]
rotation_speed = float(lines[2])
mode = lines[3][:-1]
# Upon starting, change the desktop background
while(True):
	stage_a, stage_b = splatoon_api_caller.get_schedules(mode)
	rotate_stages(stage_a, stage_b, bg_directory, rotation_speed)




