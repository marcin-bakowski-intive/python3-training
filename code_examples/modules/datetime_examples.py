from datetime import datetime, timedelta

utc_now = datetime.utcnow()
local_now = datetime.now()
print("UTC now: %s" % utc_now)
print("Now: %s" % local_now)
print("Yesterday: %s" % (local_now - timedelta(days=1)))
print("Difference between local and UTC time: %s" % abs(local_now- utc_now))

datetime_str = local_now.strftime("%A, %d. %B %Y %I:%M%p")
print("Datetime string in custom format: %s" % datetime_str)

# parse back datetime from string
dt_parsed = datetime.strptime(datetime_str, "%A, %d. %B %Y %I:%M%p")
print("Parsed datetime: %s" % dt_parsed)
