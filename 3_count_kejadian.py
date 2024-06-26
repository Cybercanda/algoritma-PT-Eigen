def count_kejadian(input_list, query_list):
 return [input_list.count(query) for query in query_list]
 
INPUT = ['xc', 'dz', 'bbb', 'dz']
QUERY = ['bbb', 'ac', 'dz']

output = count_kejadian(INPUT, QUERY)
print(output)