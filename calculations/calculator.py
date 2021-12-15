class Calculation:
    def __init__(self,values: tuple):
        self.values = Calculation.converttotuple(values)
    @classmethod
    def create(cls,values: tuple):
        return cls(values)
    @staticmethod
    def convert_args_to_tuple_of_float(values):
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
