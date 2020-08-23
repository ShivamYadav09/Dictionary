import json
from difflib import SequenceMatcher

file = json.load(open("dictionary.json"))

def check():
	print("\n")
	value = input("Enter the word: ")
	keys = sorted(file)
	ratio = 0
	#print(keys)
	if value == "exit(0)":
		print("Thank You\n\n")
		exit(0)
	if value not in keys:
		#print("The word does not have a valid meaning. Please check the word.\n")
		for n in keys:
			if (SequenceMatcher(None, value, n).ratio() > ratio):
				ratio = SequenceMatcher(None,value,n).ratio()
				probable_word = n
		if (ratio > 0.8):
			print("The entered word does not exist. Did you mean",probable_word,"? [Y/N]: ",end='')
			option = input("")
			if(option.lower()=='n'):
				check()
			else:
				print(file[probable_word])
				check()
		else:
			print("The word does not have a valid meaning. Please check the word.\n")
			check()

	else:
		print(file[value])
		check()



def main():
	print("\n\nEnter 'exit(0)' to stop searching")
	check()

if __name__ == "__main__":
	main()



