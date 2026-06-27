from backend.main import get_sheet, read_ws
import json

sh = get_sheet()
for ws in sh.worksheets():
    print(ws.title)
    rows = read_ws(ws)
    if rows:
        print("  Headers:", list(rows[0].keys()))
        print("  Sample:", rows[0])
    else:
        print("  Empty")
