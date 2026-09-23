# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# =================================================================
# SITE CONFIG — 다른 지역으로 새 사이트를 만들 때는 이 블록만 바꾸면 됨
# (레포를 통째로 복사한 뒤 이 블록 + 학교 목록만 새 지역 것으로 교체하고
#  python build.py 실행하면 끝)
# =================================================================
REGION_SHORT = "군산"              # 지역 짧은 이름 (브랜드/카피에 사용)
REGION_FULL = "전북 군산시"         # 지역 정식 명칭 (breadcrumb 등에 사용)
BRAND = "티치핏" + REGION_SHORT     # 사이트 브랜드명 (필요하면 직접 다른 값으로 덮어써도 됨)
PHONE_DISPLAY = "010-3131-5305"
PHONE_TEL = "01031315305"
BASE_URL = "https://slovrest.com"   # 이 지역 사이트의 실제 도메인
LEAD_EMAIL = "ookkoo12@naver.com"   # 상담 신청 폼이 도착할 이메일 (FormSubmit 릴레이)
NAVER_VERIFICATION = "24cc1c4678a952a91fe1248a4ce9dd147a24e2f6"  # 네이버 서치어드바이저 소유확인
GOOGLE_VERIFICATION = ""  # 구글 서치콘솔 소유확인 (등록 시 채워넣기)

# 학교 목록 — 시/군 교육지원청 공식 학교안내 기준으로 초/중/고 전체를 넣을 것
# (perfectedu 벤치마킹 원칙: 일부만 골라 넣지 않고 관할 전체를 포함 — 형평성 문제 방지)
# 출처: 전북특별자치도군산교육지원청(office.jbedu.kr) 학교안내, 2026-09-18 확인
ELEMENTARY_NAMES = [
    "개정초등학교","군산경포초등학교","군산구암초등학교","군산금광초등학교","군산나운초등학교",
    "군산남초등학교","군산내흥초등학교","군산동초등학교","군산문화초등학교","군산미성초등학교",
    "군산미장초등학교","군산산북초등학교","군산서초등학교","군산서해초등학교","소룡초등학교",
    "군산수송초등학교","군산신풍초등학교","군산신흥초등학교","군산아리울초등학교","군산용문초등학교",
    "군산월명초등학교","군산중앙초등학교","군산지곡초등학교","군산진포초등학교","군산초등학교",
    "군산푸른솔초등학교","군산풍문초등학교","해성초등학교","군산흥남초등학교","나포초등학교",
    "당북초등학교","대야남초등학교","대야초등학교","무녀도초등학교","문창초등학교",
    "미룡초등학교","발산초등학교","새만금초등학교","서수초등학교","성산초등학교",
    "술산초등학교","오봉초등학교","옥구초등학교","옥봉초등학교","옥산초등학교",
    "임피초등학교","전주교육대학교군산부설초등학교","창오초등학교","회현초등학교","군산금빛초등학교",
]
MIDDLE_NAMES = [
    "군산남중학교","군산동산중학교","군산산북중학교","군산서흥중학교","군산월명중학교",
    "군산자양중학교","군산중학교","군산진포중학교","군산금강중학교","나포중학교",
    "군산동원중학교","옥구중학교","임피중학교","회현중학교",
    "군산대성중학교","군산영광중학교","군산제일중학교","군산중앙중학교",
]
HIGH_NAMES = [
    "군산고등학교","군산기계공업고등학교","한들고등학교","군산동고등학교","군산상일고등학교",
    "군산여자고등학교","군산여자상업고등학교","전북외국어고등학교","군산영광여자고등학교",
    "군산제일고등학교","군산중앙고등학교","군산중앙여자고등학교",
]
# =================================================================
# CONFIG 끝 — 아래는 전부 재사용 가능한 공통 로직/템플릿
# =================================================================

FONT_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap">'

NAV_ITEMS = [
    ("index.html", "홈"),
    ("services.html", "화상과외 소개"),
    ("process.html", "매칭 방식"),
    ("teachers.html", "선생님"),
    ("regions.html", f"{REGION_SHORT} 학교검색"),
    ("blog.html", "블로그"),
]

def head(title, desc, path_prefix, canonical, noindex=False):
    robots_tag = '<meta name="robots" content="noindex,nofollow">\n' if noindex else ''
    verify_tags = ''
    if NAVER_VERIFICATION:
        verify_tags += '<meta name="naver-site-verification" content="{}">\n'.format(NAVER_VERIFICATION)
    if GOOGLE_VERIFICATION:
        verify_tags += '<meta name="google-site-verification" content="{}">\n'.format(GOOGLE_VERIFICATION)
    return '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" type="application/rss+xml" title="{brand} 블로그" href="{base}/rss.xml">
{verify}{robots}{font}
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
'''.format(title=title, desc=desc, canonical=canonical, font=FONT_LINK, p=path_prefix, robots=robots_tag, verify=verify_tags, brand=BRAND, base=BASE_URL)

def topbar():
    return f'''<div class="topbar">
  <div class="wrap">
    <span>지금 신청하면 30분 무료체험수업부터 받아보실 수 있어요</span>
    <a class="phone" href="tel:{PHONE_TEL}">\U0001F4DE {PHONE_DISPLAY} (09:00–21:00)</a>
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
    <a class="logo" href="{p}index.html"><span class="mark">TF</span>{brand}</a>
    <div class="navwrap">
      <nav class="main">
        {links}
      </nav>
      <a class="cta-btn" href="{p}apply.html">무료 상담 신청</a>
      <button class="menu-btn" aria-label="메뉴">☰</button>
    </div>
  </div>
  <div class="mobile-nav-wrap">
    <nav class="mobile-nav">
      {mlinks}
      <a href="{p}apply.html">무료 상담 신청</a>
    </nav>
  </div>
</header>
'''.format(p=path_prefix, brand=BRAND, links='\n        '.join(links), mlinks='\n      '.join(mlinks))

def footer(path_prefix):
    return '''<footer>
  <div class="wrap">
    <div>
      <a class="logo" href="{p}index.html" style="margin-bottom:10px;"><span class="mark">TF</span>{brand}</a>
      <div class="fnav">
        <a href="{p}services.html">화상과외 소개</a><a href="{p}process.html">매칭 방식</a><a href="{p}teachers.html">선생님</a><a href="{p}regions.html">{region} 학교검색</a><a href="{p}blog.html">블로그</a>
      </div>
      <p class="disclaimer">전화 {phone} · 운영시간 09:00–21:00 · 상담 및 매칭 신청은 무료이며, 실제 수업 진행 여부와 비용은 상담 후 안내해 드립니다. 사업자 정보는 확정 후 별도 고지 예정입니다.</p>
    </div>
  </div>
</footer>
<script src="{p}assets/site.js"></script>
</body>
</html>
'''.format(p=path_prefix, brand=BRAND, region=REGION_SHORT, phone=PHONE_DISPLAY)

def page(filename, title, desc, active, body, path_prefix="", canonical="", noindex=False, extra_js=""):
    full = head(title, desc, path_prefix, canonical, noindex) + topbar() + header(path_prefix, active) + '<main class="wrap">\n' + body + '\n</main>\n' + footer(path_prefix)
    if extra_js:
        full = full.replace('</body>', extra_js + '\n</body>')
    out_path = os.path.join(ROOT, filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full)
    print("wrote", filename)

# ---------------------------------------------------------------
# Revised Romanization (approximate, URL-slug purposes only)
# ---------------------------------------------------------------
CHO = ['g','kk','n','d','tt','r','m','b','pp','s','ss','','j','jj','ch','k','t','p','h']
JUNG = ['a','ae','ya','yae','eo','e','yeo','ye','o','wa','wae','oe','yo','u','wo','we','wi','yu','eu','ui','i']
JONG = ['','g','kk','gs','n','nj','nh','d','l','lg','lm','lb','ls','lt','lp','lh','m','b','bs','s','ss','ng','j','ch','k','t','p','h']

def romanize(text):
    out = []
    for ch in text:
        code = ord(ch) - 0xAC00
        if 0 <= code < 11172:
            cho = code // 588
            jung = (code % 588) // 28
            jong = code % 28
            out.append(CHO[cho] + JUNG[jung] + JONG[jong])
        elif ch.isalnum():
            out.append(ch.lower())
    return ''.join(out)

REGION_SLUG = romanize(REGION_SHORT)  # 예: 군산 -> gunsan (슬러그 접미사로 사용)

def josa_eun_neun(word):
    """받침 유무에 따라 '은'/'는' 중 맞는 조사를 반환 (BRAND가 지역마다 달라져도 문법 맞게)."""
    if not word:
        return "는"
    code = ord(word[-1]) - 0xAC00
    if 0 <= code < 11172:
        return "은" if (code % 28) != 0 else "는"
    return "는"

BRAND_EUN = josa_eun_neun(BRAND)

def sample_keyword(name):
    """검색창 placeholder용 짧은 예시 키워드 — 지역명 접두어·학교급 접미어를 뗀 나머지."""
    base = name.replace('초등학교', '').replace('중학교', '').replace('고등학교', '')
    if base.startswith(REGION_SHORT) and len(base) > len(REGION_SHORT):
        base = base[len(REGION_SHORT):]
    return base[:3] if base else name[:2]

LEVEL_CODE = {'초등학교': 'es', '중학교': 'ms', '고등학교': 'hs'}

def make_slug(name, level, used):
    base = name.replace('초등학교', '').replace('중학교', '').replace('고등학교', '')
    slug = '{}-{}-{}'.format(romanize(base), LEVEL_CODE[level], REGION_SLUG)
    if slug in used:
        n = 2
        while '{}-{}'.format(slug, n) in used:
            n += 1
        slug = '{}-{}'.format(slug, n)
    used.add(slug)
    return slug

_used_slugs = set()
def build_school_list(names, level):
    out = []
    for name in names:
        out.append({"name": name, "level": level, "slug": make_slug(name, level, _used_slugs)})
    return out

SCHOOLS = (
    build_school_list(ELEMENTARY_NAMES, "초등학교")
    + build_school_list(MIDDLE_NAMES, "중학교")
    + build_school_list(HIGH_NAMES, "고등학교")
)

LEVEL_INFO = {
    "초등학교": {
        "stage": "초등학생",
        "focus": "읽기·쓰기·연산 기초와 학습 습관 형성",
        "subjects": ["국어", "영어", "수학"],
        "worry": "아직 공부 습관이 안 잡혀서 무엇부터 시작해야 할지 모르겠다는 점",
    },
    "중학교": {
        "stage": "중학생",
        "focus": "내신 시험 범위에 맞춘 단원별 학습과 기초 개념 보완",
        "subjects": ["국어", "영어", "수학", "사회", "과학"],
        "worry": "시험 범위는 아는데 어디서부터 정리해야 할지 막막하다는 점",
    },
    "고등학교": {
        "stage": "고등학생",
        "focus": "내신 등급 관리와 수능 대비 학습",
        "subjects": ["국어", "영어", "수학", "사회", "과학"],
        "worry": "내신과 수능을 동시에 챙기기엔 시간이 부족하다는 점",
    },
}

# ---------------------------------------------------------------
# index.html
# ---------------------------------------------------------------
index_body = f'''
<section class="hero">
  <div class="grid">
    <div>
      <span class="eyebrow">{REGION_SHORT} 과외</span>
      <h1>{REGION_SHORT} 과외 찾고 계신가요?<br>초·중·고 1:1 <em>화상과외</em></h1>
      <p class="lead">수학·영어·국어 등 전 과목, 초등학생부터 고등학생까지 — {REGION_SHORT} 학교 사정을 잘 아는 선생님을 실시간 화상 수업으로 연결해 드려요. 방문 없이도 집에서 편하게 받을 수 있어요.</p>
      <div class="hero-ctas">
        <a class="cta-btn" href="apply.html">30분 무료체험 신청하기</a>
        <a class="cta-ghost" href="process.html">매칭 방식 보기</a>
      </div>
      <div class="trust-row">
        <span><i class="dot"></i>{REGION_SHORT} 학교 사정에 밝은 선생님</span>
        <span><i class="dot"></i>30분 무료체험수업 먼저 받아보기</span>
        <span><i class="dot"></i>체험 후 결정, 부담 없어요</span>
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
    <div><div class="num mono">{len(SCHOOLS)}개교</div><div class="lbl">{REGION_SHORT} 전체 초·중·고 매칭 가능</div></div>
    <div><div class="num mono">4단계</div><div class="lbl">선생님 검증 절차</div></div>
    <div><div class="num mono">30분</div><div class="lbl">무료체험수업 제공</div></div>
    <div><div class="num mono">24h</div><div class="lbl">이내 매칭 안내</div></div>
  </div>
</div>

<section id="grades">
  <div class="head-row">
    <div><span class="eyebrow">학년별 과외</span><h2>학년마다 필요한 과외가 달라요</h2></div>
    <p>같은 {REGION_SHORT}이라도 초등·중등·고등에 따라 고민이 다르니, 학년에 맞춰 과목과 방식을 정해드려요.</p>
  </div>
  <div class="services">
    <div class="svc-card">
      <span class="tag">초등</span>
      <h3>{REGION_SHORT} 초등학생 화상과외</h3>
      <p>국어·영어·수학 기초를 다지고 학습 습관을 잡아주는 시기예요. 놀이처럼 부담 없이 시작할 수 있게 진행해요.</p>
      <div class="subjects"><span>국어</span><span>영어</span><span>수학</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">중등</span>
      <h3>{REGION_SHORT} 중학생 수학·영어 화상과외</h3>
      <p>내신 시험 범위에 맞춘 단원별 학습이 중요해지는 시기예요. 학교별 시험 유형을 반영해 대비해요.</p>
      <div class="subjects"><span>수학</span><span>영어</span><span>국어</span><span>사회</span><span>과학</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">고등</span>
      <h3>{REGION_SHORT} 고등학생 내신·수능 화상과외</h3>
      <p>내신 등급 관리와 수능 대비를 함께 챙겨야 하는 시기예요. 목표에 맞춰 커리큘럼을 조정해요.</p>
      <div class="subjects"><span>수학</span><span>영어</span><span>국어</span><span>사회</span><span>과학</span></div>
    </div>
  </div>
</section>

<section id="services">
  <div class="head-row">
    <div><span class="eyebrow">서비스</span><h2>왜 화상과외 하나에만 집중할까요</h2></div>
    <p>방문 선생님을 구하기 어려운 과목도, 화상이라면 훨씬 넓은 범위에서 {REGION_SHORT} 학생에게 맞는 선생님을 찾을 수 있어요.</p>
  </div>
  <div class="services">
    <div class="svc-card">
      <span class="tag">실시간 화상</span>
      <h3>1:1 실시간 화상 수업</h3>
      <p>정해진 시간에 화면으로 만나 실시간으로 진행하는 수업이에요. 이동 시간이 없어 저녁 시간대도 유연하게 잡을 수 있어요.</p>
      <div class="subjects"><span>국어</span><span>영어</span><span>수학</span><span>사회</span><span>과학</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">녹화 복습</span>
      <h3>수업 녹화 다시보기</h3>
      <p>수업 내용을 녹화해 두고 이해가 안 된 부분만 다시 돌려볼 수 있어요. 시험 전 복습에 특히 도움이 돼요.</p>
      <div class="subjects"><span>단원별 복습</span><span>오답 다시보기</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">지역 맞춤</span>
      <h3>{REGION_SHORT} 학교 사정을 아는 선생님</h3>
      <p>같은 화상 수업이라도 {REGION_SHORT} 학교의 시험 범위와 분위기를 아는 선생님과 하면 훨씬 정확해요. 상담 시 재학 중인 학교를 확인해 매칭에 반영합니다.</p>
      <div class="subjects"><span>학교별 내신</span><span>지역 맞춤 매칭</span></div>
    </div>
  </div>
</section>

<section id="cost-vs-visit">
  <div class="head-row"><div><span class="eyebrow">궁금한 점</span><h2>{REGION_SHORT} 과외 비용, 방문과 화상 뭐가 다를까요</h2></div></div>
  <div class="trust-grid" style="grid-template-columns:repeat(2,1fr);">
    <div class="trust-item"><h4>{REGION_SHORT} 과외 비용은 어떻게 결정될까요</h4><p>과목·학년·수업 시간, 선생님 경력에 따라 달라져요. 정확한 비용은 상담 시 학생 상황을 확인한 뒤 안내해 드리고, 30분 무료체험수업으로 먼저 확인하실 수 있어요.</p></div>
    <div class="trust-item"><h4>방문과외와 화상과외의 차이</h4><p>방문은 대면 관리가 필요한 학생에게, 화상은 이동 시간 없이 원하는 시간대에 넓은 범위의 선생님을 찾고 싶은 학생에게 잘 맞아요. {BRAND}은(는) 화상과외 하나에 집중해 매칭 정확도를 높였어요.</p></div>
  </div>
</section>

<section id="process">
  <div class="head-row">
    <div><span class="eyebrow">매칭 방식</span><h2>우리 아이에게 맞는 선생님 찾는 방법</h2></div>
    <p>진단 없이 배정하지 않습니다. 학습 성향과 생활 패턴까지 확인한 뒤 선생님을 연결해요.</p>
  </div>
  <div class="process-track">
    <div class="p-step"><div class="n">01</div><h4>학습 진단</h4><p>현재 수준과 약점, 학습 성향을 먼저 파악해요.</p></div>
    <div class="p-step"><div class="n">02</div><h4>맞춤 설계</h4><p>목표와 생활 패턴에 맞춘 1:1 커리큘럼을 구성해요.</p></div>
    <div class="p-step"><div class="n">03</div><h4>30분 무료체험수업</h4><p>선생님과 화면으로 만나 30분 동안 무료로 먼저 받아보고 궁합을 확인해요.</p></div>
    <div class="p-step"><div class="n">04</div><h4>숙제·오답 관리</h4><p>배운 내용을 확실히 내 것으로 만들어요.</p></div>
    <div class="p-step"><div class="n">05</div><h4>리포트·피드백</h4><p>진행 상황을 학부모님께 정기 공유해요.</p></div>
  </div>
</section>

<section>
  <div class="head-row"><div><span class="eyebrow">왜 {BRAND}인가</span><h2>믿고 맡길 수 있는 이유</h2></div></div>
  <div class="trust-grid">
    <div class="trust-item"><div class="ico">\U0001F6E1️</div><h4>철저한 검증</h4><p>학력·신원·경력을 확인한 선생님만 매칭에 참여해요.</p></div>
    <div class="trust-item"><div class="ico">\U0001F9ED</div><h4>궁합 기반 매칭</h4><p>성적만이 아니라 성향·목표까지 분석해 연결해요.</p></div>
    <div class="trust-item"><div class="ico">\U0001F3AC</div><h4>30분 무료체험수업</h4><p>정식 신청 전에 30분 동안 선생님과 무료로 먼저 만나보고 결정할 수 있어요.</p></div>
    <div class="trust-item"><div class="ico">\U0001F4CB</div><h4>꼼꼼한 학습 관리</h4><p>수업 리포트와 진도 관리로 흐름을 놓치지 않아요.</p></div>
    <div class="trust-item"><div class="ico">⏱️</div><h4>빠른 응대</h4><p>신청 후 24시간 이내 체험 수업을 안내해 드려요.</p></div>
  </div>
</section>

<section id="regions">
  <div class="head-row">
    <div><span class="eyebrow">{REGION_SHORT} 학교검색</span><h2>초등학교부터 고등학교까지, {REGION_SHORT} 학교 {len(SCHOOLS)}곳 모두</h2></div>
  </div>
  <div class="region-card" style="max-width:640px;">
    <div class="count">초등학교 {len(ELEMENTARY_NAMES)}곳 · 중학교 {len(MIDDLE_NAMES)}곳 · 고등학교 {len(HIGH_NAMES)}곳 — 어느 학교든 화상과외 매칭이 가능해요.</div>
    <div style="margin-top:16px;"><a class="cta-btn" href="regions.html">우리 학교 검색해보기 →</a></div>
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
        <li>30분 무료체험수업 먼저 받아보고 결정</li>
      </ul>
    </div>
    {{apply_form}}
  </div>
</section>
'''

APPLY_FORM = f'''<form class="form-card" action="https://formsubmit.co/{LEAD_EMAIL}" method="POST">
      <input type="hidden" name="_subject" value="[{BRAND}] 새 상담 신청">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="thanks.html">
      <div class="field"><label for="tf-name">이름</label><input id="tf-name" name="이름" type="text" placeholder="학부모님 성함" required></div>
      <div class="field"><label for="tf-phone">연락처</label><input id="tf-phone" name="연락처" type="tel" placeholder="010-0000-0000" required></div>
      <div class="field"><label for="tf-school">재학 중인 학교 ({REGION_SHORT} 소재)</label><input id="tf-school" name="학교" type="text" placeholder="예: {next((s['name'] for s in SCHOOLS if s['level'] == '중학교'), SCHOOLS[0]['name'] if SCHOOLS else '')}"></div>
      <div class="field">
        <label>학년</label>
        <div class="radio-row">
          <label><input type="radio" name="학년" value="초등">초등</label>
          <label><input type="radio" name="학년" value="중등">중등</label>
          <label><input type="radio" name="학년" value="고등">고등</label>
        </div>
      </div>
      <div class="field"><label for="tf-memo">남기실 말 (선택)</label><textarea id="tf-memo" name="메모" rows="2" placeholder="희망 과목, 시간대 등"></textarea></div>
      <button class="submit-btn" type="submit">무료 상담 신청하기</button>
      <p class="form-note">신청 즉시 담당자에게 전달되며, 24시간 이내 연락드립니다.</p>
    </form>'''

index_body = index_body.format(apply_form=APPLY_FORM)

# ---------------------------------------------------------------
# services.html / process.html / teachers.html
# ---------------------------------------------------------------
services_body = f'''
<section class="page-hero">
  <span class="eyebrow">화상과외 소개</span>
  <h1>{REGION_SHORT} 학생을 위한 화상과외, 이렇게 다릅니다</h1>
  <p>{BRAND}{BRAND_EUN} 방문 수업이나 입시 컨설팅 없이, 오직 화상과외 하나에만 집중합니다. 대신 그 안에서 {REGION_SHORT} 지역 학교 사정까지 반영한 매칭을 제공해요.</p>
</section>
<section>
  <div class="services">
    <div class="svc-card">
      <span class="tag">실시간 화상</span>
      <h3>1:1 실시간 화상 수업</h3>
      <p>정해진 시간에 화면으로 만나 실시간으로 진행돼요. 선생님이 이동할 필요가 없어 저녁·주말 등 원하는 시간대를 잡기가 더 쉽고, {REGION_SHORT} 안에서 구하기 어려운 과목·스타일의 선생님도 연결할 수 있어요.</p>
      <div class="subjects"><span>국어</span><span>영어</span><span>수학</span><span>사회</span><span>과학</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">녹화 복습</span>
      <h3>수업 녹화로 다시 보는 복습</h3>
      <p>매 수업을 녹화해 두기 때문에, 이해가 덜 된 부분만 골라 다시 볼 수 있어요. 시험 기간 벼락치기 복습에도, 결석했을 때 따라잡기에도 유용해요.</p>
      <div class="subjects"><span>단원별 복습</span><span>오답 다시보기</span></div>
    </div>
    <div class="svc-card">
      <span class="tag">지역 맞춤</span>
      <h3>{REGION_SHORT} 학교 사정을 아는 선생님</h3>
      <p>같은 화상 수업이라도 학교별 시험 범위와 난이도를 아는 선생님과 하면 훨씬 정확해요. 상담 시 재학 중인 학교를 먼저 확인하고, 그 학교 학생을 지도한 경험이 있는 선생님 위주로 매칭합니다.</p>
      <div class="subjects"><span>학교별 내신</span><span>지역 맞춤 매칭</span></div>
    </div>
  </div>
</section>
<section>
  <div class="head-row"><div><span class="eyebrow">방문 수업이 필요하시다면</span><h2>화상으로 먼저 경험해보세요</h2></div></div>
  <div class="apply-wrap" style="grid-template-columns:1fr;">
    <div>
      <p style="color:#DCEEE8;">{BRAND}{BRAND_EUN} 현재 화상과외 하나에만 집중하고 있어요. 방문 수업이 꼭 필요한 경우라면 상담 시 말씀해 주세요 — 상황에 따라 안내해 드릴 수 있는 방법을 함께 찾아볼게요.</p>
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
    <div class="p-step"><div class="n">03</div><h4>30분 무료체험수업</h4><p>정해진 시간에 화면으로 만나 30분 동안 무료로 먼저 수업을 받아봐요. 이 시간으로 선생님과의 궁합을 확인해요.</p></div>
    <div class="p-step"><div class="n">04</div><h4>숙제·오답 관리</h4><p>정식 수업을 시작하면 배운 내용을 확실히 내 것으로 만듭니다. 오답 노트와 복습 계획을 함께 챙겨요.</p></div>
    <div class="p-step"><div class="n">05</div><h4>리포트·피드백</h4><p>진행 상황을 학부모님께 정기적으로 공유합니다. 필요하면 커리큘럼을 다시 조정해요.</p></div>
  </div>
</section>
<section>
  <div class="head-row"><div><span class="eyebrow">한 가지 더</span><h2>결제는 체험 수업 다음에 결정하세요</h2></div></div>
  <div class="trust-grid" style="grid-template-columns:repeat(2,1fr);">
    <div class="trust-item"><div class="ico">\U0001F3AC</div><h4>30분 무료체험수업</h4><p>정식 신청 전에 선생님과 30분 동안 무료로 먼저 만나볼 수 있어요. 궁합이 어떤지 직접 확인해보세요.</p></div>
    <div class="trust-item"><div class="ico">\U0001F4AC</div><h4>체험 후 자유롭게 결정</h4><p>체험 수업이 마음에 들 때만 정식으로 시작하시면 돼요. 부담 갖지 않으셔도 됩니다.</p></div>
  </div>
</section>
'''

teachers_body = f'''
<section class="page-hero">
  <span class="eyebrow">선생님</span>
  <h1>검증된 선생님만 매칭에 참여합니다</h1>
  <p>학력·신원·경력 확인을 거치고, {REGION_SHORT} 학생 지도 경험이 있거나 {REGION_SHORT} 학교 사정을 파악한 선생님 위주로 화상과외를 안내해 드려요.</p>
</section>
<section>
  <div class="head-row"><div><span class="eyebrow">검증 절차</span><h2>선생님 등록 전 4단계 확인</h2></div></div>
  <div class="trust-grid" style="grid-template-columns:repeat(2,1fr);">
    <div class="trust-item"><div class="ico">\U0001F4C4</div><h4>학력 확인</h4><p>졸업증명 등 학력 서류를 확인합니다.</p></div>
    <div class="trust-item"><div class="ico">\U0001F194</div><h4>신원 확인</h4><p>본인 확인 및 신원 정보를 검증합니다.</p></div>
    <div class="trust-item"><div class="ico">\U0001F4BC</div><h4>경력 확인</h4><p>과외·강의 경력을 확인하고 전공·지도 과목을 매칭합니다.</p></div>
    <div class="trust-item"><div class="ico">\U0001F4DE</div><h4>사전 인터뷰</h4><p>화상 수업 방식과 성향을 미리 확인해 학생과의 궁합을 예측합니다.</p></div>
  </div>
</section>
<section id="teachers">
  <div class="head-row"><div><span class="eyebrow">이런 방식으로 소개돼요</span><h2>선생님 프로필 예시</h2></div></div>
  <p class="sample-note"><span class="badge">예시</span>실제 서비스에서는 신청하신 과목·학년에 맞는 선생님 프로필이 이런 카드 형태로 안내됩니다.</p>
  <div class="teachers">
    <div class="t-card"><div class="avatar">이</div><h4>이OO 선생님</h4><div class="meta">수학 · 중1~고2 · 교습경력 9년차 · 화상</div><div class="fit-score">예상 궁합도 <b class="mono">92%</b></div></div>
    <div class="t-card"><div class="avatar">오</div><h4>오OO 선생님</h4><div class="meta">영어 · 중3~고3 · 코칭 인증 · 화상</div><div class="fit-score">예상 궁합도 <b class="mono">88%</b></div></div>
    <div class="t-card"><div class="avatar">윤</div><h4>윤OO 선생님</h4><div class="meta">국어·영어·수학 · 초등~고등 · 화상</div><div class="fit-score">예상 궁합도 <b class="mono">95%</b></div></div>
  </div>
</section>
'''

# ---------------------------------------------------------------
# regions.html -> {지역} 학교검색 (search UI over all schools)
# ---------------------------------------------------------------
def regions_body_and_js():
    groups = []
    for level in ["초등학교", "중학교", "고등학교"]:
        items = [s for s in SCHOOLS if s["level"] == level]
        lis = "\n        ".join(
            '<li data-name="{name}" data-level="{level}"><a href="schools/{slug}.html">{name} <span class="arrow">→</span></a></li>'.format(
                name=s["name"], level=s["level"], slug=s["slug"]
            )
            for s in items
        )
        groups.append('''<div class="school-group" data-group="{level}" hidden>
      <h3 style="font-size:15px;margin:22px 0 10px;">{level} <span class="mono" style="font-size:12px;color:var(--muted-2);font-weight:400;">({count}곳)</span></h3>
      <ul class="school-list" id="list-{level}">
        {lis}
      </ul>
    </div>'''.format(level=level, count=len(items), lis=lis))

    body = '''
<section class="page-hero">
  <span class="eyebrow">{region} 학교검색</span>
  <h1>우리 학교, 검색해서 바로 확인하세요</h1>
  <p>초등학교 {n_es}곳, 중학교 {n_ms}곳, 고등학교 {n_hs}곳까지 {region}의 모든 학교를 안내하고 있어요. 학교 이름을 입력하면 바로 찾아드려요.</p>
</section>
<section>
  <div class="field" style="max-width:480px;margin-bottom:8px;">
    <label for="school-search">학교 이름으로 검색</label>
    <input id="school-search" type="text" placeholder="예: {sample}" autocomplete="off">
  </div>
  <p id="search-prompt" class="sample-note">학교 이름을 입력하면 결과가 나타나요.</p>
  <p id="search-empty" class="sample-note" hidden>검색 결과가 없어요. 학교 이름을 다시 확인해 주세요.</p>
  <div id="school-groups">
    {groups}
  </div>
</section>
'''.format(
        region=REGION_SHORT, n_es=len(ELEMENTARY_NAMES), n_ms=len(MIDDLE_NAMES), n_hs=len(HIGH_NAMES),
        sample=", ".join(
            sample_keyword(s["name"])
            for lvl in ["초등학교", "중학교", "고등학교"]
            for s in [next((x for x in SCHOOLS if x["level"] == lvl), None)]
            if s
        ),
        groups="\n    ".join(groups),
    )

    js = '''<script>
(function(){{
  var input = document.getElementById('school-search');
  var prompt = document.getElementById('search-prompt');
  var empty = document.getElementById('search-empty');
  var groups = document.querySelectorAll('.school-group');
  if(!input) return;
  input.addEventListener('input', function(){{
    var q = input.value.trim().toLowerCase();
    if(q === ''){{
      prompt.hidden = false;
      empty.hidden = true;
      groups.forEach(function(g){{ g.hidden = true; }});
      return;
    }}
    prompt.hidden = true;
    var anyVisible = false;
    groups.forEach(function(g){{
      var items = g.querySelectorAll('li');
      var groupHasMatch = false;
      items.forEach(function(li){{
        var name = (li.getAttribute('data-name') || '').toLowerCase();
        var match = name.indexOf(q) !== -1;
        li.hidden = !match;
        if(match) groupHasMatch = true;
      }});
      g.hidden = !groupHasMatch;
      if(groupHasMatch) anyVisible = true;
    }});
    empty.hidden = anyVisible;
  }});
}})();
</script>'''
    return body, js

regions_body, regions_js = regions_body_and_js()

# ---------------------------------------------------------------
# blog.html (index only, cards to be added over time)
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 블로그 글 목록 — 새 글은 이 리스트 맨 앞(최신순)에 추가
# 각 항목: slug, title, date(YYYY-MM-DD), category, teaser(카드용 요약), body(본문 HTML, <h2>/<p>/<strong> 등)
# ---------------------------------------------------------------
BLOG_POSTS = []  # 아래에서 append (파일 뒷부분 참고)

def blog_card(post):
    return '''<div class="article-card">
      <div class="meta">{date} · {category}</div>
      <h3>{title}</h3>
      <p>{teaser}</p>
      <a class="more" href="blog/{slug}.html">본문 보기 →</a>
    </div>'''.format(date=post["date"], category=post["category"], title=post["title"], teaser=post["teaser"], slug=post["slug"])

def build_blog_body():
    cards = "\n    ".join(blog_card(p) for p in BLOG_POSTS)
    return f'''
<section class="page-hero">
  <span class="eyebrow">블로그</span>
  <h1>{REGION_SHORT} 학교별 내신·과목별 학습 전략</h1>
  <p>{REGION_SHORT} 학교별 내신 대비, 학년별·과목별 화상과외 학습 전략을 꾸준히 올리고 있어요.</p>
</section>
<section>
  <div class="article-grid">
    <!-- BLOG_GRID_START -->
    {cards}
    <!-- BLOG_GRID_END -->
  </div>
</section>
'''

def blog_post_body(post):
    return f'''
<nav class="breadcrumb"><a href="../blog.html">블로그</a> / {post["category"]}</nav>
<section class="page-hero">
  <span class="eyebrow">{post["date"]} · {post["category"]}</span>
  <h1>{post["title"]}</h1>
</section>
<section>
  <article class="prose">
    {post["body"]}
  </article>
</section>
<section>
  <div class="apply-wrap" style="grid-template-columns:1fr;">
    <div>
      <span class="eyebrow" style="color:var(--accent-strong)">지금 확인해보세요</span>
      <h2>30분 무료체험수업 먼저 받아보세요</h2>
      <p style="color:#DCEEE8;">이름과 연락처만 남겨주시면 24시간 이내에 담당자가 연락드립니다.</p>
      <div style="margin-top:18px;"><a class="cta-btn" href="../apply.html" style="background:var(--accent);color:var(--primary-strong)!important;">무료 상담 신청하기</a></div>
    </div>
  </div>
</section>
<p style="margin-top:14px;"><a href="../blog.html">← 블로그 목록으로</a></p>
'''

# ---------------------------------------------------------------
# apply.html (noindex, standalone page reusing hero form)
# ---------------------------------------------------------------
apply_body = '''
<section class="page-hero">
  <span class="eyebrow">30분 무료체험</span>
  <h1>학습 궁합부터 확인하는 화상과외 체험 신청</h1>
  <p>이름과 연락처만 남겨주시면 24시간 이내에 담당자가 직접 연락드려요. 상담과 30분 체험 수업은 모두 무료입니다.</p>
</section>
<section>
  <div class="apply-wrap">
    <div>
      <span class="eyebrow" style="color:var(--accent-strong)">신청 전 확인해주세요</span>
      <h2>이렇게 진행됩니다</h2>
      <ul class="apply-perks">
        <li>신청 후 24시간 이내 담당자 연락</li>
        <li>학습 진단 → 선생님 추천 → 30분 무료체험수업</li>
        <li>체험 수업이 마음에 들 때만 정식으로 결정</li>
      </ul>
    </div>
    {apply_form}
  </div>
</section>
'''.format(apply_form=APPLY_FORM)

# ---------------------------------------------------------------
# school page template (level-aware, templated copy + real school name)
# ---------------------------------------------------------------
def school_body(school):
    level = school["level"]
    info = LEVEL_INFO[level]
    same_level_others = [s for s in SCHOOLS if s["level"] == level and s["slug"] != school["slug"]]
    nearby = same_level_others[:5]
    other_links = "\n        ".join(
        '<li><a href="{slug}.html">{name} <span class="arrow">→</span></a></li>'.format(slug=s["slug"], name=s["name"])
        for s in nearby
    )
    subjects_row = "".join('<span>{}</span>'.format(s) for s in info["subjects"])
    return f'''
<nav class="breadcrumb"><a href="../regions.html">{REGION_SHORT} 학교검색</a> / {REGION_FULL} · {level}</nav>
<section class="page-hero">
  <span class="eyebrow">{REGION_FULL} {level} · 화상과외</span>
  <h1>{school["name"]} 화상과외, 학교 특성부터 확인하고 시작하세요</h1>
  <p>{school["name"]} {info["stage"]} 학생을 위해, 학교 사정을 아는 선생님과 실시간 화상으로 연결해 드려요.</p>
</section>
<section>
  <div class="prose">
    <h2>{school["name"]} {info["stage"]}이 상담에서 자주 이야기하는 고민</h2>
    <p>{school["name"]} 학생과 학부모님이 상담에서 가장 많이 말씀하시는 건 <strong>{info["focus"]}</strong>이에요. 특히 <strong>{info["worry"]}</strong>을 어려워하는 경우가 많아요. 학교마다 진도와 분위기가 다르기 때문에, 같은 학년이라도 접근 방식을 다르게 가져가야 해요.</p>
    <p>{BRAND}에서는 상담 시 최근 학습 상태와 취약 부분을 먼저 확인한 뒤, {school["name"]} 같은 {level} 학생을 지도해본 경험이 있거나 {REGION_SHORT} 지역 사정을 아는 선생님을 화상으로 연결해 드립니다.</p>
    <h3>왜 화상과외가 {school["name"]} 학생에게 잘 맞을까요</h3>
    <p>{REGION_SHORT} 안에서 원하는 과목·시간대·스타일의 선생님을 구하기 어려운 경우가 많아요. 화상 수업이면 지역 제약 없이 훨씬 넓은 범위에서 맞는 선생님을 찾을 수 있고, 이동 시간이 없어 저녁 시간대도 유연하게 잡을 수 있어요. 수업은 녹화되어 복습에도 활용할 수 있습니다.</p>
    <h3>과목별 과외 안내</h3>
    <p>{school["name"]} 학생 대상으로는 아래 과목의 화상과외를 안내하고 있어요.</p>
    <div class="subjects" style="margin-bottom:6px;">{subjects_row}</div>
  </div>
</section>
<section>
  <div class="head-row"><div><span class="eyebrow">같은 급 다른 학교</span><h2>{level} 학생이 많이 찾는 학교</h2></div></div>
  <ul class="school-list" style="max-width:480px;">
    {other_links}
  </ul>
  <p style="margin-top:14px;font-size:13.5px;"><a href="../regions.html">{REGION_SHORT} 학교 전체 검색하기 →</a></p>
</section>
<section>
  <div class="apply-wrap" style="grid-template-columns:1fr;">
    <div>
      <span class="eyebrow" style="color:var(--accent-strong)">{school["name"]} 학생 학부모님께</span>
      <h2>지금 무료 상담을 신청해보세요</h2>
      <p style="color:#DCEEE8;">이름과 연락처만 남겨주시면 24시간 이내에 담당자가 연락드립니다.</p>
      <div style="margin-top:18px;"><a class="cta-btn" href="../apply.html" style="background:var(--accent);color:var(--primary-strong)!important;">무료 상담 신청하기</a></div>
    </div>
  </div>
</section>
'''

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 블로그 글 1: 군산 중학생 수학과외 (학교별 접근 차이 + 화상과외 결합)
# ---------------------------------------------------------------
BLOG_POSTS.append({
    "slug": "gunsan-jungdeung-suhak-gwaoe",
    "title": "군산 중학생 수학과외, 학교마다 접근이 달라야 하는 이유",
    "date": "2026-09-23",
    "category": "중등 수학",
    "teaser": "같은 군산이라도 중학교마다 시험 범위와 분위기가 달라요. 학교별로 어떻게 접근해야 하는지 정리했어요.",
    "body": '''
    <p><strong>군산 중학생 수학과외</strong>를 검색하시는 학부모님이라면 아마 이런 고민을 하고 계실 거예요. 옆집 아이가 다니는 학원을 그대로 보내야 할지, 아니면 우리 아이 학교 사정에 맞는 선생님을 따로 구해야 할지 말이죠.</p>
    <p>사실 정답은 후자에 가까워요. 군산 안에서도 학교마다 수학 시험 범위를 정리하는 방식, 내신 난이도, 심지어 학생들의 학습 분위기까지 꽤 다르거든요. 군산제일중학교나 군산중앙중학교처럼 사립 중학교에 다니는 학생과, 군산동산중학교·군산남중학교 같은 공립 중학교에 다니는 학생이 겪는 수학 고민은 겉보기엔 비슷해도 실제로는 결이 다릅니다. 이 글에서는 군산 중학생 수학과외를 고를 때 학교별로 어떤 점을 신경 써야 하는지, 그리고 왜 화상과외가 오히려 더 정확한 매칭을 가능하게 하는지 구체적으로 짚어드릴게요.</p>

    <h2>군산 중학생 수학과외, 왜 학교별로 접근이 달라야 할까요</h2>
    <p>군산에는 군산남중학교, 군산동산중학교, 군산산북중학교, 군산서흥중학교, 군산월명중학교, 군산자양중학교, 군산중학교, 군산진포중학교, 군산금강중학교, 나포중학교, 군산동원중학교, 옥구중학교, 임피중학교, 회현중학교 같은 공립 중학교와 군산대성중학교, 군산영광중학교, 군산제일중학교, 군산중앙중학교 같은 사립 중학교까지 총 18개 중학교가 있어요. 같은 중학교 2학년이라도 학교마다 수학 시험 문제 유형이 다르고, 서술형 비중이나 난이도 체감도 다릅니다.</p>
    <p>학원가에서 흔히 파는 "중2 수학" 커리큘럼을 그대로 적용하면, 정작 우리 아이가 다니는 학교의 시험 스타일과는 살짝 어긋나는 경우가 많아요. 예를 들어 어떤 학교는 개념 이해 위주로 출제하고, 어떤 학교는 응용·서술형 문제 비중이 높습니다. 시험 범위를 쪼개는 방식도 달라서, 한 번에 두 단원을 묶어서 보는 학교가 있는가 하면 단원별로 나눠서 자주 보는 학교도 있어요. 그래서 <strong>같은 단원을 배워도 준비하는 방식이 달라야</strong> 해요.</p>
    <p>티치핏군산에서 상담 시 재학 중인 학교를 꼭 먼저 확인하는 이유도 여기에 있습니다. 학교 이름 하나만 알아도 어떤 방식으로 수학을 준비해야 할지 힌트가 되거든요. 학교별 시험 스타일을 미리 파악하고 있으면, 처음 만나는 선생님이라도 첫 수업부터 훨씬 효율적으로 방향을 잡을 수 있어요. 반대로 이 부분을 놓치면, 아무리 좋은 선생님이어도 아이가 실제로 치를 시험과는 다른 방향으로 준비하게 될 위험이 있습니다.</p>

    <h2>사립 중학교(군산제일중학교·군산중앙중학교·군산대성중학교) 수학과외, 이런 점을 신경 써야 해요</h2>
    <p>군산제일중학교, 군산중앙중학교, 군산대성중학교 같은 사립 중학교는 진학과 성적 관리에 관심이 높은 학부모님이 많은 편이에요. 그러다 보니 학생들 사이에서도 학습 속도가 빠르게 흘러가는 경향이 있고, 심화·선행 학습 수요도 꾸준히 있습니다. 이런 환경에서는 기본 개념만 다지는 수준으로는 또래 학생들과의 격차를 따라가기 어려울 수 있어요.</p>
    <p>사립 중학교 재학생을 위한 수학과외에서는 <strong>기본 개념을 빠르게 확인하고, 곧바로 응용·심화 문제로 연결</strong>하는 방식이 필요한 경우가 많아요. 또한 학교 자체 시험 난이도가 높은 편이라면 오답 관리를 더 꼼꼼하게 챙겨야 하고, 다음 단원 선행까지 함께 고려한 커리큘럼이 도움이 됩니다. 특히 서술형·논술형 문제 비중이 높은 학교라면, 답만 맞히는 연습이 아니라 풀이 과정을 논리적으로 쓰는 연습도 함께 해야 해요.</p>
    <p>티치핏군산은 상담 시 아이의 현재 진도와 목표를 확인해서, 심화 위주로 지도해본 경험이 있는 선생님을 우선 연결해 드려요. 진도가 빠른 학교일수록 한 번 뒤처지면 따라잡기 쉽지 않기 때문에, 놓친 단원이 있다면 최대한 빨리 짚고 넘어가는 게 중요합니다. 화상 수업이면 이런 심화 지도 경험이 있는 선생님의 풀을 더 넓게 확보할 수 있다는 것도 장점이에요. 군산 지역 안에서만 찾으면 조건에 맞는 선생님이 한정적일 수밖에 없는데, 화상이라면 그 범위가 훨씬 넓어지거든요. 아이 성향과 잘 맞는 선생님을 찾는 게 결국 가장 중요한 부분이라, 선택지가 넓다는 건 그만큼 유리한 출발점이 됩니다.</p>

    <h2>공립 중학교(군산동산중학교·군산남중학교·군산월명중학교 등) 수학과외는 이렇게 다가가요</h2>
    <p>군산동산중학교, 군산남중학교, 군산월명중학교, 군산산북중학교, 군산서흥중학교처럼 공립 중학교는 학생들의 학습 수준 분포가 넓은 편이에요. 한 반 안에서도 수학을 어려워하는 학생과 심화까지 원하는 학생이 함께 있는 경우가 많죠. 그래서 <strong>기초 개념부터 확실히 다지는 것</strong>이 우선인 경우가 많습니다.</p>
    <p>특히 중1에서 중2로 넘어가는 시기에 방정식·함수 단원에서 기초가 흔들리면 이후 단원까지 연쇄적으로 어려워지는 경우가 흔해요. 공립 중학교 재학생을 위한 수학과외에서는 진도를 무리하게 빼기보다, <strong>이해가 안 된 단원을 확실히 짚고 넘어가는 방식</strong>이 더 효과적이에요. 오답 노트를 꾸준히 챙기고, 다음 시험 범위에 맞춰 복습 주기를 짜는 것도 중요합니다.</p>
    <p>공립 중학교는 학교마다 내신 평균 난이도도 조금씩 다르기 때문에, 막연히 "쉬운 학교니까 대충 해도 되겠지"라고 생각하면 오히려 등급 관리에서 손해를 볼 수 있어요. 평균이 높게 형성되는 학교라면 사소한 실수 하나로도 등급이 갈릴 수 있거든요. 학교별 시험 범위와 난이도를 확인한 뒤 맞춤 커리큘럼을 짜드리는 것도 이런 이유 때문이에요. 기초를 다지는 시기라고 해서 쉬운 문제만 반복하기보다, 실수를 줄이는 훈련까지 함께 챙기는 게 좋습니다. 특히 계산 실수나 문제 조건을 놓치는 습관은 한 번 잡아두면 이후 학년에서도 계속 도움이 되니, 초반에 꼼꼼히 짚어주는 선생님을 만나는 게 중요해요. 조급하게 진도만 나가기보다, 한 문제를 풀더라도 왜 틀렸는지 스스로 설명할 수 있을 때까지 짚어주는 방식이 장기적으로 더 큰 차이를 만듭니다.</p>

    <h2>군산 중학생 수학과외 고를 때 확인해야 할 3가지</h2>
    <p>어떤 과외든 무조건 좋은 것은 없어요. 다만 군산 중학생 수학과외를 알아보실 때 꼭 확인하면 좋은 세 가지가 있습니다.</p>
    <p><strong>첫째, 선생님이 아이가 다니는 학교의 시험 유형을 파악하고 있는지</strong> 확인하세요. 같은 "군산 중학생"이라도 학교마다 출제 방식이 다르기 때문에, 이 부분을 소홀히 하면 아무리 실력 있는 선생님이어도 효율이 떨어질 수 있어요. 상담 시 학교 이름을 먼저 물어보는 곳인지도 하나의 기준이 될 수 있습니다.</p>
    <p><strong>둘째, 정식 결제 전에 수업을 미리 받아볼 수 있는지</strong> 확인하세요. 말로 듣는 것과 실제로 수업을 받아보는 것은 느낌이 완전히 달라요. 선생님의 설명 방식이 아이 성향과 맞는지, 속도가 너무 빠르거나 느리지는 않은지는 직접 겪어봐야 알 수 있어요.</p>
    <p><strong>셋째, 숙제·오답 관리와 학부모 리포트가 있는지</strong> 확인하세요. 수업만 하고 끝나는 것과, 그 사이 학습 상태를 계속 챙겨주는 것은 성적 변화 속도에서 차이가 날 수밖에 없습니다. 특히 중학생은 자기주도로 오답을 정리하는 습관이 아직 덜 잡힌 경우가 많아서, 선생님이 이 부분을 옆에서 챙겨주는지가 꽤 중요한 변수가 돼요. 이 세 가지를 한 번에 확인할 수 있는 가장 쉬운 방법은, 정식으로 시작하기 전에 짧게라도 수업을 직접 받아보는 거예요. 아무리 후기가 좋아도 결국 우리 아이와 직접 맞춰봐야 확실히 알 수 있는 부분이니, 이 과정을 생략하지 않는 걸 추천드려요.</p>

    <h2>화상과외가 군산 중학생 수학과외에 잘 맞는 이유</h2>
    <p>화상과외라고 하면 아직 낯설어하시는 학부모님도 계세요. 하지만 군산처럼 방문 선생님을 원하는 조건(시간대, 지도 스타일, 학교 경험)에 맞게 구하기 어려운 지역에서는, 화상 수업이 오히려 <strong>훨씬 넓은 범위에서 맞는 선생님을 찾을 수 있는 방법</strong>이 돼요. 이동 시간이 없다 보니 저녁 늦은 시간대도 유연하게 잡을 수 있고, 학원 갔다 오는 시간을 아낄 수 있다는 것도 큰 장점이에요.</p>
    <p>또한 수업을 녹화해 두기 때문에, 이해가 덜 된 부분만 다시 돌려볼 수 있어요. 시험 기간에 벼락치기 복습을 할 때도, 결석했을 때 따라잡을 때도 유용합니다. 화면으로 만난다고 해서 소통이 부족한 건 아니에요. 오히려 화면 공유로 문제를 함께 짚어가며 푸는 방식이 손글씨 필기보다 명확하게 전달되는 경우도 많습니다.</p>
    <p>무엇보다 화상 수업이면 군산 안에서만 선생님을 찾을 필요가 없어요. 지도 스타일이나 경력을 더 폭넓게 비교해보고 고를 수 있고, 아이가 다니는 학교를 지도해본 경험이 있는 선생님을 만날 확률도 높아집니다. 방문이 어려운 지역이라고 해서 선택지가 좁아지는 게 아니라, 오히려 더 정확한 매칭이 가능해지는 셈이에요. 처음 화상 수업을 접하는 학생이라도 며칠만 지나면 대면 수업과 크게 다르지 않게 적응하는 경우가 많아요. 오히려 화면 너머로 조용히 집중할 수 있어서 산만함이 줄었다는 학부모님 반응도 종종 있고, 화면 녹화 덕분에 부모님도 수업 분위기를 나중에 확인해보실 수 있어요.</p>

    <h2>군산 중학생 수학과외 비용, 어떻게 판단하면 될까요</h2>
    <p>군산 중학생 수학과외 비용은 과목 수, 주당 수업 횟수, 수업 시간, 선생님 경력 등 여러 요소에 따라 달라져요. 그래서 "얼마예요?"라는 질문에 딱 잘라 답하기보다는, 아이의 현재 상황을 먼저 확인한 뒤 정확한 안내를 드리는 게 맞다고 생각해요. 예를 들어 주 1회로 시작할지, 주 2회로 집중 관리할지에 따라서도 구조가 달라지고, 단기간 내신 대비인지 장기간 실력 향상인지에 따라서도 적절한 방식이 달라져요.</p>
    <p>막연히 비싸다고 느껴서 시작을 망설이시기보다, <strong>30분 무료체험수업</strong>을 먼저 받아보시는 걸 추천드려요. 선생님과의 궁합, 수업 방식이 우리 아이한테 맞는지 확인한 뒤에 비용까지 포함해서 편하게 결정하시면 됩니다. 비용만 보고 성급하게 정하기보다, 우리 아이 학교 시험 유형을 이해하고 있는 선생님인지, 꾸준히 관리해줄 수 있는 구조인지를 함께 따져보시는 걸 권해드려요.</p>
    <p>특히 화상과외는 방문과외에 비해 이동 시간이나 교통비 부담이 없다 보니, 같은 예산으로도 더 자주 수업을 잡거나 더 경력 있는 선생님을 만날 여지가 생기는 경우가 많아요. 첫 상담 때 재학 중인 학교, 현재 성적대, 목표를 함께 말씀해주시면 그에 맞춰 현실적인 비용 구조까지 같이 안내해 드릴게요. 결제는 항상 체험 수업 이후에 결정하시면 되니 부담 갖지 않으셔도 됩니다. 궁금하신 부분이 있으면 상담 단계에서 편하게 물어봐 주세요, 비용 구조까지 투명하게 설명해 드릴게요.</p>

    <h3>자주 묻는 질문</h3>
    <p><strong>Q. 군산 어느 중학교든 매칭이 가능한가요?</strong><br>
    네, 군산 관내 중학교 18곳(군산남중학교, 군산동산중학교, 군산산북중학교, 군산서흥중학교, 군산월명중학교, 군산자양중학교, 군산중학교, 군산진포중학교, 군산금강중학교, 나포중학교, 군산동원중학교, 옥구중학교, 임피중학교, 회현중학교, 군산대성중학교, 군산영광중학교, 군산제일중학교, 군산중앙중학교) 전부 매칭 가능해요.</p>
    <p><strong>Q. 화상 수업인데 정말 효과가 있을까요?</strong><br>
    30분 무료체험수업으로 먼저 확인해보실 수 있어요. 수업은 녹화되기 때문에 복습에도 활용할 수 있고, 이동 시간이 없어 오히려 더 여유 있게 집중할 수 있다는 후기가 많아요.</p>
    <p><strong>Q. 비용은 정확히 얼마인가요?</strong><br>
    과목·시간·선생님 경력에 따라 달라지기 때문에 상담 시 안내해 드려요. 30분 무료체험수업을 먼저 받아보신 뒤 결정하시면 부담이 적어요.</p>
    ''',
})

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 블로그 글 2: 군산 초등 수학과외
# ---------------------------------------------------------------
BLOG_POSTS.append({
    "slug": "gunsan-chodeung-suhak-gwaoe",
    "title": "군산 초등 수학과외, 학습 습관부터 잡아야 하는 이유",
    "date": "2026-09-23",
    "category": "초등 수학",
    "teaser": "저학년과 고학년은 접근이 달라야 해요. 군산 초등 수학과외를 언제, 어떻게 시작하면 좋을지 정리했어요.",
    "body": '''
    <p><strong>군산 초등 수학과외</strong>를 알아보시는 학부모님 중에는 "이렇게 어린데 벌써 과외가 필요할까?" 하고 망설이시는 분들이 많아요. 맞는 고민이에요. 초등 시기에 중요한 건 어려운 문제를 많이 푸는 게 아니라, 숫자와 친해지고 스스로 생각하는 습관을 만드는 거니까요.</p>
    <p>다만 이 시기를 그냥 흘려보내면, 중학교 올라가서 갑자기 수학이 어려워졌다고 느끼는 경우가 많아요. 개정초등학교, 군산경포초등학교, 군산수송초등학교, 군산나운초등학교처럼 군산 안에서도 학교마다 학습 분위기와 진도 체감이 조금씩 다르기 때문에, 우리 아이 학교와 학년에 맞는 방식으로 시작하는 게 중요합니다. 이 글에서는 군산 초등 수학과외를 학년별로 어떻게 접근하면 좋을지, 화상과외가 어린 학생에게도 괜찮은지 구체적으로 짚어드릴게요.</p>

    <h2>군산 초등 수학과외, 왜 학습 습관부터 챙겨야 할까요</h2>
    <p>초등 수학은 중·고등 수학과 달리 시험 성적보다 <strong>학습 습관과 개념 이해</strong>가 훨씬 중요해요. 연산 속도만 빠르고 원리를 이해하지 못한 채 넘어가면, 나중에 분수·소수·도형 같은 단원에서 갑자기 막히는 경우가 많습니다. 특히 3학년 즈음부터 나오는 분수 개념은 이후 중학교 수학 전체의 기초가 되기 때문에, 이 시기에 제대로 이해하고 넘어가는 게 정말 중요해요.</p>
    <p>군산 초등 수학과외를 고민하신다면, 단순히 문제집을 많이 풀리는 곳보다는 <strong>왜 그런 답이 나오는지 설명할 수 있는지</strong>를 확인해보시는 게 좋아요. 아이가 스스로 "이래서 이렇게 되는구나"를 말할 수 있으면 제대로 이해한 거고, 그냥 풀이 과정을 외운 거라면 다음 단원에서 다시 막힐 가능성이 높습니다. 학습 습관이 한 번 잡히면 중학교, 고등학교까지 쭉 이어지기 때문에 초등 시기의 투자가 장기적으로 훨씬 크게 돌아와요.</p>
    <p>또한 초등 시기에는 <strong>매일 조금씩 꾸준히 하는 습관</strong>이 몰아서 많이 하는 것보다 훨씬 효과적이에요. 하루 30분씩이라도 정해진 시간에 수학을 접하는 루틴이 생기면, 나중에 시험 기간에 벼락치기를 하지 않아도 되는 기반이 만들어집니다. 반대로 이 시기에 수학에 대한 부담감이나 거부감이 생기면, 그걸 나중에 되돌리는 데 훨씬 더 많은 시간과 노력이 필요해요. 그래서 저희는 초등 상담 시 성적보다 먼저 아이가 수학을 대하는 태도와 습관부터 확인합니다. 습관이 자리 잡으면 그다음부터는 부모님이 매번 챙기지 않아도 아이 스스로 책상에 앉는 힘이 생겨요.</p>

    <h2>저학년(1~3학년) 군산 초등 수학과외는 이렇게 접근해요</h2>
    <p>저학년 시기에는 무엇보다 <strong>수학을 재미있어하는 마음</strong>을 지키는 게 우선이에요. 이 시기에 억지로 어려운 문제를 풀리면 오히려 수학을 싫어하게 되는 역효과가 날 수 있어요. 연산 정확도를 높이는 것도 중요하지만, 그보다 "왜 이렇게 계산하는지" 스스로 설명해보게 하는 방식이 훨씬 효과적입니다.</p>
    <p>이 시기 군산 초등 수학과외에서는 짧고 집중력 있게 진행하는 게 좋아요. 한 번에 오래 붙잡고 있기보다, 20~30분 정도 짧게 자주 만나면서 흥미를 잃지 않게 하는 방식을 추천드려요. 숫자 감각을 기르는 놀이형 문제, 생활 속 수학(시계 보기, 돈 계산 등)을 활용하면 아이가 수학을 공부가 아니라 자연스러운 활동으로 받아들이게 돼요. 이 시기에 형성된 긍정적인 경험이 앞으로 수학을 대하는 태도를 크게 좌우합니다.</p>
    <p>저학년 아이들은 집중 시간이 짧기 때문에, 한 가지 유형만 반복시키기보다 다양한 방식으로 같은 개념을 접하게 해주는 게 좋아요. 예를 들어 덧셈을 배운다면 종이에 숫자만 풀게 하지 말고, 블록이나 손가락, 그림을 함께 활용해서 여러 각도로 이해하게 도와주는 방식이에요. 선생님과의 상호작용이 활발할수록 아이가 지루해하지 않고 끝까지 집중할 수 있어요. 이 시기에는 정답을 맞히는 것보다 "왜 그렇게 생각했는지" 말해보게 하는 질문이 훨씬 중요한 역할을 합니다. 정답을 못 맞혀도 괜찮다는 분위기 속에서 아이는 오히려 더 적극적으로 생각을 표현하게 돼요.</p>

    <h2>고학년(4~6학년) 군산 초등 수학과외, 중등 대비까지 생각해야 해요</h2>
    <p>4학년부터는 분수·소수·도형·비와 비율처럼 중학교 수학의 기초가 되는 단원들이 본격적으로 나와요. 이 시기에 개념이 흔들리면 중학교에 올라가서도 계속 영향을 받기 때문에, <strong>기초를 확실히 다지는 것</strong>이 무엇보다 중요합니다. 특히 분수 연산과 도형의 넓이·부피 개념은 이후 방정식·함수를 배울 때도 계속 활용되는 기본기예요.</p>
    <p>고학년 군산 초등 수학과외에서는 슬슬 <strong>중학교 수학과 연결되는 개념</strong>을 의식하면서 지도하는 게 좋아요. 예를 들어 비와 비율 단원은 중학교 함수의 기초가 되고, 도형 단원은 이후 증명 문제의 기초가 됩니다. 6학년이라면 중학교 진학을 앞두고 학습 습관을 점검하고, 부족한 단원이 있다면 미리 보완해두는 것도 좋은 방법이에요. 무리하게 중학교 선행을 서두르기보다, 초등 과정을 확실히 마무리하는 것이 더 안정적인 출발점이 됩니다.</p>
    <p>고학년이 되면 문제 유형도 서술형이나 여러 단계를 거쳐야 풀리는 응용 문제가 늘어나요. 이때는 단순 계산 실수를 줄이는 훈련과 함께, 문제를 끝까지 읽고 무엇을 묻는지 파악하는 연습이 중요해집니다. 특히 도형의 넓이·부피처럼 공식을 암기만 해서는 응용이 안 되는 단원은, 왜 그 공식이 나왔는지 원리를 먼저 이해시키는 게 훨씬 오래 기억에 남아요. 이 시기에 수학적 사고력을 제대로 다져두면 중학교 진학 후 적응이 훨씬 수월해집니다. 6학년 2학기쯤에는 중학교 1학년 1학기 내용을 가볍게 미리 살펴보는 것도 부담 없는 선에서 도움이 될 수 있어요.</p>

    <h2>군산 초등학교별로 분위기가 다른 이유</h2>
    <p>군산에는 개정초등학교, 군산경포초등학교, 군산구암초등학교, 군산금광초등학교, 군산나운초등학교, 군산수송초등학교, 군산중앙초등학교처럼 원도심과 신흥 주거지역에 걸쳐 총 50개의 초등학교가 있어요. 학교 규모나 지역에 따라 학습 분위기가 조금씩 다르게 형성되는 경우가 많습니다. 신흥 주거단지 학교는 학부모님들의 교육 관심도가 높아 또래 학습 속도가 빠른 편일 수 있고, 원도심 학교는 상대적으로 여유 있는 분위기인 경우가 많아요.</p>
    <p>어느 쪽이 더 좋고 나쁘다는 건 아니에요. 다만 우리 아이가 다니는 학교의 분위기를 알고 있으면, 조급해할 필요 없이 아이 속도에 맞춰 계획을 세울 수 있어요. 티치핏군산에서는 상담 시 재학 중인 초등학교를 확인해서, 그 지역 분위기와 학년 수준을 고려한 선생님을 연결해 드립니다. 같은 학년이라도 학교마다 체감하는 난이도가 다를 수 있다는 걸 감안해서 커리큘럼을 조정해요.</p>
    <p>군산아리울초등학교, 군산푸른솔초등학교처럼 비교적 최근에 개교한 신흥 지역 학교도 있고, 군산초등학교, 군산중앙초등학교처럼 오랜 역사를 가진 원도심 학교도 있어요. 학교 역사나 규모가 다르다고 해서 배우는 내용 자체가 달라지는 건 아니지만, 또래 친구들 사이의 학습 분위기나 학원 이용 비율 같은 주변 환경은 확실히 차이가 나는 편이에요. 이런 배경을 알고 접근하면 아이를 다른 집 아이와 무리하게 비교하지 않고, 우리 아이만의 속도를 존중하며 계획을 세울 수 있습니다.</p>

    <h2>군산 초등 수학과외 고를 때 확인해야 할 것들</h2>
    <p>초등 수학과외는 중·고등과 확인할 포인트가 조금 달라요. <strong>첫째, 아이와 대화가 잘 통하는 선생님인지</strong>가 가장 중요해요. 아무리 설명을 잘해도 아이가 편하게 질문하지 못하는 분위기라면 효과가 떨어집니다. <strong>둘째, 진도를 억지로 빼지 않고 아이 속도에 맞춰주는지</strong> 확인하세요. 초등 시기에 무리한 진도는 오히려 역효과가 날 수 있어요.</p>
    <p><strong>셋째, 학부모님께 학습 상황을 잘 공유해주는지</strong>도 중요해요. 아이가 어느 부분을 어려워하는지, 어떤 개념을 새로 이해했는지 꾸준히 전달받으면 집에서도 자연스럽게 도와줄 수 있어요. 이 세 가지를 확인하는 가장 좋은 방법은 역시 정식 등록 전에 짧게라도 수업을 직접 받아보는 거예요. 아이 표정과 반응을 보면 이 선생님이 맞는지 금방 느낌이 오거든요.</p>
    <p>추가로 <strong>넷째, 칭찬과 격려를 적절히 활용하는 선생님인지</strong>도 살펴보시면 좋아요. 초등 시기에는 작은 성취를 자주 인정받는 경험이 자신감으로 이어지고, 그 자신감이 다시 학습 동기로 연결되는 선순환이 만들어져요. 반대로 틀린 것만 계속 지적받으면 아이가 수업 자체를 부담스러워할 수 있습니다. 아이의 강점을 먼저 알아봐주고, 약점은 부드럽게 짚어주는 방식으로 지도하는 선생님을 만나는 게 장기적으로 훨씬 좋은 결과로 이어져요. 상담 시 이런 지도 스타일에 대해 미리 물어보셔도 좋고, 체험 수업에서 직접 느껴보셔도 좋아요, 편하게 말씀해 주세요. 결국 초등 과외는 성적표보다 아이가 매주 수업을 기다리는지 여부가 가장 정직한 지표가 됩니다.</p>

    <h2>화상과외가 초등학생에게도 괜찮을까요</h2>
    <p>"어린 아이가 화면으로 집중할 수 있을까요?"라는 질문을 정말 많이 받아요. 결론부터 말씀드리면, 걱정하시는 것보다 아이들은 화면 수업에 빠르게 적응해요. 요즘 아이들은 태블릿이나 스마트기기에 이미 익숙한 세대라, 오히려 화면을 통한 학습을 자연스럽게 받아들이는 경우가 많습니다.</p>
    <p>다만 저학년일수록 <strong>짧고 상호작용이 많은 수업 방식</strong>이 중요해요. 일방적으로 설명만 듣는 방식보다, 화면에 함께 문제를 풀어보고 바로바로 질문을 주고받는 구조가 훨씬 효과적입니다. 티치핏군산은 상담 시 아이의 학년과 성향을 확인해서, 어린 학생 지도 경험이 있는 선생님을 우선 연결해 드려요. 30분 무료체험수업으로 먼저 아이가 화상 수업에 잘 적응하는지 확인해보시는 것도 좋은 방법이에요.</p>
    <p>화상과외의 또 다른 장점은 <strong>부모님이 원하시면 수업을 옆에서 지켜보거나, 녹화된 내용을 나중에 함께 확인</strong>할 수 있다는 점이에요. 어린 아이일수록 부모님이 학습 과정을 파악하고 있는 게 중요한데, 화상 수업은 이 부분에서 오히려 방문 수업보다 편리할 수 있어요. 처음 며칠은 낯설어하던 아이도 익숙해지면 화면 너머 선생님을 친근하게 느끼고, 오히려 대면보다 편하게 질문하는 경우도 많습니다. 무엇보다 이동 시간이 없어서 학교·학원 스케줄이 빡빡한 요즘 아이들에게 시간적 여유를 만들어준다는 점도 부모님들이 특히 좋아하시는 부분이에요. 걱정되신다면 30분 무료체험수업으로 먼저 확인해보시고, 그다음에 편하게 결정하시면 됩니다.</p>

    <h3>자주 묻는 질문</h3>
    <p><strong>Q. 몇 학년부터 수학과외를 시작하면 좋을까요?</strong><br>
    정해진 학년은 없어요. 다만 분수 개념이 본격적으로 나오는 3~4학년 무렵, 또는 아이가 특정 단원에서 어려움을 느끼기 시작할 때 시작하시는 경우가 많아요.</p>
    <p><strong>Q. 어린 아이가 화상 수업에 정말 집중할 수 있나요?</strong><br>
    네, 생각보다 빠르게 적응해요. 30분 무료체험수업으로 먼저 우리 아이가 어떻게 반응하는지 확인해보실 수 있어요.</p>
    <p><strong>Q. 군산 어느 초등학교든 매칭 가능한가요?</strong><br>
    네, 군산 관내 초등학교 50곳 전부 매칭 가능해요. 상담 시 재학 중인 학교를 알려주시면 그에 맞춰 안내해 드려요.</p>
    ''',
})

# ---------------------------------------------------------------
# 블로그 글 3: 군산금강중학교 국어과외
# ---------------------------------------------------------------
BLOG_POSTS.append({
    "slug": "gunsangeumgang-jungdeung-gugeo-gwaoe",
    "title": "군산금강중학교 국어과외, 문학보다 비문학에서 갈리는 이유",
    "date": "2026-09-24",
    "category": "중등 국어",
    "teaser": "군산금강중학교 국어 내신, 문학은 곧잘 하는데 비문학에서 막히는 학생이 많아요. 원인과 대처법을 정리했어요.",
    "body": '''
    <p>군산금강중학교에 다니는 자녀를 둔 학부모님이라면 <strong>군산금강중학교 국어과외</strong>를 알아보시면서 조금 의아한 지점을 발견하셨을 거예요. 아이가 소설이나 시 같은 문학 지문은 곧잘 이해하는데, 유독 설명문·논설문 같은 비문학 지문에서 시간이 오래 걸리거나 문제를 틀리는 경우가 많다는 점이에요.</p>
    <p>사실 이건 군산금강중학교 학생들만의 특징은 아니고, 중학교 국어 시험 구조 자체가 문학과 비문학을 다르게 요구하기 때문에 생기는 현상이에요. 하지만 학교마다 시험에서 비문학 지문의 길이나 문제 유형이 조금씩 다르기 때문에, 우리 아이 학교의 출제 경향을 알고 준비하는 게 훨씬 효율적입니다. 이 글에서는 군산금강중학교 학생들이 국어에서 자주 겪는 어려움과, 화상과외로 어떻게 보완할 수 있는지 정리해드릴게요.</p>

    <h2>왜 문학은 되는데 비문학에서 막힐까요</h2>
    <p>문학 지문은 등장인물의 감정선이나 이야기 흐름을 따라가면 자연스럽게 이해가 되는 경우가 많아요. 반면 비문학 지문은 정보를 논리적으로 재구성하고, 문단 간의 관계(원인-결과, 대조, 예시 등)를 파악해야 하기 때문에 훨씬 능동적인 독해 능력이 필요합니다. 평소 책을 많이 읽는 학생이라도 소설 위주로 읽었다면 비문학 독해에서는 낯설어할 수 있어요.</p>
    <p>특히 중학교 국어 시험은 지문을 얼마나 꼼꼼히, 정확하게 읽었는지를 확인하는 문제가 많아요. 단순히 "무슨 내용인지 대충 알겠다"는 수준으로는 세부 정보를 묻는 문제나 추론 문제에서 실수가 나옵니다. 비문학은 특히 한 문장이라도 놓치면 답이 완전히 달라지는 경우가 많아서, 속독보다는 정확하게 읽는 습관이 훨씬 중요해요.</p>
    <p>이런 부분은 혼자 문제집만 풀어서는 스스로 깨닫기 어려운 경우가 많아요. 옆에서 "이 문장을 왜 이렇게 이해했는지" 짚어주는 사람이 있어야 자신의 독해 습관에서 무엇이 문제인지 정확히 알 수 있습니다. 실제로 상담을 해보면, 부모님이 보시기에는 "얘가 국어를 안 좋아해서 그런가 보다" 생각하셨던 부분이 사실은 습관의 문제였던 경우가 정말 많아요. 습관은 타고나는 게 아니라 훈련으로 바꿀 수 있는 영역이라, 원인을 정확히 짚으면 생각보다 빠르게 달라지는 걸 확인하실 수 있습니다.</p>
    <p>이런 문제는 특정 학생만 겪는 게 아니라, 군산금강중학교뿐 아니라 군산 관내 여러 중학교 학생들에게서 공통적으로 나타나는 패턴이에요. 그만큼 접근법만 정확히 잡으면 누구나 개선할 수 있는 부분이라는 뜻이기도 합니다. 조급해하지 않고 차근차근 습관을 바꿔나가면 분명히 달라져요.</p>

    <h2>군산금강중학교 학생들이 국어에서 자주 겪는 고민</h2>
    <p>상담을 하다 보면 군산금강중학교 학생과 학부모님으로부터 비슷한 고민을 자주 듣게 돼요. "분명 지문은 이해했다고 생각했는데 문제를 틀린다", "시간이 부족해서 뒷부분 지문은 급하게 읽는다", "서술형 문제에서 뭘 써야 할지 감이 안 잡힌다" 같은 이야기들이에요. 이런 고민들은 사실 서로 연결되어 있는 경우가 많습니다.</p>
    <p>시간이 부족한 이유는 대부분 앞부분 지문을 정확히 이해하지 못한 채 넘어가서, 뒤에서 다시 앞으로 돌아가 확인하느라 시간을 뺏기기 때문이에요. 서술형 문제에서 막히는 이유도 지문의 핵심을 정확히 짚어내지 못했기 때문인 경우가 많고요. 결국 뿌리를 따라가 보면 "정확한 독해"라는 하나의 지점으로 모이는 경우가 대부분입니다.</p>
    <p>그래서 국어 과외에서 가장 먼저 확인해야 할 건 문제 풀이 스킬이 아니라, 지문을 어떻게 읽고 있는지 그 과정 자체예요. 아이가 실제로 어떻게 지문을 읽어나가는지 옆에서 지켜보고 습관을 교정해주는 게 성적 향상의 핵심이 됩니다. 특히 중학생은 스스로 자신의 독해 습관을 객관적으로 인식하기 어려운 나이라, 선생님이 함께 지문을 읽으며 "여기서 왜 이렇게 이해했어?"라고 물어봐주는 과정 자체가 큰 도움이 돼요. 이런 대화형 지도 방식은 혼자 문제집을 푸는 것만으로는 얻기 어려운 경험입니다.</p>
    <p>이런 고민들을 하나씩 짚어가다 보면, 결국 아이가 스스로 자신의 약점을 알아차리게 되는 순간이 와요. 그 순간부터는 부모님이나 선생님이 옆에서 계속 잔소리하지 않아도 아이 스스로 문제집을 펼치는 태도가 생기는 경우가 많습니다. 그게 국어 과외의 진짜 목표라고 생각해요.</p>

    <h2>내신 국어, 이렇게 준비하면 좋아요</h2>
    <p>군산금강중학교를 포함한 대부분의 중학교 국어 내신은 <strong>교과서 본문에 대한 정확한 이해</strong>와 <strong>학교 선생님이 수업 중 강조한 포인트</strong>가 시험에 그대로 반영되는 경우가 많아요. 그래서 교과서 밖 문제집만 열심히 푸는 것보다, 학교 수업 필기와 교과서를 꼼꼼히 복습하는 게 우선입니다.</p>
    <p>다만 최근에는 교과서 밖 지문을 활용한 낯선 문제(비문학 응용, 다른 작품과의 비교 등)도 늘어나는 추세라, 교과서 학습과 병행해서 다양한 지문을 접해보는 훈련도 필요해요. 한 지문을 여러 번 반복해서 완벽히 암기하는 방식보다는, 비슷한 유형의 다양한 지문을 접하면서 독해력 자체를 키우는 방향이 장기적으로 더 도움이 됩니다.</p>
    <p>문법 단원도 놓치기 쉬운 부분이에요. 품사, 문장 성분, 맞춤법 규정 같은 문법 영역은 암기가 필요한 부분이 많아서, 시험 직전에 몰아서 하기보다 평소에 조금씩 정리해두는 게 효율적이에요. 특히 문법은 한 번 개념을 정리해두면 이후 학년에서도 계속 활용되기 때문에, 지금 확실히 잡아두는 투자가 나중에 큰 도움이 됩니다. 학교 수업 시간에 선생님이 강조한 문법 포인트를 따로 정리해두는 습관만 들여도 시험 직전 부담이 훨씬 줄어들어요.</p>
    <p>교과서를 여러 번 읽는 것도 중요하지만, 단순히 눈으로 훑는 것과 손으로 요약하며 읽는 것은 이해도에서 큰 차이가 납니다. 짧게라도 스스로 내용을 정리해보는 습관을 들이면, 시험장에서 비슷한 문제가 나왔을 때 훨씬 빠르게 반응할 수 있어요. 이런 습관은 국어뿐 아니라 다른 과목 공부에도 그대로 이어집니다.</p>

    <h2>화상과외로 국어를 배우면 좋은 점</h2>
    <p>국어는 특히 <strong>지문을 함께 짚어가며 설명하는 과정</strong>이 중요한 과목이에요. 화상 수업에서는 화면 공유로 지문에 실시간으로 밑줄을 긋고 표시하면서 설명할 수 있어서, 어느 부분에서 이해가 어긋났는지 명확하게 짚어줄 수 있어요. 오히려 대면보다 화면으로 텍스트를 함께 보는 방식이 국어 지문 분석에는 더 잘 맞는다는 의견도 많습니다.</p>
    <p>또한 서술형 답안을 작성한 뒤 화면으로 공유해서 즉시 첨삭받을 수 있다는 것도 큰 장점이에요. 어떤 표현이 애매한지, 어떤 부분을 더 명확히 써야 하는지 그 자리에서 바로 피드백을 받을 수 있어서 학습 효율이 높아집니다. 수업을 녹화해두면 시험 전에 다시 돌려보며 놓친 부분을 복습할 수도 있어요.</p>
    <p>화상 수업이면 군산 지역 안에서만 국어 선생님을 찾을 필요도 없어져요. 국어는 특히 지도 스타일에 따라 아이와의 궁합이 크게 갈리는 과목이라, 폭넓게 비교해보고 정할 수 있다는 게 실질적인 도움이 됩니다. 이동 시간이 없다 보니 학원 두세 곳을 오가며 지쳐 있던 저녁 시간에도 편하게 수업을 잡을 수 있어서, 컨디션 좋은 상태로 공부할 수 있다는 점도 은근히 중요한 장점이에요.</p>
    <p>체험 수업 때는 아이가 평소 어떤 방식으로 지문을 읽는지 먼저 관찰한 뒤, 어느 부분에서 시간이 오래 걸리는지 함께 확인해봐요. 이 과정만으로도 학부모님들이 몰랐던 아이의 학습 패턴을 새롭게 발견하시는 경우가 많습니다. 궁금한 점은 상담 과정에서 편하게 여쭤보셔도 됩니다.</p>

    <h2>국어과외 선생님, 이런 점을 확인해보세요</h2>
    <p>국어는 수학처럼 정답이 명확하게 딱 떨어지는 과목이 아니라서, 선생님의 설명 방식이 아이와 잘 맞는지가 특히 중요해요. <strong>지문을 어떻게 분석하는지 그 사고 과정을 설명해줄 수 있는 선생님</strong>인지 확인해보세요. 단순히 정답과 오답만 짚어주는 방식으로는 다음 지문에서 똑같은 실수를 반복할 수 있어요.</p>
    <p>또한 서술형 답안 첨삭 경험이 많은 선생님인지도 중요한 기준이에요. 최근 중학교 국어 시험은 서술형 비중이 꾸준히 늘고 있어서, 논리적으로 답안을 구성하는 훈련을 꾸준히 받아본 학생과 그렇지 않은 학생 사이에 실력 차이가 크게 벌어집니다. 마지막으로, 아이의 눈높이에서 지문의 어려운 부분을 풀어서 설명해줄 수 있는지도 살펴보세요. 너무 어려운 용어로만 설명하면 오히려 아이가 흥미를 잃을 수 있고, 반대로 너무 쉽게만 접근하면 실력이 늘지 않을 수 있어서 균형이 중요합니다.</p>
    <p>결국 국어 실력은 하루아침에 만들어지지 않지만, 방향을 제대로 잡고 꾸준히 쌓아가면 반드시 눈에 보이는 변화로 돌아와요. 급한 마음에 이것저것 손대기보다, 한 가지 방법을 믿고 꾸준히 밀고 나가는 태도가 오히려 더 빠른 지름길이 되는 경우가 많습니다.</p>
    <p>특히 국어는 눈에 보이는 성적 변화가 다른 과목보다 천천히 나타나는 편이라, 조금 해보고 효과가 없다고 느껴 금방 포기하시는 경우도 있어요. 하지만 꾸준히 독해 습관을 교정한 학생일수록 나중에 고등학교 국어에서 훨씬 안정적인 모습을 보이는 경우가 많으니, 긴 호흡으로 봐주시면 좋겠습니다.</p>

    <h2>군산금강중학교 국어과외, 언제 시작하면 좋을까요</h2>
    <p>국어는 단기간에 점수가 확 오르기 어려운 과목이라, 시험 2~3주 전에 급하게 시작하기보다는 평소에 꾸준히 독해 훈련을 쌓아가는 게 가장 효과적이에요. 그렇다고 지금 성적이 낮다고 너무 늦은 건 아니에요. 정확한 독해 습관은 몇 주만 집중적으로 교정해도 눈에 띄게 달라지는 경우가 많습니다.</p>
    <p>비용은 주당 수업 횟수와 시간에 따라 달라지기 때문에, 정확한 안내는 상담 시 아이의 현재 상태를 확인한 뒤 드리고 있어요. 먼저 <strong>30분 무료체험수업</strong>으로 아이의 독해 습관을 함께 확인해보시는 걸 추천드려요. 어디서부터 보완이 필요한지 파악한 뒤에 시작하시면 훨씬 효율적입니다.</p>
    <p>상담을 망설이고 계시다면, 일단 편하게 연락 주셔서 아이 상황을 말씀해주세요. 꼭 등록하지 않으셔도 괜찮으니, 지금 어떤 부분이 걱정되시는지 편하게 이야기 나눠보시는 것만으로도 방향을 잡는 데 도움이 되실 거예요. 저희도 무리하게 등록을 권하기보다, 아이에게 정말 필요한 방식이 무엇인지 함께 고민하는 걸 더 중요하게 생각합니다.</p>
    <p>많은 학부모님들이 "국어는 선행이 의미 없지 않나요?"라고 물어보시는데, 정확히 말하면 진도를 앞서가는 선행보다는 독해력이라는 기초 체력을 미리 키워두는 개념에 가까워요. 이 기초 체력은 국어뿐 아니라 다른 과목의 교과서를 읽고 이해하는 데도 그대로 활용되기 때문에, 투자한 시간이 여러 과목에서 함께 효과를 발휘하는 경우가 많습니다. 조급하게 생각하지 마시고, 지금부터 차근차근 시작해보시는 걸 권해드려요.</p>

    <h3>자주 묻는 질문</h3>
    <p><strong>Q. 국어는 원래 과외 효과가 크지 않다고 하던데 정말인가요?</strong><br>
    독해 습관을 정확히 진단하고 교정해주면 충분히 효과를 볼 수 있어요. 다만 단기 벼락치기보다는 꾸준한 훈련이 필요한 과목이라는 점은 맞습니다.</p>
    <p><strong>Q. 서술형 첨삭도 화상으로 가능한가요?</strong><br>
    네, 화면 공유로 답안을 함께 보면서 실시간 첨삭이 가능해요. 오히려 글씨로 쓴 걸 바로 화면에 띄워 짚어주는 방식이 더 명확한 경우가 많아요.</p>
    <p><strong>Q. 군산금강중학교 학생만 가능한가요?</strong><br>
    아니요, 군산 관내 모든 중학교 학생과 매칭 가능해요. 상담 시 재학 중인 학교를 알려주시면 그에 맞춰 안내해 드립니다.</p>
    ''',
})

# ---------------------------------------------------------------
# 블로그 글 4: 군산진포중학교 영어과외
# ---------------------------------------------------------------
BLOG_POSTS.append({
    "slug": "gunsanjinpo-jungdeung-yeongeo-gwaoe",
    "title": "군산진포중학교 영어과외, 단어는 아는데 독해가 안 될 때",
    "date": "2026-09-24",
    "category": "중등 영어",
    "teaser": "단어 시험은 잘 보는데 긴 지문만 나오면 막히는 학생들, 군산진포중학교 영어과외에서 이렇게 접근해요.",
    "body": '''
    <p><strong>군산진포중학교 영어과외</strong>를 찾아보시는 학부모님들이 공통적으로 하시는 말씀이 있어요. "단어 시험은 곧잘 보는데, 막상 긴 지문이 나오면 손을 못 댄다"는 거예요. 이건 정말 흔한 케이스이고, 원인을 정확히 알면 생각보다 빠르게 해결할 수 있는 문제예요.</p>
    <p>단어를 많이 알아도 문장을 구조적으로 읽는 훈련이 안 되어 있으면, 긴 지문 앞에서 무너지는 경우가 많습니다. 특히 중학교 영어는 학년이 올라갈수록 지문 길이가 늘어나고 문법 요소가 복잡해지기 때문에, 이 시기에 독해 구조를 제대로 잡아두는 게 고등학교 영어까지 이어지는 기초가 돼요. 이 글에서는 군산진포중학교 학생들이 영어에서 자주 막히는 지점과, 화상과외로 어떻게 보완할 수 있는지 살펴볼게요.</p>

    <h2>단어는 아는데 왜 독해가 안 될까요</h2>
    <p>많은 학생들이 단어를 하나하나 번역하면서 문장을 "해석"하려고 해요. 하지만 영어 문장은 한국어와 어순이 다르기 때문에, 단어 뜻만 알고 앞에서부터 순서대로 붙이면 의미가 이상해지는 경우가 많습니다. 진짜 독해력은 단어 뜻을 아는 것과 별개로, <strong>문장 구조(주어-동사-목적어 등)를 빠르게 파악하는 능력</strong>에서 나와요.</p>
    <p>특히 관계대명사, 분사구문처럼 문장이 길어지는 구조가 나오면 어디서부터 어디까지가 한 덩어리인지 구분하지 못해서 막히는 경우가 많아요. 이런 문법 요소는 단순 암기가 아니라, 실제 문장 안에서 어떻게 쓰이는지 반복적으로 확인하면서 감을 잡아야 하는 부분이에요.</p>
    <p>또한 단어를 "뜻만" 외우고 문맥 속에서 쓰이는 걸 접해본 경험이 적으면, 같은 단어라도 문장에 따라 뉘앙스가 달라지는 걸 놓치기 쉬워요. 결국 단어 암기와 독해력은 서로 다른 능력이라, 두 가지를 다 챙기는 학습이 필요합니다. 실제로 단어 시험 점수와 지문 독해 점수가 따로 노는 학생들을 보면, 십중팔구 문장을 구조가 아니라 느낌으로 대충 읽는 습관이 원인이었어요. 이 습관을 짚어주지 않으면 아무리 단어를 많이 외워도 독해 점수는 제자리걸음일 수밖에 없습니다.</p>
    <p>이런 습관은 하루 이틀 만에 바뀌지 않지만, 매번 문장을 읽을 때마다 구조를 의식하는 연습을 반복하면 어느 순간부터 자연스럽게 눈에 들어오기 시작해요. 처음엔 답답하게 느껴져도 꾸준히 하다 보면 속도와 정확도가 함께 좋아집니다.</p>

    <h2>군산진포중학교 학생들의 영어 학습, 이런 점이 특징이에요</h2>
    <p>중학교 영어는 학교마다 내신 시험에서 서술형·문법 응용 문제의 비중이 조금씩 달라요. 어떤 학교는 교과서 본문을 거의 그대로 암기하면 풀리는 문제가 많은 반면, 어떤 학교는 처음 보는 지문에 문법을 응용해야 풀리는 문제 비중이 높습니다. 학교의 출제 스타일을 미리 파악하고 있으면 훨씬 효율적으로 준비할 수 있어요.</p>
    <p>또한 최근에는 듣기·말하기 수행평가 비중도 꾸준히 늘고 있어서, 지필고사 대비만으로는 전체 영어 성적을 관리하기 어려운 경우도 많아요. 수행평가는 꾸준한 관리가 필요한 영역이라, 시험 기간에만 집중하는 방식보다 평소 학습 루틴 안에 녹여두는 게 효과적입니다.</p>
    <p>영어는 특히 한 번 뒤처지면 다음 단원에서도 계속 영향을 받는 누적형 과목이라, 지금 막힌 부분을 빨리 짚고 넘어가는 게 중요해요. 방치하는 시간이 길어질수록 따라잡는 데 드는 노력도 커집니다. 학년이 올라갈수록 문법 요소가 계속 추가되기 때문에, 이전 학년 내용이 흔들린 채로 진도만 따라가면 어느 순간 전체가 무너지는 경우도 있어요. 그래서 중학교 초반에 기초를 다지는 시간에 충분히 투자하는 게 이후 학년의 부담을 크게 줄여줍니다.</p>
    <p>군산진포중학교 학생들을 상담하다 보면, 문법을 따로 배운 적은 있지만 실제 지문 속에서 그 문법을 알아보지 못하는 경우가 특히 많다는 걸 느껴요. 배운 지식과 실전 적용 사이의 간극을 메워주는 게 이 시기 영어 학습의 핵심 과제라고 생각합니다.</p>

    <h2>문장 구조부터 다시 잡는 학습법</h2>
    <p>독해력을 키우는 가장 확실한 방법은 <strong>짧은 문장부터 구조를 분석하는 훈련</strong>을 꾸준히 하는 거예요. 주어와 동사를 먼저 찾고, 수식어구가 어디를 꾸미는지 표시하는 연습을 반복하다 보면, 점점 긴 문장도 구조가 눈에 들어오기 시작합니다. 이건 하루아침에 되는 게 아니라 꾸준한 반복이 필요한 과정이에요.</p>
    <p>단어 암기도 무작정 뜻만 외우기보다, 예문과 함께 익히는 방식이 훨씬 오래 기억에 남고 실전 독해에도 도움이 돼요. 특히 시험에 자주 나오는 숙어·구동사 표현은 따로 정리해서 반복 노출시키는 게 효과적입니다. 문법은 규칙을 외우는 데 그치지 않고, 직접 문장을 만들어보거나 오답을 분석하면서 왜 틀렸는지 이해하는 과정이 꼭 필요해요.</p>
    <p>이 모든 과정은 혼자 하기엔 지치기 쉬워서, 옆에서 방향을 잡아주고 꾸준히 점검해주는 사람이 있으면 훨씬 수월하게 진행할 수 있어요. 특히 오답을 그냥 넘기지 않고 "왜 이렇게 해석했는지" 되짚어보는 과정을 매번 거치면, 같은 실수를 반복하는 빈도가 눈에 띄게 줄어듭니다. 이런 꼼꼼한 피드백은 대형 학원의 단체 수업에서는 챙기기 어려운 부분이라, 1:1 지도의 장점이 특히 두드러지는 영역이에요.</p>
    <p>특히 예문 없이 단어 뜻만 기계적으로 외우면 금방 잊어버리기 쉬운데, 문장 속에서 반복적으로 접하면 자연스럽게 기억에 남는 경우가 많아요. 이런 학습 방식은 처음엔 느려 보여도 장기적으로 훨씬 효율적인 방법입니다.</p>

    <h2>화상과외가 영어 독해에 특히 잘 맞는 이유</h2>
    <p>영어 지문 분석은 화면에 문장을 띄워두고 실시간으로 끊어 읽기, 구문 표시를 하면서 설명하는 방식이 특히 효과적이에요. 화상 수업에서는 화면 공유로 이런 작업을 훨씬 명확하게 할 수 있어서, 오히려 종이 위에 손으로 표시하는 것보다 시각적으로 이해하기 쉬운 경우가 많습니다.</p>
    <p>또한 발음이나 듣기 연습도 화상 환경에서 충분히 가능해요. 선생님의 발음을 바로 듣고 따라 하고, 필요하면 녹화된 수업을 다시 들으면서 반복 연습할 수 있어요. 이동 시간이 없어서 그만큼 학습에 쓸 수 있는 시간이 늘어난다는 것도 실질적인 장점입니다.</p>
    <p>군산 지역 특성상 원하는 시간대에, 원하는 지도 스타일을 가진 영어 선생님을 방문 형태로 구하기 어려운 경우가 많아요. 화상이라면 이런 제약에서 자유로워져서, 아이 성향과 잘 맞는 선생님을 만날 확률이 훨씬 높아집니다. 실제로 화상 수업을 처음 접했다가 오히려 집중이 더 잘 된다는 학생들의 후기도 자주 듣는 편이에요.</p>
    <p>군산 지역에서 원하는 시간대에, 아이와 잘 맞는 지도 스타일의 영어 선생님을 구하는 게 생각보다 쉽지 않을 때가 많아요. 화상이라면 이런 지역적 제약에서 자유로워지기 때문에, 선택의 폭이 훨씬 넓어진다는 걸 체감하실 수 있습니다.</p>
    <p>실제로 처음엔 화상 수업을 낯설어하던 학생도 몇 번 해보면 오히려 집중이 더 잘 된다고 말하는 경우가 많아요. 화면 안에 선생님과 나만 있다는 느낌이 산만함을 줄여주는 효과도 있는 것 같습니다.</p>

    <h2>영어과외 선생님 고를 때 확인할 점</h2>
    <p><strong>첫째, 문장 구조를 체계적으로 설명해줄 수 있는지</strong> 확인하세요. 단순히 해석만 알려주는 방식으로는 독해력이 늘지 않아요. <strong>둘째, 학교별 내신 출제 경향을 파악하고 있는지</strong>도 중요합니다. 군산진포중학교처럼 특정 학교 시험 스타일에 맞춘 준비가 필요하거든요.</p>
    <p><strong>셋째, 수행평가(말하기·듣기)까지 함께 챙겨주는지</strong> 확인해보세요. 지필고사만 신경 쓰다가 수행평가에서 점수를 놓치는 경우도 은근히 많습니다. 이 모든 걸 확인하는 가장 좋은 방법은 정식 등록 전에 체험 수업을 받아보는 거예요. 짧은 시간이라도 직접 수업을 받아보면, 선생님의 설명 방식이 아이에게 잘 맞는지, 속도는 적절한지 금방 느낌이 옵니다. 말로만 듣고 결정하기보다는 이 과정을 꼭 거치시길 추천드려요.</p>
    <p>무엇보다 서술형·수행평가 비중이 늘어나는 요즘 중학교 영어 시험에서는, 단순 암기보다 실제로 표현하고 활용하는 능력이 점점 더 중요해지고 있어요. 화상 수업에서는 실시간으로 말하고 쓰는 연습을 병행할 수 있어서 이런 흐름에 잘 맞습니다. 지필과 수행을 따로 준비하지 않고 함께 챙길 수 있다는 것도 장점이에요.</p>
    <p>이 세 가지 기준을 한 번에 확인하는 가장 확실한 방법은 정식 등록 전에 30분 정도 체험 수업을 받아보는 거예요. 짧은 시간이지만 선생님의 설명 방식, 아이의 반응, 수업 분위기까지 충분히 느낄 수 있습니다. 결정은 그 이후에 천천히 하셔도 늦지 않아요. 부담 갖지 마시고 편하게 신청해주세요.</p>

    <h3>자주 묻는 질문</h3>
    <p><strong>Q. 문법을 아예 모르는데 지금 시작해도 될까요?</strong><br>
    네, 기초부터 차근차근 시작하시면 됩니다. 오히려 기초가 흔들린 채로 진도만 나가는 것보다 지금 확실히 잡고 가는 게 나아요.</p>
    <p><strong>Q. 듣기·말하기 수행평가도 화상으로 준비할 수 있나요?</strong><br>
    네, 실시간 발음 교정과 듣기 훈련 모두 화상 수업으로 충분히 가능해요.</p>
    <p><strong>Q. 비용은 어느 정도인가요?</strong><br>
    과목·시간·선생님 경력에 따라 달라져서 상담 시 안내해 드려요. 30분 무료체험수업을 먼저 받아보신 후 결정하시면 됩니다.</p>
    ''',
})

# generate all pages
# ---------------------------------------------------------------
page("index.html", f"{REGION_SHORT} 과외 | 초등·중등·고등 수학 영어 1:1 화상과외 · {BRAND}", f"{REGION_SHORT} 과외를 찾고 계신가요? 초등학생부터 고등학생까지, 수학·영어·국어 등 전 과목 1:1 화상과외를 30분 무료체험수업으로 먼저 받아보세요.", "index.html",
     index_body,
     path_prefix="", canonical=BASE_URL + "/index.html")

page("services.html", f"화상과외 소개 | {BRAND}", f"{REGION_SHORT} 학생을 위한 실시간 화상과외, 녹화 복습, 지역 맞춤 매칭을 소개합니다.", "services.html",
     services_body, path_prefix="", canonical=BASE_URL + "/services.html")

page("process.html", f"매칭 방식 | {BRAND}", f"학습 진단부터 리포트까지, {BRAND}의 5단계 화상과외 매칭 프로세스를 소개합니다.", "process.html",
     process_body, path_prefix="", canonical=BASE_URL + "/process.html")

page("teachers.html", f"선생님 소개 | {BRAND}", f"학력·신원·경력 검증을 거친 {BRAND} 화상과외 선생님 매칭 기준을 소개합니다.", "teachers.html",
     teachers_body, path_prefix="", canonical=BASE_URL + "/teachers.html")

page("regions.html", f"{REGION_SHORT} 학교검색 | {BRAND}", f"{REGION_SHORT} 초·중·고 {len(SCHOOLS)}개 학교를 검색해서 바로 찾는 {BRAND} 화상과외 학교 안내입니다.", "regions.html",
     regions_body, path_prefix="", canonical=BASE_URL + "/regions.html", extra_js=regions_js)

page("blog.html", f"블로그 | {BRAND}", f"{REGION_SHORT} 학교별 내신 대비, 과목별 화상과외 학습 전략을 소개하는 {BRAND} 블로그입니다.", "blog.html",
     build_blog_body(), path_prefix="", canonical=BASE_URL + "/blog.html")

for post in BLOG_POSTS:
    page(
        "blog/{}.html".format(post["slug"]),
        "{} | {}".format(post["title"], BRAND),
        post["teaser"],
        "blog.html",
        blog_post_body(post),
        path_prefix="../",
        canonical=BASE_URL + "/blog/{}.html".format(post["slug"]),
    )

page("apply.html", f"무료 상담 신청 | {BRAND}", f"{BRAND} 화상과외 매칭 무료 상담을 신청하세요.", "apply.html",
     apply_body, path_prefix="", canonical=BASE_URL + "/apply.html", noindex=True)

thanks_body = '''
<section class="page-hero" style="text-align:center;">
  <span class="eyebrow">신청 완료</span>
  <h1>상담 신청이 접수되었습니다</h1>
  <p style="max-width:52ch;margin-inline:auto;">24시간 이내에 담당자가 남겨주신 연락처로 안내드릴게요. 잠시만 기다려 주세요.</p>
  <div style="margin-top:22px;"><a class="cta-btn" href="index.html">홈으로 돌아가기</a></div>
</section>
'''
page("thanks.html", f"신청 완료 | {BRAND}", f"{BRAND} 상담 신청이 정상적으로 접수되었습니다.", "",
     thanks_body, path_prefix="", canonical=BASE_URL + "/thanks.html", noindex=True)

for school in SCHOOLS:
    page(
        "schools/{}.html".format(school["slug"]),
        "{} 화상과외 | {}".format(school["name"], BRAND),
        "{} 학생을 위한 1:1 화상과외 매칭, {}에서 상담해보세요.".format(school["name"], BRAND),
        "regions.html",
        school_body(school),
        path_prefix="../",
        canonical=BASE_URL + "/schools/{}.html".format(school["slug"]),
    )

# ---------------------------------------------------------------
# sitemap.xml (public pages only)
# ---------------------------------------------------------------
sitemap_urls = ["index.html", "services.html", "process.html", "teachers.html", "regions.html", "blog.html"]
for school in SCHOOLS:
    sitemap_urls.append("schools/{}.html".format(school["slug"]))
for post in BLOG_POSTS:
    sitemap_urls.append("blog/{}.html".format(post["slug"]))

sitemap_items = "\n".join(
    "  <url><loc>{}/{}</loc></url>".format(BASE_URL, u) for u in sitemap_urls
)
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{}\n</urlset>\n'.format(sitemap_items)
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print("wrote sitemap.xml")

robots_txt = '''User-agent: *
Disallow: /apply.html
Disallow: /thanks.html
Allow: /

Sitemap: {}/sitemap.xml
'''.format(BASE_URL)
with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)
print("wrote robots.txt")

print("DONE - {} schools (region: {})".format(len(SCHOOLS), REGION_SLUG))
