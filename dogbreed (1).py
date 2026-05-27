#Dog Breed
#The purpose of my program is to help users choose a dog breed that meets their needs.

#Init
import pandas as pd
import random
import webbrowser
#Functions
data = pd.read_csv('dogsbreed.csv')
id = data['id'].tolist()
name = data['Name'].tolist()
Breed_Group = data['Breed Group'].tolist()
BredFor = data['BredFor'].tolist()
milifespan= data['Minimum Life Span'].tolist()
malifespan = data['Maximum Life Span'].tolist()
maheight = data['Maximum Height'].tolist()
miheight = data['Minimum Height'].tolist()
miweight = data['Minimum Weight'].tolist()
maweight = data['Maximum Weight'].tolist()
temperament = data['Temperament'].tolist()
image = data['Image'].tolist()

def getDogSize(size):
    matches = []
    for i in range(len(name)):
        avg_weight = (float(miweight[i]) + float(maweight[i])) / 2
        if size == "tiny" and avg_weight <= 10:
            matches.append(name[i])
        elif size == "small" and 11 <= avg_weight <= 25:
            matches.append(name[i])
        elif size == "medium" and 26 <= avg_weight <= 60:
            matches.append(name[i])
        elif size == "large" and avg_weight > 60:
            matches.append(name[i])

    if matches:
        print(f"Recommended {size} dog: {random.choice(matches)}")
    else:
        print(f"No {size} dogs found in that range.")

url = ["https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg",
       "https://cdn2.thedogapi.com/images/tChrH8dDJ.jpg",
       "https://cdn2.thedogapi.com/images/PG8UPLSVU.jpg",
       "https://cdn2.thedogapi.com/images/SyfsC19NQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/36TXlWMDf.jpg",
        "https://cdn2.thedogapi.com/images/33mJ-V3RX.jpg",
        "https://cdn2.thedogapi.com/images/-HgpNnGXl.jpg",
        "https://cdn2.thedogapi.com/images/GhtSdrW29.jpg",
        "https://cdn2.thedogapi.com/images/EB8A5HQHX.jpg",
        "https://cdn2.thedogapi.com/images/uISezUGDV.jpg",
        "https://cdn2.thedogapi.com/images/HkC31gcNm_1280.png",
        "https://cdn2.thedogapi.com/images/SkmRJl9VQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/BJT0Jx5Nm_1280.jpg",
        "https://cdn2.thedogapi.com/images/Hyq1ge9VQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1-llgq4m_1280.jpg",
        "https://cdn2.thedogapi.com/images/SkvZgx94m_1280.jpg",
        "https://cdn2.thedogapi.com/images/H1dGlxqNQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/BkMQll94X_1280.jpg",
        "https://cdn2.thedogapi.com/images/Syd4xxqEm_1280.jpg",
        "https://cdn2.thedogapi.com/images/HJQ8ge5V7_1280.jpg",
        "https://cdn2.thedogapi.com/images/ByK8gx947_1280.jpg",
        "https://cdn2.thedogapi.com/images/r1f_ll5VX_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1KdxlcNX_1280.jpg",
        "https://cdn2.thedogapi.com/images/S1fFlx5Em_1280.jpg",
        "https://cdn2.thedogapi.com/images/Skdcgx9VX_1280.jpg",
        "https://cdn2.thedogapi.com/images/rJxieg9VQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/HyOjge5Vm_1280.jpg",
        "https://cdn2.thedogapi.com/images/HJOpge9Em_1280.jpg",
        "https://cdn2.thedogapi.com/images/rkZRggqVX_1280.jpg",
        "https://cdn2.thedogapi.com/images/Byd0xl5VX_1280.jpg",
        "https://cdn2.thedogapi.com/images/ry1kWe5VQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/ryHJZlcNX_1280.jpg",
        "https://cdn2.thedogapi.com/images/S13yZg5VQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/rkVlblcEQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/HJWZZxc4X_1280.jpg",
        "https://cdn2.thedogapi.com/images/r1ifZl5E7_1280.jpg",
        "https://cdn2.thedogapi.com/images/Sk7Qbg9E7_1280.jpg",
        "https://cdn2.thedogapi.com/images/r15m-lc4m_1280.jpg",
        "https://cdn2.thedogapi.com/images/SyXN-e9NX_1280.jpg",
        "https://cdn2.thedogapi.com/images/BJcNbec4X_1280.jpg",
        "https://cdn2.thedogapi.com/images/r1rrWe5Em_1280.jpg",
        "https://cdn2.thedogapi.com/images/HJRBbe94Q_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1pDZx9Nm_1280.jpg",
        "https://cdn2.thedogapi.com/images/Sypubg54Q_1280.jpg",
        "https://cdn2.thedogapi.com/images/ry8KWgqEQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/rkeqWgq4Q_1280.jpg",
        "https://cdn2.thedogapi.com/images/HkRcZe547_1280.jpg",
        "https://cdn2.thedogapi.com/images/SyviZlqNm_1280.jpg",
        "https://cdn2.thedogapi.com/images/SkJ3blcN7_1280.jpg",
        "https://cdn2.thedogapi.com/images/S1nhWx94Q_1280.jpg",
        "https://cdn2.thedogapi.com/images/H1QyMe5EQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/Hk0Jfe5VQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/S1VWGx9Nm_1280.jpg",
        "https://cdn2.thedogapi.com/images/SkJfGecE7_1280.jpg",
        "https://cdn2.thedogapi.com/images/S1KMGg5Vm_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1u4zgqE7_1280.jpg",
        "https://cdn2.thedogapi.com/images/SJyBfg5NX_1280.jpg",
        "https://cdn2.thedogapi.com/images/SJqBMg5Nm_1280.jpg",
        "https://cdn2.thedogapi.com/images/H1NIzlcV7_1280.jpg",
        "https://cdn2.thedogapi.com/images/H1oLMe94m_1280.jpg",
        "https://cdn2.thedogapi.com/images/HJ7Pzg5EQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/SJ5vzx5NX_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1Edfl9NX_1280.jpg",
        "https://cdn2.thedogapi.com/images/B12uzg9V7_1280.png",
        "https://cdn2.thedogapi.com/images/ryNYMx94X_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1IcfgqE7_1280.jpg",
        "https://cdn2.thedogapi.com/images/rkXiGl9V7_1280.jpg",
        "https://cdn2.thedogapi.com/images/S1osGeqVm_1280.jpg",
        "https://cdn2.thedogapi.com/images/Hyd2zgcEX_1280.jpg",
        "https://cdn2.thedogapi.com/images/SJAnzg9NX_1280.jpg",
        "https://cdn2.thedogapi.com/images/r1H6feqEm_1280.jpg",
        "https://cdn2.thedogapi.com/images/S1GAGg9Vm_1280.jpg",
        "https://cdn2.thedogapi.com/images/Bko0fl547_1280.jpg",
        "https://cdn2.thedogapi.com/images/BykZ7ecVX_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1uW7l5VX_1280.jpg",
        "https://cdn2.thedogapi.com/images/ryzzmgqE7_1280.jpg",
        "https://cdn2.thedogapi.com/images/ByrmQlqVm_1280.jpg",
        "https://cdn2.thedogapi.com/images/SJp7Qe5EX_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1SV7gqN7_1280.jpg",
        "https://cdn2.thedogapi.com/images/SJIUQl9NX_1280.jpg",
        "https://cdn2.thedogapi.com/images/Sk4DXl54m_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1ADQg94X_1280.jpg",
        "https://cdn2.thedogapi.com/images/SkJj7e547_1280.jpg",
        "https://cdn2.thedogapi.com/images/rJ6iQeqEm_1280.jpg",
        "https://cdn2.thedogapi.com/images/Byz6mgqEQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/B1i67l5VQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/HyJvcl9N7_1280.jpg",
        "https://cdn2.thedogapi.com/images/HJMzEl5N7_1280.jpg",
        "https://cdn2.thedogapi.com/images/By9zNgqE7_1280.jpg",
        "https://cdn2.thedogapi.com/images/r1xXEgcNX_1280.jpg",
        "https://cdn2.thedogapi.com/images/S1T8Ee9Nm_1280.jpg",
        "https://cdn2.thedogapi.com/images/SyBvVgc47_1280.jpg",
        "https://cdn2.thedogapi.com/images/SkNjqx9NQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/BkrJjgcV7_1280.jpg",
        "https://cdn2.thedogapi.com/images/ByzGsl5Nm_1280.jpg",
        "https://cdn2.thedogapi.com/images/HJHmix5NQ_1280.jpg",
        "https://cdn2.thedogapi.com/images/HJf4jl9VX_1280.jpg",
        "https://cdn2.thedogapi.com/images/r1o0jx9Em_1280.jpg",
        "https://cdn2.thedogapi.com/images/SyU12l9V7_1280.jpg"]

def lookupBreed(breed_name):
    if breed_name in name:
        index = name.index(breed_name)
        print(f"{name[index]}")
        print(f"Temperament: {temperament[index]}")
        print(f"Image: {image[index]}")
        webbrowser.open(url[index])
    else:
        print("Breed not found.")

def filterByPurpose(purpose):
    matches = []
    for i in range(len(BredFor)):
        if purpose in BredFor[i]:
            matches.append(name[i])

    if matches:
        print(f"Found {len(matches)} breeds for {purpose}:")
        print(matches)
    else:
        print("No breeds found for that purpose.")

#Main
def main():
    while True:
        print("Dog Breed Finder")
        print("1. Find dog by size")
        print("2. Look up breed details")
        print("3. Find dog by purpose")
        print("4. Quit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            size = input("Enter size (tiny, small, medium, large): ")
            getDogSize(size)
        elif choice == '2':
            breed = input("Enter breed name: ")
            lookupBreed(breed)
        elif choice == '3':
            purpose = input("Enter purpose (e.g., Companion, Guarding): ")
            filterByPurpose(purpose)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

main()

#Sources
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
