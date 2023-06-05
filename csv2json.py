# 读取origal_data.txt
import json

if __name__ == '__main__':
    with open("data/comment_pass_data.txt", "r") as f:
        data = []
        for line in f:
            obj = {
                "instruction": line.strip("\n"),
                "input": "",
                "output": "no"
            }
            data.append(obj)
    with open("data/comment_pass_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
