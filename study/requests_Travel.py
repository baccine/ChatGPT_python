import requests

def chat_gpt_api(user_input):
    url = "https://open-api.jejucodingcamp.workers.dev/"
    
    data = [
        {"role": "system", "content": "assistant는 세계 주요 도시의 관광 정보를 제공하는 여행 전문가입니다."},
        {"role": "user", "content" : user_input}
    ]
    
    headers = {
        "Content-Type" : "application/json"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"
    
def main():
    print("ChatGPT API를 사용한 세계 주요 도시 관광 정보 제공(종료하려면 'q'를 입력하세요)")
    
    while True:
        user_input = input("도시 이름을 입력하세요: ")
        
        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        
        prompt = f"""
        {user_input}에 대한 관광 정보를 다음 형식으로 제공해주세요:
        
        도시명 : {user_input}
        국가: [국가 이름]
        주요 관광지 3곳:
        1. [관광지 이름]
           - 설명: [2-3문장으로 관광지에 대한 설명과 주요 활동]
        2. [관광지 이름]
           - 설명: [2-3문장으로 관광지에 대한 설명과 주요 활동]
        3. [관광지 이름]
           - 설명: [2-3문장으로 관광지에 대한 설명과 주요 활동]
        현지 음식 추천: [대표적인 현지 음식과 간단한 설명]
        교통 팁: [대중교통 이용에 관한 팁과 주의사항]
        예산 고려사항: [중간 수준 예산으로 여행할 때의 조언]
        """
        
        response = chat_gpt_api(prompt)
        print(f"답변:\n{response}\n")
        
if __name__ == "__main__":
    main()