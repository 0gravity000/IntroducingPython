# 8.2.9 pickleによるシリアライズ
import pickle
import datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
now1

now2

#
import pickle
class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
obj1

str(obj1)

pickled = pickle.dumps(obj1)
pickled

obj2 = pickle.loads(pickled)
obj2

str(obj2)