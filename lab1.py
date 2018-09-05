"""
Practice with defining functions
lab1.py
Scott Geilen
9/5/18
"""

def alarm_clock():
	"""
	Calculates and outputs the time when
	the alarm goes off based on current time
	(in hours) and number of hours to wait
	for the alarm
	"""
	current_time_string = input("What is the current time (in hours)? ")
	waiting_time_string = input("How many hours do you have to wait? ")

	current_time_int = int(current_time_string)
	waiting_time_int = int(waiting_time_string)

	hours = current_time_int + waiting_time_int

	timeofday = hours % 24

	print(timeofday)

def print_words():
	word1 = "All"
	word2 = "work"
	word3 = "and"
	word4 = "no"
	word5 = "play"
	word6 = "makes"
	word7 = "Jack"
	word8 = "a"
	word9 = "dull"
	word10 = "boy."

	print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

def compound_interest():
	P = 10000
	n = 12
	r = 0.08

	t = int(input("Compound for how many years? "))

	final = P * ( ((1 + (r/n)) ** (n * t)) )

	print ("The final amount after", t, "years is", final)
