import urllib
import urllib2

email = "facebook email"
passw = "facebook pass"

home_url = "http://facebook.com"
login_url = "https://www.facebook.com/login.php?login_attempt=1"
video_page_url = "http://www.facebook.com/video/video.php?v=1636906955426"#"http://www.facebook.com/video/video.php?v=150195341703457"

send_data = None
headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3"}
client_host = "127.0.0.1"

o = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(o);

request = urllib2.Request(home_url, send_data, headers, client_host)
response = urllib2.urlopen(request)
home_content = response.read()
start = home_content.find("lsd")+12
finish = start+5
lsd = home_content[start:finish]

send_data = {"charset_test":"&euro;,&acute;,€,´,水,Д,Є",
             "lsd":lsd, "locale":"en_US", "email":email,
             "pass":passw, "persistent":"1", "default_persistent":"0"}
send_data = urllib.urlencode(send_data)

request = urllib2.Request(login_url, send_data, headers, client_host)
response = urllib2.urlopen(request)

# get source
request = urllib2.Request(video_page_url, None, headers, client_host)
response = urllib2.urlopen(request)
video_page_source = response.read()

# parse url
start_key = "\"video_src\","
finish_key = "\");"
start = video_page_source.find(start_key) + 14
finish = video_page_source.find(finish_key, start+2)
encoded_url = video_page_source[start:finish]

url = r'' + encoded_url
url = url.replace("\\","")
url = url.replace("u00253A",":")
url = url.replace("u00252F","/")
url = url.replace("u00253F","?")
url = url.replace("u00253D","=")
url = url.replace("u002526","&")

print 'url='+url
