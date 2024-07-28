import requests

def chat_gpt_api(prompt):
    url = "https://open-api.jejucodingcamp.workers.dev/"

    data = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"

def print_result(step, prompt, response):
    print(f"\n--- 단계 {step} ---")
    print(f"프롬프트:\n{prompt}")
    print(f"\n응답:\n{response}")
    print("-" * 50)
    
def run_prompt_engineering_example(step=None):
    
    
    #단계 1 : 초기 프롬프트
    if step == 1:
        initial_prompt = "건강한 생활습관 대해서 설명해주세요."
        response1 = chat_gpt_api(initial_prompt)
        print_result(1,initial_prompt,response1)

    # 단계 2: 반복적 개선
    if step == 2:
        improved_prompt = """
        일상생활에서 실천할 수 있는 건강한 습관 5가지를 설명해주세요.
        각 습관에 대해 그 중요성과 실천 방법을 포함해주세요.
        """
        response2 = chat_gpt_api(improved_prompt)
        print_result(2, improved_prompt, response2)

    # 단계 3: 단계별 지시 추가
    if step == 3:
        step_by_step_prompt = """
        건강한 생활 습관 가이드를 작성해주세요. 다음 단계를 따라주세요:
        1. 건강한 식습관 2가지를 설명하세요.
        2. 규칙적인 운동의 중요성과 간단한 운동 루틴을 제안하세요.
        3. 충분한 수면의 이점과 좋은 수면 습관을 설명하세요.
        4. 스트레스 관리를 위한 기술 2가지를 제안하세요.
        5. 이러한 습관들이 전반적인 건강에 미치는 영향을 요약하세요.
        """
        response3 = chat_gpt_api(step_by_step_prompt)
        print_result(3, step_by_step_prompt, response3)

    # 단계 4: 예시 제공
    if step == 4:
        example_prompt = """
        건강한 생활 습관 가이드를 작성해주세요. 각 항목을 다음 형식으로 작성해주세요:
        습관: [습관 이름]
        중요성: [1-2문장 설명]
        실천 방법: [구체적인 실천 방법 2-3가지]

        예시:
        습관: 충분한 수분 섭취
        중요성: 수분은 체내 대사와 체온 조절에 필수적입니다. 적절한 수분 섭취는 피부 건강과 집중력 향상에도 도움을 줍니다.
        실천 방법:
        - 매일 아침 기상 직후 물 한 잔 마시기
        - 식사 때마다 물 한 잔씩 곁들이기
        - 운동 전후로 충분한 수분 보충하기

        위 예시와 같은 형식으로 총 4가지 건강한 생활 습관을 설명해주세요.
        """
        response4 = chat_gpt_api(example_prompt)
        print_result(4, example_prompt, response4)

    # 단계 5: 제약 조건 설정
    if step == 5:
        
        constrained_prompt = """
        건강한 생활 습관 가이드를 작성해주세요. 각 항목을 다음 형식으로 작성해주세요:
        습관: [습관 이름]
        중요성: [1-2문장 설명]
        실천 방법: [구체적인 실천 방법 2-3가지]

        예시:
        습관: 충분한 수분 섭취
        중요성: 수분은 체내 대사와 체온 조절에 필수적입니다. 적절한 수분 섭취는 피부 건강과 집중력 향상에도 도움을 줍니다.
        실천 방법:
        - 매일 아침 기상 직후 물 한 잔 마시기
        - 식사 때마다 물 한 잔씩 곁들이기
        - 운동 전후로 충분한 수분 보충하기

        위 예시와 같은 형식으로 총 4가지 건강한 생활 습관을 설명해주세요.
        
        앞서 설명한 건강한 생활 습관 가이드를 바탕으로, 바쁜 직장인을 위한 버전을 만들어주세요. 다음 조건을 반드시 지켜주세요:
        - 각 습관은 하루 15분 이내로 실천할 수 있어야 합니다.
        - 특별한 장비나 시설이 필요 없는 방법만 포함해주세요.
        - 과학적 근거를 바탕으로 한 조언만 제공해주세요.
        - 특정 제품이나 브랜드를 언급하지 마세요.
        총 3가지 습관을 위 조건에 맞춰 설명해주세요.
        """
        response5 = chat_gpt_api(constrained_prompt)
        print_result(5, constrained_prompt, response5)
    
def main():
    print("이 프로그램은 여행지를 추천해주는 서비스입니다. (종료를 원하시면 q를 입력해 주세요)")
    
    while True:
        user_input = input("실행할 단계를 선택해주세요 (1~5)  만약에 전부다 수행하고 싶으면 all을 입력해주세요 : ")
        
        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        
        if user_input.lower() == 'all':
            run_prompt_engineering_example() # 모든 것을 출력!
        elif user_input in ['1','2','3','4','5']:
            step = int(user_input)
            run_prompt_engineering_example(step)
        else:
            print("잘못된 입력입니다. 1~5 사이의 숫자나 all을 입력해주세요.")
        
if __name__ == "__main__":
    main()