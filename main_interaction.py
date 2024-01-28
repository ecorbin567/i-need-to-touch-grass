"""
A rudimentary way for the user to interact with places!
"""
import places_information

if __name__ == '__main__':
    print("Welcome to I Need To Touch Grass!")

    address = input("Enter your address.")
    keyword = input("What kind of nature do you want to visit? Some suggestions: park, beach, trail, forest")
    km = int(input("How many kilometers away are you willing to travel? Please enter an integer."))

    places = places_information.get_places(address, keyword, km)
    df = places_information.places_to_dataframe(places)
    print(df)

    parameter = input("How would you like to sort the data? Please enter one of the following values: "
                      "km away, Minutes away, Rating out of 5")
    print(places_information.sort_dataframe(df, parameter))

    looking_at_places = True
    while looking_at_places:
        place_name = input("Which place would you like to know more about?")
        found = False
        for place in places:
            if place[0] == place_name:
                found = True
                places_information.get_picture(place[7], place_name)
                mode = input("Please choose one of the following: driving, walking, bicycling, transit")
                print(places_information.get_directions(address, place[3], mode))
        if not found:
            print("Place not found, sorry!")
        keep_looking = input("Would you like to keep looking at different places? Y/N")
        if keep_looking == 'N':
            looking_at_places = False
