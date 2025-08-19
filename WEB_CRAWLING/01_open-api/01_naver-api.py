import urllib.request

# 애플리케이션 발급
client_id = "FIZvVi35nzEiqC5WxF_F"
client_secret = "KKE4m5V5Bw"

text = "AI"
# 인코딩
encText = urllib.parse.quote(text)

url = "https://openapi.naver.com/v1/search/blog.json?query=" + encText

request = urllib.request.Request(url)
# 헤더 세팅
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

# 응답상태 코드
print(response.getcode())

# 응답내용 디코딩
response_body = response.read()
print(response_body.decode('utf-8'))

