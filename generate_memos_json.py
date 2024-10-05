import requests
import json
import os
import re

MEMOS_API_URL = os.environ['MEMOS_API_URL']

def fetch_memos():
    response = requests.get(MEMOS_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch memos. Status code: {response.status_code}")
        return None

def extract_images(content):
    image_pattern = r'!\[.*?\]\((.*?)\)'
    return re.findall(image_pattern, content)

def process_memos(memos):
    processed_memos = []
    for memo in memos:
        content = memo.get("content", "")
        images = extract_images(content)
        
        processed_memo = {
            "id": memo.get("id"),
            "content": content,
            "createdTs": memo.get("createdTs"),
            "updatedTs": memo.get("updatedTs"),
            "rowStatus": memo.get("rowStatus", "NORMAL"),  # 默认值
            "creatorId": memo.get("creatorId"),
            "title": memo.get("title", ""),  # 可选字段
            "tags": memo.get("tags", []),  # 标签字段
            "url": memo.get("url", ""),  # 原链接字段
            "images": images,
            "resourceList": memo.get("resourceList", []),
            "visibility": memo.get("visibility", "PRIVATE"),
            "pinned": memo.get("pinned", False),
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