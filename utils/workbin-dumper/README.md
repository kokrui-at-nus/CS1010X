# workbin dumper
bodged-together python script to download everything from a workbin. stores list of previously downloaded files in a csv file that will be skipped on subsequent runs.

## INSTALLATION:
1. download the python file
2. `pip3 install requests beautifulsoup4`


## USAGE
1. on Chrome, navigate to your coursemology workbin page (`/courses/<some_number_1>/materials/folders/<some_number_2>`)
2. inspect element / open developer tools, navigate to the `Network` tab
3. refresh the page, you will see an network entry (an http request) named `<some_number_2>`
4. right click the entry, click on `Copy -> Copy as cURL (bash)`
5. go to https://curlconverter.com/, select `Python` as the language, copypaste the output into the area specified in `workbin_dumper.py`
6. `python3 workbin_dumper.py`

the curlconverter output should look something like:

```py
import requests

headers = <some giant dict>

response = requests.get(<someurl>, headers=headers)
```
