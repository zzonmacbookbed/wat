import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.instagram.com/1_j27p/"
# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["white", "purple"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "제민국")
write("description", "곧 입시")
write("button", "인스타")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "학교": "",
  "ID": "1_j27p",
  "취미": "코딩",
  "그만": "물어"
}
information(informations)
