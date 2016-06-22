# Chap01/demo_json.py
import json

if __name__ == '__main__':
    user_json = '{"user_id": "1", "name": "Marco"}'
    user_data = json.loads(user_json)
    print(user_data['name'])
    # Output: Marco

    user_data['likes'] = ['Python', 'Data Mining']
    user_json = json.dumps(user_data, indent=4)
    print(user_json)
    """
    Output: 
    {
        "user_id": "1",
        "name": "Marco",
        "likes": [
            "Python",
            "Data Mining"
        ]
    }
    """
