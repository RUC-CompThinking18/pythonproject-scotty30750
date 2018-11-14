def openfile():
    show_file = open("qf.txt", "r")
#this function opens up my text so that the facts and questions can be available
    print showfile.readlines()
    for i in range (40):
#will spit out lines 0 to 40
        print i

print "True and False Ocean Quiz"

class Question:
    def __init__(self, question, answer, fact):
        self.question = question
        self.answer = answer
        self.fact = fact

Question_1 =Question("Is plastic the most common element in the ocean?", "T", "Plastic is the most common element that is found in the ocean. It is harmful for the environment as it does not get break down easily and is often considered as food by marine animals.")

Question_2 =("Is the biggest source of pollution in the ocean from land based sources?", "T", "The biggest source of pollution in the ocean is directly from land based sources, such as oil, dirt, septic tanks, farms, ranches, motor vehicles, among larger sources. Thousands of tons of waste and trash are dumped into the ocean on a daily basis.")

Question_3 =("Over a million birds are killed from pollution each year.", "T", "Over one million seabirds are killed by ocean pollution each year. Three hundred thousand dolphins and porpoises die each year as a result of becoming entangled in discarded fishing nets, among other items. One hundred thousand sea mammals are killed in the ocean by pollution each year.")

Question_4 =("Pollution from out at sea can't end up on land.", "F", "Even though much the trash and waste dumped into the ocean is released hundreds of miles away from land, it still washes up on beaches and coastal areas, and affects everything in between. Every marine animal is affected by man-made chemicals released in the water.")

Question_5 =("There's garbage in the Pacific double the size of Texas.", "T", "There is an island of garbage twice the size of Texas inside the Pacific Ocean: the North Pacific Gyre off the coast of California is the largest oceanic garbage site in the entire world. There, the number of floating plastic pieces outnumbers total marine life six to one in the immediate vicinity.")

Question_6 =("Oil is the slowest source of deterioration to the ocean.", "F", "Oil is the fastest source of deterioration to the ocean, being far more harmful than trash and waste. However, only a small percentage of oil (around 12%) dumped in the ocean comes as a result of actual oil spills. Most oil causing harm in the ocean is a result of drainage from land. Oil spills suffocate marine life to death, and leads to behavioral changes and a breakdown in thermal insulation to those that do survive. It essentially changes the entire ecosystem of an affected area, such as a long coastline or deep ocean.")

Question_7 =("Toxic metals can destroy marine life.", "T", "Toxic metals can destroy the biochemistry, behavior, reproduction, and growth in marine life.")

Question_8 =("Plastic debris absorb poison and kill anything that eats it.", "T", "Plastic debris can absorb toxic chemicals from ocean pollution, therefore poisoning whatever eats it. In fact, plastic pollution is one of the most serious threats to the ocean. Plastic does not degrade; instead, it breaks down into progressively smaller pieces, but never disappears. They then attract more debris. It poses a significant health threat to the various sea creatures, and to the entire marine ecosystem. Overall, plastic is the number one source of pollution in the ocean.")

Question_9 =("Radioactive waste is also a major source of pollution.", "T", "Not all sources of contamination in the ocean come from just oil, trash and solid wastes. The dumping of radioactive waste from nuclear reactors, industrial race (such as heavy metals and acids), and drained sewage are also heavy contributors to pollution.")

Question_10 =("Sewage doesn't lead to the decomposition of organic matter.", "F", "Sewage leads to the decomposition of organic matter that in turn leads to a change in biodiversity. Even if the ocean’s ecosystem isn’t destroyed entirely, it is still changed drastically, and usually not for the better.")

Question_11 =("Industrial run off can't affect ocean well being.", "F", "Fertilizer runoff creates eutrophication that flourishes algal bloom (rapid increase or accumulation in the population of algae in aquatic systems) which depletes the oxygen content in the water that affects marine life.")

Question_12 =("Pollution causes a chain reaction of death from animal to animal.", "T", "Small animals at the bottom of food chain absorb the chemicals as part of their food. These small animals are then eaten by larger animals that again increases the concentration of chemicals. Animals at the top of hierarchy of food chain have contamination levels millions times higher than the water in which they live.")

Question_13 =("People can't be affected by bad seafood.", "F", "People get contaminated easily by eating contaminated seafood that can cause serious health problems, from cancer to damage to immune system.")

Question_14 =("Plastic bottles and aluminum cans can reach the sea and end up back on land.", "T", "The garbage like plastic bottles, aluminium cans, shoes, packaging material – if not disposed correctly, can reach the sea and the same garbage can again reach the sea shore where it pollutes beaches and affects local tourism industry.")

Question_15 =("Salt water from the oceans can push pollutants into freshwater areas.", "T", "Salty water of ocean has the capability to move pollutants from the ocean into coastal freshwater making wells and groundwater contaminated.")

Question_16 =("Chemical waste from industries can make it's way to the ocean by seeping through soil.", "T", "Chemicals from industries and mines can also enter ocean through land based activities. They can seep through soil, water or land either during their manufacture, use or accidental leaks. From soil, water or land, they can enter into ocean currents and can travel longer distances.")

Question_17 =("Pollutants can disappear in the ocean.", "F", "As 70% of the earth is covered with water, people actually assumed that all pollutants would be diluted and get disappeared. But in reality, they have not disappeared and their effects can be easily seen as they have entered the food chain.")

Question_18 =("Before the 1970s chemicals and garbage were regularly dumped into oceans.", "T", "Until 1970’s, the chemicals and garbage was deliberately dumped into the oceans and became as common practice for disposing everything including pesticides and radioactive waste, assuming that it would get dissolved to safe levels.")

Question_19 =("Eutrophication cannot create dead zones.", "F", "In several parts of the world including Gulf of Mexico and the Baltic Sea, Eutrophication has created enormous dead zones.")

Question_20 =("Dumping sewage into the ocean isn't a big deal.", "F", "Till today, in many parts of the world, sewage water is discharged in the ocean – untreated or under-treated. This can cause serious effect on marine and human life and can also lead to eutrophication.")

def game_loop():
    question_count = 0
    while question_count < 20:
    print "Question" + str(question_count + 1) + ":\n"
    first_choice = ask_question(question_count)
    answer = raw_input("\nHit \'T\, \'F\n").lower()
    if answer == first_choice[0]:
        print "Select Answer"
        answer = raw_input("Type True or False")
        if answer == True:
            question_count += 1
#now add method
#first choice is true second choice is False
#just need to print fact after answer whether right or wrong
#show score at end
def ask_question(question):
    for questions in Question:
        ask_question(Question)
        print Question_1
        raw_input()
        if input == Question_1.answer
        print Question_1.fact
#for loop

'''
'''questions = (qf.txt)
def ask_questions(questions):
    item = qf.txt.random(list(questions.items()))
    question = item[0]
    (variants, answer) = item[1]
    print (question, variants)
    attempt = input("\nHit \'T\, \'F\n")
    return (attempt, answer)
#added ask questions function so my quiz can recieve input and be interactive
#quiz takers will have a choice between true and false questions

score = 0
wrong = True
if string == raw_input
openfile()
def ocean_quiz(question, true_false, fact):
    print question
    if answer is == True
        points += 1
        print matching fact
    if answer is == False
        print matching fact
#fact will print after question is asked and add total score
print total score
reconfigure this to get this rawinput'''
'''
