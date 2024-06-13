# String concatenation is the process of combining, or joining, two or more strings together to create a new string. 
# Example of string concatenation.
# -> youtuber = ""
# 3 ways to concatenate Strings: 
# -> print("Subscribe to"+ youtuber)
# -> print("Subscribe to {}".format(youtuber))
# -> print( f" Subscribe to {youtuber}")

def generate_madlib():
    """
    Generates a Madlib story based on user input.

    This function prompts the user to input an adjective, two verbs, 
    and a famous person's name to construct a Madlib story.

    Returns:
    str: The generated Madlib story.
    """
    # Prompt the user for input
    adj = input("Enter an adjective: ")         # Request an adjective
    verb1 = input("Enter a verb: ")             # Request a verb
    verb2 = input("Enter another verb: ")       # Request another verb
    famous_person = input("Enter a famous person's name: ")  # Request a famous person's name

    # Construct the Madlib story using string formatting
    madlib = (
        f"Computer programming is so {adj}! It makes me so excited all the time because "
        f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
    )

    return madlib

def main():
    """
    Main function to execute the Madlib generator.

    This function calls generate_madlib() to generate a Madlib story
    based on user input, and prints the generated Madlib.
    """
    madlib = generate_madlib()    # Generate the Madlib story
    print(madlib)                 # Print the generated Madlib

if __name__ == "__main__":
    main()  # Call the main function
