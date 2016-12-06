import gspread
import quickstart
from oauth2client.service_account import ServiceAccountCredentials
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

json_key = 'gspread-test.json'
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)

gc = gspread.authorize(credentials)

spreadsheet = gc.open("SSTB")

treeBankDict = open('dictionary.txt')

lines = treeBankDict.readlines()
worksheet = spreadsheet.add_worksheet(title="Phrases", rows=(len(lines) + 1), cols=1)
worksheet.update_acell('A1', 'Phrase')
counterOffset = 2
for line in lines:
	worksheet.update_acell('A' + str(counterOffset), unicode(line[:line.index('|') - 1], errors='ignore'))
	counterOffset = counterOffset + 1
