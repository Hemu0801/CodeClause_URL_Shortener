import pyshorteners

def choose_service():
    print("Choose a URL shortening service:")
    print("1. TinyURL")
    print("2. Bitly")
   
    
    choice = input("Enter the number of your choice: ")
    return choice

def shorten_url(url, service):
    if service == "1":
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)
    elif service == "2":
        s = pyshorteners.Shortener(api_key="6d9b99478f221c1a62658163db34f53ba01bbde9")
        return s.bitly.short(url)
    else:
        return "Invalid choice. Please choose a valid option."

def main():
    url = input("Enter URL: ")
    choice = choose_service()
    short_url = shorten_url(url, choice)
    print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
