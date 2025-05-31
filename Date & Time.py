

# importing datetime

import datetime

a= datetime.datetime.now()   # syntax to find date time
print(a)

print("Date - ",a.strftime("%a"))  # short form of date

print("\nFull Form of Date     -",a.strftime("%A")) # full form of date

print("\nNumber of weekday     -",a.strftime("%w")) # week day as number

print("\nDay of the Month      -",a.strftime("%d")) # Day of the month

print("\nShort Month Name      -",a.strftime("%b")) # month name short version

print("\nFull Month Name       -",a.strftime("%B")) # month name full version

print("\nMonth Number          -",a.strftime("%m")) # month as a number

print("\nYear as short form    -",a.strftime("%y")) # Year as short version

print("\nYear as full form     -",a.strftime("%Y")) # Year as a full version

print("\nHour b2n (0-023)      -",a.strftime("%H")) # hour 0-23

print("\nHour b2n (0-12)       -",a.strftime("%I")) # hour 0-12

print("\n AM Or PM             -",a.strftime("%p")) # am or pm

print("\nMinute                -",a.strftime("%M")) # Minute

print("\nSecond                -",a.strftime("%S")) # Second
