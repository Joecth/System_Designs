# Web Crawler
# Implement a webpage Crawler to crawl webpages of http://www.wikipedia.org/. To simplify the question, let's use url instead of the the webpage content.

# Your crawler should:

# Call HtmlHelper.parseUrls(url) to get all urls from a webpage of given url.
# Only crawl the webpage of wikipedia.
# Do not crawl the same webpage twice.
# Start from the homepage of wikipedia: http://www.wikipedia.org/
# Example
# Example 1

# Input:
#     "http://www.wikipedia.org/": ["http://www.wikipedia.org/help/"]
#     "http://www.wikipedia.org/help/": []
# Output: ["http://www.wikipedia.org/", "http://www.wikipedia.org/help/"]
# Example 2

# Input:
#     "http://www.wikipedia.org/": ["http://www.wikipedia.org/help/"]
#     "http://www.wikipedia.org/help/": ["http://www.wikipedia.org/","http://www.wikipedia.org/about/"]
#     "http://www.wikipedia.org/about/": ["http://www.google.com/"]

# Output: ["http://www.wikipedia.org/", "http://www.wikipedia.org/help/", "http://www.wikipedia.org/about/"]
# Notice
# You need do it with multithreading.
# You can use up to 3 threads

"""
class HtmlHelper:
    # @param (string)
    # @return (list)
    @classmethod
    def parseUrls(url):
        # Get all urls from a webpage of given url. 
"""
from collections import deque
from threading import Thread
import re
            
class ThreadWithReturnVal(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
 
        self._return = None
 
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
 
    def join(self):
        Thread.join(self)
        return self._return


class Solution:
    def __init__(self):
        # self.visited = set()
        pass
        
    """
    @param url(string): a url of root page
    @return (list): all urls
    """
    def crawler(self, url):
        # write your code here


        return self.run(url)
        
        # TODO: Fix multi-threading
        threads = []
        for i in range(0, 3):
            thread = ThreadWithReturnVal(target=self.run, args=(url,))
            thread.start()
            threads.append(thread)
        
        ans = []
        for thread in threads:
            tmp = thread.join()
            ans.append(tmp)
        
        return ans

    def run(self, url):
            Q = deque()
            Q.append(url)
            # ans = set()

            visited = set()
            visited.add(url)

            pat = re.compile("http[s]*:\/\/[a-zA-Z]*.wikipedia.org\/")

            while Q:
                cur_url = Q.popleft()
                anchors = HtmlHelper.parseUrls(cur_url)

                for tmp in anchors:
                    # if not tmp.startswith(url):
                    if not pat.search(tmp):
                        print(f'ignored url: {tmp}')
                        continue

                    if tmp not in visited:
                        Q.append(tmp)
                    visited.add(tmp)

            return list(visited)
    """
    Big Case:
        "http://www.wikipedia.org/": ["https://en.wikipedia.org/","https://ja.wikipedia.org/","https://es.wikipedia.org/","https://it.wikipedia.org/","https://zh.wikipedia.org/","https://de.wikipedia.org/","https://ru.wikipedia.org/","https://fr.wikipedia.org/","https://pl.wikipedia.org/wiki/","https://nl.wikipedia.org/"]
    "https://zh.wikipedia.org/": []
    "https://en.wikipedia.org/": ["https://es.wikipedia.org/wiki/Wikipedia:Portada","https://it.wikipedia.org/wiki/Pagina_principale","https://meta.wikimedia.org/wiki/Privacy_policy/it","https://fr.wikipedia.org/wiki/Arabe_(cheval)"]
    "https://ru.wikipedia.org/": []
    "https://fr.wikipedia.org/": ["http://www.google.cn","https://fr.wikipedia.org/wiki/Cheval_oriental","https://fr.wikipedia.org/wiki/Arabe_(cheval)"]
    "https://it.wikipedia.org/": ["https://it.wikipedia.org/wiki/Pagina_principale","https://it.wikipedia.org/wiki/1883","https://it.wikipedia.org/wiki/Anatolia"]
    "https://it.wikipedia.org/wiki/1883": ["https://it.wikipedia.org/wiki/Stati_nel_1883","https://it.wikipedia.org/wiki/7_dicembre","https://it.wikipedia.org/wiki/16_gennaio"]
    "https://it.wikipedia.org/wiki/16_gennaio": ["https://it.wikipedia.org/wiki/3_gennaio","https://it.wikipedia.org/wiki/3_gennaio","https://it.wikipedia.org/wiki/Stati_Uniti_d%27America"]
    "https://it.wikipedia.org/wiki/Pagina_principale": ["https://it.wikipedia.org/wiki/Papa_Sisto_IV","https://it.wikipedia.org/wiki/Michelangelo_Buonarroti","https://it.wikipedia.org/wiki/Giovanni_Pico_della_Mirandola","https://it.wikipedia.org/wiki/Rinascimento_fiorentino"]
    "http://www.google.cn": []

    """        