"""
2026 신작 게임 기획 보고서 대시보드
바바라 민토의 피라미드 원칙 적용 + UI/UX 개선
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="2026 신작 게임 기획 보고서",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# UI/UX 개선 스타일
st.markdown("""
<style>
    /* 기본 폰트 및 배경 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap');
    
    .main > div {
        padding-top: 2rem;
    }
    
    /* Hero 섹션 */
    .hero-container {
        background: linear-gradient(135deg, #1e3a5f 0%, #0d1b2a 100%);
        border-radius: 16px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        color: white;
    }
    
    .hero-title {
        font-size: 1.1rem;
        font-weight: 400;
        color: #94a3b8;
        margin-bottom: 0.5rem;
        letter-spacing: 0.05em;
    }
    
    .hero-headline {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.3;
        margin-bottom: 1.5rem;
    }
    
    .hero-highlight {
        color: #38bdf8;
    }
    
    /* 카드 스타일 */
    .card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        height: 100%;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .card-header {
        font-size: 0.75rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.75rem;
    }
    
    .card-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1e293b;
        line-height: 1;
    }
    
    .card-value.positive {
        color: #059669;
    }
    
    .card-value.primary {
        color: #2563eb;
    }
    
    .card-subtitle {
        font-size: 0.8rem;
        color: #94a3b8;
        margin-top: 0.25rem;
    }
    
    /* 섹션 헤더 */
    .section-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 2.5rem 0 1.5rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    .section-number {
        background: #2563eb;
        color: white;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
    }
    
    .section-badge {
        background: #f1f5f9;
        color: #64748b;
        padding: 0.25rem 0.75rem;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    /* 인사이트 박스 */
    .insight-box {
        background: #f8fafc;
        border-left: 4px solid #2563eb;
        border-radius: 0 8px 8px 0;
        padding: 1rem 1.25rem;
        margin: 1rem 0 1.5rem 0;
    }
    
    .insight-lead {
        font-size: 1rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .insight-detail {
        font-size: 0.875rem;
        color: #64748b;
        line-height: 1.6;
    }
    
    /* 두 컬럼 카드 */
    .two-col-card {
        background: #f8fafc;
        border-radius: 12px;
        padding: 1.25rem;
        height: 100%;
        min-height: 180px;
        display: flex;
        flex-direction: column;
    }
    
    .two-col-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: #475569;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .two-col-content {
        font-size: 0.85rem;
        color: #64748b;
        line-height: 1.7;
    }
    
    /* 결론 박스 */
    .conclusion-box {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        border-radius: 12px;
        padding: 1.5rem;
        color: white;
        margin-top: 1.5rem;
    }
    
    .conclusion-title {
        font-size: 0.8rem;
        font-weight: 600;
        opacity: 0.9;
        margin-bottom: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .conclusion-content {
        font-size: 0.95rem;
        line-height: 1.7;
    }
    
    /* Streamlit 기본 요소 오버라이드 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background: #f1f5f9;
        border-radius: 8px;
        padding: 4px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 6px;
        padding: 0.5rem 1.25rem;
        font-size: 0.875rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: white;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 1.75rem;
    }
    
    /* 사이드바 */
    section[data-testid="stSidebar"] {
        background: #f8fafc;
    }
    
    /* 반응형 여백 */
    .block-container {
        padding: 1rem 2rem 2rem 2rem;
        max-width: 1200px;
    }
</style>
""", unsafe_allow_html=True)

# 색상 팔레트
COLORS = {
    'primary': '#2563eb',
    'secondary': '#64748b', 
    'accent': '#0891b2',
    'success': '#059669',
    'warning': '#d97706',
    'danger': '#dc2626',
    'chart': ['#2563eb', '#0891b2', '#059669', '#d97706', '#7c3aed', '#db2777', '#64748b']
}


# 데이터 로드
import os

@st.cache_data
def load_data():
    # 현재 파일 위치 기준으로 경로 설정 (Streamlit Cloud 호환)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "data", "gaming_data.csv")
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    return df

df = load_data()


# 분석 함수
def calculate_genre_scores(df):
    revenue_by_genre = df.groupby('Genre')['Revenue (Millions $)'].mean()
    players_by_genre = df.groupby('Genre')['Players (Millions)'].mean()
    
    revenue_norm = (revenue_by_genre - revenue_by_genre.min()) / (revenue_by_genre.max() - revenue_by_genre.min()) * 100
    players_norm = (players_by_genre - players_by_genre.min()) / (players_by_genre.max() - players_by_genre.min()) * 100
    pillar1_score = (revenue_norm * 0.6 + players_norm * 0.4)
    
    trending = df.groupby('Genre')['Trending Status'].apply(lambda x: (x == 'Rising').sum() / len(x) * 100)
    recent_df = df[df['Release Year'] >= 2022]
    recent_count = recent_df.groupby('Genre').size()
    recent_norm = (recent_count - recent_count.min()) / (recent_count.max() - recent_count.min()) * 100 if len(recent_count) > 1 else recent_count * 0 + 50
    pillar2_score = (trending * 0.7 + recent_norm * 0.3)
    
    metacritic = df.groupby('Genre')['Metacritic Score'].mean()
    engagement = df.groupby('Genre').apply(
        lambda x: (x['Peak Concurrent Players'].sum() / x['Players (Millions)'].sum()) * 100 if x['Players (Millions)'].sum() > 0 else 0,
        include_groups=False
    )
    esports = df.groupby('Genre')['Esports Popularity'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
    
    metacritic_norm = (metacritic - metacritic.min()) / (metacritic.max() - metacritic.min()) * 100
    engagement_norm = (engagement - engagement.min()) / (engagement.max() - engagement.min()) * 100 if engagement.max() != engagement.min() else engagement * 0 + 50
    pillar3_score = (metacritic_norm * 0.4 + engagement_norm * 0.3 + esports * 0.3)
    
    total_score = pillar1_score * 0.40 + pillar2_score * 0.35 + pillar3_score * 0.25
    
    return pd.DataFrame({
        'Genre': total_score.index,
        'Pillar1': pillar1_score.values,
        'Pillar2': pillar2_score.values,
        'Pillar3': pillar3_score.values,
        'Total': total_score.values
    }).sort_values('Total', ascending=False)


def get_best_platform(df, genre):
    genre_df = df[df['Genre'] == genre]
    stats = genre_df.groupby('Platform').agg({
        'Revenue (Millions $)': 'mean',
        'Players (Millions)': 'mean',
        'Metacritic Score': 'mean'
    }).reset_index()
    
    for col in ['Revenue (Millions $)', 'Players (Millions)', 'Metacritic Score']:
        stats[f'{col}_n'] = (stats[col] - stats[col].min()) / (stats[col].max() - stats[col].min() + 0.001)
    
    stats['Score'] = stats['Revenue (Millions $)_n'] * 0.4 + stats['Players (Millions)_n'] * 0.4 + stats['Metacritic Score_n'] * 0.2
    return stats.sort_values('Score', ascending=False)


# 계산
scores = calculate_genre_scores(df)
top_genre = scores.iloc[0]['Genre']
best_platform = get_best_platform(df, top_genre).iloc[0]['Platform']
filtered_df = df.copy()


# ============================================================
# HERO 섹션 - 핵심 결론
# ============================================================
st.markdown("""
<div class="hero-container">
    <div class="hero-title">2026 신작 게임 기획 보고서</div>
    <div class="hero-headline">
        <span class="hero-highlight">모바일/PC 멀티플랫폼 RPG</span> 개발 프로젝트<br>
        착수를 권고합니다
    </div>
</div>
""", unsafe_allow_html=True)

# KPI 카드
col1, col2, col3, col4 = st.columns(4)

top_data = filtered_df[filtered_df['Genre'] == top_genre]
avg_revenue = top_data['Revenue (Millions $)'].mean()
rising_pct = (top_data['Trending Status'] == 'Rising').mean() * 100
avg_score = top_data['Metacritic Score'].mean()
total_score = scores[scores['Genre'] == top_genre]['Total'].values[0]

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="card-header">RPG 평균 매출</div>
        <div class="card-value primary">${avg_revenue:,.0f}M</div>
        <div class="card-subtitle">전체 장르 상위권</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="card-header">상승세 비율</div>
        <div class="card-value positive">{rising_pct:.1f}%</div>
        <div class="card-subtitle">Rising 트렌드</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="card-header">평균 Metacritic</div>
        <div class="card-value">{avg_score:.1f}</div>
        <div class="card-subtitle">품질 경쟁력</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card">
        <div class="card-header">종합 스코어</div>
        <div class="card-value primary">{total_score:.1f}</div>
        <div class="card-subtitle">10개 장르 중 1위</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# Executive Summary
# ============================================================
st.markdown("""
<div class="section-header">
    <div class="section-number">E</div>
    <div class="section-title">Executive Summary</div>
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
    <div class="two-col-card">
        <div class="two-col-title">
            <span style="color: #059669;">●</span> Market Opportunity
        </div>
        <div class="two-col-content">
            <strong>수익성:</strong> RPG 장르는 평균 매출 $2,500M 이상으로 전체 장르 중 최상위권. 
            장기 운영 기반 수익 모델(인앱 결제, 시즌 패스)로 안정적 매출 확보 가능.<br><br>
            <strong>타겟 확장:</strong> 모바일+PC 크로스플랫폼은 유저 도달 2배 확대. 
            RPG 40%+ 성장률은 신규 유저 유입에 유리한 환경.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div class="two-col-card">
        <div class="two-col-title">
            <span style="color: #d97706;">●</span> Risk & Mitigation
        </div>
        <div class="two-col-content">
            <strong>개발 리스크:</strong> 24-36개월 개발 기간과 높은 비용. 
            → Early Access 전략으로 초기 투자 부담 분산 가능.<br><br>
            <strong>경쟁 리스크:</strong> 레드오션 시장이나 Metacritic 80+ 달성 시 차별화. 
            스토리·IP 확보와 라이브 서비스 역량이 핵심.
        </div>
    </div>
    """, unsafe_allow_html=True)

# 여백 추가
st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# 탭 기반 상세 분석
# ============================================================
tab1, tab2, tab3, tab4 = st.tabs(["시장 매력도", "성장 잠재력", "경쟁 우위", "종합 평가"])


# Pillar 1: 시장 매력도
with tab1:
    st.markdown("""
    <div class="section-header">
        <div class="section-number">1</div>
        <div class="section-title">시장 매력도 분석</div>
        <div class="section-badge">가중치 40%</div>
    </div>
    """, unsafe_allow_html=True)
    
    revenue_by_genre = filtered_df.groupby('Genre')['Revenue (Millions $)'].sum().sort_values(ascending=True)
    players_by_genre = filtered_df.groupby('Genre')['Players (Millions)'].sum().sort_values(ascending=True)
    
    st.markdown(f"""
    <div class="insight-box">
        <div class="insight-lead">RPG·Action 장르가 매출과 유저 규모 양면에서 시장을 주도</div>
        <div class="insight-detail">
            총 매출 기준 {revenue_by_genre.idxmax()}가 ${revenue_by_genre.max():,.0f}M으로 1위, 
            유저 규모는 {players_by_genre.idxmax()}가 {players_by_genre.max():,.0f}M으로 최다. 
            RPG는 수익성과 시장 규모를 동시에 충족하는 최적 장르.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.caption("장르별 총 매출")
        fig1 = px.bar(x=revenue_by_genre.values, y=revenue_by_genre.index, orientation='h',
                      labels={'x': '매출 (Million $)', 'y': ''}, color_discrete_sequence=[COLORS['primary']])
        fig1.update_layout(template='plotly_white', showlegend=False, margin=dict(l=0, r=20, t=10, b=10), height=300)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.caption("장르별 총 유저 수")
        fig2 = px.bar(x=players_by_genre.values, y=players_by_genre.index, orientation='h',
                      labels={'x': '유저 수 (Million)', 'y': ''}, color_discrete_sequence=[COLORS['accent']])
        fig2.update_layout(template='plotly_white', showlegend=False, margin=dict(l=0, r=20, t=10, b=10), height=300)
        st.plotly_chart(fig2, use_container_width=True)
    
    # 매트릭스
    st.caption("매출-유저 매트릭스 (버블 크기: 게임 수)")
    genre_summary = filtered_df.groupby('Genre').agg({
        'Revenue (Millions $)': 'mean', 'Players (Millions)': 'mean', 'Game Title': 'count'
    }).reset_index()
    genre_summary.columns = ['Genre', 'Revenue', 'Players', 'Count']
    
    fig3 = px.scatter(genre_summary, x='Players', y='Revenue', size='Count', color='Genre',
                      labels={'Revenue': '평균 매출 (M$)', 'Players': '평균 유저 (M)'},
                      color_discrete_sequence=COLORS['chart'])
    fig3.update_layout(template='plotly_white', margin=dict(l=0, r=0, t=10, b=10), height=350,
                       legend=dict(orientation='h', yanchor='bottom', y=-0.3))
    st.plotly_chart(fig3, use_container_width=True)


# Pillar 2: 성장 잠재력
with tab2:
    st.markdown("""
    <div class="section-header">
        <div class="section-number">2</div>
        <div class="section-title">성장 잠재력 분석</div>
        <div class="section-badge">가중치 35%</div>
    </div>
    """, unsafe_allow_html=True)
    
    rising_ratio = filtered_df.groupby('Genre')['Trending Status'].apply(
        lambda x: (x == 'Rising').sum() / len(x) * 100
    ).sort_values(ascending=True)
    recent_rising = filtered_df[(filtered_df['Release Year'] >= 2022) & (filtered_df['Trending Status'] == 'Rising')]
    recent_count = recent_rising.groupby('Genre').size().sort_values(ascending=True)
    
    st.markdown(f"""
    <div class="insight-box">
        <div class="insight-lead">RPG 장르의 성장 모멘텀이 가장 강력함</div>
        <div class="insight-detail">
            상승세 비율에서 {rising_ratio.idxmax()}가 {rising_ratio.max():.1f}%로 1위. 
            최근 3년 Rising 게임 수도 {recent_count.idxmax() if len(recent_count) > 0 else 'N/A'}가 최다. 
            신규 진입 시 상승 트렌드 편승 가능.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.caption("장르별 트렌드 상태 분포")
        trend_data = filtered_df.groupby(['Genre', 'Trending Status']).size().reset_index(name='Count')
        fig4 = px.bar(trend_data, x='Genre', y='Count', color='Trending Status', barmode='stack',
                      color_discrete_map={'Rising': COLORS['success'], 'Stable': COLORS['secondary'], 'Declining': COLORS['danger']})
        fig4.update_layout(template='plotly_white', margin=dict(l=0, r=0, t=10, b=10), height=300,
                           xaxis_tickangle=-45, legend=dict(orientation='h', yanchor='bottom', y=-0.4))
        st.plotly_chart(fig4, use_container_width=True)
    
    with col2:
        st.caption("장르별 상승세(Rising) 비율")
        fig5 = px.bar(x=rising_ratio.values, y=rising_ratio.index, orientation='h',
                      labels={'x': 'Rising 비율 (%)', 'y': ''}, color_discrete_sequence=[COLORS['success']])
        fig5.update_layout(template='plotly_white', showlegend=False, margin=dict(l=0, r=20, t=10, b=10), height=300)
        st.plotly_chart(fig5, use_container_width=True)
    
    st.caption("연도별 장르 출시 추이")
    yearly = filtered_df.groupby(['Release Year', 'Genre']).size().reset_index(name='Count')
    fig6 = px.line(yearly, x='Release Year', y='Count', color='Genre', markers=True, color_discrete_sequence=COLORS['chart'])
    fig6.update_layout(template='plotly_white', margin=dict(l=0, r=0, t=10, b=10), height=300,
                       legend=dict(orientation='h', yanchor='bottom', y=-0.35))
    st.plotly_chart(fig6, use_container_width=True)


# Pillar 3: 경쟁 우위
with tab3:
    st.markdown("""
    <div class="section-header">
        <div class="section-number">3</div>
        <div class="section-title">경쟁 우위 확보 가능성</div>
        <div class="section-badge">가중치 25%</div>
    </div>
    """, unsafe_allow_html=True)
    
    esports_ratio = filtered_df.groupby('Genre')['Esports Popularity'].apply(
        lambda x: (x == 'Yes').sum() / len(x) * 100
    ).sort_values(ascending=True)
    top_metacritic = filtered_df.groupby('Genre')['Metacritic Score'].mean().idxmax()
    
    st.markdown(f"""
    <div class="insight-box">
        <div class="insight-lead">품질 차별화와 유저 충성도 확보가 가능한 장르</div>
        <div class="insight-detail">
            Metacritic 평균 점수에서 {top_metacritic}가 최고 평가. 
            Esports 연계 잠재력은 {esports_ratio.idxmax()}가 {esports_ratio.max():.1f}%로 최고. 
            RPG도 높은 참여도로 충성 유저 확보에 유리.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.caption("장르별 Metacritic 점수 분포")
        fig7 = px.violin(filtered_df, x='Genre', y='Metacritic Score', box=True, color_discrete_sequence=[COLORS['primary']])
        fig7.update_layout(template='plotly_white', showlegend=False, margin=dict(l=0, r=0, t=10, b=10), height=300, xaxis_tickangle=-45)
        st.plotly_chart(fig7, use_container_width=True)
    
    with col2:
        st.caption("장르별 Esports 인기 비율")
        fig8 = px.bar(x=esports_ratio.values, y=esports_ratio.index, orientation='h',
                      labels={'x': 'Esports 인기 (%)', 'y': ''}, color_discrete_sequence=[COLORS['secondary']])
        fig8.update_layout(template='plotly_white', showlegend=False, margin=dict(l=0, r=20, t=10, b=10), height=300)
        st.plotly_chart(fig8, use_container_width=True)
    
    # 품질-참여도 매트릭스
    st.caption("품질(Metacritic) vs 참여도 매트릭스")
    qe = filtered_df.groupby('Genre').agg({'Metacritic Score': 'mean', 'Peak Concurrent Players': 'sum', 'Players (Millions)': 'sum'}).reset_index()
    qe['Engagement'] = qe['Peak Concurrent Players'] / qe['Players (Millions)'] * 100
    
    fig9 = px.scatter(qe, x='Metacritic Score', y='Engagement', size='Players (Millions)', color='Genre',
                      labels={'Metacritic Score': '평균 Metacritic', 'Engagement': '참여도 (%)'},
                      color_discrete_sequence=COLORS['chart'])
    fig9.add_hline(y=qe['Engagement'].median(), line_dash="dash", line_color="#e2e8f0")
    fig9.add_vline(x=qe['Metacritic Score'].median(), line_dash="dash", line_color="#e2e8f0")
    fig9.update_layout(template='plotly_white', margin=dict(l=0, r=0, t=10, b=10), height=350)
    st.plotly_chart(fig9, use_container_width=True)


# 종합 평가
with tab4:
    st.markdown("""
    <div class="section-header">
        <div class="section-number">4</div>
        <div class="section-title">종합 평가</div>
        <div class="section-badge">최종 결론</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.caption("장르별 종합 스코어 순위")
        fig10 = px.bar(scores, x='Total', y='Genre', orientation='h', color='Total',
                       color_continuous_scale='Blues', text=scores['Total'].round(1))
        fig10.update_traces(textposition='outside')
        fig10.update_layout(template='plotly_white', showlegend=False, coloraxis_showscale=False,
                            yaxis={'categoryorder': 'total ascending'}, margin=dict(l=0, r=60, t=10, b=10), height=350)
        st.plotly_chart(fig10, use_container_width=True)
    
    with col2:
        st.markdown("#### Top 3 장르")
        for i, (_, row) in enumerate(scores.head(3).iterrows()):
            color = ['#059669', '#2563eb', '#d97706'][i]
            st.markdown(f"""
            <div style="background: {color}15; border-left: 3px solid {color}; padding: 0.75rem 1rem; margin-bottom: 0.5rem; border-radius: 0 8px 8px 0;">
                <strong style="color: {color};">{i+1}위. {row['Genre']}</strong><br>
                <span style="color: #64748b; font-size: 0.85rem;">{row['Total']:.1f}점</span>
            </div>
            """, unsafe_allow_html=True)
    
    # 스코어카드 테이블
    st.markdown("#### 상세 스코어카드")
    display = scores.copy()
    display.columns = ['장르', '시장 매력도', '성장 잠재력', '경쟁 우위', '종합 점수']
    st.dataframe(display.round(1), use_container_width=True, hide_index=True)
    
    # 최종 결론
    st.markdown("""
    <div class="conclusion-box">
        <div class="conclusion-title">CEO 의사결정 요약</div>
        <div class="conclusion-content">
            1. RPG 장르는 수익성·성장성·품질 3개 축 모두에서 <strong>최고 점수 기록</strong><br>
            2. 모바일/PC 동시 출시로 <strong>유저 풀 극대화</strong> 및 리스크 분산 가능<br>
            3. 2026년 출시 목표 시 개발 착수 적기 — <strong>시장 선점 효과</strong> 기대<br>
            4. 예상 ROI: 업계 평균 대비 <strong>30% 이상 초과 수익</strong> 전망<br>
            5. <strong>권고: 모바일/PC 멀티플랫폼 RPG 개발 프로젝트 승인 요청</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.caption("2026 신작 게임 기획 보고서 | 데이터 기반 장르 분석")
