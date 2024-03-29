import random
import string
import time


def token_expired(expire_date):
    return expire_date < time.time()


# generates a token of specified length "A3E6"
def generate_token(length=4):
    return random.choices(string.ascii_uppercase + string.digits, k=length)


class TokenManager:

    def __init__(self):
        self.tokens = {}


    def insert_random_token(self, expire_time):
        random_token = "abc"
        self.insert_token(random_token, expire_time)
        return random_token

    def insert_token(self, token, valid_time):
        now = time.time()
        self.tokens[token] = now + valid_time

    def delete_token(self, token):
        del self.tokens[token]

    def token_is_valid(self, token):
        self.check_all_tokens()
        if token in self.tokens:
            valid = not token_expired(self.tokens[token])
            # delete token if you want to delete if immediately after succeeded check
            return valid
        return False

    def check_all_tokens(self):
        for token, exp_date in self.tokens.items():
            if token_expired(exp_date):
                # delete_list.append(token)
                self.tokens.pop(token)