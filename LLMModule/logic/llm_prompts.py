prompt_qa1 = """ 
Please parse the following english sentences into the semantic parse. The available keywords are: go_to, be_in:

Sentence: Mary moved to the bathroom.
Semantic parse: go_to(mary,bathroom)

Sentence: John went to the hallway.
Semantic parse: go_to(john,hallway)

Sentence: Where is Mary? 
Semantic parse: be_in(mary,V1)
	
Sentence: Daniel went back to the hallway.
Semantic parse: go_to(daniel,hallway)

Sentence: Sandra moved to the garden.
Semantic parse: go_to(sandra,garden)

Sentence: Where is Daniel? 
Semantic parse: be_in(daniel,V1)
	
Sentence: John moved to the office.
Semantic parse: go_to(john,office)

Sentence: Sandra journeyed to the bathroom.
Semantic parse: go_to(sandra,bathroom)

Sentence: Where is Daniel? 
Semantic parse: be_in(daniel,V1)
	
Sentence: Mary moved to the hallway.
Semantic parse: go_to(mary,hallway)

Sentence: Daniel travelled to the office.
Semantic parse: go_to(daniel,office)

Sentence: Where is Daniel? 
Semantic parse: be_in(daniel,V1)
	
Sentence: John went back to the garden.
Semantic parse: go_to(john,garden)

Sentence: John moved to the bedroom.
Semantic parse: go_to(john,bedroom)

Sentence: Where is Sandra? 
Semantic parse: be_in(sandra,V1)

Your turn:
"""

prompt_qa6 =  """Please parse the following statements into facts. The available keywords are: pickup, drop, and go_to:

Sentence: Mary went to the garden.
Semantic parse: go_to(mary, garden)

Sentence: Mary moved to the bathroom.
Semantic parse: go_to(mary, bathroom)

Sentence: Mary got the milk there.
Semantic parse: pickup(mary, milk)

Sentence: Daniel went back to the hallway.
Semantic parse: go_to(daniel, hallway)

Sentence: John is in the garden.
Semantic parse: be_in(john, garden)

Sentence: Max journeyed to the bathroom.
Semantic parse: go_to(max, bathroom)

Sentence: Mary grabbed the football there.
Semantic parse: pickup(mary, football)

Sentence: Mary grabbed the milk there.
Semantic parse: pickup(mary, milk)

Sentence: Sandra picked up the apple there.
Semantic parse: pickup(sandra, apple)

Sentence: Bob is in the hallway.
Semantic parse: be_in(bob, hallway)

Sentence: Daniel is no longer in the garden.
Semantic parse: be_in(daniel, garden)

Sentence: Daniel took the apple there.
Semantic parse: pickup(daniel, apple)

Sentence: Susan dropped the milk.
Semantic parse: drop(susan, milk)

Sentence: Mary discarded the milk.
PSemantic parse: drop(mary, milk)

Sentence: Sandra put down the football.
Semantic parse: drop(sandra, football)

Sentence: John put down the apple.
Semantic parse: drop(john, apple)

Sentence: Bob got the football there.
Semantic parse: pickup(bob, football)

Sentence: Sandra got the apple there.
Semantic parse: pickup(sandra, apple)

Sentence: Max left the cup.
Semantic parse: drop(max, cup)

Sentence: Kevin is in the bathroom.
Semantic parse: be_in(kevin, bathroom)

Sentence: John took the football there.
Semantic parse: pickup(john, football)

Sentence: Sandra is not in the bedroom.
Semantic parse: be_in(sandra, bedroom)

Sentence: John is not in the garden.
Semantic parse: be_in(john, garden)

Sentence: Mice are afraid of cats.
Semantic parse: be_afraid_of(mouse, cat)

Sentence: Is Mary in the bedroom? 
Semantic parse: be_in(mary, bedroom)

Sentence: Is Daniel in the bathroom?
Semantic parse: be_in(daniel, bathroom)

Sentence: Is Sandra in the office?
Semantic parse: be_in(sandra, office)

Sentence: Is Daniel in the hallway?
Semantic parse: be_in(daniel, hallway)


Your turn:
"""

prompt_qa8 = """Please parse the following english sentences into the semantic parse. The available keywords are: pickup, drop, and go_to:

Sentence: Mary moved to the bathroom.
Semantic parse: go_to(mary, bathroom)

Sentence: Sandra journeyed to the bedroom.
Semantic parse: go_to(sandra, bedroom)

Sentence: Mary got the football there.
Semantic parse: pickup(mary, football)

Sentence: John went to the kitchen.
Semantic parse: go_to(john, kitchen)

Sentence: Mary went back to the garden.
Semantic parse: go_to(mary, garden)

Sentence: Sandra went back to the office.
Semantic parse: go_to(sandra, office)

Sentence: Sandra journeyed to the hallway.
Semantic parse: go_to(sandra, hallway)

Sentence: Mary dropped the football.
Semantic parse: drop(mary, football)

Sentence: John got the milk there.
Semantic parse: pickup(john, milk)

Sentence:  What is Mary carrying?
Semantic parse: carry(mary, V1)

Sentence: Mary took the football there.
Semantic parse: pickup(mary, football)

Sentence: Mary took the football there.
Semantic parse: pickup(mary, football)

Sentence: John got the football there.
Semantic parse: pickup(john, football)

Sentence: Sandra picked up the apple there.
Semantic parse: pickup(sandra, apple)

Sentence: Sandra left the apple.
Semantic parse: drop(sandra, apple)

Sentence: Mary is a mouse.
Semantic parse: be(mary, mouse)

Sentence: Where is the apple? 
Semantic parse: be_in(apple, V1)

Sentence: John left the milk.
Semantic parse: drop(john, milk)

Sentence: Mary left the apple.
Semantic parse: drop(mary, apple)

Sentence: Daniel discarded the football.
Semantic parse: drop(daniel, football)

Sentence: Sandra put down the football there.
Semantic parse: drop(sandra, football)

Sentence: Daniel picked up the apple there.
Semantic parse: pickup(daniel, apple)

Sentence: Mary grabbed the milk there.
Semantic parse: pickup(mary, milk)

Sentence: What is Sandra carrying?
Semantic parse: carry(sandra, V1)

Sentence: What is John carrying?
Semantic parse: carry(john , V1) 

Sentence: What is Daniel carrying? 
Semantic parse: carry(daniel, V1) 

Your turn:
"""

prompt_qa9 = """Please parse the following english sentences into the semantic parse. The available keywords are: go_to and be_in:


Sentence: Daniel moved to the hallway.	
Semantic parse: go_to(daniel,hallway)

Sentence: Sandra moved to the bedroom.
Semantic parse: go_to(sandra,bedroom)

Sentence: Sandra travelled to the kitchen.
Semantic parse: go_to(sandra,kitchen)

Sentence: Sandra journeyed to the bedroom.
Semantic parse: go_to(sandra,bedroom)

Sentence: Daniel went to the office.
Semantic parse: go_to(daniel,office)
	
Sentence: Sandra went to the bedroom.
Semantic parse: go_to(sandra,bedroom)

Sentence: John went to the kitchen.
Semantic parse: go_to(john,kitchen)

Sentence: Daniel went back to the kitchen.
Semantic parse: go_to(daniel,kitchen)

Sentence: Mary went back to the bedroom.	
Semantic parse: go_to(mary,bedroom)
	
Sentence: Daniel is not in the hallway.
Semantic parse: be_in(daniel,hallway)

Sentence: John is not in the bedroom.
Semantic parse: be_in(john,bedroom)

Sentence: Mary is no longer in the bedroom.
Semantic parse: be_in(mary, bedroom)

Sentence: Sandra is no longer in the bathroom.
Semantic parse: be_in(sandra,bathroom)

Sentence: Sandra is not in the bedroom.
Semantic parse: be_in(sandra,bedroom)

Sentence: Mary is no longer in the bathroom.
Semantic parse: be_in(mary,bathroom)

Sentence: John is no longer in the kitchen.
Semantic parse: be_in(john,kitchen)
	
Sentence: John is no longer in the office.
Semantic parse: be_in(john,office)

Sentence: Sandra is in the bathroom.
Semantic parse: be_in(sandra,bathroom)
	
Sentence: Daniel is in the office.
Semantic parse: be_in(daniel,office)

Sentence: Daniel is in the bedroom.
Semantic parse: be_in(daniel,bedroom)
	
Sentence: Sandra is in the garden.
Semantic parse: be_in(sandra,garden)
	
Sentence: Daniel is in the bedroom.
Semantic parse: be_in(daniel,bedroom)
	
Sentence: Is Mary in the bedroom? 
Semantic parse: be_in(mary,bedroom)

Sentence: Is Daniel in the bedroom? 
Semantic parse: be_in(daniel,bedroom)

Sentence: Is Daniel in the garden? 
Semantic parse: be_in(daniel,garden)

Sentence: Is Daniel in the kitchen? 
Semantic parse: be_in(daniel,kitchen)

Sentence: Is Sandra in the bedroom? 
Semantic parse: be_in(sandra,bedroom)

Sentence: Is Sandra in the office? 
Semantic parse: be_in(sandra,office)

Sentence: Is Daniel in the bathroom?
Semantic parse: be_in(daniel,bathroom) 	

Your turn:
"""

prompt_qa10 = """Please parse the following english sentences into the semantic parse. The available keywords are: go_to, and be_in:

Sentence: Bill went back to the office.
Semantic parse: go_to(bill,office)

Sentence: Bill moved to the cinema.
Semantic parse: go_to(bill,cinema)

Sentence: Bill journeyed to the bedroom.
Semantic parse: go_to(bill,bedroom)

Sentence: Bill is in the park.
Semantic parse: be_in(bill,park)

Sentence: Bill is in the kitchen.
Semantic parse: be_in(bill,kitchen)

Sentence: Bill is either in the kitchen or the park.
Semantic parse: be_in(bill,kitchen), be_in(bill,park)

Sentence: Bill is either in the office or the kitchen.
Semantic parse: be_in(bill,office), be_in(bill,kitchen)

Sentence: Bill is either in the cinema or the park.
Semantic parse: be_in(bill,cinema), be_in(bill,park)

Sentence: Bill is either in the school or the office.
Semantic parse: be_in(bill,school), be_in(bill,office)

Sentence: Bill is either in the park or the kitchen.
Semantic parse: be_in(bill,park), be_in(bill,kitchen)

Sentence: Bill is either in the bedroom or the school.
Semantic parse: be_in(bill,bedroom), be_in(bill,school)

Sentence: Bill is either in the school or the school.
Semantic parse: be_in(bill,school), be_in(bill,school)

Sentence: Bill is either in the park or the park.
Semantic parse: be_in(bill,park), be_in(bill,park)

Sentence: Fred went back to the park.
Semantic parse: go_to(fred,park)

Sentence: Fred moved to the cinema.
Semantic parse: go_to(fred,cinema)

Sentence: Fred journeyed to the office.
Semantic parse: go_to(fred,office)

Sentence: Fred travelled to the cinema.
Semantic parse: go_to(fred,cinema)

Sentence: Fred is in the office.
Semantic parse: be_in(fred,office)

Sentence: Fred is in the bedroom.
Semantic parse: be_in(fred,bedroom)

Sentence: Fred is either in the school or the park.
Semantic parse: be_in(fred,school), be_in(fred,park)

Sentence: Fred is either in the kitchen or the park.
Semantic parse: be_in(fred,kitchen), be_in(fred,park)

Sentence: Fred is either in the park or the park.
Semantic parse: be_in(fred,park), be_in(fred,park)

Sentence: Fred is either in the bedroom or the bedroom.
Semantic parse: be_in(fred,bedroom), be_in(fred,bedroom)

Sentence: Fred is either in the office or the kitchen.
Semantic parse: be_in(fred,office), be_in(fred,kitchen)

Sentence: Fred is either in the kitchen or the kitchen.
Semantic parse: be_in(fred,kitchen), be_in(fred,kitchen)

Sentence: Fred is either in the cinema or the bedroom.
Semantic parse: be_in(fred,cinema), be_in(fred,bedroom)

Sentence: Mary went back to the office.
Semantic parse: go_to(mary,office)

Sentence: Mary moved to the park.
Semantic parse: go_to(mary,park)

Sentence: Mary went to the cinema.
Semantic parse: go_to(mary,cinema)

Sentence: Mary is in the school.
Semantic parse: be_in(mary,school)

Sentence: Mary is either in the cinema or the park.
Semantic parse: be_in(mary,cinema), be_in(mary,park)

Sentence: Mary is either in the office or the kitchen.
Semantic parse: be_in(mary,office), be_in(mary,kitchen)

Sentence: Mary is either in the school or the bedroom.
Semantic parse: be_in(mary,school), be_in(mary,bedroom)

Sentence: Julie journeyed to the school.
Semantic parse: go_to(julie,school)

Sentence: Julie is either in the park or the kitchen.
Semantic parse: be_in(julie,park), be_in(julie,kitchen)

Sentence: Julie is either in the cinema or the park.
Semantic parse: be_in(julie,cinema), be_in(julie,park)

Sentence: Julie is either in the bedroom or the school.
Semantic parse: be_in(julie,bedroom), be_in(julie,school)

Sentence: Julie is either in the school or the office.
Semantic parse: be_in(julie,school), be_in(julie,office)

Sentence: Julie is either in the park or the school.
Semantic parse: be_in(julie,park), be_in(julie,school)

Sentence: Julie is either in the school or the office.
Semantic parse: be_in(julie,school), be_in(julie,office)

Sentence: Bill is either in the school or the school.
Semantic parse: be_in(bill,school), be_in(bill,school)

Sentence: Fred is either in the bedroom or the bedroom.
Semantic parse: be_in(fred,bedroom), be_in(fred,bedroom)

Sentence: Bill is either in the bedroom or the bedroom.
Semantic parse: be_in(bill,bedroom), be_in(bill,bedroom)

Sentence: Fred is either in the cinema or the cinema.
Semantic parse: be_in(fred,cinema), be_in(fred,cinema)

Sentence: Is Mary in the office?
Semantic parse: be_in(mary,office)

Sentence: Is Bill in the office? 
Semantic parse: be_in(bill,office)
 
Sentence: Is Bill in the cinema?
Semantic parse: be_in(bill,cinema)
	
Sentence: Is Fred in the park? 
Semantic parse: be_in(fred,park)

Sentence: Is Bill in the park?
Semantic parse: be_in(bill,park)

Sentence: Is Julie in the school?
Semantic parse: be_in(julie,school)

Your turn:
"""

prompt_qa11 = """Please parse the following english sentences into the semantic parse. The available keywords are: go_to, and be_in:


Sentence: Mary moved to the bathroom.
Semantic parse: go_to(mary,bathroom)
Sentence: Following that she went back to the bedroom.
Semantic parse: go_to(mary,bedroom)

Sentence: Sandra went back to the bathroom.
Semantic parse: go_to(sandra,bathroom)
Sentence: Afterwards she travelled to the office.
Semantic parse: go_to(sandra,office)

Sentence: Sandra went to the office.
Semantic parse: go_to(sandra,office)
Sentence: Then she went back to the garden.
Semantic parse: go_to(sandra,garden)

Sentence: Sandra went to the office.
Semantic parse: go_to(sandra,office)
Sentence: Then she went back to the garden.
Semantic parse: go_to(sandra,garden)

Sentence: Sandra moved to the office.
Semantic parse: go_to(sandra,office)
Sentence: Then she journeyed to the kitchen.
Semantic parse: go_to(sandra,kitchen)

Sentence: Sandra moved to the bathroom.
Semantic parse: go_to(sandra,bathroom)
Sentence: After that she moved to the kitchen.
Semantic parse: go_to(sandra,kitchen)

Sentence: Sandra travelled to the garden.
Semantic parse: go_to(sandra,garden)
Sentence: Following that she went to the bedroom.
Semantic parse: go_to(sandra,bedroom)

Sentence: Mary went back to the bathroom.
Semantic parse: go_to(mary,office)
Sentence: After that she went to the bedroom.
Semantic parse: go_to(mary,office)

Sentence: Mary moved to the bathroom.
Semantic parse: go_to(mary,bathroom)
Sentence: Following that she went back to the bedroom.
Semantic parse: go_to(mary,bedroom)

Sentence: Mary went to the garden.
Semantic parse: go_to(mary,garden)
Sentence: Afterwards she went to the office.
Semantic parse: go_to(mary,office)

Sentence: Mary went to the office.
Semantic parse: go_to(mary,office)
Sentence: Then she journeyed to the garden.
Semantic parse: go_to(mary,garden)

Sentence: John travelled to the bathroom.
Semantic parse: go_to(john,bathroom)
Sentence: After that he journeyed to the hallway.
Semantic parse: go_to(john,hallway)

Sentence: John went to the garden.
Semantic parse: go_to(john,garden)
Sentence: Following that he went to the bedroom.
Semantic parse: go_to(john,bedroom)

Sentence: John travelled to the bathroom.
Semantic parse: go_to(john,bathroom)
Sentence: After that he journeyed to the hallway.
Semantic parse: go_to(john,hallway)

Sentence: John journeyed to the kitchen.
Semantic parse: go_to(john,kitchen)
Sentence: Following that he travelled to the bedroom.
Semantic parse: go_to(john,bedroom)

Sentence: Daniel went back to the garden.
Semantic parse: go_to(daniel,garden)
Sentence: Following that he moved to the bathroom.
Semantic parse: go_to(daniel,bathroom)

Sentence: Daniel journeyed to the hallway.
Semantic parse: go_to(daniel,hallway)
Sentence: After that he travelled to the bedroom.
Semantic parse: go_to(daniel,bedroom)

Sentence: Daniel moved to the office.
Semantic parse: move_to(daniel,office)
Sentence: Afterwards he moved to the hallway.
Semantic parse: go_to(daniel,hallway)

Sentence: Daniel travelled to the bathroom.
Semantic parse: go_to(daniel,bathroom)
Sentence: Afterwards he went back to the garden.
Semantic parse: go_to(daniel,garden)

Sentence: Daniel travelled to the hallway.
Semantic parse: go_to(daniel,hallway)
Sentence: Following that he went back to the bathroom.
Semantic parse: go_to(daniel,bathroom)

Sentence: Where is Sandra?
Semantic parse: be_in(sandra,V1)

Sentence: Where is Mary?
Semantic parse: be_in(mary,V1)

Sentence: Where is Daniel?
Semantic parse: be_in(daniel,V1)

Sentence: Where is John?
Semantic parse: be_in(john,V1)

Your turn:
"""

prompt_qa12 = """Please parse the following english sentences into the semantic parse. The available keywords are: go_to, be:

Sentence: Mary and Daniel travelled to the bathroom.
Semantic parse: go_to(mary,bathroom), go_to(daniel,bathroom)

Sentence: John and Daniel travelled to the office.
Semantic parse: go_to(john,office), go_to(daniel,office)

Sentence: Where is Daniel? 
Semantic parse: be(daniel,V1)	

Sentence: Sandra and Daniel moved to the kitchen.
Semantic parse: go_to(sandra,kitchen), go_to(daniel,kitchen)

Sentence: Sandra and John moved to the garden.
Semantic parse: go_to(sandra,garden), go_to(john,garden)

Sentence: Where is Sandra? 
Semantic parse: be(sandra,V1)	
	
Sentence: Mary and Sandra went to the bedroom.
Semantic parse: go_to(mary,bedroom), go_to(sandra,bedroom)

Sentence: Mary and Daniel moved to the garden.
Semantic parse: go_to(mary,garden), go_to(daniel,garden)

Sentence: Where is Sandra?
Semantic parse: be(sandra,V1)	
 	
Sentence: Daniel and Mary went to the bathroom.
Semantic parse: go_to(daniel,bathroom), go_to(mary,bathroom)

Sentence: Sandra and Mary travelled to the garden.
Semantic parse: go_to(sandra,garden), go_to(mary,garden)

Sentence: Where is Daniel?
Semantic parse: be(daniel,V1)	
	
Sentence: John and Sandra travelled to the hallway.
Semantic parse: go_to(john,hallway), go_to(sandra,hallway)

Sentence: John and Sandra went back to the office.
Semantic parse: go_to(john,office), go_to(sandra,office)

Sentence: Where is John? 
Semantic parse: be(daniel,V1)

Sentence: John and Sandra journeyed to the office.
Semantic parse: go_to(john,office), go_to(sandra,office)

Sentence: John and Daniel journeyed to the kitchen.
Semantic parse: go_to(john,kitchen), go_to(daniel,kitchen)

Sentence: Where is John? 
Semantic parse: be(john,V1)

Your turn:
"""

prompt_qa13 = """Please parse the following english sentences into the semantic parse. The available keywords are: go_to, be:

Sentence: Daniel and Sandra journeyed to the office.
Semantic parse: go_to(daniel,office), go_to(sandra,office)

Sentence: Then they moved to the bedroom.
Semantic parse: go_to(daniel,office), go_to(daniel,office)

Sentence: Daniel and Sandra went to the office.
Semantic parse: go_to(daniel,office), go_to(sandra,office)

Sentence: Following that they went back to the kitchen.
Semantic parse: go_to(daniel,kitchen), go_to(daniel,kitchen)

Sentence: Mary and Daniel went to the bathroom.
Semantic parse: go_to(mary,bathroom), go_to(daniel,bathroom)

Sentence: Then they journeyed to the hallway.
Semantic parse: go_to(mary,hallway), go_to(daniel,hallway)

Sentence: Sandra and John moved to the kitchen.
Semantic parse: go_to(sandra,kitchen), go_to(john,kitchen)

Sentence: Then they moved to the hallway.
Semantic parse: go_to(sandra,kitchen), go_to(john,kitchen)

Sentence: Mary and Daniel travelled to the office.
Semantic parse: go_to(mary,office), go_to(daniel,office)

Sentence: After that they moved to the hallway.
Semantic parse: go_to(mary,hallway), go_to(daniel,hallway)

Sentence: Sandra and Mary went back to the kitchen.
Semantic parse: go_to(sandra,kitchen), go_to(mary,kitchen)

Sentence: Following that they travelled to the bathroom.
Semantic parse: go_to(sandra,bathroom), go_to(mary,bathroom)

Sentence: John and Mary went back to the hallway.
Semantic parse: go_to(john,hallway), go_to(mary,hallway)

Sentence: Then they went to the bathroom.
Semantic parse: go_to(john,bathroom), go_to(mary,bathroom)

Sentence: Mary and John moved to the hallway.
Semantic parse: go_to(mary,hallway), go_to(john,hallway)

Sentence: Following that they moved to the kitchen.
Semantic parse: go_to(mary,kitchen), go_to(john,kitchen)

Sentence: John and Daniel journeyed to the office.
Semantic parse: go_to(john,office), go_to(daniel,office)

Sentence: Following that they travelled to the hallway.
Semantic parse: go_to(john,hallway), go_to(daniel,hallway)

Sentence: Mary and Sandra travelled to the garden.
Semantic parse: go_to(mary,garden), go_to(sandra,garden)

Sentence: After that they went back to the kitchen.
Semantic parse: go_to(mary,kitchen), go_to(sandra,kitchen)

Sentence: Where is Daniel?
Semantic parse: be(daniel,V1)

Sentence: Where is John? 
Semantic parse: be(daniel,V1)

Sentence: Where is Sandra?
Semantic parse: be(sandra,V1)

Sentence: Where is Mary? 
Semantic parse: be(mary,V1)


Your turn:
"""

prompt_qa14 = """Please parse the following english sentences into the semantic parse. The available keywords are: go_to, and be_before:

Sentence: Bill went back to the cinema yesterday.
Semantic parse: go_to(bill,cinema,yesterday)

Sentence: Bill went back to the school this morning.
Semantic parse: go_to(bill,school,morning)

Sentence: This afternoon Bill went to the park.
Semantic parse: go_to(bill,park,afternoon)

Sentence: Bill moved to the school this evening.
Semantic parse: go_to(bill,school,evening)

Sentence: Yesterday Julie went to the office.
Semantic parse: go_to(julie,office,yesterday)

Sentence:Julie went to the school this morning.
Semantic parse: go_to(julie,school,morning)

Sentence: This afternoon Julie travelled to the cinema.
Semantic parse: go_to(julie,cinema,afternoon)

Sentence: This evening Julie went to the school.
Semantic parse: go_to(julie,school,evening)

Sentence: Fred went to the park yesterday.
Semantic parse: go_to(fred,park,yesterday)

Sentence: Fred moved to the office this morning.
Semantic parse: go_to(fred,office,morning)

Sentence: This afternoon Fred moved to the park.
Semantic parse: go_to(fred,park,afternoon)

Sentence: Yesterday Mary journeyed to the school.
Semantic parse: go_to(mary,school,yesterday)

Sentence: Mary travelled to the kitchen this morning.
Semantic parse: go_to(mary,kitchen,morning)

Sentence: Yesterday Mary went back to the office.
Semantic parse go_to(mary,office,yesterday)

Sentence: Yesterday Mary travelled to the park.
Semantic parse: go_to(mary,park,yesterday)

Sentence: This morning Mary moved to the kitchen.
Semantic parse: go_to(mary,kitchen,morning)

Sentence: Yesterday Fred journeyed to the cinema.
Semantic parse: go_to(fred,cinema,yesterday)

Sentence: Yesterday Mary moved to the kitchen.
Semantic parse: go_to(mary,kitchen,yesterday)

Sentence: Yesterday Bill moved to the park.
Semantic parse: go_to(bill,park,yesterday)

Sentence: This afternoon Julie journeyed to the office.
Semantic parse: go_to(julie,office,afternoon)

Sentence: This afternoon Julie journeyed to the office.
Semantic parse: go_to(julie,office,afternoon)

Sentence: Where was Bill before the school? 	
Semantic parse: be_before(bill,school,V1)

Sentence: Where was Bill before the office? 
Semantic parse: be_before(bill,office,V1)

Sentence: Where was Julie before the school? 	
Semantic parse: be_before(julie,school,V1)

Sentence: Where was Fred before the cinema? 
Semantic parse: be_before(fred,cinema,V1)

Sentence: Where was Mary before the park?
Semantic parse: be_before(mary,park,V1)

Your turn:
"""

prompt_qa15 = """
Please parse the follwoing english sentencts into the semantic parse. The available keywords are: be and be_afraid_of:

Sentence: Emily is a cat.
Semantic parse: be(emily,cat)

Sentence: Emily is a mouse.
Semantic parse: be(emily,mouse)

Sentence: Gertrude is a cat.
Semantic parse: be(gertrud,cat)

Sentence: Gertrude is a mouse.
Semantic parse: be(gertrude,mouse)

Sentence: Gertrude is a wolf.
Semantic parse: be(gertrude,wolf)

Sentence: Winona is a cat.
Semantic parse: be(winona,cat)

Sentence: Winona is a wolf.
Semantic parse: be(winona,wolf)

Sentence: Winona is a mouse.
Semantic parse: be(winona,mouse)

Sentence: Sentence: Winona is a sheep.
Semantic parse: be(winona,sheep)

Sentence: Jessica is a cat.
Semantic parse: be(jessica,cat)

Sentence: Jessica is a wolf.
Semantic parse: be(jessica,wolf)

Sentence: Jessica is a mouse.
Semantic parse: be(jessica,mouse)

Sentence: Mice are afraid of wolves.
Semantic parse: be_afraid_of(mouse,wolf)

Sentence: Mice are afraid of cats.
Semantic parse: be_afraid_of(mouse,cat)

Sentence: Cats are afraid of sheep.
Semantic parse: be_afraid_of(cat,sheep)

Sentence: Cats are afraid of wolves.
Semantic parse: be_afraid_of(cat,wolf)

Sentence: Sheep are afraid of wolves.
Semantic parse: be_afraid_of(sheep,wolf)

Sentence: Sheep are afraid of mice.
Semantic parse: be_afraid_of(sheep,mouse)

Sentence: Wolves are afraid of cats.
Semantic parse: be_afraid_of(wolf,cat)

Sentence: Wolves are afraid of mice.
Semantic parse: be_afraid_of(wolf,mouse)

Sentence: What is Gertrude afraid of?
Semantic parse: be_afraid_of(gertrude,V1)

Sentence: What is Winona afraid of?
Semantic parse: be_afraid_of(winona,V1)

Sentence: What is Jessica afraid of?
Semantic parse: be_afraid_of(jessica,V1)

Sentence: What is Emily afraid of?
Semantic parse: be_afraid_of(emily,V1)


Your turn:
"""

prompt_qa16 = """
Please parse the following English sentences into the semantic parse. The available keywords are: be_color and be:


Sentence: Lily is yellow.
Semantic parse:be_color(lily,yellow)

Sentence: Lily is white.
Semantic parse:be_color(lily,white)

Sentence: Brian is yellow.
Semantic parse: be_color(brian,yellow)

Sentence: Brian is white.
Semantic parse: be_color(brian,white)

Sentence: Brian is green.
Semantic parse: be_color(brian,green)

Sentence:  Greg is green.
Semantic parse: be_color(greg,green)

Sentence: Greg is gray.
Semantic parse: be_color(greg,gray)

Sentence: Julius is green.
Semantic parse: be_color(julius,green)

Sentence: Julius is yellow.
Semantic parse: be_color(julius,yellow)

Sentence: Bernhard is green.
Semantic parse: be_color(bernhard,green)

Sentence: Bernhard is white.
Semantic parse: be_color(bernhard,white)

Sentence: Bernhard is gray.
Semantic parse: be_color(bernhard,gray)

Sentence: Lily is a frog.
Semantic parse: be(lily,frog)

Sentence: Bernhard is a frog.
Semantic parse: be(bernhard,frog)

Sentence: Brian is a lion.
Semantic parse: be(brian,lion)

Sentence: Julius is a swan.
Semantic parse: be(julius,swan)

Sentence: Greg is a swan.
Semantic parse: be(greg,swan)

Sentence: Julius is a lion.
Semantic parse: be(julius,lion)

Sentence: Lily is a rhino.
Semantic parse: be(lily,rhino)

Sentence: Bernhard is a swan.
Semantic parse: be(bernhard,swan)

Sentence: Greg is a frog
Semantic parse: be(greg,frog)

Sentence: Greg is a rhino.
Semantic parse: be(greg,rhino)

Sentence: What color is Greg?
Semantic parse: be_color(greg,V1)

Sentence: What color is Brian?
Semantic parse: be_color(brian,V1)

Sentence: What color is Lily?
Semantic parse: be_color(lily,V1)

Sentence: What color is Bernhard?
Semantic parse: be_color(bernhard,V1)

Your turn:
"""

prompt_qa18 = """Please parse the following English sentences into the semantic parse. The available keywords are: fit_inside, and be_big:

Sentence: The container fits inside the suitcase.
Semantic parse: fit_inside(container,suitcase)

Sentence: The chocolate fits inside the box.
Semantic parse: fit_inside(chocolate,box)

Sentence: The chocolate fits inside the chest.
Semantic parse: fit_inside(chocolate,chest)

Sentence: The chocolate fits inside the container.
Semantic parse: fit_inside(chocolate,container)

Sentence: The container fits inside the suitcase.
Semantic parse: fit_inside(container,suitcase)

Sentence: The suitcase is bigger than the chocolate.
Semantic parse: be_big(suitcase,chocolate)

Sentence: The suitcase fits inside the box.
Semantic parse: fit_inside(suitcase,box)

Sentence: The container is bigger than the suitcase.
Semantic parse: be_big(container,suitcase)

Sentence: The box of chocolates fits inside the chest.
Semantic parse: fit_inside(box_of_chocolates,chest)

Sentence: The box of chocolates fits inside the suitcase.
Semantic parse: fit_inside(box_of_chocolates,suitcase)

Sentence: The box of chocolates fits inside the box.
Semantic parse: fit_inside(box_of_chocolates,box)

Sentence: The box of chocolates fits inside the container.
Semantic parse: fit_inside(box_of_chocolates,container)

Sentence: The chocolate fits inside the box of chocolates.
Semantic parse: fit_inside(chocolate,box_of_chocolates)


Sentence: Does the box fit in the box of chocolates?	
Semantic parse: fit_inside(box,box_of_chocolates)

Sentence: Is the box bigger than the box of chocolates?
Semantic parse: be_big(box,box_of_chocolates)

Sentence: Does the chocolate fit in the box?
Semantic parse: fit_inside(chocolate,box)


Sentence: Does the box of chocolates fit in the container?
Semantic parse: fit_inside(box_of_chocolates,container)

Sentence: Is the box of chocolates bigger than the box?	
Semantic parse: be_big(box_of_chocolates,box)


Sentence: Does the box of chocolates fit in the box?	
Semantic parse: fit_inside(box_of_chocolates,box)

Sentence: Is the chocolate bigger than the suitcase?	
Semantic parse: be_big(chocolate,suitcase)

Sentence: Is the container bigger than the chocolate?
Semantic parse: be_big(container,chocolate)

Your turn:
"""

prompt_qa20 = """Please parse the following English sentences into the semantic parse. The available keywords are: go_to, be, and get:

Sentence: Yann picked up the football there.
Semantic parse: get(yann,football)

Sentence: Sumit took the football there.
Semantic parse: get(sumit,football)

Sentence: Yann got the pajamas there.
Semantic parse: get(yann,pajama)

Sentence: Antoine moved to the garden.
Semantic parse: go_to(antoine,garden)

Sentence: Sumit grabbed the pajamas there.
Semantic parse: get(sumit,pajama)

Sentence: Yann got the football there.
Semantic parse: get(yann,football)

Sentence: Jason grabbed the milk there.
Semantic parse: get(jason,milk)

Sentence: Where will Sumit go?	
Semantic parse: go_to(sumit,V1)


Sentence: Why did Yann go to the garden?
Semantic parse: go_to(yann,garden,V1)

Sentence: Why did Yann go to the kitchen?
Semantic parse: go_to(yann,kitchen,V1)

Sentence: Why did Antoine go to the kitchen?
Semantic parse: go_to(antoine,kitchen,V1)

Sentence: Why did Sumit go to the bedroom?
Semantic parse: go_to(sumit,bedroom,V1)

Sentence: Why did Jason get the milk?
Semantic parse: get(jason,milk,V1)

Sentence: Why did Yann get the football?
Semantic parse: get(yann,football,V1)

Sentence: Why did Yann get the pajamas?
Semantic parse: get(yann,pajama,V1)


Sentence: Sumit is tired.
Semantic parse: be(sumit,tired)

Sentence: Jason went back to the kitchen.
Semantic parse: go_to(jason,kitchen)

Sentence: Sumit went back to the bedroom.
Semantic parse: go_to(sumit,bedroom)

Sentence: Antoine journeyed to the garden.
Semantic parse: go_to(antoine,garden)

Sentence: Antoine travelled to the kitchen.
Semantic parse: go_to(antoine,kitchen)

Sentence: Sumit went to the kitchen.
Semantic parse: go_to(sumit,kitchen)

Sentence: Yann travelled to the garden.
Semantic parse: go_to(yann,garden)


Your turn:
"""

prompts = {1: prompt_qa1, 
           6: prompt_qa6, 
           8: prompt_qa8, 
           9: prompt_qa9, 
           10: prompt_qa10, 
           11: prompt_qa11, 
           12: prompt_qa12, 
           13: prompt_qa13, 
           14: prompt_qa14, 
           15: prompt_qa15, 
           16: prompt_qa16, 
           18: prompt_qa18, 
           20: prompt_qa20}
