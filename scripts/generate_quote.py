import urllib.request
import json


def get_response(url) -> dict:
    url = urllib.request.urlopen(url)
    if url.getcode() == 200:
        return json.loads(url.read())
    print("Error receiving data", url.getcode())
    return dict()


def write_to_readme(quote):
    with open('./README.md', 'r+') as file:
        data = file.read().split("***", maxsplit=1)
        file.seek(0)
        file.write(quote.strip() + "\n***\n" + data[-1].strip())
        file.truncate()


def main() -> None:
    quote_response = get_response(
        "https://quoteslate.vercel.app/api/quotes/random?tags=knowledge"
    )
    quote_parts = [
        ">",
        quote_response.get('quote', 'Sleep is the ultimate debugger'),
        " -",
        quote_response.get('author', 'Vibhakar Solanki')
    ]
    # print(quote)
    write_to_readme(''.join(quote_parts))


if __name__ == '__main__':
    main()
