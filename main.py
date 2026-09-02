import os
from datetime import datetime

def create_daily_poll():
    """매일 실행될 함수"""
    print(f"✅ 투표 생성됨: {datetime.now()}")
    
    # 나중에 카카오톡 메시지 API를 여기 추가할 예정
    # 지금은 실행만 확인하는 단계

if __name__ == "__main__":
    create_daily_poll()
