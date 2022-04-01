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
        # testing the case given in the problem statement
        p1 = Picture()
        p1.dims = (3,3)
        p1.corners = [(1,3),(3,1),(3,3),(1,1)]
        self.assertEqual(p1.get_pixels(),(
        [[[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]], [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]], [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]]))
        
        
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
        # should return false if it's not a list
        p1.corners = ((1,3),(3,7),(1,7),(3,3))
        self.assertFalse(p1.valid_corners())
        # return false if the length of the list is not 4
        p1.corners = [(1,2),(2,5)]
        self.assertFalse(p1.valid_corners())
        # return false if each element is not a tuple
        p1.corners = [(1,2),(2,3),[3,4],(4,5)]
        self.assertFalse(p1.valid_corners())
        # return false if a tuple is not of length two
        p1.corners = [(1,2),(2,5),(1,2,3),(4,5)]
        self.assertFalse(p1.valid_corners())
        # return false if a tuple does not contain a number
        p1.corners = [(1,2),('x',4),(5,7),(2,6)]
        self.assertFalse(p1.valid_corners())

if __name__ == '__main__':
    unittest.main()