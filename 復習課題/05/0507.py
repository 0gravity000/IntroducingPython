# 5-1
import zoo
zoo.hours()

# 5-2
import zoo as menagerie
menagerie.hours()

# 5-3
from zoo import hours
hours()

# 5-4
from zoo import hours as info
info()

# 5-5
plain = {'a': 1, 'b': 2, 'c':3}
plain

# 5-6
from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy

# 5-7
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']
