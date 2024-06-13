# Madlib Generator

## Overview
This Python script generates a Madlib story based on user input. Madlibs are word games where players fill in the blanks with different word types (such as nouns, verbs, adjectives) to create funny and often nonsensical stories.

## How to Use
1. Run the Python script `madlib_generator.py`.
2. Follow the prompts to enter an adjective, two verbs, and the name of a famous person.
3. The script will construct a Madlib story using your inputs.
4. Once you've provided all the inputs, the Madlib story will be displayed.

## Programming Techniques
- **User Input**: The script uses the `input()` function to prompt the user for adjective, verbs, and a famous person's name.
- **String Formatting**: String formatting is utilized to construct the Madlib story, inserting the user-inputted words into the story template.
- **Function Definition**: The functionality of generating the Madlib story is encapsulated within a function `generate_madlib()` for modularity and reusability.
- **Main Function**: A `main()` function is defined to orchestrate the Madlib generation process. It calls the `generate_madlib()` function and prints the resulting story.
- **Conditional Execution**: The `if __name__ == "__main__":` block ensures that the `main()` function is executed only when the script is run directly, not when it's imported as a module.

## Example
```
Enter an adjective: funny
Enter a verb: dance
Enter another verb: sing
Enter a famous person's name: Beyoncé

Computer programming is so funny! It makes me so excited all the time because I love to dance. Stay hydrated and sing like you are Beyoncé!
```
