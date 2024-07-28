import requests

def chat_gpt_api(user_input):
    url = "https://open-api.jejucodingcamp.workers.dev/"
    
    data = [
        {"role": "system", "content": "assistant 세계적인 기술 연구 기관의 수석 미래 학자입니다."},
        {"role": "user", "content": user_input}
    ]
    
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'],[0],['message'],['content']
    else:
        return f"Error: {response.status_code}, {response.text}"
    
def main():
    print("향후 10년(2024-2034) 동안의 주요 기술 트렌드에 대한 분석 보고서를 작성해 드립니다.\n(종료할려면 'q'를 입력하세요.)")
    
    while True:
        user_input = input("관심 있는 기술 트렌드를 입력하세요: ")
        
        if user_input.lower() == 'q':
            print("프로그램을 종료하세요.")
            break
        
        prompt = f"""
        {user_input}에 대한 트렌드 정보를 다음 형식으로 제공해주세요:
        트렌드명: {user_input}
        """
        
        response = chat_gpt_api(prompt)
        print(f"답변:\n{response}\n")
        
if __name__ == "__main__":
    main()