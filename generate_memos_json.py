import requests
import json

api_url = 'https://i.hux.ink:5233/api/memo?creatorId=1&rowStatus=NORMAL&limit=100'  # 修改为你的API URL

def fetch_memos():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()

        # 提取所需字段
        memos = [{
            'id': memo.get('id'),
            'content': memo.get('content'),
            'createdTs': memo.get('createdTs'),
            'updatedTs': memo.get('updatedTs'),
            'rowStatus': memo.get('rowStatus'),
            'images': memo.get('images', []),  # 假设images字段存在
            'creatorId': memo.get('creatorId', None),  # 可选字段
            'title': memo.get('title', ''),  # 可选字段
            'tags': memo.get('tags', []),  # 添加tags字段
            'url': memo.get('url', '')  # 添加原链接字段
        } for memo in data]

        # 保存为JSON文件
        with open('memos.json', 'w', encoding='utf-8') as f:
            json.dump(memos, f, ensure_ascii=False, indent=2)
        print('Memos saved to memos.json')
    except Exception as e:
        print(f'Error fetching memos: {e}')

if __name__ == '__main__':
    fetch_memos()