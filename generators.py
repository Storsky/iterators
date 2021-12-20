nested_list = [
	['a', 'b', 'c'],
	['d', 'e', ['f', 'kk'], 'h', False],
	[1, 2, None],
    '2f'
]


def flatlist(l):
    for item in l:
        if isinstance(item, list):
           for n in flatlist(item):
               yield n
        else: 
            yield item



print([x for x in flatlist(nested_list)])
