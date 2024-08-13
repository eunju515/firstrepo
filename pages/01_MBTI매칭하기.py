import streamlit as st

# 제목 설정
st.title('MBTI 특성 분석 및 추천 서비스')

# 이름 입력 받기
name = st.text_input('이름을 입력해주세요!')

# MBTI 유형 입력 받기
mbti = st.text_input('당신의 MBTI 유형을 입력해주세요! (예: INFP, ESTJ)')

# MBTI 특성 사전
mbti_traits = {
    'INFP': ('이상적이고 공감력이 뛰어나며, 깊은 내면의 가치를 중요시합니다. 종종 혼자만의 시간을 가지며 내면을 탐구합니다.', 'ENFJ', 'ESTJ'),
    'ESTJ': ('실용적이고 논리적이며, 조직적이고 계획적입니다. 명확한 규칙과 구조를 선호하며, 일을 효율적으로 처리합니다.', 'ISFP', 'INFP'),
    'ENFJ': ('따뜻하고 외향적이며, 타인에 대한 관심이 많습니다. 리더십을 발휘하며 타인을 돕는 데 기쁨을 느낍니다.', 'INFP', 'ISTP'),
    'ISTP': ('실용적이고 논리적이며, 독립적이고 유연합니다. 문제 해결 능력이 뛰어나고, 실용적인 활동을 즐깁니다.', 'ESTP', 'ENFJ'),
    # 여기에 다른 MBTI 유형에 대한 특성 추가 가능
}

# 특성 분석 및 추천 결과 출력
if st.button('결과 보기'):
    if mbti in mbti_traits:
        trait, best_match, worst_match = mbti_traits[mbti]
        st.write(f"{name}님! 당신은 {mbti} 유형이군요. {trait}")
        st.write(f"가장 잘 맞는 MBTI 유형: {best_match}")
        st.write(f"가장 맞지 않는 MBTI 유형: {worst_match}")
    else:
        st.write("유효한 MBTI 유형을 입력해주세요.")
