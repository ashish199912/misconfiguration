import requests

def check_content_type(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' in content_type:
                body = response.text
                if '<html' in body:
                    return "Matched"
                else:
                    return "Not Matched - Content-Type is HTML but HTML tag is missing in the response body"
            else:
                return f"Not Matched - Content-Type is {content_type}"
        else:
            return "Website is not reachable"
    except Exception as e:
        return f"Error: {e}"

url = input("Enter the URL to check: ")
result = check_content_type(url)
print(f"Result for {url}: {result}")
