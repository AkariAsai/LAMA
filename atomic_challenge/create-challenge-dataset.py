# NOTE: A script that generates a challenge dataset from the ATOMIC dev set
import ast
import json
import pandas as pd
from tqdm import tqdm

csv_file = 'atomic_dev.csv'
df = pd.read_csv(csv_file)

events = set()

output_file = open("test.jsonl", "w", encoding='utf-8')

for index, row in tqdm(df.iterrows()):
    attrs = ast.literal_eval(row['xAttr'])
    if '_' not in row['event'] and len(attrs) == 1 and row['event'] not in events:
        text = row['event']
        appended = ". PersonX is seen as [MASK]."

        datum = {
            "masked_sentences": [text + appended],
            "obj_label": attrs[0],
            "sub_label": 'Squad'
        }

        events.add(text)

        output_file.write(json.dumps(datum) + "\n")