import json
import os

# Define the file name for storing scores
SCORE_FILE = 'scores.json'

def load_scores():
    """
    Load the scores from the 'scores.json' file. If the file does not exist, return an empty dictionary.

    :return: A dictionary of scores where keys are usernames and values are their scores
    """
    if os.path.exists(SCORE_FILE):  # Check if the scores file exists
        with open(SCORE_FILE, 'r') as f:  # Open the file in read mode
            return json.load(f)  # Parse and return the JSON data as a dictionary
    return {}  # If the file doesn't exist, return an empty dictionary

def save_scores(scores):
    """
    Save the provided scores to the 'scores.json' file. The scores are written in JSON format with indentation.

    :param scores: A dictionary of scores where keys are usernames and values are their scores
    """
    with open(SCORE_FILE, 'w') as f:  # Open the file in write mode (this will overwrite the existing file)
        json.dump(scores, f, indent=4)  # Convert the dictionary to JSON and save it to the file with indentation for readability
