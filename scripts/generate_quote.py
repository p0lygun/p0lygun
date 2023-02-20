import urllib.request
import json


def get_response(url) -> dict | str:
    url = urllib.request.urlopen(url)
    if url.getcode() == 200:
        return json.loads(url.read())
    print("Error receiving data", url.getcode())
    return ''


def write_to_readme(quote):
    with open('./README.md', 'r+') as file:
        data = file.read().split("***", maxsplit=1)
        file.seek(0)
        file.write(quote.strip() + "\n***\n" + data[-1].strip())
        file.truncate()



def main():
    url_eng = "https://api.quotable.io/random?tags=technology"
    quote_response = get_response(url_eng)
    quote = ">" + quote_response['content'] + " -" + quote_response['author']
    # print(quote)
    write_to_readme(quote)


if __name__ == '__main__':
    main()
