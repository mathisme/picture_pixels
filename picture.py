from ast import literal_eval

class Picture():

    def __init__(self, dims="None", corners="None"):
        sefl.dims = literal_eval(dims)
        self. corners = literal_eval(corners)
        
        