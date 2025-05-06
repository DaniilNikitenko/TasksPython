# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.


# def format_duration(seconds):
#     second = seconds % 60
#     minuts = 0
#     hours = 0
#     days = 0
#     years = 0
#     if seconds / 86400:
#         days = seconds // 86400
#         if days >= 365:
#             years = days // 365
#     days = days % 365
#     hours = seconds // 3600
#     hours = hours % 24
#     minuts = seconds // 60
#     minuts = minuts % 60
#     return f"{years}, {days}, {hours}, {minuts}, {second}"


def format_duration(seconds):
    if seconds == 0:
        return "now"

    numbers = [
        ("year", 365 * 24 * 60 * 60),
        ("day", 24 * 60 * 60),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1),
    ]

    parts = []

    for name, unit_seconds in numbers:
        print(f"name:{name}")
        print(f"unit_seconds:{unit_seconds}")
        value = seconds // unit_seconds
        print(f"value: {value}")
        print(f"seconds:{seconds}")
        if value:
            seconds %= unit_seconds
            print(f"seconds:{seconds}")
            part = f"{value} {name}" + ("s" if value > 1 else "")
            parts.append(part)
        print(f"parts{parts}")
    if len(parts) == 1:
        return parts[0]
    else:
        return ", ".join(parts[:-1]) + " and " + parts[-1]
