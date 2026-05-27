#Images
#Tutorial on how to open images using python
#2/23

#Initialize
import webbrowser

#Functions

#Main
url = ["https://tinyurl.com/48567ajx", #Grand Teton
       "https://tinyurl.com/2r9dp2su", #Grand Canyon
       "https://tinyurl.com/3dft5zft", #Moab
       "https://tinyurl.com/y59dxju7" #Sequoia
]

descriptions = ["Grand Teton National Park is an awe-inspiring wilderness in Wyoming, featuring dramatic, jagged 13,000-foot peaks rising directly from the valley floor without foothills.", #Grand Teton
                "Grand Canyon National Park in Arizona is an awe-inspiring, world-renowned natural wonder, offering unparalleled views of a mile-deep chasm carved by the Colorado River.", #Grand Canyon
                "Moab situated between Arches National Park and Canyonlands National Park, this quiet town in eastern Utah is the springboard for visitors wanting to hike through one-of-a-kind landscapes and raft down the Colorado River", #Moab
                "Sequoia is best known for its giant sequoia groves, and you're guaranteed to see hundreds of the massive namesake trees when you drive through the park." #Sequoia
                ]

#Sources of Information

#Picture of Grand Teton National Park
#Website Name:US News
#URL:https://travel.usnews.com/rankings/best-affordable-usa-destinations/
#Author Name:Elizabeth Von Tersch
#Article Name: Best Affordable Vacations in the U.S. for 2026
#Date: Dec 15, 2025

#Picture of Grand Canyon National Park
#Website Name:US News
#URL:https://travel.usnews.com/rankings/best-affordable-usa-destinations/
#Author Name:Elizabeth Von Tersch
#Article Name: Best Affordable Vacations in the U.S. for 2026
#Date: Dec 15, 2025

#Picture of Moab
#Website Name:US News
#URL:https://travel.usnews.com/rankings/best-affordable-usa-destinations/
#Author Name:Elizabeth Von Tersch
#Article Name: Best Affordable Vacations in the U.S. for 2026
#Date: Dec 15, 2025

#Picture of Sequoia National Park
#Website Name:US News
#URL:https://travel.usnews.com/rankings/best-affordable-usa-destinations/
#Author Name:Elizabeth Von Tersch
#Article Name: Best Affordable Vacations in the U.S. for 2026
#Date: Dec 15, 2025

print("National Park Vacation Recommender")
terrain = input("Do you prefer Mountains or Desert? (m/d): ").lower()
activity = input("Do you prefer Hiking or Sightseeing? (h/s): ").lower()

selected_index = 0

if terrain == 'm' and activity == 'h':
    selected_index = 0
elif terrain == 'm' and activity == 's':
    selected_index = 3
elif terrain == 'd' and activity == 'h':
    selected_index = 2
else:
    selected_index = 1

print("Recommendation")
print(descriptions[selected_index])

webbrowser.open(url[selected_index])

print("Image opened in your browser.")
print("Source: US News, Elizabeth Von Tersch, Best Affordable Vacations 2026, Dec 15, 2025")
