# Relevant Content Application

## Overview
This is a simple Python web application that recommends content to users based on their interests.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/radovcic/flask_app.git
    ```

2. **Create and activate a virtual environment**: for example with venv.
    ```sh
    python -m venv venv
    venv\Scripts\Activate.ps1
    or
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Add data**: Optionally, replace the already provided users.json and content.json files in the data folder and test that the data is in the correct format.
    ```sh
    python -m unittest -v test_data_ingestion
    ```
   
5. **Run the application**:
    ```sh
    python app.py
    ```

6. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

In case of compatibility problems, please make sure to use Python 3.6.8.

## Tests

1. **Data ingestion**: A set of unit tests for verifying the structure and content of user and content data
    stored in JSON files.
    ```sh
    python -m unittest -v test_data_ingestion
    ```
   
2. **Matching logic**: A set of unit tests for verifying the functionality of python functions used for content matching.
    ```sh
    python -m unittest -v test_matching_logic
    ```
## User Interface
The application allows users to select a username from a dropdown menu to view relevant content. Here's how the UI is structured:

1. **Dropdown Menu**: A form with a dropdown menu is used to select the username.
On selecting a username, the form is submitted, and the relevant content for the selected user is displayed.

2. **Content Display**: After selecting a username, a list of relevant content is shown.
Each piece of relevant content includes:
The title of the content.
Relevant tags that matched the user's interests.
The content itself.
If no relevant content is found, a message is displayed.

By showing the relevant tags, users can immediately recognize why is the shown content relevant for them. 

## Matching Logic
A piece of content is considered relevant to a user if any of the user's interests match any of the content's tags based on:
- The interest type matches the tag type.
- The interest value matches the tag value.
- The content tag's threshold is equal to or greater than the user's interest threshold.

## Data Structure

It is expected that the data is stored in users.json and content.json files in the data folder
and that it is structured as a list of users and as a list of content. 

1. **user.json**:
```json
[
    {
        "name": "John Dow",
        "interests": [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.5},
            {"type": "country", "value": "UK", "threshold": 0.24},
            {"type": "sector", "value": "Renewable Energy", "threshold": 0.4},
            {"type": "instrument", "value": "BP.L", "threshold": 0.3}
        ]
    },
    {
        "name": "Jane Smith",
        "interests": [
            {"type": "instrument", "value": "AAPL", "threshold": 0.3},
            {"type": "country", "value": "USA", "threshold": 0.4},
            {"type": "sector", "value": "Finance", "threshold": 0.5},
            {"type": "instrument", "value": "MSFT", "threshold": 0.4},
            {"type": "sector", "value": "Retail", "threshold": 0.35}
        ]
    }
]
```

2. **content.json**:
```json
[
    {
        "id": "123",
        "title": "Vodafone: A Deep Dive into the UK Telecom Giant",
        "content": "Analysis of Vodafone's recent performance, market position in the UK, and future outlook.",
        "tags": [
            {"type": "instrument", "value": "VOD.L", "threshold": 0.8},
            {"type": "country", "value": "UK", "threshold": 0.7}
        ]
    },
    {
        "id": "456",
        "title": "Apple vs. Microsoft: A Head-to-Head Comparison",
        "content": "Compares the two tech giants in terms of products, services, financials, and growth potential.",
        "tags": [
            {"type": "instrument", "value": "AAPL", "threshold": 0.7},
            {"type": "instrument", "value": "MSFT", "threshold": 0.7},
            {"type": "country", "value": "USA", "threshold": 0.5}
        ]
    }
]
```