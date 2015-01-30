image bg dorm = "school_dormhisao.jpg"
image bg courtyard = "school_courtyard.jpg"
image bg restaurant = "city_restaurant.jpg"
image bg clubentrance = "club_clubint.jpg"
image bg clubpool = "city_clubpool.jpg"
image bg schoolentrance = "school_dormext.jpg"
image bg classroom = "school_scienceroom.jpg"

image lilly normal = "lilly_basic_smile.png"
image lilly please = "lilly_basic_oops.png"
image lilly pouting = "lilly_basic_pouting.png"
image lilly cheerful = "lilly_behind_cheerful.png"

image hanako normal = "hanako_basic_bashful.png"
image hanako worry = "hanako_basic_worry.png"
image hanako outnormal = "hanako_basic_bashul_cas.png"
image hanako outhappy = "hanako_emb_emb_cas.png"
image hanako outsad = "hanako_emb_sad_cas.png"

define m = Character('Me', color="#000A00")
define h = Character('Hanako', color="#000A00")
define l = Character('Lilly', color="#A37A00")

label start:
	
	scene bg black #todo

	python:
		name = renpy.input("What is your name?")
		name = name.strip()

		if not name:
			name = "Pat Smith"
	
	
	scene bg dorm
	with fade
	
	# Phone starts ringing
	"Ughh...."
	"What... time is it anyways?"
	m "FUCK I'M LATE"
	"It's Lilly calling me. Should I answer the phone?"
	
	
	menu:
		"Answer her, I'm late already.":
			
			jump answer
			
		"There's no time! I can still make it!":
		
			jump classroom
			
			
label answer:

	"Guess I will answer it since I'm late already."
	"And I also like Lilly a bit."
	# Phone answer
	m "Hey Lilly what's up?"
	l "Hello [name], what's up? "
	
	
	
	
	
