import json
from selenium import webdriver

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

profile = {
           'printing.print_preview_sticky_settings.appState': json.dumps(appState),
           'savefile.default_directory':"/home/song-ruyang/AutoPDF/download"
           }

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')

driver = webdriver.Chrome(chrome_options=chrome_options)
