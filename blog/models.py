from mongoengine import Document, StringField, DateTimeField
import datetime

class Blog(Document):
    title = StringField(required=True, max_length=200)
    content = StringField()
    author = StringField(max_length=100)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.title
