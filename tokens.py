import time


def token_expired(expire_date):
    return expire_date < time.time()


class TokenManager:

    def __init__(self):
        self.tokens = {}

    def insert_random_token(self, expire_date):
        random_token = "abc"
        self.insert_token(random_token, expire_date)
        return random_token

    def insert_token(self, token, expire_date):
        self.tokens[token] = expire_date

    def token_is_valid(self, token):
        if token in self.tokens:
            return not token_expired(self.tokens[token])
        return False

    def delete_token(self, token):
        self.tokens[token] = None

    def check_all_tokens(self):
        delete_list = []
        for token, exp_date in self.tokens:
            if token_expired(exp_date):
                delete_list.append(token)

        # delete tokens from all tokens
        for token in delete_list:
            self.delete_token(token)
