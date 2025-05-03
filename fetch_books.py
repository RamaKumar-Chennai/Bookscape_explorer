import requests
#This function fetches the book data from Google Books API
def fetch_books(search_query):
    
    url = f"https://www.googleapis.com/books/v1/volumes?q={search_query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("the keys in data dictionary are ",data.keys())
        print("the data type of data is ",type(data))
        print("the len of data is ",len(data))
        return data.get("items", [])
    else:
        print("Error fetching data:", response.status_code)
        return []
