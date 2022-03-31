import os
import shutil
import time

def mainfolder():

    dlt_folders = 0
    dlt_files = 0

	path = "/Removing_files"
	days = 90
	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= get_file_or_folder_age(root_folder):
				remove_folder(root_folder)
				dlt_folders += 1
				break

			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= get_file_or_folder_age(folder_path):
						remove_folder(folder_path)
						dlt_folders += 1 
				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= get_file_or_folder_age(file_path):
						remove_file(file_path)
						dlt_files += 1
		else:
			if seconds >= get_file_or_folder_age(path):
				remove_file(path)
				dlt_files += 1

	else:
		print(f'"{path}" is not found')
		dlt_files += 1

	print(f"Total folders deleted: {dlt_folders}")
	print(f"Total files deleted: {dlt_files}")



def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)



def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime


if __name__ == '__main__':
	mainfolder()
