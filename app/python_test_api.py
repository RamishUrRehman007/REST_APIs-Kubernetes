import json
try:
    import unittest
    from ramish_mart import app

except Exception as e:
    print("Something is Wrong {}".format(e))

class RamishMartTest(unittest.TestCase):

    #check for the response 200
    def test_index_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=json.dumps({
        "username":"postgres",
        "password":"ramish534"
        }), content_type='application/json')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #check if content is returned or not
    def test_index_login_content(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=json.dumps({
        "username":"postgres",
        "password":"ramish534"
        }), content_type='application/json')
        self.assertEqual(response.content_type, 'application/json')
    
    #check if content is returned or not
    def test_index_login_data(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=json.dumps({
        "username":"postgres",
        "password":"ramish534"
        }), content_type='application/json')
        response = response.data
        res= dict(json.loads(response))
        self.assertIn('code',list(res.keys()))
    
    def test_index_create_product(self):
        tester = app.test_client(self)
        header = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyOTk0NTY1OCwianRpIjoiZGY4ZGQ2ZTctMzU1Mi00MDM3LTg2OGMtZTBkNTBhYTRiZDFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBvc3RncmVzIiwibmJmIjoxNjI5OTQ1NjU4LCJleHAiOjE2Mjk5NDY1NTh9.TXPXB4HWESETmuhLDmCqNK701hLEgYBXd2xrumHcUmA'}

        response = tester.post('/products', data=json.dumps({
        "name":"Spritse",
        "price":90
        }), content_type='application/json', headers=header)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_index_content_product(self):
        tester = app.test_client(self)
        header = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyOTk0NTY1OCwianRpIjoiZGY4ZGQ2ZTctMzU1Mi00MDM3LTg2OGMtZTBkNTBhYTRiZDFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBvc3RncmVzIiwibmJmIjoxNjI5OTQ1NjU4LCJleHAiOjE2Mjk5NDY1NTh9.TXPXB4HWESETmuhLDmCqNK701hLEgYBXd2xrumHcUmA'}

        response = tester.post('/products', data=json.dumps({
        "name":"Colaa",
        "price":30
        }), content_type='application/json', headers=header)
        self.assertEqual(response.content_type, 'application/json')
    
    def test_index_product_data(self):
        tester = app.test_client(self)
        header = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyOTk0NTY1OCwianRpIjoiZGY4ZGQ2ZTctMzU1Mi00MDM3LTg2OGMtZTBkNTBhYTRiZDFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBvc3RncmVzIiwibmJmIjoxNjI5OTQ1NjU4LCJleHAiOjE2Mjk5NDY1NTh9.TXPXB4HWESETmuhLDmCqNK701hLEgYBXd2xrumHcUmA'}

        response = tester.post('/products', data=json.dumps({
        "name":"Pespii",
        "price":40
        }), content_type='application/json', headers=header)
        response = response.data
        res= dict(json.loads(response))
        self.assertIn('code',list(res.keys()))

    def test_index_get_product_data(self):
        tester = app.test_client(self)
        header = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyOTk0NTY1OCwianRpIjoiZGY4ZGQ2ZTctMzU1Mi00MDM3LTg2OGMtZTBkNTBhYTRiZDFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBvc3RncmVzIiwibmJmIjoxNjI5OTQ1NjU4LCJleHAiOjE2Mjk5NDY1NTh9.TXPXB4HWESETmuhLDmCqNK701hLEgYBXd2xrumHcUmA'}

        response = tester.post('/products?name=Cola', content_type='application/json', headers=header)
        response = response.data
        res= dict(json.loads(response))
        self.assertIn('code',list(res.keys()))

if __name__ == "__main__":
    unittest.main()