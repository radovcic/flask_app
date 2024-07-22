import unittest
from app import find_relevant_tags, find_relevant_content


class TestFindRelevantTags(unittest.TestCase):
    """
    A set of unit tests for verifying the functionality of the `find_relevant_tags` function.

    The `find_relevant_tags` function is expected to match user interests with relevant tags based
    on the type, value, and threshold of each interest and tag.

    Methods
    -------
    test_basic_match():
        Tests a basic scenario where one interest matches one tag.

    test_same_threshold():
        Tests the scenario where the interest and tag have the same threshold value.

    test_no_match():
        Tests the scenario where no interests match any tags.

    test_multiple_matches():
        Tests the scenario where multiple interests match multiple tags.

    test_empty_interests():
        Tests the scenario where the interests list is empty.

    test_empty_tags():
        Tests the scenario where the tags list is empty.
    """

    def test_basic_match(self):
        interests = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.5},
            {"type": "country", "value": "UK", "threshold": 0.24}
        ]
        tags = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.6},
            {"type": "country", "value": "UK", "threshold": 0.20}
        ]
        expected = ["VOD.L"]
        self.assertEqual(find_relevant_tags(interests, tags), expected, 'Problem with basic match.')

    def test_same_threshold(self):
        interests = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.5},
            {"type": "country", "value": "UK", "threshold": 0.24}
        ]
        tags = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.5},
            {"type": "country", "value": "UK", "threshold": 0.20}
        ]
        expected = ["VOD.L"]
        self.assertEqual(find_relevant_tags(interests, tags), expected, 'Problem with same threshold.')

    def test_no_match(self):
        interests = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.5}
        ]
        tags = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.4},
            {"type": "country", "value": "UK", "threshold": 0.23}
        ]
        expected = []
        self.assertEqual(find_relevant_tags(interests, tags), expected, 'Problem with no match.')

    def test_multiple_matches(self):
        interests = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.5},
            {"type": "country", "value": "UK", "threshold": 0.24}
        ]
        tags = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.6},
            {"type": "country", "value": "UK", "threshold": 0.25}
        ]
        expected = ["VOD.L", "UK"]
        self.assertEqual(find_relevant_tags(interests, tags), expected, 'Problem with multiple matches.')

    def test_empty_interests(self):
        interests = []
        tags = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.6},
            {"type": "country", "value": "UK", "threshold": 0.25}
        ]
        expected = []
        self.assertEqual(find_relevant_tags(interests, tags), expected, 'Problem with empty interests.')

    def test_empty_tags(self):
        interests = [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.5},
            {"type": "country", "value": "UK", "threshold": 0.24}
        ]
        tags = []
        expected = []
        self.assertEqual(find_relevant_tags(interests, tags), expected, 'Problem with empty tags.')


class TestFindRelevantContent(unittest.TestCase):
    """
    A set of unit tests for verifying the functionality of the `find_relevant_content` function.

    The `find_relevant_content` function is expected to match user interests with relevant content
    based on the type, value, and threshold of each interest and tag.

    Attributes
    ----------
    user : dict
        A dictionary representing a user and their interests.
    content : list
        A list of dictionaries representing content items, each with tags.

    Methods
    -------
    setUp():
        Initializes the user and content attributes for use in the tests.

    test_find_relevant_content_basic_match():
        Tests a basic scenario where user interests match content tags.

    test_find_relevant_content_no_match():
        Tests the scenario where user interests do not match any content tags.

    test_find_relevant_content_empty_user_interests():
        Tests the scenario where the user has no interests.

    test_find_relevant_content_empty_content():
        Tests the scenario where there is no content available.
    """

    def setUp(self):
        self.user = {
            "name": "John Doe",
            "interests": [
                {"type": "instrument", "value": "VOD.L", "threshold": 0.5},
                {"type": "country", "value": "UK", "threshold": 0.24}
            ]
        }

        self.content = [
            {"id": "123", "title": "Title 1", "content": "Content about VOD.L",
             "tags": [{"type": "instrument", "value": "VOD.L", "threshold": 0.6}]},
            {"id": "124", "title": "Title 2", "content": "Content about UK",
             "tags": [{"type": "country", "value": "UK", "threshold": 0.25}]},
            {"id": "125", "title": "Title 3", "content": "Content about something else",
             "tags": [{"type": "genre", "value": "Sci-Fi", "threshold": 0.1}]}
        ]

    def test_find_relevant_content_basic_match(self):
        expected = [
            {"id": "123", "title": "Title 1", "content": "Content about VOD.L",
             "tags": [{"type": "instrument", "value": "VOD.L", "threshold": 0.6}],
             "relevant_tags": ["VOD.L"]},
            {"id": "124", "title": "Title 2", "content": "Content about UK",
             "tags": [{"type": "country", "value": "UK", "threshold": 0.25}],
             "relevant_tags": ["UK"]}
        ]

        result = find_relevant_content(self.user, self.content)
        self.assertEqual(result, expected, 'Problem with basic match in relevant content.')

    def test_find_relevant_content_no_match(self):
        user = self.user
        content = [
            {"id": "126", "title": "Title 4", "content": "Content about DEF",
             "tags": [{"type": "instrument", "value": "DEF", "threshold": 0.6}]}
        ]
        expected = []
        result = find_relevant_content(user, content)
        self.assertEqual(result, expected, 'Problem with no match in relevant content.')

    def test_find_relevant_content_empty_user_interests(self):
        user = {"name": "John Doe", "interests": []}
        content = self.content
        expected = []
        result = find_relevant_content(user, content)
        self.assertEqual(result, expected, 'Problem with empty user interests in relevant content.')

    def test_find_relevant_content_empty_content(self):
        user = self.user
        content = []
        expected = []
        result = find_relevant_content(user, content)
        self.assertEqual(result, expected, 'Problem with empty content in relevant content.')


if __name__ == '__main__':
    unittest.main()
