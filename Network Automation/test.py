class test1():
    """
    lorem ipsum test 1
    """

    def function1(self, value1, value2):
        '''
        function1 testing value
        '''
        self.value1 = value1
        self.value2 = value2
        object_value = value1 + value2
        return object_value

import_class = test1()

output = import_class.function1(value1=1, value2=5)

print(output)