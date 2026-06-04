import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}  # short_code -> original_url

    def _generate_short_code(self, url):
        hash_object = hashlib.md5(url.encode())
        return hash_object.hexdigest()[:6]

    def shorten_url(self, url):
        if not isinstance(url, str) or url.strip() == "":
            return "Invalid URL!"

        short_code = self._generate_short_code(url)
        self.url_map[short_code] = url

        return f"Short URL: {short_code}"

    def retrieve_url(self, short_code):
        return self.url_map.get(short_code, "URL not found!")


# ---------------- Demo ----------------
shortener = URLShortener()

original_url = "https://www.google.com"

short = shortener.shorten_url(original_url)
print(short)

code = short.split(": ")[1]

print("Original URL:", shortener.retrieve_url(code))