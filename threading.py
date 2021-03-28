# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import threading
import time
import requests

GOOGLE = "https://www.google.com"
AMAZON = "https://www.amazon.com"
FACEBOOK = "https://www.facebook.com"
APPLE = "https://www.apple.com"
NETFLIX = "https://www.netflix.com"
TESLA = "https://www.tesla.com"

FAANG = [FACEBOOK, APPLE, AMAZON, NETFLIX, GOOGLE, TESLA]
FAANG_HTML = []

lock = threading.RLock()


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.url = url

    def run(self):
        print("Starting " + self.name + "\n")
        print("Fetching content for : " + self.url + "\n")
        with lock:
            FAANG_HTML.append(get_html(self.url))
        # print_time(self.name,5, self.counter)
        print("Exiting " + self.name + "\n")


def get_html(url):
    page = requests.get(url)
    return page.text


def print_html(html_tree):
    print(html_tree)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        counter = 1
        for url in FAANG:
            thread = myThread(counter, "Thread " + str(counter), 1, url)
            thread.start()
            counter += 1
    except:
        print("Error: unable to start thread")

    while len(FAANG_HTML) != 5:
        pass

    # for content in FAANG_HTML:
    #     print_html(content)
