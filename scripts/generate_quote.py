import urllib.request
import json

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def write_to_readme(static_readme , quote):    
    with open(static_readme,'r') as f:
        with open('./README.md','w') as f2: 
            f2.write(quote)
            f2.write(f.read())

def main():
    url_eng = "https://api.quotable.io/random?tags=technology"
    quote_response = getResponse(url_eng)
    context = quote_response['content']
    author = quote_response['author']
    quote = ">" + context + " -" + author
    # print(quote)
    static_readme = './static_readme.md'
    write_to_readme(static_readme , quote)

if __name__ == '__main__':
    main()
