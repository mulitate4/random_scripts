import os
import shutil
import time
import sys


path = "C:/Users/Goofy/Documents/all artworks/autosort"

comic_project_folder = "C:/Users/Goofy/Documents/all artworks/Project files/Comics"
comic_jpeg_folder = "C:/Users/Goofy/Documents/all artworks/Comic JPEGs"

artwork_project_folder = "C:/Users/Goofy/Documents/all artworks/Project files"
logo_png_folder = "C:/Users/Goofy/Documents/all artworks/Logo PNGs"
logo_jpeg_folder = "C:/Users/Goofy/Documents/all artworks/Logo JPEGs"


def comic():
	files = os.listdir(path)
	if files == []:
		print ("no file present!")
	else:
		print (files)
		print ("What do you want to name the folder?")
		name = input("Enter Name: ")		
		for file in files:
				ext = os.path.splitext(file)[1:]
				if ext == ('.ai',):
					shutil.move(path + '/' + file, comic_project_folder)
				elif ext == ('.jpg',):
					#os.rename(file, file_name + "/" + '.jpg')
					if os.path.exists(comic_jpeg_folder + '/' + name):
						shutil.move(path + '/' + file, comic_jpeg_folder + '/' + name)
					else:
						os.makedirs(comic_jpeg_folder + '/' + name)
						shutil.move(path + '/' + file, comic_jpeg_folder + '/' + name)
				else:
					print ("not a valid file")

def artwork():
	files = os.listdir(path)
	if files == []:
		print ("no file present!")
	else:
		print (files)
		for file in files:
			ext = os.path.splitext(file)[1:]
			if ext == ('.ai',):
				shutil.move(path + '/' + file, artwork_project_folder)
			elif ext == ('.png',):
				shutil.move(path + '/' + file, logo_png_folder)
			elif ext == ('.jpg',):
				shutil.move(path + '/' + file, logo_jpeg_folder)


#Main execution of the script
if len(sys.argv) != 1:
	choice = sys.argv[1]
else:
	print ("Enter 1 for comics")
	print ("Enter 2 for art")
	choice = input()
	if choice == "1":
		comic()
		print("Done!")
		time.sleep(2)
	elif choice == "2":
		artwork()
		print("Done!")
		time.sleep(2)
	else:
		print ("Enter Valid Feature")
		time.sleep(2)
