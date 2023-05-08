import json
in_str = """[{"T":"t","S":"BTC/USD","p":29534.66,"s":0.00067,"t":"2023-05-06T03:45:31.805Z","i":16205910,"tks":"B"},{"T":"t","S":"BTC/USD","p":29535.38,"s":0.15,"t":"2023-05-06T03:45:31.805Z","i":16205911,"tks":"B"}]"""
out_str = json.loads(in_str.replace("'", '"'))
print((out_str))
print(type(out_str))
for i in out_str:
    print(type(i))
