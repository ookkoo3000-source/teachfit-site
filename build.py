# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

FONT_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap">'

NAV_ITEMS = [
    ("index.html", "홈"),
    ("services.html", "서비스"),
    ("process.html", "매칭 방식"),
    ("teachers.html", "선생님"),
    ("regions.html", "지역별 과외"),
    ("blog.html", "블로그"),
]

def head(title, desc, path_prefix, canonical, noindex=False):
    robots_tag = '<meta name="robots" content="noindex,nofollow">\n' if noindex else ''
    return '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{robots}{font}
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
'''.format(title=title, desc=desc, canonical=canonical, font=FONT_LINK, p=path_prefix, robots=robots_tag)

def topbar():
    return '''<div class="topbar">
  <div class="wrap">
    <span>선생님과 학생의 학습 궁합, 데이터로 맞춰드립니다</span>
    <a class="phone" href="tel:01031315305">\U0001F4DE 010-3131-5305 (09:00–21:00)</a>
  </div>
</div>
'''

def header(path_prefix, active):
    links = []
    mlinks = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active else ''
        links.append('<a href="{p}{href}"{cur}>{label}</a>'.format(p=path_prefix, href=href, cur=cur, label=label))
        mlinks.append('<a href="{p}{href}"{cur}>{label}</a>'.format(p=path_prefix, href=href, cur=cur, label=label))
    return '''<header class="site">
  <div class="wrap">
    <a class="logo" href="{p}index.html"><span class="mark">TF</span>티치핏</a>
    <div class="navwrap">
      <nav class="main">
        {links}
      </nav>
      <a class="cta-btn" href="{p}apply.html">무료 상담 신청</a>
      <button class="menu-btn" aria-label="메뉴">☰</button>
    </div>
  </div>
  <div class="wrap mobile-nav">
    {mlinks}
    <a href="{p}apply.html">무료 상담 신청</a>
  </div>
</header>
'''.format(p=path_prefix, links='\n        '.join(links), mlinks='\n    '.join(mlinks))

def footer(path_prefix):
    return '''<footer>
  <div class="wrap">
    <div>
      <a class="logo" href="{p}index.html" style="margin-bottom:10px;"><span class="mark">TF</span>티치핏</a>
      <div class="fnav">
        <a href="{p}services.html">서비스</a><a href="{p}process.html">매칭 방식</a><a href="{p}teachers.html">선생님</a><a href="{p}regions.html">지역별 과외</a><a href="{p}blog.html">블로그</a>
      </div>
      <p class="disclaimer">전화 010-3131-5305 · 운영시간 09:00–21:00 · 상담 및 매칭 신청은 무료이며, 실제 수업 진행 여부와 비용은 상담 후 안내해 드립니다. 사업자 정보는 확정 후 별도 고지 예정입니다.</p>
    </div>
  </div>
</footer>
<script src="{p}assets/site.js"></script>
</body>
</html>
'''.format(p=path_prefix)

def page(filename, title, desc, active, body, path_prefix="", canonical="", noindex=False):
    full = head(title, desc, path_prefix, canonical, noindex) + topbar() + header(path_prefix, active) + '<main class="wrap">\n' + body + '\n</main>\n' + footer(path_prefix)
    out_path = os.path.join(ROOT, filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full)
    print("wrote", filename)

BASE_URL = "https://teachfit.example"  # placeholder domain, update once real domain is registered

# ---------------------------------------------------------------
# Region / school data (real school names, seeded 2026-09-18)
# ---------------------------------------------------------------
REGIONS = [
    {
        "key": "gangnam",
        "name": "서울 강남구",
        "blurb": "대치·역삼·도곡 학군 중심 내신 관리 수요가 높은 지역이에요.",
        "schools": [
            {"name": "대치중학교", "slug": "daechi-gangnam", "note": "대치동 학원가 인접, 내신 경쟁이 치열한 학교"},
            {"name": "역삼중학교", "slug": "yeoksam-gangnam", "note": "강남구 역삼동, 국영수 균형 학습이 필요한 학교"},
            {"name": "도곡중학교", "slug": "dogok-gangnam", "note": "도곡동, 특목고 진학 준비 학생이 많은 학교"},
        ],
    },
    {
        "key": "songpa",
        "name": "서울 송파구",
        "blurb": "잠실·문정·방이 생활권으로 방문 수업 배치가 활발한 지역이에요.",
        "schools": [
            {"name": "잠실중학교", "slug": "jamsil-songpa", "note": "잠실 생활권, 방문·화상 모두 수요가 많은 학교"},
            {"name": "문정중학교", "slug": "munjeong-songpa", "note": "문정동, 신흥 주거단지 학부모 상담 문의가 많은 학교"},
            {"name": "방이중학교", "slug": "bangyi-songpa", "note": "방이동, 개념 기초부터 다지는 학생이 많은 학교"},
        ],
    },
    {
        "key": "nowon",
        "name": "서울 노원구",
        "blurb": "중계·상계·월계 학원가와 함께 방문 과외 수요가 꾸준한 지역이에요.",
        "schools": [
            {"name": "중계중학교", "slug": "junggye-nowon", "note": "중계동 은행사거리 학원가 인접 학교"},
            {"name": "상계중학교", "slug": "sanggye-nowon", "note": "상계동, 기초 개념 보완 수요가 많은 학교"},
            {"name": "월계중학교", "slug": "wolgye-nowon", "note": "월계동, 성적 관리형 방문 수업 문의가 많은 학교"},
        ],
    },
    {
        "key": "yangcheon",
        "name": "서울 양천구(목동)",
        "blurb": "목동 학원가와 맞닿아 있어 심화·선행 학습 문의가 많은 지역이에요.",
        "schools": [
            {"name": "목운중학교", "slug": "mogun-yangcheon", "note": "목동 학원가 인접, 심화 학습 수요가 많은 학교"},
            {"name": "신목중학교", "slug": "sinmok-yangcheon", "note": "신정동, 내신 등급 관리 문의가 많은 학교"},
            {"name": "목일중학교", "slug": "mogil-yangcheon", "note": "목동, 특목고 준비 학생 비중이 높은 학교"},
        ],
    },
    {
        "key": "bundang",
        "name": "경기 성남시 분당구",
        "blurb": "수내·서현 학원가 중심으로 화상·방문 수업을 함께 찾는 지역이에요.",
        "schools": [
            {"name": "수내중학교", "slug": "sunae-bundang", "note": "수내동, 방문 선생님 배치 문의가 많은 학교"},
            {"name": "서현중학교", "slug": "seohyeon-bundang", "note": "서현동 학원가 인접, 내신 대비 수요가 많은 학교"},
            {"name": "내정중학교", "slug": "naejeong-bundang", "note": "판교 인접, 화상 수업 문의가 늘고 있는 학교"},
        ],
    },
]

SUBJECT_CHOICES = ["국어", "영어", "수학", "사회", "과학"]

# ---------------------------------------------------------------
# index.html
# ---------------------------------------------------------------
index_body = '''
<section class="hero">
  <div class="grid">
    <div>
      <span class="eyebrow">1:1 과외 매칭 플랫폼</span>
      <h1>성적이 아니라<br><em>학습 궁합</em>부터 맞춥니다</h1>
      <p class="lead">방문·화상 수업부터 대입 컨설팅까지, 아이의 성향·목표·생활 패턴을 먼저 진단하고 그 다음에 딱 맞는 선생님 한 분을 연결해 드려요.</p>
      <div class="hero-ctas">
        <a class="cta-btn" href="apply.html">내 아이 학습 진단받기</a>
        <a class="cta-ghost" href="process.html">매칭 방식 보기</a>
      </div>
      <div class="trust-row">
        <span><i class="dot"></i>신원·학력 검증 선생님</span>
        <span><i class="dot"></i>첫 수업 후 결제</span>
        <span><i class="dot"></i>불만족 시 무료 재매칭</span>
      </div>
    </div>
    <div>
      <svg viewBox="0 0 300 300" fill="none" style="max-width:380px;margin-inline:auto;display:block;">
        <circle cx="150" cy="150" r="128" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="2 8"/>
        <path d="M95 150a55 55 0 1 1 110 0 55 55 0 0 1-110 0Z" fill="var(--primary-soft)"/>
        <path d="M150 95a55 55 0 0 1 47.5 82.5L150 150Z" fill="var(--accent-soft)"/>
        <circle cx="150" cy="150" r="55" fill="none" stroke="var(--primary)" stroke-width="2.5"/>
        <path d="M132 150l12 12 26-26" stroke="var(--accent-strong)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
  </div>
</section>

<div class="stats">
  <div class="wrap">
    <div><div class="num mono">4단계</div><div class="lbl">선생님 검증 절차</div></div>
    <div><div class="num mono">24h</div><div class="lbl">이내 매칭 안내</div></div>
    <div><div class="num mono">5개 지역</div><div class="lbl">서비스 오픈 지역</div></div>
    <div><div class="num mono">1회</div><div class="lbl">무료 재매칭 지원</div></div>
  </div>
</div>

<section id="services">
  <div class="head-row">
    <div><span class="eyebrow">서비스</span><h2>필요한 과외, 방식만 골라주세요</h2></div>
    <p>대면 관리가 필요한 아이부터 화상 수업을 원하는 학생까지, 상황에 맞는 세 가지 방식을 운영합니다.</p>
  </div>
  <div class="services">
    <div class="svc-card">
      <span class="tag">방문 수업</span>
      <h3>초·중·고 방문 과외</h3>
      <p>선생님이 직접 찾아오는 1:1 대면 수업. 집중 관리가 필요한 학생에게 가장 밀착된 방식이에요.</p>
      <div class="subjects"><span>국어</span><span>영어</span><span>수학</span><span>사회</span><span>과학</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">화상 수업</span>
      <h3>비대면 화상 과외</h3>
      <p>장소에 상관없이 어디서든. 방문 배치가 어려운 지역의 학생도 검증된 선생님과 실시간으로 만납니다.</p>
      <div class="subjects"><span>실시간 화상</span><span>녹화 복습</span><span>코딩</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">입시 컨설팅</span>
      <h3>대입 학습 컨설팅</h3>
      <p>학생부종합·정시 전략부터 생기부·자소서·면접까지, 전문 컨설턴트가 로드맵을 함께 설계합니다.</p>
      <div class="subjects"><span>학종</span><span>정시</span><span>생기부</span><span>면접</span></div>
    </div>
  </div>
</section>

<section id="process">
  <div class="head-row">
    <div><span class="eyebrow">매칭 방식</span><h2>딱 맞는 핏을 찾는 5단계</h2></div>
    <p>진단 없이 배정하지 않습니다. 학습 성향과 생활 패턴까지 확인한 뒤 선생님을 연결해요.</p>
  </div>
  <div class="process-track">
    <div class="p-step"><div class="n">01</div><h4>학습 진단</h4><p>현재 수준과 약점, 학습 성향을 먼저 파악해요.</p></div>
    <div class="p-step"><div class="n">02</div><h4>맞춤 설계</h4><p>목표와 생활 패턴에 맞춘 1:1 커리큘럼을 구성해요.</p></div>
    <div class="p-step"><div class="n">03</div><h4>1:1 수업</h4><p>방문 또는 화상으로 밀착 지도가 시작돼요.</p></div>
    <div class="p-step"><div class="n">04</div><h4>숙제·오답 관리</h4><p>배운 내용을 확실히 내 것으로 만들어요.</p></div>
    <div class="p-step"><div class="n">05</div><h4>리포트·피드백</h4><p>진행 상황을 학부모님께 정기 공유해요.</p></div>
  </div>
</section>

<section>
  <div class="head-row"><div><span class="eyebrow">왜 티치핏인가</span><h2>믿고 맡길 수 있는 이유</h2></div></div>
  <div class="trust-grid">
    <div class="trust-item"><div class="ico">\U0001F6E1️</div><h4>철저한 검증</h4><p>학력·신원·경력을 확인한 선생님만 매칭에 참여해요.</p></div>
    <div class="trust-item"><div class="ico">\U0001F9ED</div><h4>궁합 기반 매칭</h4><p>성적만이 아니라 성향·목표까지 분석해 연결해요.</p></div>
    <div class="trust-item"><div class="ico">\U0001F4B3</div><h4>첫 수업 후 결제</h4><p>수업을 직접 겪어본 뒤 결정하는 안심 구조예요.</p></div>
    <div class="trust-item"><div class="ico">\U0001F4CB</div><h4>꼼꼼한 학습 관리</h4><p>수업 리포트와 진도 관리로 흐름을 놓치지 않아요.</p></div>
    <div class="trust-item"><div class="ico">\U0001F501</div><h4>무료 재매칭</h4><p>선생님이 맞지 않으면 추가 비용 없이 다시 연결해요.</p></div>
    <div class="trust-item"><div class="ico">⏱️</div><h4>빠른 응대</h4><p>신청 후 24시간 이내 선생님을 안내해 드려요.</p></div>
  </div>
</section>

<section id="regions">
  <div class="head-row">
    <div><span class="eyebrow">지역별 과외</span><h2>우리 동네도 매칭돼요</h2></div>
    <p><a href="regions.html">전체 지역·학교별 안내 보기 →</a></p>
  </div>
  <div class="regions">
    {region_chips}
  </div>
</section>

<section id="apply">
  <div class="apply-wrap">
    <div>
      <span class="eyebrow" style="color:var(--accent-strong)">무료 상담</span>
      <h2>지금 우리 아이 학습 궁합을 확인해보세요</h2>
      <p>이름과 연락처만 남겨주시면 24시간 이내에 담당자가 직접 연락드려요.</p>
      <ul class="apply-perks">
        <li>상담·매칭 신청 전 과정 무료</li>
        <li>검증된 선생님만 매칭에 참여</li>
        <li>첫 수업 후 결제, 불만족 시 무료 재매칭</li>
      </ul>
    </div>
    {apply_form}
  </div>
</section>
'''

def region_chip(r):
    return '<div class="region-chip"><strong>{name}</strong> {blurb}</div>'.format(name=r["name"], blurb="학교 {}곳 매칭 안내".format(len(r["schools"])))

APPLY_FORM = '''<form class="form-card" action="https://formsubmit.co/ookkoo12@naver.com" method="POST">
      <input type="hidden" name="_subject" value="[티치핏] 새 상담 신청">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="thanks.html">
      <div class="field"><label for="tf-name">이름</label><input id="tf-name" name="이름" type="text" placeholder="학부모님 성함" required></div>
      <div class="field"><label for="tf-phone">연락처</label><input id="tf-phone" name="연락처" type="tel" placeholder="010-0000-0000" required></div>
      <div class="field">
        <label>학년</label>
        <div class="radio-row">
          <label><input type="radio" name="학년" value="초등">초등</label>
          <label><input type="radio" name="학년" value="중등">중등</label>
          <label><input type="radio" name="학년" value="고등">고등</label>
          <label><input type="radio" name="학년" value="대입준비">대입준비</label>
        </div>
      </div>
      <div class="field">
        <label>희망 방식</label>
        <div class="radio-row">
          <label><input type="radio" name="희망방식" value="방문">방문</label>
          <label><input type="radio" name="희망방식" value="화상">화상</label>
          <label><input type="radio" name="희망방식" value="입시컨설팅">입시컨설팅</label>
        </div>
      </div>
      <div class="field"><label for="tf-memo">남기실 말 (선택)</label><textarea id="tf-memo" name="메모" rows="2" placeholder="희망 과목, 시간대, 지역 등"></textarea></div>
      <button class="submit-btn" type="submit">무료 상담 신청하기</button>
      <p class="form-note">신청 즉시 담당자에게 전달되며, 24시간 이내 연락드립니다.</p>
    </form>'''

# ---------------------------------------------------------------
# services.html / process.html / teachers.html
# ---------------------------------------------------------------
services_body = '''
<section class="page-hero">
  <span class="eyebrow">서비스</span>
  <h1>방문 · 화상 · 입시 컨설팅, 세 가지 방식</h1>
  <p>학생의 성향과 생활 패턴에 맞춰 방문 수업, 화상 수업, 대입 컨설팅 중 가장 잘 맞는 방식을 추천해 드려요.</p>
</section>
<section>
  <div class="services">
    <div class="svc-card">
      <span class="tag">방문 수업</span>
      <h3>초·중·고 방문 과외</h3>
      <p>선생님이 직접 집으로 찾아오는 1:1 대면 수업이에요. 집중력이 흐트러지기 쉬운 학생, 옆에서 관리가 필요한 학생에게 가장 밀착된 방식입니다. 수업 중 이해도를 바로 확인하고, 숙제와 오답 관리까지 현장에서 챙겨요.</p>
      <div class="subjects"><span>국어</span><span>영어</span><span>수학</span><span>사회</span><span>과학</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">화상 수업</span>
      <h3>비대면 화상 과외</h3>
      <p>거주 지역에 상관없이 검증된 선생님과 실시간으로 만나는 방식이에요. 방문 선생님 배치가 어려운 지역이거나, 이동 시간을 아끼고 싶은 학생에게 적합합니다. 수업 녹화로 복습도 가능해요.</p>
      <div class="subjects"><span>실시간 화상</span><span>녹화 복습</span><span>코딩</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">입시 컨설팅</span>
      <h3>대입 학습 컨설팅</h3>
      <p>학생부종합전형·정시 전략부터 생활기록부 관리, 자기소개서, 면접 준비까지 전문 컨설턴트가 함께 로드맵을 설계해 드려요. 성적 관리와 입시 전략을 동시에 챙기고 싶은 고등학생에게 추천합니다.</p>
      <div class="subjects"><span>학종</span><span>정시</span><span>생기부</span><span>면접</span></div>
    </div>
  </div>
</section>
<section>
  <div class="head-row"><div><span class="eyebrow">방식을 못 정하셨다면</span><h2>상담에서 함께 정해드려요</h2></div></div>
  <div class="apply-wrap" style="grid-template-columns:1fr;">
    <div>
      <p style="color:#DCEEE8;">방문과 화상 중 무엇이 더 맞을지 고민되신다면, 상담 시 아이의 학습 성향과 생활 패턴을 바탕으로 담당자가 방식을 함께 추천해 드려요.</p>
      <div style="margin-top:18px;"><a class="cta-btn" href="apply.html" style="background:var(--accent);color:var(--primary-strong)!important;">무료 상담 신청하기</a></div>
    </div>
  </div>
</section>
'''

process_body = '''
<section class="page-hero">
  <span class="eyebrow">매칭 방식</span>
  <h1>성적이 오르는 5단계 관리 시스템</h1>
  <p>진단 없이 곧바로 선생님을 배정하지 않아요. 아이의 학습 상태를 먼저 확인하고, 그 다음 순서로 매칭과 관리가 이어집니다.</p>
</section>
<section>
  <div class="process-track">
    <div class="p-step"><div class="n">01</div><h4>학습 진단</h4><p>현재 수준·약점을 정확히 파악합니다. 최근 시험 결과와 학습 습관을 함께 확인해요.</p></div>
    <div class="p-step"><div class="n">02</div><h4>맞춤 설계</h4><p>목표에 맞춘 1:1 커리큘럼을 만듭니다. 단기 내신 대비인지 장기 실력 향상인지에 따라 설계가 달라져요.</p></div>
    <div class="p-step"><div class="n">03</div><h4>1:1 수업</h4><p>방문·화상 중 선택한 방식으로 밀착 지도합니다. 수업마다 이해도를 확인하며 속도를 조절해요.</p></div>
    <div class="p-step"><div class="n">04</div><h4>숙제·오답 관리</h4><p>배운 내용을 확실히 내 것으로 만듭니다. 오답 노트와 복습 계획을 함께 챙겨요.</p></div>
    <div class="p-step"><div class="n">05</div><h4>리포트·피드백</h4><p>진행 상황을 학부모님께 정기적으로 공유합니다. 필요하면 커리큘럼을 다시 조정해요.</p></div>
  </div>
</section>
<section>
  <div class="head-row"><div><span class="eyebrow">한 가지 더</span><h2>선생님이 안 맞으면, 다시 맞춰드려요</h2></div></div>
  <div class="trust-grid" style="grid-template-columns:repeat(2,1fr);">
    <div class="trust-item"><div class="ico">\U0001F504</div><h4>무료 재매칭</h4><p>수업을 진행해봤는데 아이와 맞지 않는다면, 추가 비용 없이 다른 선생님으로 다시 연결해 드려요.</p></div>
    <div class="trust-item"><div class="ico">\U0001F4B3</div><h4>첫 수업 후 결제</h4><p>첫 수업을 먼저 경험해보고 결제 여부를 결정할 수 있어 부담이 적어요.</p></div>
  </div>
</section>
'''

teachers_body = '''
<section class="page-hero">
  <span class="eyebrow">선생님</span>
  <h1>검증된 선생님만 매칭에 참여합니다</h1>
  <p>학력·신원·경력 확인을 거친 선생님만 등록되고, 신청하신 지역·과목·학년에 맞는 선생님을 안내해 드려요.</p>
</section>
<section>
  <div class="head-row"><div><span class="eyebrow">검증 절차</span><h2>선생님 등록 전 4단계 확인</h2></div></div>
  <div class="trust-grid" style="grid-template-columns:repeat(2,1fr);">
    <div class="trust-item"><div class="ico">\U0001F4C4</div><h4>학력 확인</h4><p>졸업증명 등 학력 서류를 확인합니다.</p></div>
    <div class="trust-item"><div class="ico">\U0001F194</div><h4>신원 확인</h4><p>본인 확인 및 신원 정보를 검증합니다.</p></div>
    <div class="trust-item"><div class="ico">\U0001F4BC</div><h4>경력 확인</h4><p>과외·강의 경력을 확인하고 전공·지도 과목을 매칭합니다.</p></div>
    <div class="trust-item"><div class="ico">\U0001F4DE</div><h4>사전 인터뷰</h4><p>수업 방식과 성향을 미리 확인해 학생과의 궁합을 예측합니다.</p></div>
  </div>
</section>
<section id="teachers">
  <div class="head-row"><div><span class="eyebrow">이런 방식으로 소개돼요</span><h2>선생님 프로필 예시</h2></div></div>
  <p class="sample-note"><span class="badge">예시</span>실제 서비스에서는 신청하신 지역·과목에 맞는 선생님 프로필이 이런 카드 형태로 안내됩니다.</p>
  <div class="teachers">
    <div class="t-card"><div class="avatar">이</div><h4>이OO 선생님</h4><div class="meta">수학 · 중1~고2 · 교습경력 9년차 · 방문</div><div class="fit-score">예상 궁합도 <b class="mono">92%</b></div></div>
    <div class="t-card"><div class="avatar">오</div><h4>오OO 선생님</h4><div class="meta">영어 · 중3~고3 · 코칭 인증 · 화상</div><div class="fit-score">예상 궁합도 <b class="mono">88%</b></div></div>
    <div class="t-card"><div class="avatar">윤</div><h4>윤OO 선생님</h4><div class="meta">국어·영어·수학 · 초등~고등 · 방문+화상</div><div class="fit-score">예상 궁합도 <b class="mono">95%</b></div></div>
  </div>
</section>
'''

# ---------------------------------------------------------------
# regions.html (hub)
# ---------------------------------------------------------------
def region_card(r):
    items = "\n".join(
        '<li><a href="schools/{slug}.html">{name} <span class="arrow">→</span></a></li>'.format(slug=s["slug"], name=s["name"])
        for s in r["schools"]
    )
    return '''<div class="region-card">
      <h3>{name}</h3>
      <div class="count">{blurb}</div>
      <ul class="school-list">
        {items}
      </ul>
    </div>'''.format(name=r["name"], blurb=r["blurb"], items=items)

regions_body = '''
<section class="page-hero">
  <span class="eyebrow">지역별 과외</span>
  <h1>학교별로 필요한 과외가 다릅니다</h1>
  <p>같은 학년이라도 학교마다 내신 시험 범위와 난이도, 학원가 분위기가 달라요. 티치핏은 학교 단위로 상담을 진행해 더 정확하게 맞춰 드립니다. 아직 오픈 지역이 많지 않지만, 매주 새로운 지역을 추가하고 있어요.</p>
</section>
<section>
  <div class="region-grid">
    {region_cards}
  </div>
</section>
'''.format(region_cards="\n    ".join(region_card(r) for r in REGIONS))

# ---------------------------------------------------------------
# blog.html (index only, cards to be added over time)
# ---------------------------------------------------------------
blog_body = '''
<section class="page-hero">
  <span class="eyebrow">블로그</span>
  <h1>학교별 내신·과목별 학습 전략</h1>
  <p>학교별 내신 대비, 학년별·과목별 학습 전략을 꾸준히 올리고 있어요.</p>
</section>
<section>
  <div class="article-grid">
    <!-- BLOG_GRID_START -->
    <!-- BLOG_GRID_END -->
  </div>
</section>
'''

# ---------------------------------------------------------------
# apply.html (noindex, standalone page reusing hero form)
# ---------------------------------------------------------------
apply_body = '''
<section class="page-hero">
  <span class="eyebrow">무료 상담</span>
  <h1>학습 궁합부터 확인하는 상담 신청</h1>
  <p>이름과 연락처만 남겨주시면 24시간 이내에 담당자가 직접 연락드려요. 상담과 매칭 신청은 모두 무료입니다.</p>
</section>
<section>
  <div class="apply-wrap">
    <div>
      <span class="eyebrow" style="color:var(--accent-strong)">신청 전 확인해주세요</span>
      <h2>이렇게 진행됩니다</h2>
      <ul class="apply-perks">
        <li>신청 후 24시간 이내 담당자 연락</li>
        <li>학습 진단 → 선생님 추천 → 첫 수업</li>
        <li>첫 수업 후 결제, 불만족 시 무료 재매칭</li>
      </ul>
    </div>
    {apply_form}
  </div>
</section>
'''.format(apply_form=APPLY_FORM)

# ---------------------------------------------------------------
# school page template
# ---------------------------------------------------------------
def school_body(region, school):
    other_schools = [s for s in region["schools"] if s["slug"] != school["slug"]]
    other_links = "\n        ".join(
        '<li><a href="{slug}.html">{name} <span class="arrow">→</span></a></li>'.format(slug=s["slug"], name=s["name"])
        for s in other_schools
    )
    subjects_row = "".join('<span>{}</span>'.format(s) for s in SUBJECT_CHOICES)
    return '''
<nav class="breadcrumb"><a href="../regions.html">지역별 과외</a> / {region_name}</nav>
<section class="page-hero">
  <span class="eyebrow">{region_name} · 학교별 과외</span>
  <h1>{school_name} 과외, 학교 특성부터 확인하고 시작하세요</h1>
  <p>{note}예요. 티치핏은 이 학교 학생들의 내신 범위와 학습 분위기를 고려해 방문·화상 선생님을 매칭해 드려요.</p>
</section>
<section>
  <div class="prose">
    <h2>{school_name} 학생들에게 자주 나오는 상담 포인트</h2>
    <p>{school_name} 학생과 학부모님이 상담에서 가장 많이 묻는 내용은 <strong>내신 시험 범위에 맞춘 단원별 학습</strong>과 <strong>기초 개념 보완</strong>이에요. 학교별로 시험 출제 방식과 난이도 체감이 다르기 때문에, 같은 학년이라도 접근 방식을 다르게 가져가야 해요.</p>
    <p>티치핏에서는 상담 시 최근 시험 성적과 취약 단원을 먼저 확인한 뒤, {region_name} 인근에서 활동 중인 선생님 중 지도 스타일이 맞는 분을 추천해 드립니다.</p>
    <h3>방문 수업과 화상 수업, 어떤 게 더 맞을까요</h3>
    <p>등하교 후 시간이 빠듯하거나 옆에서 관리가 필요한 학생은 <strong>방문 수업</strong>이 더 잘 맞고, 이동 시간을 아끼고 싶거나 특정 시간대 선생님을 원하는 경우엔 <strong>화상 수업</strong>도 좋은 선택이에요. 상담 시 생활 패턴을 말씀해주시면 더 정확하게 추천해 드립니다.</p>
    <h3>과목별 과외 안내</h3>
    <p>{school_name} 학생 대상으로는 아래 과목의 방문·화상 과외를 안내하고 있어요.</p>
    <div class="subjects" style="margin-bottom:6px;">{subjects}</div>
  </div>
</section>
<section>
  <div class="head-row"><div><span class="eyebrow">{region_name} 다른 학교</span><h2>인근 학교도 함께 보세요</h2></div></div>
  <ul class="school-list" style="max-width:480px;">
    {other_links}
  </ul>
</section>
<section>
  <div class="apply-wrap" style="grid-template-columns:1fr;">
    <div>
      <span class="eyebrow" style="color:var(--accent-strong)">{school_name} 학생 학부모님께</span>
      <h2>지금 무료 상담을 신청해보세요</h2>
      <p style="color:#DCEEE8;">이름과 연락처만 남겨주시면 24시간 이내에 담당자가 연락드립니다.</p>
      <div style="margin-top:18px;"><a class="cta-btn" href="../apply.html" style="background:var(--accent);color:var(--primary-strong)!important;">무료 상담 신청하기</a></div>
    </div>
  </div>
</section>
'''.format(region_name=region["name"], school_name=school["name"], note=school["note"], subjects=subjects_row, other_links=other_links)

# ---------------------------------------------------------------
# generate all pages
# ---------------------------------------------------------------
page("index.html", "티치핏 | 1:1 과외 선생님 매칭", "성적이 아니라 학습 궁합부터 맞추는 1:1 과외 매칭 서비스, 티치핏.", "index.html",
     index_body.format(region_chips="\n    ".join(region_chip(r) for r in REGIONS), apply_form=APPLY_FORM),
     path_prefix="", canonical=BASE_URL + "/index.html")

page("services.html", "서비스 안내 | 티치핏", "방문 수업, 화상 수업, 입시 컨설팅까지 티치핏의 세 가지 과외 서비스를 안내합니다.", "services.html",
     services_body, path_prefix="", canonical=BASE_URL + "/services.html")

page("process.html", "매칭 방식 | 티치핏", "학습 진단부터 리포트까지, 티치핏의 5단계 매칭 프로세스를 소개합니다.", "process.html",
     process_body, path_prefix="", canonical=BASE_URL + "/process.html")

page("teachers.html", "선생님 소개 | 티치핏", "학력·신원·경력 검증을 거친 티치핏 선생님 매칭 기준을 소개합니다.", "teachers.html",
     teachers_body, path_prefix="", canonical=BASE_URL + "/teachers.html")

page("regions.html", "지역별 과외 | 티치핏", "학교별 내신 특성에 맞춘 티치핏의 지역별·학교별 과외 안내입니다.", "regions.html",
     regions_body, path_prefix="", canonical=BASE_URL + "/regions.html")

page("blog.html", "블로그 | 티치핏", "학교별 내신 대비, 과목별 학습 전략을 소개하는 티치핏 블로그입니다.", "blog.html",
     blog_body, path_prefix="", canonical=BASE_URL + "/blog.html")

page("apply.html", "무료 상담 신청 | 티치핏", "티치핏 1:1 과외 매칭 무료 상담을 신청하세요.", "apply.html",
     apply_body, path_prefix="", canonical=BASE_URL + "/apply.html", noindex=True)

thanks_body = '''
<section class="page-hero" style="text-align:center;">
  <span class="eyebrow">신청 완료</span>
  <h1>상담 신청이 접수되었습니다</h1>
  <p style="max-width:52ch;margin-inline:auto;">24시간 이내에 담당자가 남겨주신 연락처로 안내드릴게요. 잠시만 기다려 주세요.</p>
  <div style="margin-top:22px;"><a class="cta-btn" href="index.html">홈으로 돌아가기</a></div>
</section>
'''
page("thanks.html", "신청 완료 | 티치핏", "티치핏 상담 신청이 정상적으로 접수되었습니다.", "",
     thanks_body, path_prefix="", canonical=BASE_URL + "/thanks.html", noindex=True)

for region in REGIONS:
    for school in region["schools"]:
        page(
            "schools/{}.html".format(school["slug"]),
            "{} 과외 | 티치핏".format(school["name"]),
            "{} 학생을 위한 방문·화상 1:1 과외 매칭, 티치핏에서 상담해보세요.".format(school["name"]),
            "regions.html",
            school_body(region, school),
            path_prefix="../",
            canonical=BASE_URL + "/schools/{}.html".format(school["slug"]),
        )

# ---------------------------------------------------------------
# sitemap.xml (public pages only)
# ---------------------------------------------------------------
sitemap_urls = ["index.html", "services.html", "process.html", "teachers.html", "regions.html", "blog.html"]
for region in REGIONS:
    for school in region["schools"]:
        sitemap_urls.append("schools/{}.html".format(school["slug"]))

sitemap_items = "\n".join(
    "  <url><loc>{}/{}</loc></url>".format(BASE_URL, u) for u in sitemap_urls
)
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{}\n</urlset>\n'.format(sitemap_items)
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print("wrote sitemap.xml")

print("DONE")
