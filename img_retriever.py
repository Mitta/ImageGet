#!/usr/bin/python

import sys, getopt, json, uuid
import requests
import urllib.request

google_api_key = ""
cx = ""
keyword = ""
amount = 10
target_directory = "."
url = "https://www.googleapis.com/customsearch/v1?key={0}&cx={1}&q={2}&searchType=image&start={3}"
count = 0
def main(args):
    try:
        opts, args = getopt.getopt(args,'g:k:n:d:c:h')
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h"):
            usage()
            sys.exit()
        elif opt in ("-g"):
            global google_api_key
            google_api_key = arg
        elif opt in ("-k"):
            global  keyword
            keyword = arg
        elif opt in ("-n"):
            global amount
            amount = arg
        elif opt in ("-d"):
            global target_directory
            target_directory = arg
        elif opt in ("-c"):
            global cx
            cx = arg
    page_index = 1
    downloadPictures(1)

def downloadPictures(page_index):
    request_url = url.format(google_api_key, cx, keyword, page_index)
    r = requests.get(request_url)
    data = r.json()
    for entry in data["items"]:
        r = requests.get(entry["link"])
        filename = str(uuid.uuid4()) + ".jpg"
        with open(filename, "wb") as pic:
            pic.write(r.content)
        global count
        count = count + 1
    if count < int(amount):
        queries = data["queries"]
        nextpage = queries["nextPage"]
        index = nextpage[0]["startIndex"]
        downloadPictures(index)



def usage():
    print("ImageGet")
    print("-------------------------------------------")
    print("This simple script pull images from the Google Search Engine API and stores them on disk.")
    print("")
    print("-g   Required. Specify your google api key.")
    print("-k   Required. The keyword the custom search needs to search on.")
    print("-n   Optional. The amount of images that is saved to the target directory. Defaults to 10")
    print("-d   Optional. The target directory where the images are saved. Defaults to working directory")
    print("-c   Required. The cx search engine ID which is needed to use the Google Custom Search API")
    print("-h   Display usage")
    print("")
    print("Made by ByMitta. https://mitta.github.io")


if __name__ == "__main__":
    main(sys.argv[1:])
