# __Auth__  : @GitBlackSir
# __Date__  : 2018/5/3
# __Email__ : gitblacksir@gmail.com

import requests
# def get_status(url):
#     try:
#         r = requests.get(url, allow_redirects=False)
#         return r.status_code
#     except:
#         return False
#
#
# def is_value_url(URL):
#     status = get_status(URL)
#     if status == 200:
#         return True
#     else:
#         return False
def is_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)