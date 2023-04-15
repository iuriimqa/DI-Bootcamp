import requests
import time

def get_load_time(url):
    start_time = time.time()
    requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    return load_time

print( "The page 1 loading:",get_load_time('https://www.google.com'))
print( "The page 2 loading:",get_load_time('https://www.imdb.com/'))
print( "The page 3 loading:",get_load_time('https://www.youtube.com/'))