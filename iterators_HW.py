nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class IterNestedList:
    def __init__(self, nested_list):
        self.main_list = nested_list
        self.index = 0
        self.inner_index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index != len(self.main_list):
            if self.inner_index < len(self.main_list[self.index]):
                tmp = self.main_list[self.index][self.inner_index]
                self.inner_index += 1
                if self.inner_index == len(self.main_list[self.index]):
                    self.index += 1
                    self.inner_index = 0
            return tmp
        else:       
            raise StopIteration()



for i in IterNestedList(nested_list):
    print(i)
