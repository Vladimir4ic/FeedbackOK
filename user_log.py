# user_log.py
class UserLog:
    def __init__(self):
        self.user_responses = {}

    def log_response(self, user_id, response):
        if user_id not in self.user_responses:
            self.user_responses[user_id] = []
        self.user_responses[user_id].append(response)

    def get_user_responses(self, user_id):
        return self.user_responses.get(user_id, [])
