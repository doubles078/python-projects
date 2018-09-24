#run this in any directory add -v for verbose
#pip install Image
import os
import sys
from PIL import Image, ExifTags

def buildDirectories(file, subdir):
	pwd = subdir
	new_directories = [pwd + '/compressed', pwd + '/compressed_and_resized']
	#makes two new dirs for compressed and resized
	new_filename = 'Compressed_' + pwd.replace('/', '_') + file

	for directory in new_directories:
		if not os.path.exists(directory):
			os.mkdir(directory)

	path_to_compressed = new_directories[0] + '/Compressed_' + file
	path_to_resized = new_directories[1] + '/1200_' + file

	return [path_to_compressed, path_to_resized]

def compressImages(file, filepath, subdir, verbose=False):
	#What percentage quality of the original image to keep. 65 to 85 is best bet here
	compress_quality = 80
	oldsize = os.stat(filepath).st_size
	picture = Image.open(filepath)

	#Build the directories
	path_compress = buildDirectories(file, subdir)[0]
	path_resize = buildDirectories(file, subdir)[1]

	#Save the compressed pic to its correct path
	#Removing the just compress for now
	#picture.save(path_compress,optimize=True,quality=compress_quality)
	resizeImages(picture, path_resize, compress_quality)

	#Log information about the compression savings
	newsize = os.stat(os.path.join(os.getcwd(), path_resize)).st_size
	percent = round((oldsize-newsize)/float(oldsize)*100, 2)

	if (verbose):
		print("File compressed from %s to %s or %s%%" % (oldsize,newsize,percent))

	return percent


def resizeImages(picture, path_to_resized, compress_quality):
	#Static width in pixels.  Could also change this to be a param in the CLI
	new_width = 1200

	for orientation in ExifTags.TAGS.keys():
		if ExifTags.TAGS[orientation]=='Orientation':
			break

	try:
		e = picture._getexif()    # returns None if no EXIF data
	except:
		e = None

	if e is not None:
		exif=dict(e.items())

		try:
			orientation = exif[orientation]
		except:
			print("There was no orientation # so I set it to 0")
			orientation = 0

	if orientation == 1 or orientation == 0:
		width, height = picture.size
		new_height = int(new_width * height / width)
		print("Height: " + str(height) + "Width: " + str(width) + ' New height: ')
	else:
		height, width = picture.size
		new_height = int(new_width * height / width)

	if width >= 1200:
		if width > height:
			if orientation == 1 or orientation == 0:
				picture_resized = picture.resize((new_width, new_height), Image.ANTIALIAS)
				print("Width bigger, width: " + str(width) + " height: " + str(height) + " New width: " + str(new_width) + " New height: " + str(new_height))
			else:
				picture_resized = picture.resize((new_height, new_width), Image.ANTIALIAS)
		else:
			if orientation == 6:
				picture_resized = picture.resize((new_height, new_width), Image.ANTIALIAS)
				print("ORIENTATION 6 Width bigger, width: " + str(width) + " height: " + str(height) + " New width: " + str(new_width) + " New height: " + str(new_height))
			else:
				picture_resized = picture.resize((new_width, new_height), Image.ANTIALIAS)
				print("Height bigger, width: " + str(width) + " height: " + str(height))
	else:
		picture_resized = picture

	print("Orientation: " + str(orientation))

	if orientation == 3:
		picture_resized = picture_resized.transpose(Image.ROTATE_180)
	elif orientation == 6:
		picture_resized = picture_resized.transpose(Image.ROTATE_270)
		print("I reoriented")
	elif orientation == 8:
		picture_resized = picture_resized.transpose(Image.ROTATE_90)



	#Save the compressed and resized image to the correct path
	picture_resized.save(path_to_resized, optimize=True, quality=compress_quality)

	return picture_resized



def main():
	verbose = False
	#checks for verbose flag
	if (len(sys.argv)>1):
		if (sys.argv[1].lower()=="-v"):
			verbose = True

	#finds present working dir
	pwd = os.getcwd()
	#Dont look in here
	exclude = set(['.git', 'venv'])

	tot = 0
	num = 0
	for subdir, dirs, files in os.walk(pwd):
		dirs[:] = [d for d in dirs if d not in exclude]
		for file in files:
			if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg', '.png'):
				filepath = os.path.join(subdir, file)
				print(filepath)
				num += 1
				tot += compressImages(file, filepath, subdir, verbose)

		#dirArray = os.path.join(subdir, file).split('\\')
		#result = []

		#for i in dirArray[::-1]:
		#	if(i == "image_opt"):
		#		break
		#	result.append(i)

		#result.reverse()
		#string = ('_').join(result)
		#print(string)

if __name__ == "__main__":
	main()
