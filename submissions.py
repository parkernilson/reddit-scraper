from db import DB
from enum import Enum

class Classification(Enum):
    sexual = 'sexual'
    non_sexual = 'non-sexual'

class SubmissionModel:
    def __init__(self, classification: Classification, selftext, title, id):
        self.classification: Classification = classification
        self.selftext = selftext
        self.title = title
        self.id = id

    def save(self):
        with DB() as cursor:
            cursor.execute(
                """
                INSERT INTO submissions (class, selftext, title, id)
                VALUES (?, ?, ?, ?)
                """,
                (self.classification.value, self.selftext, self.title, self.id)
            )
            