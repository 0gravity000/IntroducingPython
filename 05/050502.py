# 5.5.2 Counter()による要素数の計算
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
breakfast_counter

breakfast_counter.most_common()

breakfast_counter.most_common(1)

breakfast_counter

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
lunch_counter

breakfast_counter + lunch_counter

breakfast_counter + lunch_counter

lunch_counter - breakfast_counter

breakfast_counter & lunch_counter

breakfast_counter | lunch_counter