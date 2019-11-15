import os
import time
from hashlib import sha1

create_session_id = lambda: sha1(bytes('%s%s' % (os.urandom(16), time.time()), encoding='utf-8')).hexdigest()

# print(create_session_id())