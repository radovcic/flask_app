from flask import Flask, render_template, request
import json


def load_json(file_path):
    """
    Loads a JSON file and returns its contents as a Python object.

    Args:
        file_path (str): The path to the JSON file to be loaded.

    Returns:
        The contents of the JSON file as a Python object.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def find_relevant_tags(interests, tags):
    """
    Finds and returns a list of relevant tags based on given interests.

    Args:
        interests (list of dict): A list of interests, where each interest is a dictionary
                                  with 'type', 'value', and 'threshold' keys.
        tags (list of dict): A list of tags, where each tag is a dictionary
                             with 'type', 'value', and 'threshold' keys.

    Returns:
        list of str: A list of tag values that match the interests based on type, value, and threshold criteria.
    """
    relevant_tags = []
    for interest in interests:
        for tag in tags:
            if (tag['type'] == interest['type'] and
                    tag['value'] == interest['value'] and
                    tag['threshold'] >= interest['threshold']):
                relevant_tags.append(tag['value'])
    return relevant_tags


def find_relevant_content(user, content):
    """
    Finds and returns a list of content relevant to a user's interests.

    This function checks each content item's tags against the user's interests and includes
    the content item in the result if it has any relevant tags. Relevant tags are added
    to the content item under the 'relevant_tags' key.

    Args:
        user (dict): A dictionary representing the user, which contains a key 'interests'
                     that maps to a list of interest dictionaries. Each interest dictionary
                     has 'type', 'value', and 'threshold' keys.
        content (list of dict): A list of content items, where each content item is a
                                dictionary containing a 'tags' key. The 'tags' key maps to
                                a list of tag dictionaries. Each tag dictionary has 'type',
                                'value', and 'threshold' keys.

    Returns:
        list of dict: A list of content items that have at least one relevant tag based on
                      the user's interests. Each content item in the list includes an
                      additional key 'relevant_tags' which maps to a list of relevant tag
                      values.
    """
    relevant_content = []
    for item in content:
        relevant_tags = find_relevant_tags(user['interests'], item['tags'])
        if relevant_tags:
            item['relevant_tags'] = relevant_tags
            relevant_content.append(item)
    return relevant_content


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles the main index route for the web application.

    This function processes both GET and POST requests. On a GET request, it loads user and content data,
    sorts the usernames, and renders the index template with the sorted usernames. On a POST request, it retrieves
    the selected user's name from the form data, finds relevant content based on the user's interests, and renders
    the index template with the relevant content for the selected user.
    """

    # load user and content data
    users = load_json('data/users.json')
    content = load_json('data/content.json')

    # Extract and sort usernames
    usernames = list(u['name'] for u in users)
    usernames.sort()

    selected_user = None
    relevant_content = None

    # Handle POST request to find relevant content for the selected user
    if request.method == 'POST':
        # Get the selected username from the form data
        selected_user = request.form['name']

        # Find the user with the matching name
        for user in users:
            if user['name'] == selected_user:
                # Find relevant content for the selected user
                relevant_content = find_relevant_content(user, content)
                break

    # Render the index template with the usernames, selected user, and relevant content
    return render_template('index.html',
                           usernames=usernames,
                           selected_user=selected_user,
                           relevant_content=relevant_content)


if __name__ == '__main__':
    app.run(debug=True)
