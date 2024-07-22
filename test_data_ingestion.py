import unittest
import json


class TestDataIngestion(unittest.TestCase):
    """
    A set of unit tests for verifying the structure and content of user and content data
    stored in JSON files.

    Methods
    -------
    test_users_data():
        Tests the validity and structure of the users data in 'data/users.json'.

    test_content_data():
        Tests the validity and structure of the content data in 'data/content.json'.
    """

    def test_users_data(self):
        """
        Verify that the users data is properly structured and contains the expected fields
        and data types.

        Checks:
        - The users data is a list.
        - Each user in the list has a 'name' field.
        - The 'name' field in each user is a string.
        - No 'name' field is empty.
        - Each user has an 'interests' field.
        - The 'interests' field in each user is a list.
        - Each interest in the 'interests' list has a 'type' field.
        - Each interest in the 'interests' list has a 'value' field.
        - Each interest in the 'interests' list has a 'threshold' field.
        """
        with open('data/users.json') as f:
            users = json.load(f)
            self.assertTrue(isinstance(users, list), 'Users data is not a list.')
            self.assertTrue(all('name' in user for user in users), 'Not every user has a name.')
            self.assertTrue(all(isinstance(user['name'], str) for user in users),
                            'Not every user name is a string.')
            self.assertTrue(all(user['name'] for user in users), 'Some user names are empty.')
            self.assertTrue(all('interests' in user for user in users), 'Not every user has interests.')
            self.assertTrue(all(isinstance(user['interests'], list) for user in users),
                            'Not every user interests is a list.')
            self.assertTrue(all('type' in interest for user in users for interest in user['interests']),
                            'Not every user interests has a type.')
            self.assertTrue(all('value' in interest for user in users for interest in user['interests']),
                            'Not every user interests has a value.')
            self.assertTrue(all('threshold' in interest for user in users for interest in user['interests']),
                            'Not every user interests has a threshold.')

    def test_content_data(self):
        """
        Verify that the content data is properly structured and contains the expected fields
        and data types.

        Checks:
        - The content data is a list.
        - Each content item in the list has an 'id' field.
        - Each content item has a 'title' field.
        - Each content item has a 'content' field.
        - Each content item has a 'tags' field.
        - The 'tags' field in each content item is a list.
        """
        with open('data/content.json') as f:
            content = json.load(f)
            self.assertTrue(isinstance(content, list), 'Content data is not a list.')
            self.assertTrue(all("id" in item for item in content), 'Not every content has an id.')
            self.assertTrue(all("title" in item for item in content), 'Not every content had a title.')
            self.assertTrue(all("content" in item for item in content), 'Not every content had a content.')
            self.assertTrue(all("tags" in item for item in content), 'Not every content had tags.')
            self.assertTrue(all(isinstance(item['tags'], list) for item in content),
                            'Not every content tags is a list.')


if __name__ == '__main__':
    unittest.main()
