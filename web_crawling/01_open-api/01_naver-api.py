import urllib.request

# API KEY 설정
client_id = "vPn2yQZIJXeRMIXoJ7Ap"
client_secret = "jCXg4fxXUo"

# 검색어 설정 (인코딩)
text = "AI"
encText = urllib.parse.quote(text)

# url 및 헤더 설정
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText

# api 요청 및 결과값 json 반환
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

print(response.getcode())               # 응답상태 코드

response_body = response.read()         # 응답내용
print(response_body.decode('utf-8'))
