from picture import Picture
import unittest

class TestPicture(unittest.TestCase):
    def test_init(self):
        # testing that dim and corners are none when nothing gets passed to the constructor
        p1 = Picture()
        self.assertIsNone(p1.dims)
        self.assertIsNone(p1.corners)
        # testing none is assigned when passed invalid arguments
        p2 = Picture("hello")
        self.assertIsNone(p2.dims)
        self.assertIsNone(p2.corners)
         
    def test_getminmax(self):
        pass
    
    def test_get_pixels(self):
        pass
        
    def test_valid_dim(self):
        pass
       
    def test_valid_corners(self):
        pass

if __name__ == '__main__':
    unittest.main()