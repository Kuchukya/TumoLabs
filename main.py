templates = ['template1', 'template2', 'template3']
template1 = "  1. It was about {} {} ago when I arrived at the hospital in a {}.The hospital is a/an {} place, there are a lot of {} {} here. There are nurses here who have {} {}. If someone wants to come into my room I told them that they have to {} first. I've decorated my room with {} {}. Today I talked to a doctor and they were wearing a {} on their {}. I heard that all doctors {} {} every day for breakfast. The most {} thing about being in the hospital is the {} {} !"
template2 = "  2. This weekend I am going camping with {} {}. I packed my lantern, sleeping bag, and {}. I am so {} to {} in a tent. I am {} we might see a(n) {}, I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and {}. I have heard that the {} lake is great for {}. Then we will {} hike through the forest for {} {}. If I see a {} {} while hiking, I am going to bring it home as a pet! At night we will tell {} {} stories and roast {} around the campfire!! "
template3 = "  3. Dear {} {}, I am writing to you from a {} castle in an enchanted forest. I found myself here one day after going for a ride on a {} {} in {}. There are {} {} and {} {} here! In the {} there is a pool full of {}. I fall asleep each night on a {} of {} and dream of {} {}. It feels as though I have lived here for {} {}. I hope one day you can visit, although the only way to get here now is {} on a {} {}!!"

print(template1, "\n", template2, "\n", template3)

print("   ")
print("Please select a template:")
for i, template in enumerate(templates):
  print(f"{i+1}. {template}")

user_choice = int(input("Enter the number of the template you want to use: "))

if user_choice > 0 and user_choice <= len(templates):
  chosen = templates[user_choice - 1]
  print(f"You have chosen {chosen}")
else:
  print("Invalid choice, please try again.")

if user_choice == 1:
  Number = int(input("Question 1/18 \nInput a number "))
  Measure_of_time = input("Question 2/18 \nInput a measure of time ")
  Mode_of_Transportation = input(
    "Question 3/18 \nInput a mode of Transportation ")
  Adjective = input("Question 4/18 \nInput an adjective ")
  Adjective2 = input("Question 5/18 \nInput another adjective ")
  Noun = input("Question 6/18 \nInput a noun ")
  Color = input("Question 7/18 \nInput a color ")
  Part_of_the_Body = input("Question 8/18 \nInput a part of the body ")
  Verb = input("Question 9/18 \nInput a verb ")
  Number1 = int(input("Question 10/18 \nInput a number "))
  Noun2 = input("Question 11/18 \nInput the 2nd noun ")
  Noun3 = input("Question 12/18 \nInput the 3nd noun ")
  Part_of_the_Body_2 = input(
    "Question 13/18 \nInput another part of the body ")
  Verb2 = input("Question 14/18 \nInput another verb ")
  Noun4 = input("Question 15/18 \nInput the 3nd noun ")
  Adjectives = input("Question 16/18 \nInput another adjective ")
  Silly_Word = input("Question 17/18 \nInput another adjective ")
  Noun5 = input("Question 18/18 \nInput a noun ")

  print(
    template1.format(Number, Measure_of_time, Mode_of_Transportation,
                     Adjective, Adjective2, Noun, Color, Part_of_the_Body,
                     Verb, Number1, Noun2, Noun3, Part_of_the_Body_2, Verb2,
                     Noun4, Adjectives, Silly_Word, Noun5))

if user_choice == 2:
  Number = int(input("Question 1/20 \nInput a number "))
  Number2 = int(input("Question 2/20 \nInput a number "))
  Proper_Noun = input("Question 3/20 \nInput a proper noun ")
  Person_Name = input("Question 4/20 \nInput a name ")
  Adjective_f1 = input("Question 5/20 \nInput an adjective (feeling) ")
  Adjective_fe2 = input("Question 6/20 \nInput another adjective (feeling) ")
  Noun = input("Question 7/20 \nInput a noun ")
  Feeling1 = input("Question 8/20 \nInput a feeling ")
  Feeling2 = input("Question 9/20 \nInput another feeling ")
  Verb = input("Question 10/20 \nInput a verb ")
  Verb2 = input("Question 11/20 \nInput another verb ")
  Animal = input("Question 12/20 \nInput an animal ")
  Animal2 = input("Question 13/20 \nInput an animal ")
  Color = input("Question 14/20 \nInputan color ")
  Color2 = input("Question 15/20 \nInput another color ")
  Verb_ing = input("Question 16/20 \nInput a verb ending in "
                   "-ing"
                   " ")
  Adverb_ly = input("Question 17/20 \nInput an adverb ending in "
                    "-ly"
                    " ")
  Measure_of_Time = input("Question 18/20 \nInput a measure of time ")
  Silly_Word = input("Question 19/20 \nInput another adjective ")
  Noun2 = input("Question 20/20 \nInput another noun ")

  print(
    template2.format(Proper_Noun, Person_Name, Noun, Adjective_f1, Feeling1,
                     Feeling2, Animal, Verb2, Color, Verb_ing, Adverb_ly,
                     Number, Measure_of_Time, Color2, Animal2, Number2,
                     Silly_Word, Noun2))

if user_choice == 3:
  Proper_Noun = input("Question 1/21 \nInput a proper noun ")
  Person_Name = input("Question 2/21 \nInput a name ")
  Adjective1 = input("Question 3/21 \nInput an adjective ")
  Color = input("Question 4/21 \nInputan color ")
  Animal = input("Question 5/21 \nInput an animal ")
  Place = input("Question 6/21 \nInput a place ")
  Adjective2 = input("Question 7/21 \nInput an adjective ")
  Magical_Creatures = input(
    "Question 8/21 \nInput magical creatures in plural form ")
  Adjective3 = input("Question 9/21 \nInput another adjective ")
  Magical_Creatures2 = input(
    "Question 10/21 \nInput magical creatures in plural form ")
  Room_in_a_House = input("Question 11/21 \nInput a room in a house ")
  Noun = input("Question 12/21 \nInput a noun ")
  Noun2 = input("Question 13/21 \nInput another noun ")
  Noun3 = input("Question 14/21 \nInput another noun in plural form ")
  Adjective4 = input("Question 15/21 \nInput another Adjective ")
  Noun4 = input("Question 16/21 \nInput a noun in plural form ")
  Number = int(input("Question 17/21 \nInput a number "))
  Measure_of_Time = input("Question 18/21 \nInput a measure of time ")
  Verb_ing = input("Question 19/21 \nInput a verb ending in "
                   "-ing"
                   " ")
  Adjective5 = input("Question 20/21 \nInput an adjective one more time ")
  Noun5 = input("Question 21/21 \nInput another noun in plural form ")

  print(
    template3.format(Proper_Noun, Person_Name, Adjective1, Color, Animal,
                     Place, Adjective2, Magical_Creatures, Adjective3,
                     Magical_Creatures2, Room_in_a_House, Noun, Noun2, Noun3,
                     Adjective4, Noun4, Number, Measure_of_Time, Verb_ing,
                     Adjective5, Noun5))
