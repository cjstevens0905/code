#opens the file
text_file = open("stopwords.txt")
#reads the file
stopWordsRead = text_file.read()
#splits it up by specified character and then turns it into a list
stopWordsList = stopWordsRead.split("\n")
#closes the file
text_file.close()

happyMoods = ["happy", "great", "bland", "blissful", "blithe",
"calm", "capricious", "captivated",	"cheerful",
"cheery", "chipper", "chirpy", "confident",	"content",
"convivial", "dazed" ,"delighted",	"delightful",
"ecstatic",	"elated", "enchanted", "euphoric",
"excited", "exstatic",	"exuberant",	 
"fain",	"fanciful",	"felicitous", "formidable"
"glad",	"gleeful",	"glorious",	"gratified",	 
"happy", "hilarious",	"hopeful",	"humorous",	 
"intoxicated", "jolly",	"joyful",	"joyous",
"jubilant",	"laughing",	"light",	"lively",	"lunatic",
"lucky",	"merry",	"mirthful", "optimistic",
"overwhelmed",	"peaceful",	"peppy",	"perky",	"playful",
"pleased",	"providential", "positive"]

sadMoods = ["sad","unhappy", "gloomy","subdued",
"bleak","homesick","annoyed","bitter",
"resentful","fuming","ashamed","guilty","terrible",
"embarrassed","tense","empty","distresed","incapable",
"useless","pathetic","tragic","forced",
"vunerable","uncertain","skeptical","disgusting",
"sulky","cross","worked up"]

name = raw_input("Hola, My name is Spencer, What is your name?\n")
response = raw_input("Bonjour, " + name + " How are you feeling today?\n")
#splits response up by specified character and then adds to list
typedWordsList = response.split(" ")
#creates a blank list
importantWordsList = []
#for loop that runs as many times as there is words in the list
for everyWord in typedWordsList:
    #checks if the words in the list match the words in the stop words list
    if (everyWord not in stopWordsList):
        #moves any words that DO NOT match into a filtered list
        importantWordsList.append(everyWord)

#conversational items that react based on the filtered list
for everyImportantWord in importantWordsList:
    if(everyImportantWord in happyMoods):
        print("Wonderful!\n")
    elif(everyImportantWord in sadMoods):
        print("Oh no!")
        #else: print("Im sorry, I didn't understand that! Please try again!")
    

speak = raw_input("What would you like to discuss today " + name + "?\n")





