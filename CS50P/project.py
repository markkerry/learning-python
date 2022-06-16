import argparse
import pyshorteners
import requests
import sys
from datetime import datetime
from tabulate import tabulate

def main():
    # get args using argparse
    args = get_args()

    if args.count > 25:
        print("A count of " + str(args.count) + " is too many and will take some time. Try 25 or less.")
        sys.exit()
    elif args.count < 1:
        print("A count of at least 1 is required")
        sys.exit()

    #g set the uri
    uri = "https://api.stackexchange.com/2.3/questions?pagesize=" + str(args.count) + "&order=desc&sort=activity&tagged=" + args.tag + "&site=stackoverflow"

    # Get posts from Stack Overflow
    o = get_posts(uri)

    # Exit if the tag did not return anything
    if str(o).startswith("{'items': [], 'has_more': False"):
        print("No posts for tag " + args.tag + " found. Try another")
        sys.exit()

    # Gather the information and append to a dict
    print()
    print("Gathering information... Tag " + args.tag + ", count " + str(args.count) + ", output " + args.output)
    print()
    posts = []
    for item in o["items"]:
        creation_date = convert_date(item["creation_date"])
        last_activity_date = convert_date(item["last_activity_date"])
        url = tiny_url(item["link"])
        title = clean_title(item["title"])

        p = {"Title": title, "URL": url, "Creation Date": creation_date, "Last Activity Date": last_activity_date}
        posts.append(p)

    # Print as text or tabulate table
    if args.output == "text":
        for post in posts:
            print("Title: " + post["Title"])
            print("URL: " + post["URL"])
            print("Creation date: " + post["Creation Date"])
            print("Last activity date " + post["Last Activity Date"])
            print()
    else:
        print(tabulate(posts, headers="keys", tablefmt="fancy_grid"))
        print()

# Get the programs arguments
def get_args():
    """
    gets the arguments of the proagram using argparse

    :param: none
    :type: none
    :return: parsed arguments
    :rtype: <class 'argparse.Namespace'>
    """
    parser = argparse.ArgumentParser(description="Get the latest Stack Overflow questions from desired 'tag'")
    parser.add_argument("-t", "--tag", default="cs50", help="Subject tag to search for E.g. 'python', 'c' or 'cs50'", type=str)
    parser.add_argument("-c", "--count", default=10, help="Number of items to show, maximum of 25", type=int)
    parser.add_argument("-o", "--output", choices = ["text", "table"], default="text", help="Output as text or table", type=str)
    return parser.parse_args()

# try to query the stack exchange api
def get_posts(u):
    """
    performs and HTTP GET request using requests library

    :param u: short for url
    :type u: str
    :raise: If failed request
    :return: A string of reposnse.json
    :rtype: dict
    """
    try:
        response = requests.get(u)
    except:
        print("Failed GET request method to Stack Exchange API. Status code was " + response.status_code)
        print("Is 2.3 still the correct version?")
        print("https://api.stackexchange.com/docs")
        sys.exit(1)
    return response.json()

# Replace the html characters in the title
def clean_title(s):
    """
    cleans up the title replacing html charcters
    Also shortens the string if longer than 65

    :param s: short for string
    :type s: str
    :raise TypeError: if s not str
    :return: A string of text no longer than 65
    :rtype: str
    """
    if not type(s) == str:
        raise TypeError
    else:
        clean = s.replace("&#39;", "'")
        clean = clean.replace("&amp;", "&")
        clean = clean.replace('&quot;', '"')
        clean = clean.replace("&#180;", "'")
        if len(clean) > 65:
            clean = clean[:65] + "..."
    return clean

# Convert the long to tiny urls
def tiny_url(n):
    """
    converts a long url to a tiny one using pyshorteners library

    :param n: url to shorten
    :type n: str
    :raise TypeError: if s not str
    :return: a tinyurl
    :rtype: str
    """
    if not type(n) == str:
        raise TypeError
    else:
        tiny = pyshorteners.Shortener()
    return  tiny.tinyurl.short(n)

# Convert the 
def convert_date(d):
    """
    converts a unix date using datetime library

    :param d: date to convert
    :type d: int
    :raise TypeError: if d not int
    :return: the converted date
    :rtype: str
    """
    global date
    try:
        date = datetime.utcfromtimestamp(d).strftime('%Y-%m-%d %H:%M:%S')
    except TypeError:
        print("Failed to convert date")
        raise
    return date

if __name__ == "__main__":
    main()