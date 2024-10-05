import requests
import json
import os

MEMOS_API_URL = os.environ['MEMOS_API_URL']

def fetch_memos():
    response = requests.get(MEMOS_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch memos. Status code: {response.status_code}")
        return None

def process_memos(memos):
    processed_memos = []
    for memo in memos:
        processed_memo = {
            "content": memo["content"],
            "created": memo["createdTs"],
            "updated": memo["updatedTs"],
            "id": memo["id"],
            "from": "Memos"
        }
        processed_memos.append(processed_memo)
    return processed_memos

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    memos = fetch_memos()
    if memos:
        processed_memos = process_memos(memos)
        filename = "memos.json"
        save_to_json(processed_memos, filename)
        print(f"Saved {len(processed_memos)} memos to {filename}")

if __name__ == "__main__":
    main()