import requests
import unittest


class TestPostRequest(unittest.TestCase):
    def test_post_request_positive_1(self):
        url = "https://reqres.in/api/users"
        data = {
            "name": "morpheus",
            "job": "leader"
        }

        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "morpheus")
        self.assertEqual(response.json()["job"], "leader")
        self.assertIn("id", response.json())
        self.assertIn("createdAt", response.json())

    def test_post_request_positive_2(self):
        url = "https://reqres.in/api/users"
        data = {
            "name": "john",
            "job": "developer"
        }

        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "john")
        self.assertEqual(response.json()["job"], "developer")
        self.assertIn("id", response.json())
        self.assertIn("createdAt", response.json())

    def test_post_request_positive_3(self):
        url = "https://reqres.in/api/users"
        data = {
            "name": "jane",
            "job": "designer"
        }

        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "jane")
        self.assertEqual(response.json()["job"], "designer")
        self.assertIn("id", response.json())
        self.assertIn("createdAt", response.json())

    def test_post_request_negative_1(self):
        url = "https://reqres.in/api/users"
        data = {
            "job": "leader"
        }

        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 201)
        self.assertNotIn("name", response.json())
        self.assertEqual(response.json()["job"], "leader")
        self.assertIn("id", response.json())
        self.assertIn("createdAt", response.json())

    def test_post_request_negative_2(self):
        url = "https://reqres.in/api/users"
        data = {
            "name": "morpheus"
        }

        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "morpheus")
        self.assertNotIn("job", response.json())
        self.assertIn("id", response.json())
        self.assertIn("createdAt", response.json())

    def test_post_request_negative_3(self):
        url = "https://reqres.in/api/users"
        data = {}

        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 201)
        self.assertNotIn("name", response.json())
        self.assertNotIn("job", response.json())
        self.assertIn("id", response.json())
        self.assertIn("createdAt", response.json())


if __name__ == "__main__":
    unittest.main()