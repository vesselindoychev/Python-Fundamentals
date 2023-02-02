century = int(input())

YEARS = 100 * century
DAYS = int(365.2422 * YEARS)
HOURS = 24 * DAYS
MINUTES = 60 * HOURS

print(f"{century} centuries = {YEARS} years = {DAYS} days = {HOURS} hours = {MINUTES} minutes")