class Entry:
    def __init__(self, id: int, title: str, body: str):

        self.id = id
        self.title = title
        self.body = body
        #self.date_created

    def set_title(self, title: str):
        self.title = title

    def set_body(self, body: str):
        self.body = body

    def __repr__(self):
        return f"id: {self.id} title:{self.title} body{self.body}"
