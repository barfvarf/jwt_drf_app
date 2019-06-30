import os
import random
import unittest
import requests
import config


class BasicTests(unittest.TestCase):

    def setUp(self):
        self.base_url = config.base_url
        self.users = []
        self.user_access_tokens = []
        self.posts = []
        self.user_post_actions = ["like", "dislike"]

    def test_user_activity(self):
        route = "user/signup/"
        request_url = os.path.join(self.base_url, route)
        self.amount_of_users = random.randint(1, config.number_of_users)
        [self.users.append({"username": "test_user_%s" % i,
                            "password": "password%s" % i})
            for i in range(self.amount_of_users)]
        print("users:", self.users)
        for user_request in self.users:
            resp = requests.post(request_url, json=user_request)
            print(resp.text)
            self.assertEqual(resp.status_code, 201)

        route = "user/token/"
        request_url = os.path.join(self.base_url, route)
        for user_request in self.users:
            resp = requests.post(request_url, json=user_request)
            print(resp.text)
            self.assertEqual(resp.status_code, 200)
            data = resp.json()
            self.assertIn("access", data)
            self.user_access_tokens.append(data["access"])
        print("user_access_tokens:", self.user_access_tokens)

        route = "post/create/"
        request_url = os.path.join(self.base_url, route)
        for access_token in self.user_access_tokens:
            amount_of_user_posts = random.randint(1, config.max_posts_per_user)
            for i in range(amount_of_user_posts):
                user_post = {"title": "test title %s" % i,
                             "body": "test body %s" % i}
                headers = {"Authorization": "Bearer %s" % access_token}
                resp = requests.post(request_url, json=user_post,
                                     headers=headers)
                print(resp.text)
                self.assertEqual(resp.status_code, 201)
                data = resp.json()
                self.assertIn("id", data)
                self.posts.append(data["id"])
        print("post ids:", self.posts)

        for access_token in self.user_access_tokens:
            amount_of_user_actions = random.randint(1,
                                                    config.max_likes_per_user)
            for i in range(amount_of_user_actions):
                action = random.choice(self.user_post_actions)
                post_id = random.choice(self.posts)
                headers = {"Authorization": "Bearer %s" % access_token}
                route = "post/%s/%s/" % (post_id, action)
                request_url = os.path.join(self.base_url, route)
                resp = requests.post(request_url, headers=headers)
                print(resp.text)
                self.assertEqual(resp.status_code, 200)
