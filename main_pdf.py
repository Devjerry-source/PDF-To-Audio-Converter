#Importing Libraries
from PyPDF2 import PdfFileReader
from gtts import gTTS

'''DEFINING VARIABLES
'''
status, status1 = False, False
file_name = ""
length_pdf = len(file_name)

'''JASB TECH
An Automated Pdf-To-Audio converter
'''
print("Jasb-Tech-Pdf-to-Audio-Converter".upper().center(65, "-"))
print()
print("This is an Automated PDF(Portable Document Format)-To-Audio Converter.\nBest Used for Journals, Novels, PDF with page numbers,etc".title(),)
print()

def homepage():
	'''funtion displays the homepage of this Application and allows user to select from the Options
	'''
	global status1,status, user_input1
	
	print("Choose from the Options below",
	          "Press 1- Pdf to Audio Converter",
	          "Press 2 - Exit", sep = "\n")
	print()
	       
	while status1 is False:
		try:
			user_input1 = int(input(("Select from the Above Options: ")))
			
			if user_input1 == 1:
				status = False
				main()
				status1 = True
			elif user_input1 == 2:
				exit()
				status1 = True
			else:
				raise ValueError
		except ValueError:
			print()
			
			print("Invalid input!")	 

def main():
	'''This function allows for the invocation of the three functions
	'''
	print("--" * 30)
	
	print("Hello.....\nI am here to guide you through the whole process.")
	print()
	
	prompt()
	
	read_text()
	
	prompt_2()


def prompt():
	'''This function converts pdf to text for further processing.
	'''
	global file_name, status, my_text
	
	while status is False:
		try:
			
			file_name = input("Enter the File name: ")
			print()
			
			with open(file_name, "rb") as f:
				
				pdfReader = PdfFileReader(f)
				
				print("Please Kindly wait as your pdf is processing....")
				print()
				
				my_text = ""
				
				for pageNum in range(pdfReader.numPages):
					
					pageObj = pdfReader.getPage(pageNum)
					
					my_text += pageObj.extractText()
					
					status = True
				
		except FileNotFoundError:
			print()
			
			print("File name is not found in your file folder.\nEnsure your file is stored in SD-card/Andriod/data/ru.iiec.pydriod3/files and enter the file name.")
			print()
	
def read_text():
	'''This function converts the text to an audio
	'''
	global my_voice
	
	print("Ensure your Internet is connected and Kindly wait as Pdf is converting to Audio...... ..... .... ..... .....")
	
	my_voice = gTTS(text = my_text, lang = "en")
	#This removes '.pdf'' from the file name
	name = file_name[: (length_pdf - 4)] 
	
	my_voice.save(f"{name}.mp3")
	print()
	
	print("Done.........", f"{name} is saved successfully in SD-card",f"(SD-card/Andriod/data/ru.iiec.pydriod3/files/{name}) ", sep = "\n")
	
def prompt_2():
	global user_input, status, status1
	
	user_input = input("Do you want to convert another pdf: ").title()
	
	while user_input not in ("Yes", "No"):
		print()
		
		print("Invalid input!")
		print()
		
		user_input = input("Do you want to convert another pdf: ").title()
		
	if user_input == "Yes":
		status = False
		main()
	elif user_input == "No":
		print("--" * 30)
		status = False
		status1 = False
		homepage()

'''MAIN INVOCATION
'''		
homepage()