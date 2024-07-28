import requests

def chat_gpt_api(user_input):
    #API 엔드포인트 URL
    url = "https://open-api.jejucodingcamp.workers.dev/"
    
    #API 요청에 사용 될 데이터
    data = [
        {"role": "system", "content": "assistant는 점심 메뉴를 추천해주는 요리사입니다."},
        {"role": "user", "content": user_input}
    ]
    # HTTP 요청 헤더
    headers = {
        "Content-Type": "application/json"
    }
    # POST 요청 보내기
    response = requests.post(url, json=data, headers=headers)
    #응답 처리
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

        
def main():
    print("ChatGPT API를 사용한 점심 메뉴 추천 (종료하려면 'q'를 입력하세요)")
    
    while True:
        user_input = input("질문을 입력하세요: ")
        
        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        
        response = chat_gpt_api(user_input)
        print(f"답변: {response}\n")

if __name__ == "__main__":
    main()