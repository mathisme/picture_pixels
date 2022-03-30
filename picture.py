from ast import literal_eval

class Picture():

    def __init__(self, dims="None", corners="None"):
        # need to add a try catch here to check for invalid enteries
        sefl.dims = literal_eval(dims)
        self.corners = literal_eval(corners)
        self.min_X, self.max_X = float("inf"), float("-inf")
        self.min_Y, self.max_Y = float("inf"), float("-inf")
        
    def get_minmaxXY(self):
        ''' 
            gets the ordinates for the bottom left corner and top right corner 
        '''
        for corner in self.corners:
            if corner[0] < self.min_X:
                self.min_X = corner[0]
            if corner[0] > self.max_X:
                self.max_X = corner[0]
            if corner[1] < self.min_Y:
                self.min_Y = corner[1]
            if corner[1] > self.max_Y:
                self.max_Y = corner[1]
    
    def valid_dimensions(self):
        '''
            Determines if the dimensions of the picture are valid
            returns a boolean
        '''
        # checking to see that the dimensions are a tuple
        if type(self.dims) is not tuple:
            return False
        # checking to see the tuple is two dimensional
        if len(self.dims)!=2:
            return False
        # checking to see the tuple contains numeric values
        if type(self.dims[0]) not in [float,int] or type(self.dims[1]) not in [float,int]:
            return False
        # checking to see the dimensions are positive
        if self.dims[0] <= 0 or self.dims[1] <= 0:
            return False
        return True            
        
    def valid_corners(self):
        '''
            checks to make sure the corners vairable is a list of 4 tuples containing two numbers
            returns a boolean
        '''
        # check that it's a list
        if type(self.corners) is not list:
            return False
        # check that the length of the list is four
        if len(self.corners)!=4:
            return False
        # for each item check that it is a tuple of length two with two numeric values
        for item in self.corners:
            if type(item) is not tuple:
                return False
            if len(item)!=2:
                return False
            if type(item[0]) not in [float,int] or type(item[1]) not in [float, int]:
                return False
        return True                

