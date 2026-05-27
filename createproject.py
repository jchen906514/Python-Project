#Global Language Explorer
#The program allows users to explore a dataset of the most spoken languages in the world.

#Init
#Import Libraries
#pandas is used to read the dataset file
#random is used to generate a random language
import pandas as pd
import random
#Functions
#load the dataset
#the csv file contains information about the most spoken languages
data = pd.read_csv('MSLW.csv')
#convert dataset colums into lists
#lists allows us to easily access and compare information
id = data['id'].tolist()
rank = data['Rank'].tolist()
language = data['Language'].tolist()
speakers = data['Speakers in millions'].tolist()
percentage_population= data['Percentage of world population'].tolist()
language_family = data['Language family'].tolist()
branch = data['Branch'].tolist()

#Lookup Language
def lookupLanguage(lang_name):
    #loop through the list of languages
    #check if the languages exists in the dataset
    for i in range(len(language)):
        #check if the user input matches a languagein the dataset
        if lang_name.lower() in language[i].lower():
            print("Language:", language[i])
            print("Rank:", rank[i])
            print("Speakers (millions):", speakers[i])
            print("Percentage of world population:", percentage_population[i])
            print("Language Family:", language_family[i])
            print("Branch:", branch[i])
            return
    else:
        print("Language not found.")

#filter by family
def filterByFamily(family):
    #create an empty list to store matching languages
    matches = []

    #loop through langauge_family list
    for i in range(len(language_family)):
        #check of the language family matches user input
        if family.lower() in language_family[i].lower():
            #add matching languages to list
            matches.append(language[i])

    if matches:
        print("Languages in", family, "family:")
        print(matches)
    else:
        print("No languages found")

#languages above speakers
def languagesAboveSpeakers(min_speakers):
    matches =[]

    #loop through speakers list
    for i in range(len(speakers)):
        #convert speaker value to float before comparing
        if float(speakers[i]) >= min_speakers:
            matches.append(language[i])

    if matches:
        print("Languages with more than", min_speakers, "million speakers:")
        for lang in matches:
            print(lang)
    else:
        print("No languages found")

#compare languages
def compareLanguages(lang1,lang2):
    #search for both languages
    for i in range (len(language)):
        if lang1.lower() in language[i].lower():
            index1 = i
        if lang2.lower() in language[i].lower():
            index2 = i

    #if both languages exit
    if index1 != -1 and index2 != -1:
        #convert speaker values to floats for comparison
        s1 = float(speakers[index1])
        s2 = float(speakers[index2])

        #compare speaker counts
        if s1 > s2:
            print(language[index1], "has more speakers.")
        elif s2 > s1:
            print(language[index2], "has more speakers.")
        else:
            print("They have the same number of speakers.")

    else:
        print("One or both languages not found.")

#Show top N languages based on rank
def showTopLanguages(n):
    print("Top", n, "Most Spoken Languages:")

    #loop through first n items
    for i in range(min(n, len(language))):
        print(rank[i], language[i],speakers[i], "million speakers")

# Filter languages by branch
def filterByBranch(branch_name):

    matches = []

    for i in range(len(branch)):

        if branch_name.lower() in branch[i].lower():
            matches.append(language[i])

    if matches:
        print("Languages in branch:", branch_name)
        for lang in matches:
            print(lang)
    else:
        print("No languages found in that branch.")

#Find the language with the highest number of speakers
def mostSpokenLanguage():

    max_speakers = 0
    max_language = ''

    for i in range(len(speakers)):

        if float(speakers[i])>max_speakers:
            max_speakers = float(speakers[i])
            max_language = language[i]

    print("The most spoken language in the dataset is:")
    print(max_language, max_speakers, "million speakers")

#show a random language
def randomLanguage():

    #generate a random index form dataset
    i = random.randint(0,len(language)-1)

    print("Random Language Discovery!")
    print("Language:", language[i])
    print("Rank:", rank[i])
    print("Speakers:", speakers[i], "million")
    print("Family:", language_family[i])

def averageSpeakers():

    total = 0

    #add all speaker values together
    for i in range(len(speakers)):
        total += float(speakers[i])

    avg = total / len(speakers)

    print("Average number of speakers:", round(avg,2), "million")

#Main
#display a menu so users can choose different actions
def main():
    while True:
        print("Global Language Analyzer")
        print("1. Look up language details")
        print("2. Filterby language family")
        print("3. Find languages above x speakers")
        print("4. Compare two languages by speakers")
        print("5. Show top N languages")
        print("6. Filter Languages by Branch")
        print("7. Find Most Spoken Language")
        print("8. Random Languages Discovery")
        print("9. Average Number of Speakers")
        print("10. Quit")

        #ask the user for a choice
        choice = input("Enter choice(1-10):")

        #run different functions based on the user's choice
        if choice == '1':
            language = input("Enter language name:")
            lookupLanguage(language)
        elif choice == '2':
            family = input("Enter language family:")
            filterByFamily(family)
        elif choice == '3':
            num = float(input("Enter minimum speakers (millions):"))
            languagesAboveSpeakers(num)
        elif choice == '4':
            lang1 = input("Enter first language:")
            lang2 = input("Enter second language:")
            compareLanguages(lang1,lang2)
        elif choice == '5':
            n = int(input("How many top languages would you like to see?"))
            showTopLanguages(n)
        elif choice == '6':
            branch_name = input("Enter branch name:")
            filterByBranch(branch_name)
        elif choice == '7':
            mostSpokenLanguage()
        elif choice == '8':
            randomLanguage()
        elif choice == '9':
            averageSpeakers()
        elif choice == '10':
            break
        else:
            print("Invalid choice.")
main()

#Sources
#Most Spoken Language Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://www.ethnologue.com/statistics/
