# Chap04/facebook_my_profile.py
import os
import json
import facebook

if __name__ == '__main__':
    token = os.environ.get('FACEBOOK_TEMP_TOKEN')

    graph = facebook.GraphAPI(token)
    profile = graph.get_object("me", fields='name,location{general_info,location},languages{name,description}')

    print(json.dumps(profile, indent=4))
