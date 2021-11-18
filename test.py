import time
import calendar
from datetime import datetime, time, timedelta, timezone
dt = datetime.datetime.strptime('2015-07-03 20:25', '%Y-%m-%d %H:%M').replace(tzinfo=us)
time.mktime(dt.utctimetuple())
# 1435955100 => 2015-07-03 20:25 GMT
calendar.timegm(dt.utctimetuple())
# 1435983900 => 2015-07-04 04:25 GMT
print(datetime.timestamp())
