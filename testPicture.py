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
        # testing if only dims is sent, that dims is correct and corners is none
        p3 = Picture("(1,2)")
        self.assertEqual(p3.dims,(1,2))
        self.assertIsNone(p3.corners)
        # testing sending correct values
        p4 = Picture("(1,2)","[(1,2)]")
        self.assertEqual(p4.dims,(1,2))
        self.assertEqual(p4.corners,[(1,2)])
         
    def test_getminmax(self):
        p1 = Picture()
        p1.corners = [(1,3),(3,1),(3,5),(1,5)] #not a rectangle, but just used for testing minmax
        p1.get_minmaxXY()
        self.assertEqual(p1.min_X,1)
        self.assertEqual(p1.min_Y,1)
        self.assertEqual(p1.max_X,3)
        self.assertEqual(p1.max_Y,5)
        # later add more tests here
    
    def test_get_pixels(self):
        pass
        # [[[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]], [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]], [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]]
        # [(1,3),(3,1),(3,3),(1,1)]
        
    def test_valid_dim(self):
        # if no dim is set, should return false
        p1=Picture()
        self.assertFalse(p1.valid_dimensions())
        # if dim is not a tuple should return false
        p1.dims = [1,2]
        self.assertFalse(p1.valid_dimensions())
        # if dim is not two dimensions, should return false
        p1.dims=(1,2,3)
        self.assertFalse(p1.valid_dimensions())
        # if dim contains anything other than numbers, should return false
        p1.dims=('x',3)
        self.assertFalse(p1.valid_dimensions())
        # if either dim value is <= 0, should return false
        p1.dims = (-5,3)
        self.assertFalse(p1.valid_dimensions())
        p1.dims = (2,0)
        self.assertFalse(p1.valid_dimensions())
        # later need to add checking for integer dimensions in picture.py
        
    def test_valid_corners(self):
        p1 = Picture()
        

if __name__ == '__main__':
    unittest.main()