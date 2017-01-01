import gspread
import quickstart
import threading
from oauth2client.service_account import ServiceAccountCredentials
import sys
import fce_api as fd

def create_worksheet_sentence_batch(_spreadsheet, title, _error_sentences):
    worksheet = _spreadsheet.add_worksheet(title=title, rows=(len(error_sentences) + 1), cols=1)
    worksheet.update_acell('A1', 'Sentence')
    counterOffset = 2
    for sentence in _error_sentences:
        worksheet.update_acell('A' + str(counterOffset), sentence[0])
        counterOffset = counterOffset + 1

json_key = 'gspread-test.json'
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)

gc = gspread.authorize(credentials)

spreadsheet = gc.open("FCE_ERR")

error_sentences = fd.extract_data('fce_train.gold.max.rasp.old_cat.m2')

threads = []
batch_size = 5000
batch_count = len(error_sentences) // batch_size
for i in range(batch_count):
    t = threading.Thread(target=create_worksheet_sentence_batch, args=(spreadsheet,"fce_errors"+ str(i), error_sentences[i * batch_size: (i + 1) * batch_size]))
    threads.append(t)
    t.start()

