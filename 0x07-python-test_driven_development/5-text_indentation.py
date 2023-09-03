#!/usr/bin/python3

def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing spaces from the input text
    text = text.strip()

    # Initialize an empty result string
    result = ""

    # Initialize a flag to track if a line break has occurred
    line_break = False

    # Iterate through each character in the input text
    for char in text:
        if char in ".?:":  # Check if the character is one of ".", "?", or ":"
            result += char  # Add the character to the result string
            line_break = True  # Set the line break flag to True
        else:
            if line_break:
                result += "\n\n"  # Add two new lines if a line break is pending
                line_break = False  # Reset the line break flag
            result += char  # Add the character to the result string

    # Print the formatted text
    print(result)
