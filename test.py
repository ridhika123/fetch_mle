import unittest 
from app import app

class FlaskTest(unittest.TestCase):

    # Checking that Flask is set up correctly
    def test_1_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # Checking inputs page loads correctly
    def test_2_input_page (self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'Calculating Coordinates' in response.data)
    
    # Checking solution page is set up correctly
    def test_3_solution_post (self):
        tester = app.test_client()
        response = tester.post("/solution", 
                      data = {"dimensions": "(3, 3)", "corner_points": "[(1, 1), (3, 1), (1, 3), (3, 3)]"}, 
                      follow_redirects = True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        
    # Checking solution page gives appropriate response when correct inputs
    def test_4_solution_output_correct (self):
        tester = app.test_client()
        response = tester.post("/solution", 
                      data = {"dimensions": "(3, 3)", "corner_points": "[(1, 1), (3, 1), (1, 3), (3, 3)]"}, 
                      follow_redirects = True)
        self.assertIn(b'The solution matrix is:', response.data)
        
    # Checking solution page gives appropriate response when incorrect inputs
    def test_5_solution_output_incorrect (self):
        tester = app.test_client()
        response = tester.post("/solution", 
                      data = {"dimensions": "(0, 0)", "corner_points": "[(1, 1), (3, 1), (1, 3), (3, 3)]"}, 
                      follow_redirects = True)
        self.assertIn(b'Please enter valid values.', response.data)
        
if __name__ == "__main__":
    unittest.main()