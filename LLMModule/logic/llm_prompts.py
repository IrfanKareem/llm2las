prompt_qa1 = """Please parse the sentence is provided below into a first-order logic predicate form. The available predicates names are: go_to, be_in.
Here are a few examples of parsings to guide you in the task:
\"\"\"
Sentence: Mary moved to the bathroom.
Semantic parse: go_to(mary,bathroom).

Sentence: John went to the hallway.
Semantic parse: go_to(john,hallway).

Sentence: Where is Mary? 
Semantic parse: be_in(mary,V1).

Sentence: Daniel went back to the hall.
Semantic parse: go_to(daniel,hall).

Sentence: Sandra moved to the garden.
Semantic parse: go_to(sandra,garden).

Sentence: Where is Steve? 
Semantic parse: be_in(steve,V1).

Sentence: Sarah journeyed to the bathroom.
Semantic parse: go_to(sarah,bathroom).

Sentence: Douglas travelled to the office.
Semantic parse: go_to(douglas, office).

Sentence: Where is Daniel? 
Semantic parse: be_in(daniel,V1).
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa4 = """Please parse the sentence is provided below into a first-order logic predicate form. 
The available predicates names are: be_east_of, be_west_of, be_north_of, and be_south_of.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: The office is north of the kitchen.
Semantic parse: be_north_of(office,kitchen)

Sentence: The garden is south of the kitchen.
Semantic parse: be_south_of(office,kitchen)

Sentence: The park is west of the store.
Semantic parse: be_west_of(park,store)

Sentence: The supermarket is west of the mall.
Semantic parse: be_east_of(supermarket,mall)

Sentence: What is north of the parking?
Semantic parse: be_north_of(V1,parking)

Sentence: What is east of the supermarket?
Semantic parse: be_east_of(V1,parking)

Sentence: What is the office north of?
Semantic parse: be_north_of(office,V1)

Sentence: What is the stadium west of?
Semantic parse: be_west_of(stadium,V1)

\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa5 = """Please parse the sentence is provided below into a first-order logic predicate form. 
The available predicates names are: give_to, give, take, go_to, and leave.
Look that the give_to based predicates implies also give and receive.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: Alvin travelled to the office.
Semantic parse: go_to(alvin,office)

Sentence: Mathilde picked up the baseball there.
Semantic parse: take(mathilde,baseball)

Sentence: Ricardo went back to the park.
Semantic parse: go_to(ricardo,park)

Sentence: Aaron gave the fork to Albert.
Semantic parse: give_to(aaron,fork,albert)

Sentence: Who received the football?
Semantic parse: receive(V1,football)

Sentence: What did Juan give to Ramon?
Semantic parse: give_to(juan,V1,ramon)

Sentence: Who did Axel give the apple to?
Semantic parse: give_to(axel,apple,V1)

Sentence: Who gave the milk?
Semantic parse: give(V1,milk)

Sentence: Margarita put down the milk.
Semantic parse: leave(Margarita,milk)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa6 =  """Please parse the sentence is provided below into a first-order logic predicate form. The available predicates names are: pickup, drop, go_to, and be_in.
Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: Sandra put down the football.  
Semantic parse: drop(sandra, football)

Sentence: Max left the cup.  
Semantic parse: drop(max, cup)

Sentence: Is Steve in the livingroom?  
Semantic parse: be_in(steve, livingroom)

Sentence: Gilda moved to the bathroom.  
Semantic parse: go_to(gilda, bathroom)

Sentence: Marian picked up the apple there.  
Semantic parse: pickup(marian, apple)

Sentence: Is Mary in the bedroom?  
Semantic parse: be_in(mary, bedroom)

Sentence: Max journeyed to the bathroom.  
Semantic parse: go_to(max, bathroom)

Sentence: Arthur got the milk there.  
Semantic parse: pickup(arthur, milk)

Sentence: Cloe is in the room.  
Semantic parse: be_in(cloe, room)

Sentence: Mary discarded the milk.  
Semantic parse: drop(mary, milk)

Sentence: Is Sandra in the park?  
Semantic parse: be_in(sandra, park)

Sentence: Susan dropped the spoon.  
Semantic parse: drop(susan, spoon)

Sentence: John is in the garden.  
Semantic parse: be_in(john, garden)

Sentence: Daniel went back to the hallway.  
Semantic parse: go_to(daniel, hallway)

Sentence: Francesco took the cup there.  
Semantic parse: pickup(francesco, cup)

Sentence: Joan is currently in the room.  
Semantic parse: be_in(joan, room)

Sentence: Is Daniel in the bathroom?  
Semantic parse: be_in(daniel, bathroom)

Sentence: Mary went to the garden.  
Semantic parse: go_to(mary, garden)

Sentence: Alex got the coconut there.  
Semantic parse: pickup(alex, coconut)

Sentence: John is in the garden.  
Semantic parse: be_in(john, garden)

Sentence: Babar put down the jug.  
Semantic parse: drop(babar, jug)

Sentence: Is Mary in the bedroom?  
Semantic parse: be_in(mary, bedroom)

Sentence: Sarah grabbed the milk there.  
Semantic parse: pickup(sarah, milk)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa8 = """Please parse the sentence is provided below into a first-order logic predicate form. The available predicates names are: pickup, drop, go_to, and carry.
Here are a few examples of parsings to guide you in the task:
\"\"\"
Sentence: What is Esther carrying?
Semantic parse: carry(sandra, V1)

Sentence: Mary moved to the bathroom.
Semantic parse: go_to(mary, bathroom)

Sentence: Joan picked up the apple there.
Semantic parse: pickup(joan, apple)

Sentence: Daniel discarded the football.
Semantic parse: drop(daniel, football)

Sentence: Joaquin put down the baseball there.
Semantic parse: drop(joaquin, baseball)

Sentence: Mariah got the football there.
Semantic parse: pickup(mariah, football)

Sentence: Cloe journeyed to the livingroom.
Semantic parse: go_to(cloe, livingroom)

Sentence: John went to the kitchen.
Semantic parse: go_to(john, kitchen)

Sentence: Mary took the football there.
Semantic parse: pickup(mary, football)

Sentence: Max got the milk there.
Semantic parse: pickup(max, milk)

Sentence: Carmen grabbed the glass there.
Semantic parse: pickup(carmen, glass)

Sentence: Mathilde left the hammer.
Semantic parse: drop(mathilde, hammer)

Sentence: Susan went back to the park.
Semantic parse: go_to(susan, park)

Sentence: Mary dropped the football.
Semantic parse: drop(mary, football)

Sentence: Savanah picked up the dish there.
Semantic parse: pickup(savanah, dish)

Sentence: John left the coconut.
Semantic parse: drop(john, coconut)

Sentence: What is Babar carrying?
Semantic parse: carry(babar, V1)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa9 = """Please parse the sentence is provided below into a first-order logic predicate form. 
The available predicates names are: go_to and be_in.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: Sandra travelled to the kitchen.
Semantic parse: go_to(sandra, kitchen)

Sentence: Mel is not in the hallway.
Semantic parse: be_in(mel, hallway)

Sentence: William is no longer in the garage.
Semantic parse: be_in(william, garage)

Sentence: Is Mary in the bedroom?
Semantic parse: be_in(mary, bedroom)

Sentence: Babar went back to the supermarket.
Semantic parse: go_to(Babar, supermarket)

Sentence: Giuseppe went to the bedroom.
Semantic parse: go_to(giuseppe, bedroom)

Sentence: Cloe is no longer in the bedroom.
Semantic parse: be_in(cloe, bedroom)

Sentence: Sandra is in the garden.
Semantic parse: be_in(sandra, garden)

Sentence: Tom is in the garage.
Semantic parse: be_in(tom, garage)

Sentence: Daniel went to the office.
Semantic parse: go_to(daniel, office)

Sentence: Kirsten journeyed to the park.
Semantic parse: go_to(kirsten, park)

Sentence: Pauline moved to the hallway.
Semantic parse: go_to(pauline, hallway)

Sentence: Bruce is not in the garden.
Semantic parse: be_in(bruce, garden)

Sentence: Giuseppe went to the bedroom.
Semantic parse: go_to(giuseppe, bedroom)

Sentence: Is William in the kitchen?
Semantic parse: be_in(william, kitchen)
\"\"\"

Please, provide just the parsing data using the examples format and do not negate predicates.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa10 = """Please parse the sentence is provided below into a first-order logic predicate form. 
The available predicates names are: go_to, and be_in. Please use the "|" character to represent disjunction.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: Joulie is either in the school or the home.
Semantic parse: be_in(joulie,school) | be_in(joulie,home)

Sentence: Angelina is either in the cinema or the garden.
Semantic parse: be_in(angelina,cinema) | be_in(angelina,garden)

Sentence: Bill moved to the park.
Semantic parse: go_to(bill,park)

Sentence: Is Fred in the park?
Semantic parse: be_in(fred,park)

Sentence: Fred travelled to the cinema.
Semantic parse: go_to(fred,cinema)

Sentence: Is Rita in the office?
Semantic parse: be_in(rita,office)

Sentence: Monica is in the store.
Semantic parse: be_in(monica,store)

Sentence: Is Margherita in the kitchen?
Semantic parse: be_in(margherita,kitchen)

Sentence: Jim went back to the office.
Semantic parse: go_to(jim,office)

Sentence: Mary moved to the park.
Semantic parse: go_to(mary,park)

Sentence: Bill is either in the kitchen or the park.
Semantic parse: be_in(bill,kitchen) | be_in(bill,park)

Sentence: Leonardo is in the roof.
Semantic parse: be_in(Leonardo,roof)

Sentence: Sean is either in the store or the theater.
Semantic parse: be_in(sean,store) | be_in(sean,theater)

Sentence: Nicolas went to the cinema.
Semantic parse: go_to(nicolas,cinema)

Sentence: Susan journeyed to the school.
Semantic parse: go_to(susan,school)

Sentence: Is Mameli in the theater?
Semantic parse: be_in(mameli,theater)

Sentence: Giacomo is either in the kitchen or the kitchen.
Semantic parse: be_in(giacomo,kitchen) | be_in(giacomo,kitchen)
\"\"\"

Please, provide the parsing data using the examples format and avoid commenting the results.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa11 = """Please parse the sentence is provided below into a first-order logic predicate form. 
The available predicates names are: go_to, and be_in.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: John travelled to the bathroom.
Semantic parse: go_to(john,bathroom)

Sentence: After that Carlos travelled to the car.
Semantic parse: go_to(carlos,car)

Sentence: Then Albert went back to the garden.
Semantic parse: go_to(albert,garden)

Sentence: After that Javier moved to the gym.
Semantic parse: go_to(javier,gym)

Sentence: Then Nick journeyed to the kitchen.
Semantic parse: go_to(nick,kitchen)

Sentence: Following that Sandra went to the bedroom.
Semantic parse: go_to(sandra,bedroom)

Sentence: Where is Sandra?
Semantic parse: be_in(sandra,V1)

Sentence: Afterwards Margarita went back to the garden.
Semantic parse: go_to(margarita,garden)

Sentence: After that Carlos moved to the hallway.
Semantic parse: go_to(carlos,hallway)

Sentence: Then Giuseppina journeyed to the garden.
Semantic parse: go_to(giuseppina,garden)

Sentence: Following that Elena travelled to the bedroom.
Semantic parse: go_to(elena,bedroom)

Sentence: Sentence: Mary moved to the bathroom.
Semantic parse: go_to(mary,bathroom)

Sentence: Afterwards Noel went to the mall.
Semantic parse: go_to(noel,mall)

Sentence: Afterwards Sandra travelled to the office.
Semantic parse: go_to(sandra,office)

Sentence: Then Pauline went back to the farm.
Semantic parse: go_to(pauline,farm)

Sentence: Following that Cloe went back to the bedroom.
Semantic parse: go_to(cloe,bedroom)

Sentence: John journeyed to the kitchen.
Semantic parse: go_to(john,kitchen)

Sentence: Frank went back to the store.
Semantic parse: go_to(frank,store)

Sentence: Where is Antonio?
Semantic parse: be_in(antonio,V1)

Sentence: Following that Daniel moved to the bathroom.
Semantic parse: go_to(daniel,bathroom)

Sentence: Pedro moved to the roof.
Semantic parse: go_to(pedro,roof)

Sentence: Then Julius went to the bar.
Semantic parse: go_to(julius,bar)

Sentence: Mathilde went to the office.
Semantic parse: go_to(mathilde,office)

Sentence: Sandra travelled to the garden.
Semantic parse: go_to(sandra,garden)

Sentence: After that Marilyn went to the bedroom.
Semantic parse: go_to(marilyn,office)

Sentence: Where is Albert?
Semantic parse: be_in(albert,V1)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa12 = """Please parse the sentence is provided below into a first-order logic predicate form. 
The available predicates names are: go_to, be.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: Mary and Daniel travelled to the park.
Semantic parse: go_to(mary,park), go_to(daniel,park)

Sentence: Marianna and Martina travelled to the library.
Semantic parse: go_to(marianna,library), go_to(martina,library)

Sentence: Where is Daniel? 
Semantic parse: be(daniel,V1)	

Sentence: Sandra and Daniel moved to the kitchen.
Semantic parse: go_to(sandra,kitchen), go_to(daniel,kitchen)

Sentence: Where is Sandra? 
Semantic parse: be(sandra,V1)	
	
Sentence: Cloe and Winona went to the bedroom.
Semantic parse: go_to(cloe,bedroom), go_to(winona,bedroom)

Sentence: Antonio and Andrea went back to the classroom.
Semantic parse: go_to(antonio,office), go_to(andrea,classroom)

Sentence: Where is Steve?
Semantic parse: be(steve,V1)	

Sentence: Valeria and Giorgio journeyed to the mall.
Semantic parse: go_to(valeria,office), go_to(giorgio,mall)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa13 = """Please parse the sentence is provided below into a first-order logic predicate form.
The available predicates names are: go_to, be.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: After that Esther and Noel went back to the home.
Semantic parse: go_to(esther,home), go_to(noel,home)

Sentence: Where is Sandra?
Semantic parse: be(sandra,V1)

Sentence: Following that Thiery and Diego travelled to the field.
Semantic parse: go_to(thiery,field), go_to(diego,field)

Sentence: After that Kate and Micah moved to the hallway.
Semantic parse: go_to(kate,hallway), go_to(micah,hallway)

Sentence: Sentence: Daniel and Sandra journeyed to the office.
Semantic parse: go_to(daniel,office), go_to(sandra,office)

Sentence: Following that Oscar and Ana moved to the kitchen.
Semantic parse: go_to(oscar,kitchen), go_to(ana,kitchen)

Sentence: Following that Micah and Kate went back to the mall.
Semantic parse: go_to(micah,mall), go_to(kate,mall)

Sentence: Mary and Daniel travelled to the store.
Semantic parse: go_to(mary,store), go_to(daniel,store)

Sentence: Then Francesco and Alessandra journeyed to the hallway.
Semantic parse: go_to(francesco,hallway), go_to(alessandra,hallway)

Sentence: Where is Juan?
Semantic parse: be(daniel,V1)

Sentence: Sandra and John moved to the kitchen.
Semantic parse: go_to(sandra,kitchen), go_to(john,kitchen)

Sentence: Then Pilar and Evelio moved to the bedroom.
Semantic parse: go_to(pilar,bedroom), go_to(evelio,bedroom)

Sentence: Daniel and Sandra went to the office.
Semantic parse: go_to(daniel,office), go_to(sandra,office)

Sentence: Where is Peter?
Semantic parse: be(daniel,V1)

Sentence: Then Oscar and Ana moved to the kitchen.
Semantic parse: go_to(oscar,kitchen), go_to(ana,kitchen)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa14 = """Please parse the sentence is provided below into a first-order logic predicate form.
The available predicates names are: go_to, and be_before.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: This morning Mary moved to the kitchen.
Semantic parse: go_to(mary,kitchen,morning)

Sentence: Where was Oscar before the office?
Semantic parse: be_before(oscar,office,V1)

Sentence: This afternoon Freud moved to the hospital.
Semantic parse: go_to(freud,hospital,afternoon)

Sentence: Yesterday Alessia journeyed to the school.
Semantic parse: go_to(alessia,school,yesterday)

Sentence: This afternoon Cloe travelled to the cinema.
Semantic parse: go_to(cloe,cinema,afternoon)

Sentence: Where was Austin before the school?
Semantic parse: be_before(austin,school,V1)

Sentence: Yesterday Valeria went to the office.
Semantic parse: go_to(valeria,office,yesterday)

Sentence: This afternoon Micah went to the park.
Semantic parse: go_to(micah,park,afternoon)

Sentence: Julie went to the park this morning.
Semantic parse: go_to(julie,park,morning)

Sentence: This evening Julie went to the mall.
Semantic parse: go_to(julie,mall,evening)

Sentence: Bill went back to the cinema yesterday.
Semantic parse: go_to(bill,cinema,yesterday)

Sentence: Babbar moved to the office early in the morning.
Semantic parse: go_to(Babbar,office,morning)

Sentence: This evening Giuseppe moved to the mall.
Semantic parse: go_to(giuseppe,mall,evening)

Sentence: Maria went back to the school this morning.
Semantic parse: go_to(maria,school,morning)

Sentence: This afternoon Jude journeyed to the office.
Semantic parse: go_to(Jude,office,afternoon)

Sentence: Mary travelled to the kitchen this morning.
Semantic parse: go_to(mary,kitchen,morning)

Sentence: Where was Julie before the park?
Semantic parse: be_before(julie,park,V1)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa15 = """Please parse the sentence is provided below into a first-order logic predicate form.
The available predicates names are: be and be_afraid_of.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: Mice are afraid of wolves.
Semantic parse: be_afraid_of(mouse,wolf)

Sentence: What is Winona afraid of?
Semantic parse: be_afraid_of(winona,V1)

Sentence: Luis is a rat.
Semantic parse: be(luis,rat)

Sentence: What is Gertrude afraid of?
Semantic parse: be_afraid_of(gertrude,V1)

Sentence: Mice are afraid of cats.
Semantic parse: be_afraid_of(mouse,cat)

Sentence: Gertrude is a horse.
Semantic parse: be(gertrud,horse)

Sentence: Winona is a sheep.
Semantic parse: be(winona,sheep)

Sentence: Mike is a dog.
Semantic parse: be(mike,dog)

Sentence: Massiel is a cat.
Semantic parse: be(massiel,cat)

Sentence: Marianna is a kangaroo.
Semantic parse: be(marianna,kangaroo)

Sentence: Cats are afraid of wolves.
Semantic parse: be_afraid_of(cat,wolf)

Sentence: What is Emily afraid of?
Semantic parse: be_afraid_of(emily,V1)

Sentence: Sheep are afraid of wolves.
Semantic parse: be_afraid_of(sheep,wolf)

Sentence: Kangaroos are afraid of lions.
Semantic parse: be_afraid_of(kangaroo,lion)

Sentence: What is Jessica afraid of?
Semantic parse: be_afraid_of(jessica,V1)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa16 = """Please parse the sentence is provided below into a first-order logic predicate form.
The available predicates names are: be_color and be.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: What color is Joan?
Semantic parse: be_color(joan,V1)

Sentence: Antonio is gray.
Semantic parse: be_color(antonio,gray)

Sentence: What color is David?
Semantic parse: be_color(david,V1)

Sentence: Salvatore is a cat.
Semantic parse: be(salvatore,cat)

Sentence: Greg is a frog.
Semantic parse: be(greg,frog)

Sentence: Lily is yellow.
Semantic parse: be_color(lily,yellow)

Sentence: August is yellow.
Semantic parse: be_color(august,yellow)

Sentence: Antonio is a elephant.
Semantic parse: be(antonio,elephant)

Sentence: Salvatore is green.
Semantic parse: be_color(salvatore,green)

Sentence: Brian is white.
Semantic parse: be_color(brian,white)

Sentence: Frank is white.
Semantic parse: be_color(frank,white)

Sentence: Giusuppe is a rhino.
Semantic parse: be(julius,rhino)

Sentence: Manuel is a dog.
Semantic parse: be(manuel,dog)

Sentence: What color is Greg?
Semantic parse: be_color(greg,V1)

Sentence: Lily is yellow.
Semantic parse: be_color(lily,yellow)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa17 = """Please parse the sentence is provided below into a first-order logic predicate form.
The available predicates names are: above, below, right, and below.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: The triangle is above the pink rectangle.
Semantic parse: be_above_of(triangle,pink_rectangle)

Sentence: The blue square is to the left of the triangle.
Semantic parse: be_left_of(blue_square,triangle)

Sentence: The blue square is to the right of the circle.
Semantic parse: be_right_of(blue_square,circle)

Sentence: The red square is below the blue square.
Semantic parse: be_below_of(red_square,blue_square)

Sentence: The sphere is below the square.
Semantic parse: be_below_of(sphere,square)

Sentence: Is the blue square below the yellow square?
Semantic parse: be_below_of(blue_square,yellow_square)

Sentence: Is the sphere to the right of the triangle?
Semantic parse: be_right_of(sphere,triangle)

Sentence: Is the red circle above the cyan square?
Semantic parse: be_above_of(red_circle,cyan_square)

Sentence: Is the square to the right of the circle?
Semantic parse: be_right_of(square,circle)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa18 = """Please parse the sentence is provided below into a first-order logic predicate form.
The available predicates names are: fit_inside and be_big.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: The chocolate fits inside the chest.
Semantic parse: fit_inside(chocolate,chest)

Sentence: Is the box bigger than the box of chocolates?
Semantic parse: be_big(box,box_of_chocolates)

Sentence: The container fits inside the suitcase.
Semantic parse: fit_inside(container,suitcase)

Sentence: Does the chocolate fit in the box?
Semantic parse: fit_inside(chocolate,box)

Sentence: The suitcase is bigger than the chocolate.
Semantic parse: be_big(suitcase,chocolate)

Sentence: Is the container bigger than the chocolate?
Semantic parse: be_big(container,chocolate)

Sentence: The box of chocolates fits inside the chest.
Semantic parse: fit_inside(box_of_chocolates,chest)

Sentence: Does the box fit in the box of chocolates?
Semantic parse: fit_inside(box,box_of_chocolates)

Sentence: The chocolate fits inside the box.
Semantic parse: fit_inside(chocolate,box)

Sentence: The container is bigger than the suitcase.
Semantic parse: be_big(container,suitcase)

Sentence: Is the chocolate bigger than the suitcase?
Semantic parse: be_big(chocolate,suitcase)

Sentence: The box is bigger than the suitcase.
Semantic parse: be_big(box,suitcase)

Sentence: The chocolate fits inside the box of chocolates.
Semantic parse: fit_inside(chocolate,box_of_chocolates)

Sentence: Does the box of chocolates fit in the container?
Semantic parse: fit_inside(box_of_chocolates,container)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa19 = """Please parse the sentence is provided below into a first-order logic predicate form. 
The available predicates names are: edge, and path.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: The garden is west of the bathroom.
Semantic parse: edge(garden,bathroom,west),edge(bathroom,garden,east).

Sentence: The bedroom is east of the hallway.
Semantic parse: edge(bedroom,hallway,east),edge(hallway,bedroom,west).

Sentence: The kitchen is north of the kitchen.
Semantic parse: edge(kitchen,park,north),edge(park,kitchen,south).

Sentence: The roof is south of the bathroom.
Semantic parse: edge(roof,bathroom,south),edge(bathroom,roof,north).

Sentence: How do you go from the bathroom to the hallway?
Semantic parse: path(bathroom, hallway, V1, V2).
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_qa20 = """Please parse the sentence is provided below into a first-order logic predicate form. 
The available predicates names are: go_to, be, and get.

Here are a few examples of parsings to guide you in the task:

\"\"\"
Sentence: Yann picked up the baseball there.
Semantic parse: get(yann,baseball)

Sentence: Steve took the football there.
Semantic parse: get(steve,football)

Sentence: Adrian got the laptop there.
Semantic parse: get(adrian,laptop)

Sentence: Lisa grabbed the pajamas there.
Semantic parse: get(lisa,pajama)

Sentence: Antoine moved to the garden.
Semantic parse: go_to(antoine,garden)

Sentence: Grace went back to the park.
Semantic parse: go_to(grace,park)

Sentence: Rafael journeyed to the mall.
Semantic parse: go_to(rafael,mall)

Sentence: Olivia travelled to the supermarket.
Semantic parse: go_to(olivia,supermarket)

Sentence: Sumit went to the kitchen.
Semantic parse: go_to(sumit,kitchen)

Sentence: Sumit is tired.
Semantic parse: be(sumit,tired)

Sentence: Joan is bored.
Semantic parse: be(joan,bored)

Sentence: Luisa is sleepy.
Semantic parse: be(luisa,sleepy)

Sentence: Where will Alain go?	
Semantic parse: go_to(alain,V1)

Sentence: Where will Victoria go?	
Semantic parse: go_to(victoria,V1)

Sentence: Why did Steve go to the store?
Semantic parse: go_to(steve,store,V1)

Sentence: Why did Susan go to the hall?
Semantic parse: go_to(susan,hall,V1)

Sentence: Why did Johan get the juice?
Semantic parse: get(johan,juice,V1)

Sentence: Why did Pancho get the football?
Semantic parse: get(pancho,football,V1)
\"\"\"

Please, provide just the parsing data using the examples format.
The sentence to parse is:
\"\"\"
Sentence: {{sentence}}
Semantic parse:
\"\"\"
"""

prompt_mb = """I want you to parse a sentence given its fluent representation (fact atoms) into its Mode bias fluent representation.
The Mode bias fluent consist of atoms from the sentence's fluent representation where all arguments have been replaced by their types as argument for  "var" or "const". For example, const(type) or var(type). The argument types are determined using the POS tagging data of the sentence and the WH-determiners (whose POS tag is WDT).

Lest break the task in several steps:
1. Determine the POS tagging sequence for the input sentence.
2. If the input sentence fluent representation contains an argument that is a variable, then apply just one of the following cases: 
	2.1 If the question starting word is a WH-determiner (WDT), use noun lemma text as type for the variable. For example, for "What color is Mary?" mode bias is: be_color(var(nnp), var(color)) ;
	2.2 If there is not WH-determiner (WDT) in the sentence, but it is a "when", "where" or a "what" question , then the variable’s type is "nn";
	2.3 If the question is a "who" question, then the variable’s type is "nnp";
	2.4 If the question is a "why" question, then the variable’s type is "jj";
	2.5 If the question is a "how many" question, then the variable’s type is "number".
3. If the argument has an "isA" relationship with any WH-determiners from the story's questions, then its type is given by the WH-determiner;
4. Otherwise, the argument's type is given by its associated tag.

We provide the types for all arguments that have a temporal aspect and the types of variables in "why" questions with "const" wrappings. We give the types of all arguments that have a temporal aspect or that are adjectives without "isA" relationships with determiners "const" wrappings. The types of all other arguments are given "var" wrappings. Table 2 provides the mode bias fluents for the sentences in a story. 

##Notes
- For case 2.1 does not derive the noun POS tagging for the type but use the noun lemma itself.
- A Temporal Aspect is when a word is related to some temporal like "day". Fo example, "yesterday" has a temporal aspect.

The following are some examples to allow you to understand the task: 

Sentence: Mice are afraid of wolves. 
Fact atom: be_afraid_of(mouse, wolf).
Mode bias: be_afraid_of(var(nn), var(nn)).

Sentence: Mary is a mouse.
Fluent representation: be(mary, mouse).
mode bias: be(var(nnp), var(nn)).

Sentence: What is Mary afraid of?
Fluent representation: be_afraid_of(mary, V1).
Mode bias: be_afraid_of(var(nnp), var(nn)).

Sentence: What color is Mary?.
Fluent representation: be_color(mary, V1).
Mode bias: be_color(var(nnp), var(color)).

Sentence: What is Luca carrying?
Fluent representation: carry(luca, V1).
Mode bias: carry(var(nnp), var(nn)).

Sentence: What size is Phill?.
Fluent representation: be_size(phill, V1).
Mode bias: be_size(var(nnp), var(size)).

Sentence: Joan is sick.
Fluent representation: be(joan, V1).
Mode bias: be(var(nnp), const(jj)).


Please, strictly provide just the parsing data using the examples format. 
No extra comments or explanations are needed.
The sentence to parse is:
Sentence: {{sentence}}	
Fluent representation: {{fluent}}
Mode bias:
"""



prompts = {0: prompt_mb,
           1: prompt_qa1, 
           4: prompt_qa4,
           5: prompt_qa5,
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
           17: prompt_qa17, 
           18: prompt_qa18, 
           19: prompt_qa19,
           20: prompt_qa20}
