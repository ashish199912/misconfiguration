# Content-Type Checker

This Python script checks whether the "Content-Type" header of a given URL matches the content in the response body. It is useful for identifying instances where the server incorrectly specifies the content type, which can lead to unexpected behavior in web browsers.

## Examples

### Example 1: Checking a Valid URL with Correct Content-Type

```bash
$ python check_content_type.py
Enter the URL to check: https://www.example.com
Result for https://www.example.com: Matched
```

In this example, the script successfully checks the provided URL (`https://www.example.com`) and finds that the content type matches the content in the response body.

### Example 2: Checking a Valid URL with Incorrect Content-Type

```bash
$ python check_content_type.py
Enter the URL to check: https://www.example.com/image.jpg
Result for https://www.example.com/image.jpg: Not Matched - Content-Type is image/jpeg
```

Here, the script checks a URL (`https://www.example.com/image.jpg`) that serves an image (`image/jpeg` content type). However, the script expects HTML content, so it reports a mismatch.

### Example 3: Checking an Invalid URL

```bash
$ python check_content_type.py
Enter the URL to check: https://www.nonexistentwebsite.com
Result for https://www.nonexistentwebsite.com: Website is not reachable
```

When provided with an invalid URL (`https://www.nonexistentwebsite.com`), the script detects that the website is not reachable and returns an appropriate error message.


