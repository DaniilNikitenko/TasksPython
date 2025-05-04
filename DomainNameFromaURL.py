# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"
import re


def domain_name(url):
    return re.sub(r"(https?://)?(www\.)?", "", url).split(".")[0]


print(domain_name("http://google.com"))


print(domain_name("https://123.net"))
print(domain_name("https://hyphen-site.org"))
print(domain_name("http://codewars.com"))
print(domain_name("http://www.codewars.com/kata/"))

print(domain_name("icann.org"))
print(domain_name("https://youtube.com"))
