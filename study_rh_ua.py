from requests_html import HTMLSession

session = HTMLSession()

r = session.get("https://www.cloudgate.jp/ua.php")
print(r.html.text)
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8
# デフォルトで設定されているUA

# HTMLSessionがrequestsの子クラスなので、requestsと同様の指定方法でUAを指定可能
headers = {'User-Agent':'test'}
r = session.get("https://www.cloudgate.jp/ua.php",headers=headers)
print(r.html.text)
