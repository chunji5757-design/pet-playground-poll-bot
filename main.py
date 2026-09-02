import os
import requests
from datetime import datetime

def send_kakao_message():
    """카카오톡에 메시지 발송"""
    
    # GitHub Secrets에서 API 키 가져오기
    api_key = os.getenv('KAKAO_API_KEY')
    
    if not api_key:
        print("❌ 오류: KAKAO_API_KEY가 설정되지 않았습니다")
        return
    
    # 카카오톡 메시지 API 엔드포인트
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    
    # 메시지 내용
    message_text = f"""
🐾 반려동물 놀이터 일일 투표 🐾

오늘은 어떤 투표일까요?
지금 바로 참여해주세요!

생성 시간: {datetime.now().strftime('%Y년 %m월 %d일 %H:%M:%S')}
    """.strip()
    
    # 요청 헤더
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # 요청 본문
    data = {
        "template_object": {
            "object_type": "text",
            "text": message_text,
            "link": {
                "web_url": "https://open.kakao.com"
            }
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            print("✅ 카카오톡 메시지 발송 성공!")
            print(f"시간: {datetime.now()}")
        else:
            print(f"❌ 오류 발생: {response.status_code}")
            print(f"응답: {response.text}")
    
    except Exception as e:
        print(f"❌ 네트워크 오류: {str(e)}")

if __name__ == "__main__":
    send_kakao_message()
