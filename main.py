from datetime import datetime
import pytz

def print_utah_time():
    # Timezone for Utah - Either 'America/Denver' can be used for Mountain Time
    utah_timezone = pytz.timezone('America/Denver')
    
    # Current time in UTC
    utc_time = datetime.utcnow()
    
    # Convert to Utah time
    utah_time = utc_time.astimezone(utah_timezone)
    
    # Print the time in Utah
    print("Current time in Utah:", utah_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

if __name__ == '__main__':
    print_utah_time()