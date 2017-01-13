# ImageGet
Simple script to retrieve an amount of images through the Google Custom Search API

## Dependencies
The script relies on Python3 and the module `requests`.
Install this through pip

`pip install requests`

## Usage
Simply run the script with the parameters including the API key and the search engine ID.

```bash
ImageGet
-------------------------------------------
This simple script pull images from the Google Search Engine API and stores them on disk.

-g   Required. Specify your google api key.
-k   Required. The keyword the custom search needs to search on.
-n   Optional. The amount of images that is saved to the target directory. Defaults to 10
-d   Optional. The target directory where the images are saved. Defaults to working directory
-c   Required. The cx search engine ID which is needed to use the Google Custom Search API
-h   Display usage

Made by ByMitta. https://mitta.github.io
```
