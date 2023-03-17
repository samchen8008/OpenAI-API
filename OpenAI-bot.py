import openai
import tkinter as tk
from tkinter import messagebox
import os
import argparse
def get_api_key():
    # Create a GUI window for the user to enter their API key
    root = tk.Tk()
    root.title("ChatGPT API Tool")

    # Create a label for the API key entry field
    api_key_label = tk.Label(root, text="OpenAI API Key:")
    api_key_label.grid(row=0, column=0)

    # Create an entry field for the API key
    api_key_entry = tk.Entry(root, width=50)
    api_key_entry.grid(row=0, column=1)

    # Create a button to submit the API key
    submit_button = tk.Button(root, text="Submit", command=lambda: root.quit())
    submit_button.grid(row=1, column=0, columnspan=2)

    root.mainloop()

    # Retrieve the API key entered by the user
    api_key = api_key_entry.get()

    return api_key


def interact_with_api(api_key):
    # Configure the OpenAI API client with the provided API key
    openai.api_key = api_key

    # Create a file to store the history of questions asked
    history_file = open("history.txt", "a")

    # Loop to accept user input and send requests to the API
    while True:
        # Get user input from the command line
        question = input("Ask a question (or type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        # Send the question to the OpenAI API
        response = openai.Completion.create(
            engine="davinci", prompt=question, max_tokens=1024
        )

        # Print the API's response
        answer = response.choices[0].text
        print(answer)

        # Write the question and answer to the history file
        history_file.write("Q: " + question + "\n")
        history_file.write("A: " + answer + "\n\n")

    # Close the history file
    history_file.close()

def main():
    # Get the API key from the user
    api_key = get_api_key()

    # Interact with the API and save the history of questions asked
    interact_with_api(api_key)

if __name__ == "__main__":
    main()
