import base64
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Vijaylal Bussa | AI Engineer", page_icon="🧠", layout="wide")

PHOTO = base64.b64encode((Path(__file__).parent / "photo.jpg").read_bytes()).decode()

LINKS = {
    "email": "mailto:vijaylalbussa@gmail.com",
    "linkedin": "https://linkedin.com/in/vijaylal-bussa",
    "github": "https://github.com/Vijaylal8055",
    "credly": "https://www.credly.com/users/vijaylal-bussa",
}

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
:root{--bg:#0D0F1F;--ink:#ECEAF6;--mute:#9A9DB8;--line:rgba(255,255,255,.09);--glass:rgba(255,255,255,.04);
--a:#7C6CFF;--b:#FF7A9C;--c:#3DE0C5;}
html{scroll-behavior:smooth}
header[data-testid="stHeader"],footer,#MainMenu,[data-testid="stToolbar"],[data-testid="stDecoration"]{display:none!important}
.stApp{background:
 radial-gradient(900px 520px at 85% -5%,rgba(124,108,255,.28),transparent 60%),
 radial-gradient(700px 480px at -5% 25%,rgba(255,122,156,.16),transparent 60%),
 radial-gradient(800px 500px at 60% 95%,rgba(61,224,197,.12),transparent 60%),var(--bg);
 background-attachment:fixed;color:var(--ink);font-family:'DM Sans',sans-serif}
.block-container{max-width:1120px!important;padding:0 1.5rem 3rem!important}
.pf *{box-sizing:border-box}
.pf a{color:inherit;text-decoration:none}
.pf :where(h1,h2,h3,p){margin:0}
.nav{position:sticky;top:12px;z-index:50;display:flex;justify-content:space-between;align-items:center;padding:12px 22px;margin-top:14px;
 border:1px solid var(--line);border-radius:16px;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);background:rgba(13,15,31,.6)}
.logo{font:800 1.15rem 'Bricolage Grotesque';letter-spacing:-.02em}
.nav .links{display:flex;gap:22px;font-size:.92rem;color:var(--mute)}
.nav .links a:hover{color:var(--ink)}
.hero{display:grid;grid-template-columns:1.25fr 1fr;gap:48px;align-items:center;padding:56px 0 40px}
.title{font:600 1.2rem 'Bricolage Grotesque';color:var(--c);margin-bottom:14px}
.status{display:inline-flex;gap:10px;align-items:center;padding:7px 14px;border:1px solid var(--line);border-radius:99px;
 background:var(--glass);font-size:.85rem;color:var(--mute)}
.dot{width:8px;height:8px;border-radius:50%;background:var(--c);box-shadow:0 0 0 0 rgba(61,224,197,.6);animation:pulse 2s infinite}
@keyframes pulse{70%{box-shadow:0 0 0 9px rgba(61,224,197,0)}100%{box-shadow:0 0 0 0 rgba(61,224,197,0)}}
.name{font:800 clamp(3rem,8vw,6.2rem)/.92 'Bricolage Grotesque';letter-spacing:-.045em;margin:22px 0 18px;
 background:linear-gradient(100deg,#fff 10%,#C9C2FF 45%,var(--b) 80%);background-size:200% 100%;
 -webkit-background-clip:text;background-clip:text;color:transparent;animation:sheen 8s ease-in-out infinite alternate}
@keyframes sheen{to{background-position:100% 0}}
.role{font:500 1.35rem/1.35 'Bricolage Grotesque';color:var(--ink);max-width:30ch}
.lede{color:var(--mute);line-height:1.65;max-width:52ch;margin-top:14px}
.aboutme{margin-top:26px;max-width:54ch}
.aboutme h3{font:700 1.1rem 'Bricolage Grotesque';margin-bottom:6px}
.aboutme p{color:var(--mute);line-height:1.65;font-size:.95rem}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
.btn{padding:12px 22px;border-radius:12px;font-weight:600;border:1px solid var(--line);background:var(--glass);transition:.2s}
.btn:hover{border-color:var(--a);transform:translateY(-2px)}
.btn.pri{background:linear-gradient(120deg,var(--a),#A06BFF 50%,var(--b));border:0;color:#fff;box-shadow:0 10px 30px -10px var(--a)}
 box-shadow:0 30px 80px -30px rgba(124,108,255,.55)}
 font:400 .74rem 'JetBrains Mono';color:var(--mute)}
.portrait{position:relative;width:100%;aspect-ratio:4/5;border-radius:26px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 80px -30px rgba(124,108,255,.6)}
.portrait img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;display:block}
.portrait:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 70%,rgba(13,15,31,.45))}
 background:var(--glass);margin:36px 0 12px}
.sec{padding-top:84px}
.sec h2{font:800 clamp(2rem,4vw,3rem)/1.05 'Bricolage Grotesque';letter-spacing:-.035em;margin-bottom:10px}
.sec .sub{color:var(--mute);max-width:60ch;line-height:1.65;margin-bottom:34px}
.story{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.card{border:1px solid var(--line);background:var(--glass);border-radius:18px;padding:26px}
.card p{color:var(--mute);line-height:1.7}
.card h3{font:700 1.25rem 'Bricolage Grotesque';margin-bottom:10px}
.job{position:relative;padding-bottom:34px}
.job:before{content:"";position:absolute;left:-41px;top:7px;width:14px;height:14px;border-radius:50%;background:var(--bg);
 border:2px solid var(--a)}
.job.now:before{background:var(--c);border-color:var(--c);box-shadow:0 0 18px var(--c)}
.job h3{font:700 1.3rem 'Bricolage Grotesque'}
.job .org{color:var(--mute);font-size:.92rem;margin:4px 0 12px}
.job ul{margin:0;padding-left:18px;color:#C3C6E0;line-height:1.7;max-width:80ch}
.job li{margin-bottom:6px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:18px}
.proj{position:relative;border:1px solid var(--line);border-radius:18px;padding:26px;background:var(--glass);transition:.25s;overflow:hidden}
.proj:hover{border-color:rgba(124,108,255,.6);transform:translateY(-4px)}
.proj.big{grid-column:span 2}
.proj h3{font:700 1.3rem 'Bricolage Grotesque';margin-bottom:8px}
.proj p{color:var(--mute);line-height:1.65;font-size:.95rem}
.proj .metric{font:500 .82rem 'JetBrains Mono';color:var(--c);margin-top:14px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
.chip{padding:5px 12px;border-radius:99px;border:1px solid var(--line);font-size:.8rem;color:#C3C6E0;background:rgba(255,255,255,.03)}
.skills{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}
.skills h3{font:700 1.05rem 'Bricolage Grotesque';margin-bottom:4px}
.cert{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:24px}
.cert .chip{border-color:rgba(61,224,197,.28)}
.contact{margin-top:90px;padding:60px 40px;border-radius:26px;text-align:center;border:1px solid var(--line);
 background:linear-gradient(135deg,rgba(124,108,255,.22),rgba(255,122,156,.14))}
.contact h2{font:800 clamp(2.2rem,5vw,3.8rem)/1 'Bricolage Grotesque';letter-spacing:-.04em;margin-bottom:14px}
.contact p{color:var(--mute);margin-bottom:26px}
.contact .cta{justify-content:center}
.foot{text-align:center;color:var(--mute);font-size:.82rem;padding:34px 0 0}
a:focus-visible{outline:2px solid var(--c);outline-offset:3px;border-radius:8px}
@media(max-width:900px){.side{order:-1}.portrait{max-width:380px;aspect-ratio:1}.hero,.story{grid-template-columns:1fr}.proj.big{grid-column:auto}.nav .links{display:none}
 .contact{padding:44px 22px}.grid{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.tl div{opacity:1;transform:none}}
</style>
"""

def chips(items, cls="chip"):
    return "".join(f'<span class="{cls}">{i}</span>' for i in items)

def job(role, org, dates, bullets, now=False):
    li = "".join(f"<li>{b}</li>" for b in bullets)
    return (f'<div class="job{" now" if now else ""}"><h3>{role}</h3><div class="org">{org} &nbsp;|&nbsp; {dates}</div><ul>{li}</ul></div>')

def project(title, desc, metric, tags, big=False):
    return (f'<div class="proj{" big" if big else ""}"><h3>{title}</h3><p>{desc}</p>'
            f'<div class="metric">{metric}</div><div class="chips">{chips(tags)}</div></div>')

nav = ('<div class="nav"><div class="logo">VB</div><div class="links">'
       '<a href="#about">About</a><a href="#experience">Experience</a><a href="#projects">Projects</a>'
       '<a href="#skills">Skills</a><a href="#contact">Contact</a></div></div>')

hero = (
    '<div class="hero"><div>'
    '<h1 class="name">Vijaylal Bussa</h1>'
    '<p class="title">AI Developer &amp; Generative AI Specialist</p>'
    '<p class="role">I build multi-agent AI systems that hold up in production.</p>'
    '<p class="lede">Forward Deployed AI Engineer and AI Data Scientist specializing in production-grade multi-agent AI, '
    'agentic-AI frameworks, Agentic RAG, AI chatbots and AI automation.</p>'
    '<div class="aboutme"><h3>About me</h3><p>I am an AI developer with 3+ years of hands-on experience building agentic and generative AI systems: '
    'multi-agent workflows, Agentic RAG pipelines, document intelligence and LLM applications. I work directly with clients and teams '
    'to take models from prototype to production, focusing on results that are fast, reliable and measurable.</p></div>'
    f'<div class="cta"><a class="btn pri" href="{LINKS["email"]}">Email me</a>'
    f'<a class="btn" href="{LINKS["github"]}" target="_blank">GitHub</a>'
    f'<a class="btn" href="{LINKS["linkedin"]}" target="_blank">LinkedIn</a></div>'
    '</div>'
    f'<div class="side"><div class="portrait"><img src="data:image/jpeg;base64,{PHOTO}" alt="Portrait of Vijaylal Bussa"></div></div></div>'
)

about = (
    '<div class="sec" id="about"><h2>What I build</h2>'
    '<p class="sub">Agents, retrieval and model serving, taken all the way to production.</p>'
    '<div class="story"><div class="card"><h3>Agentic systems</h3><p>Multi-agent workflows where a router hands each task to specialist agents, '
    'with memory, tool use and tracing built in. My latest platform runs a 12-agent setup for 500+ concurrent sessions.</p></div>'
    '<div class="card"><h3>Retrieval and models</h3><p>Agentic RAG on vector databases, fine-tuned and optimized models, and the APIs around them. '
    'I care about latency, cost and accuracy, and I measure all three.</p></div></div></div>'
)

experience = (
    '<div class="sec" id="experience"><h2>Experience</h2><p class="sub">Most recent first.</p><div class="tlw">'
    + job("AI Developer", "Independent Contractor, Remote", "Aug 2026 – Present", [
        "Built the <b>Squatch Signal Lead Generation Pipeline</b>, a Python pipeline that turns company websites into evidence-backed leads with an explainable 0–100 ICP score.",
        "Wrote a robots.txt-compliant crawler with SSRF protection, parallel workers, TTL caching and MX email validation; 21 offline tests.",
        "Designed a Supabase PostgreSQL backend with auth and row-level security; deployed on Streamlit Community Cloud with CD from GitHub.",
    ], now=True)
    + job("Forward Deployed AI Engineer", "KeeMakr.ai, Delaware, USA (Remote)", "Feb 2026 – Jul 2026", [
        "Architected <b>BTU Virtual University</b>: a multi-agent AI platform with a master agent, coach agent and 10 professor sub-agents, serving 500+ concurrent sessions.",
        "Built an agentic RAG pipeline on Supabase pgvector with sub-2-second answers and 99.5% uptime.",
        "Added LLM observability and voice interfaces; cut average LLM latency 35% with prompt caching and agent routing.",
    ])
    + job("AI Developer / AI Data Scientist", "Huly.ai, USA (Remote)", "Sep 2025 – Nov 2025", [
        "Shipped 5+ production models for content generation: 22% better accuracy, 35% faster query resolution, tracked in MLflow.",
        "Built an avatar generator with Stable Diffusion and ControlNet (40% faster); ONNX Runtime and TensorRT cut latency 30% at 1,000+ req/min.",
    ])
    + job("Machine Learning Engineer", "Unified Mentor Pvt. Ltd., Gurugram", "Apr 2025 – Jul 2025", [
        "End-to-end ML workflows with GridSearchCV and Optuna; automation cut prep time 35% and feature engineering lifted performance 18%.",
    ])
    + job("Python Full-Stack Developer", "Codegnan IT Solutions, Vijayawada", "Oct 2024 – Apr 2025", [
        "Secure Flask REST APIs with JWT, RBAC and rate limiting; MySQL tuning reduced query time 25%.",
    ])
    + job("Freelance AI Engineer", "Independent, Remote", "Jan 2023 – Oct 2024", [
        "Delivered 10+ RAG, LLM and document-intelligence solutions using LangChain, Hugging Face, FAISS and pgvector.",
    ])
    + "</div></div>"
)

projects = (
    '<div class="sec" id="projects"><h2>Selected work</h2><p class="sub">Production systems first, experiments after.</p><div class="grid">'
    + project("BTU Virtual University", "A multi-agent learning platform. A master agent routes each question, a coach agent tracks the learner, and ten professor agents answer from a shared knowledge base.",
              "500+ sessions · 99.5% uptime · &lt;2s answers", ["Multi-agent AI", "Agentic RAG", "pgvector", "LLM observability", "Voice"], big=True)
    + project("Squatch Signal: Lead Generation Pipeline", "Paste a website, get a scored prospect with ranked emails, phone, LinkedIn and buying signals such as hiring or funding.",
              "0–100 explainable ICP score", ["Python", "Streamlit", "Supabase", "RLS", "Web crawling"])
    + project("AI Avatar Generator", "Stable Diffusion and ControlNet pipeline with an optimized inference path.",
              "40% faster creation · 30% lower latency", ["Stable Diffusion", "ONNX", "TensorRT"])
    + project("Multi-Agent Orchestration", "CrewAI and LangGraph workflow with specialized agents, task routing and parallel execution.",
              "Tracked with MLflow", ["CrewAI", "LangGraph", "MLflow"])
    + project("Document Intelligence", "OCR invoice extraction that writes structured records to PostgreSQL.",
              "Invoice to database, no retyping", ["OCR", "PostgreSQL", "Python"])
    + project("Enterprise RAG Chatbot", "Retrieval QA over private documents with semantic search and grounded answers.",
              "Hugging Face + FAISS + LangChain", ["RAG", "FAISS", "LangChain"])
    + project("Fraud Detection Pipeline", "SMOTE-balanced XGBoost model served through FastAPI with real-time monitoring.",
              "Imbalanced data, live scoring", ["XGBoost", "FastAPI", "SMOTE"])
    + "</div></div>"
)

skills_data = {
    "Agentic and GenAI": ["Multi-agent systems", "Agentic RAG", "LangChain", "LangGraph", "CrewAI", "OpenAI API", "PEFT", "Prompt engineering", "AI chatbots", "AI automation"],
    "Retrieval": ["pgvector", "FAISS", "Pinecone", "ChromaDB", "Weaviate", "Supabase", "Semantic search"],
    "ML and NLP": ["PyTorch", "TensorFlow", "Scikit-learn", "XGBoost", "Hugging Face", "spaCy", "PySpark"],
    "Backend and MLOps": ["Python", "SQL", "FastAPI", "Flask", "Docker", "Kubernetes", "GitHub Actions", "MLflow", "AWS", "Azure", "GCP"],
}
skills = ('<div class="sec" id="skills"><h2>Skills and credentials</h2><p class="sub">The tools I reach for, and the certificates behind them.</p>'
          '<div class="skills">' + "".join(f'<div class="card"><h3>{k}</h3><div class="chips">{chips(v)}</div></div>' for k, v in skills_data.items()) + "</div>"
          '<div style="height:28px"></div><div class="cert">'
          + chips(["IBM: Generative AI in Action", "IBM: Machine Learning & Deep Learning", "IBM: NLP & Computer Vision", "IBM: Data Science L1 & L2",
                   "AWS Cloud Practitioner Essentials", "Azure Services Fundamentals", "Google Cloud: Generative AI Studio",
                   "Quantum Computing (WISER / Qubitech)", "Pro5ai Top 5%"]) + "</div>"
          f'<a class="btn" href="{LINKS["credly"]}" target="_blank">View badges on Credly</a></div>')

contact = (
    '<div class="contact" id="contact"><h2>Have an agent to ship?</h2>'
    '<p>Available for remote roles and contract work, starting immediately. Based in Vijayawada, India.</p>'
    f'<div class="cta"><a class="btn pri" href="{LINKS["email"]}">vijaylalbussa@gmail.com</a>'
    f'<a class="btn" href="{LINKS["linkedin"]}" target="_blank">LinkedIn</a>'
    f'<a class="btn" href="{LINKS["github"]}" target="_blank">GitHub</a>'
    f'<a class="btn" href="{LINKS["credly"]}" target="_blank">Credly</a></div></div>'
    '<div class="foot">Built with Python and Streamlit</div>'
)

st.markdown(CSS, unsafe_allow_html=True)
st.markdown('<div class="pf">' + nav + hero + about + experience + projects + skills + contact + "</div>", unsafe_allow_html=True)
