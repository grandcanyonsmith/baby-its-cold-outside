import datetime
import pytz
import sys

def print_utah_time():
    """Print the current time in Utah in a human readable format."""
    utah_time_zone = pytz.timezone('America/Denver')
    utah_time = datetime.datetime.now(utah_time_zone)
    
    # Format the time for human readability
    utah_time_human_readable = utah_time.strftime('%B %d, %Y at %I:%M:%S %p')

    # Standard output for aligned display
    print(f"Standard Output: The time in Utah is: {utah_time_human_readable}")

    # Standard error to indicate the conversion to a human readable format
    print(f"Standard Error: Converted to human readable format", file=sys.stderr)

print_utah_time()