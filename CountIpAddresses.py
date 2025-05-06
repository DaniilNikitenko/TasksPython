# My version


def ips_between(start, end):
    newstart = 0
    newend = 0
    step = 3
    for i in start.split("."):
        newstart += int(i) * (256**step)
        step -= 1
    if newend == 0:
        step = 3
        for i in end.split("."):
            newend += int(i) * (256**step)
            step -= 1
    return newend - newstart


# ChatGpt version


def ip_to_int(ip):
    parts = list(map(int, ip.split(".")))
    print(parts)
    return sum(part * (256 ** (3 - i)) for i, part in enumerate(parts))


def ips_betweennew(start, end):
    return ip_to_int(end) - ip_to_int(start)


print(ips_betweennew("10.0.0.0", "10.0.1.0"))
