#!/usr/bin/env python3
"""Generate static HTML for denisadragomir coach site (stitch-loop without Stitch MCP)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "site" / "public"


def prefix(depth: int) -> str:
    return "../" * depth


def head(title: str, depth: int) -> str:
    p = prefix(depth)
    return f"""<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{p}css/coach.css" />
  <script src="{p}js/coach.js" defer></script>
</head>
"""


def nav(depth: int, active: str) -> str:
    p = prefix(depth)

    def link(slug: str, label: str, fname: str) -> str:
        cls = ' class="is-active"' if slug == active else ""
        return f'<a{cls} href="{p}{fname}">{label}</a>'

    links = (
        f'{link("index", "Acasă", "index.html")}\n'
        f'    {link("despre", "Despre mine", "despre-mine.html")}\n'
        f'    {link("planuri", "Planuri", "planuri-de-antrenament.html")}\n'
        f'    {link("blog", "Blog", "blog.html")}\n'
        f'    {link("contact", "Contact", "contact.html")}\n'
        f'    <a class="btn btn-primary nav-cta" href="{p}contact.html">Scrie-mi</a>'
    )

    return f"""<div class="site-header-wrap">
<header class="site-header">
  <a class="logo" href="{p}index.html">Denisa <span>Dragomir</span></a>
  <button type="button" class="nav-burger" id="nav-burger-btn" aria-expanded="false" aria-controls="primary-navigation" aria-label="Deschide meniul">
    <span class="nav-burger-box" aria-hidden="true">
      <span class="nav-burger-lines"></span>
    </span>
  </button>
</header>
<div class="nav-scrim" id="nav-scrim" aria-hidden="true"></div>
<nav class="main-nav" id="primary-navigation" aria-label="Principal">
    <div class="main-nav-drawer-head">
      <span class="main-nav-drawer-title">Meniu</span>
      <button type="button" class="nav-drawer-close" aria-label="Închide meniul">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </button>
    </div>
    <div class="main-nav-links">
    {links}
    </div>
</nav>
</div>
"""


def footer(depth: int) -> str:
    p = prefix(depth)
    return f"""<footer class="site-footer">
  <div class="inner">
    <div class="cols">
      <div class="col">
        <h3>Explorează</h3>
        <a href="{p}rezultate.html">Rezultate</a>
        <a href="{p}aparitii-media.html">Apariții media</a>
        <a href="{p}concursuri.html">Concursuri</a>
        <a href="{p}testimoniale.html">Testimoniale</a>
        <a href="{p}sponsori.html">Sponsori</a>
      </div>
      <div class="col">
        <h3>Planuri</h3>
        <a href="{p}planuri-de-antrenament.html">Toate nivelurile</a>
        <a href="{p}plan-beginners.html">Beginners</a>
        <a href="{p}plan-basic.html">Basic</a>
        <a href="{p}plan-advanced.html">Advanced</a>
        <a href="{p}plan-pro.html">Pro</a>
      </div>
      <div class="col">
        <h3>Social</h3>
        <a href="https://www.facebook.com/denisadragomir.ro" target="_blank" rel="noopener noreferrer">Facebook</a>
        <a href="https://www.instagram.com/dragomir.denisad" target="_blank" rel="noopener noreferrer">Instagram</a>
        <a href="https://denisadragomir.ro" target="_blank" rel="noopener noreferrer">Site live</a>
      </div>
    </div>
    <p class="fine">Rebuild static coach edition · generat local (fără Stitch MCP în acest mediu).</p>
  </div>
</footer>
"""


def page_shell(
    *,
    title: str,
    depth: int,
    active: str,
    h1: str,
    lede: str,
    body_html: str,
    hero_class: str = "page-hero",
) -> str:
    return (
        head(title, depth)
        + "<body>\n"
        + nav(depth, active)
        + f'<main class="page-main">\n<div class="{hero_class}">\n<h1>{h1}</h1>\n<p class="lede">{lede}</p>\n</div>\n'
        + f'<div class="page-body">\n{body_html}\n</div>\n</main>\n'
        + footer(depth)
        + "</body>\n</html>\n"
    )


def index_page() -> str:
    p = prefix(0)
    return (
        head("Denisa Dragomir — Coach alergare montană", 0)
        + "<body>\n"
        + '<section class="hero" aria-label="Acasă">\n'
        + '<div class="hero-sky" aria-hidden="true"></div>\n'
        + '<div class="hero-glow" aria-hidden="true"></div>\n'
        + '<div class="mountains" aria-hidden="true">\n'
        + '<svg viewBox="0 0 1200 320" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">\n'
        + '<path fill="#2a3f36" d="M0,320 L0,180 L120,95 L220,140 L340,60 L480,130 L620,40 L780,120 L920,50 L1040,100 L1200,30 L1200,320 Z" opacity="0.92"/>\n'
        + '<path fill="#1E2A24" d="M0,320 L0,220 L180,150 L300,200 L440,120 L600,200 L760,130 L900,190 L1080,140 L1200,160 L1200,320 Z" opacity="0.55"/>\n'
        + "</svg>\n</div>\n"
        + '<div class="trail" aria-hidden="true"></div>\n'
        + '<div class="runner" aria-hidden="true" title="Alergător pe potecă">\n'
        + '<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">\n'
        + '<circle cx="32" cy="14" r="6" fill="#1E2A24"/>\n'
        + '<path d="M28 22 L36 22 L38 34 L44 42 L40 44 L34 36 L32 48 L26 48 L28 36 L22 42 L18 40 L26 32 Z" fill="#1E2A24"/>\n'
        + '<path d="M30 48 L28 58 M36 48 L38 58 M26 32 L18 38 M38 34 L46 30" stroke="#1E2A24" stroke-width="3" stroke-linecap="round"/>\n'
        + "</svg>\n</div>\n"
        + nav(0, "index").replace('<div class="site-header-wrap"', '<div class="site-header-wrap site-header-wrap--hero"', 1)
        + '<div class="hero-inner">\n'
        + '<p class="eyebrow">Coach alergare · trail &amp; montan</p>\n'
        + "<h1>Putere calmă pe potecă și șosea.</h1>\n"
        + '<p class="lede">Planuri de antrenament gândite pentru viața ta reală — de la primii pași pe munte până la obiective ambițioase de ultramaraton. Un ritm cald, constant, susținut.</p>\n'
        + '<div class="cta-row">\n'
        + f'<a class="btn btn-primary" href="#plans">Vezi planurile</a>\n'
        + f'<a class="btn btn-ghost" href="{p}despre-mine.html">Povestea mea</a>\n'
        + "</div>\n</div>\n"
        + '<div class="strip">\n'
        + '<div class="chip"><strong>15+</strong><span>ani pe trasee, șosea și competiții internaționale</span></div>\n'
        + '<div class="chip"><strong>4</strong><span>niveluri de planuri — de la începători la pro</span></div>\n'
        + '<div class="chip"><strong>1:1</strong><span>feedback uman, nu doar fișiere descărcabile</span></div>\n'
        + "</div>\n</section>\n"
        + '<section class="plans-home" id="plans" aria-labelledby="plans-heading">\n'
        + '<div class="plans-home-inner">\n'
        + '<header class="plans-home-header">\n'
        + '<p class="plans-home-eyebrow">Pachete lunare</p>\n'
        + '<h2 id="plans-heading">Alege planul tău</h2>\n'
        + '<p class="plans-home-intro">Fiecare plan este construit pentru a te ajuta să îți atingi obiectivele, indiferent de nivelul tău.</p>\n'
        + f'<p class="plans-home-more"><a href="{p}planuri-de-antrenament.html">Compară toate nivelurile</a></p>\n'
        + "</header>\n"
        + '<div class="plans-home-grid">\n'
        + '<article class="plan-pack">\n'
        + '<p class="plan-pack-label">Explorer</p>\n'
        + '<h3 class="plan-pack-title">Beginners</h3>\n'
        + '<p class="plan-pack-tagline">Plan lunar, feedback săptămânal de bază</p>\n'
        + '<div class="plan-pack-price"><span class="plan-pack-amount">250</span><span class="plan-pack-currency">lei/lună</span></div>\n'
        + '<hr class="plan-pack-rule" />\n'
        + '<ul class="plan-pack-list">\n'
        + "<li>Ședință Skype pentru adaptarea corpului la efort</li>\n"
        + "<li>Plan de antrenament personalizat, livrat săptămânal</li>\n"
        + "<li>Monitorizare pe TrainingPeaks + grup WhatsApp</li>\n"
        + "<li>Sfaturi echipament, mobilitate și stretching</li>\n"
        + "</ul>\n"
        + f'<a class="plan-pack-btn plan-pack-btn--outline" href="{p}plan-beginners.html">Vezi planul</a>\n'
        + "</article>\n"
        + '<article class="plan-pack">\n'
        + '<p class="plan-pack-label">Peak Performance</p>\n'
        + '<h3 class="plan-pack-title">Basic</h3>\n'
        + '<p class="plan-pack-tagline">Check-in săptămânal, ghidare nutriție</p>\n'
        + '<div class="plan-pack-price"><span class="plan-pack-amount">350</span><span class="plan-pack-currency">lei/lună</span></div>\n'
        + "<p class=\"plan-pack-note\">10% reducere la plata în avans pe 3 luni — 315 lei/lună</p>\n"
        + '<hr class="plan-pack-rule" />\n'
        + '<ul class="plan-pack-list">\n'
        + "<li>Ședință Skype pentru stabilirea obiectivelor</li>\n"
        + "<li>Analiză activități la final de săptămână + feedback</li>\n"
        + "<li>Calendar competițional și sfaturi alimentație</li>\n"
        + "<li>Analiză progres la 3 luni (video call)</li>\n"
        + "</ul>\n"
        + f'<a class="plan-pack-btn plan-pack-btn--outline" href="{p}plan-basic.html">Vezi planul</a>\n'
        + "</article>\n"
        + '<article class="plan-pack plan-pack--featured">\n'
        + '<p class="plan-pack-badge">Popular</p>\n'
        + '<p class="plan-pack-label">Elite Ultra</p>\n'
        + '<h3 class="plan-pack-title">Advanced</h3>\n'
        + '<p class="plan-pack-tagline">Contact intens, analiză video, strategie de cursă</p>\n'
        + '<div class="plan-pack-price"><span class="plan-pack-amount">450</span><span class="plan-pack-currency">lei/lună</span></div>\n'
        + "<p class=\"plan-pack-note\">10% reducere la plata în avans pe 3 luni — 405 lei/lună</p>\n"
        + '<hr class="plan-pack-rule" />\n'
        + '<ul class="plan-pack-list">\n'
        + "<li>Toate beneficiile din planul Basic</li>\n"
        + "<li>Analiză activități de 2 ori pe săptămână + feedback</li>\n"
        + "<li>Ajustări ale antrenamentelor ori de câte ori e nevoie</li>\n"
        + "<li>Consiliere pre-competițională și plan de cursă</li>\n"
        + "</ul>\n"
        + f'<a class="plan-pack-btn plan-pack-btn--inverse" href="{p}plan-advanced.html">Vezi planul</a>\n'
        + "</article>\n"
        + '<article class="plan-pack">\n'
        + '<p class="plan-pack-label">Summit</p>\n'
        + '<h3 class="plan-pack-title">Pro</h3>\n'
        + '<p class="plan-pack-tagline">Tot din Advanced plus suport nutriție complet</p>\n'
        + '<div class="plan-pack-price"><span class="plan-pack-amount">600</span><span class="plan-pack-currency">lei/lună</span></div>\n'
        + "<p class=\"plan-pack-note\">10% reducere la plata în avans pe 3 luni — 540 lei/lună</p>\n"
        + '<hr class="plan-pack-rule" />\n'
        + '<ul class="plan-pack-list">\n'
        + "<li>Toate beneficiile din planul Advanced</li>\n"
        + "<li>Feedback zilnic și analiză permanentă</li>\n"
        + "<li>Video call lunar pentru analiza progresului</li>\n"
        + "<li>Sfaturi nutriție și hidratare completă</li>\n"
        + "</ul>\n"
        + f'<a class="plan-pack-btn plan-pack-btn--outline" href="{p}plan-pro.html">Vezi planul</a>\n'
        + "</article>\n"
        + "</div>\n"
        + f'<p class="plans-home-cta"><a class="btn btn-primary" href="{p}contact.html">Scrie-mi pentru înscriere</a></p>\n'
        + "</div>\n</section>\n"
        + '<section class="cards" aria-labelledby="servicii">\n'
        + '<h2 id="servicii">Cu ce te pot ajuta</h2>\n'
        + '<div class="grid">\n'
        + '<article class="card"><h3>Planuri online</h3><p>Structură clară pe săptămâni, volum progresiv și mesaje care explică „de ce” în spatele fiecărui antrenament.</p></article>\n'
        + '<article class="card"><h3>Montan &amp; ultra</h3><p>Diferență de nivel, denivelate, nutriție la efort lung — experiență trăită la concursuri și campionate.</p></article>\n'
        + '<article class="card"><h3>Încredere măsurată</h3><p>Rezultate, media și testimoniale — transparență despre ce înseamnă să lucrezi cu mine.</p></article>\n'
        + "</div>\n</section>\n"
        + footer(0)
        + "</body>\n</html>\n"
    )


def main() -> None:
    (PUB / "css").mkdir(parents=True, exist_ok=True)
    (PUB / "js").mkdir(parents=True, exist_ok=True)
    (PUB / "concurs").mkdir(parents=True, exist_ok=True)

    pages: list[tuple[Path, str]] = []

    pages.append((PUB / "index.html", index_page()))

    pages.append(
        (
            PUB / "despre-mine.html",
            page_shell(
                title="Despre mine — Denisa Dragomir",
                depth=0,
                active="despre",
                h1="Despre mine",
                lede="Alergătoare, antrenoare, om care își construiește sezoanele cu răbdare și curiozitate.",
                body_html="""<p class="lead">Cred în progres măsurabil, nu în promisiuni goale. Lucrez cu alergători care vor claritate: ce facem săptămâna asta, de ce, și cum știm că mergem în direcția bună.</p>
<p>Pe munte și la ultramaraton am învățat că respectul pentru recuperare și nutriție face diferența la linia de sosire — la fel și în viața de zi cu zi a unui plan online.</p>
<h2>Ce poți aștepta</h2>
<ul>
<li>comunicare directă, în română</li>
<li>planuri care se adaptează jobului, familiei și oboselii reale</li>
<li>accent pe trail și denivelat, fără să neglijăm baza aerobă</li>
</ul>
<p><a class="btn btn-primary" href="planuri-de-antrenament.html">Vezi planurile</a></p>""",
            ),
        )
    )

    pages.append(
        (
            PUB / "rezultate.html",
            page_shell(
                title="Rezultate — Denisa Dragomir",
                depth=0,
                active="",
                h1="Rezultate",
                lede="Momente de pe traseu — podiumuri, încheieri, învățăminte.",
                body_html="""<p class="lead">Această pagină este un placeholder de structură pentru rebuild. Conținutul detaliat (cronologie, clasamente, fotografii) poate fi migrat din site-ul WordPress.</p>
<h2>2020–2026</h2>
<ul>
<li>Ultramaraton &amp; skyrunning — selecție de concursuri internaționale</li>
<li>National &amp; regional — reprezentare și clasamente</li>
</ul>
<p><a href="concursuri.html">Citește povești de concurs</a></p>""",
            ),
        )
    )

    pages.append(
        (
            PUB / "aparitii-media.html",
            page_shell(
                title="Apariții media — Denisa Dragomir",
                depth=0,
                active="",
                h1="Apariții media",
                lede="Interviuri, articole, podcasturi — vocea mea despre alergare și disciplină.",
                body_html="""<p class="lead">Placeholder: listează aici aparițiile de pe denisadragomir.ro (link extern sau PDF).</p>
<ul>
<li>Emisiuni TV și radio</li>
<li>Articole în presa sportivă</li>
<li>Podcasturi despre alergare montană</li>
</ul>""",
            ),
        )
    )

    pages.append(
        (
            PUB / "concursuri.html",
            page_shell(
                title="Concursuri — Denisa Dragomir",
                depth=0,
                active="",
                h1="Concursuri",
                lede="Experiențe care mi-au definit sezoanele — poți citi relatări detaliate.",
                body_html="""<div class="plan-grid">
<a class="plan-card" href="concurs/limone-extreme-skyrunning.html"><div class="tier">Limone Extreme 2019</div><div class="meta">Skyrunning · Italia</div></a>
<a class="plan-card" href="concurs/campionatul-mondial-de-ultramarathon.html"><div class="tier">Campionatul Mondial Ultramarathon</div><div class="meta">Relatare competiție</div></a>
<a class="plan-card" href="concurs/giir-di-mont.html"><div class="tier">Giir di Mont</div><div class="meta">Ultra în munți</div></a>
</div>""",
            ),
        )
    )

    concurs_bodies = {
        "limone-extreme-skyrunning.html": (
            "Limone Extreme 2019",
            "Skyrunning la înălțime — o lecție despre concentrare și ritm.",
            """<p class="lead">Relatare scurtă (placeholder): traseu, altitudine, ce a mers bine, ce ai schimba la pregătire.</p>
<p>Poți înlocui acest text cu conținutul publicat pe WordPress, păstrând SEO și imagini.</p>
<h2>Takeaways pentru alergători</h2>
<ul>
<li>gestionarea segmentelor tehnice</li>
<li>nutriție la cald/rece</li>
<li>psihologie la start în masă</li>
</ul>""",
        ),
        "campionatul-mondial-de-ultramarathon.html": (
            "Campionatul Mondial Ultramarathon",
            "Când startul e global, pregătirea e locală — zi de zi.",
            """<p class="lead">Placeholder pentru relatarea completă a experienței la campionat.</p>
<p>Include clasament, link către organizator, și lecții pentru planurile tale de antrenament.</p>""",
        ),
        "giir-di-mont.html": (
            "Giir di Mont",
            "Ultra cu suflet alpin — economie de efort pe distanță lungă.",
            """<p class="lead">Placeholder: poveste personală + sfaturi practice pentru ture lungi în Carpați sau în Alpi.</p>
<p>Legătură cu <a href="../plan-advanced.html">planul Advanced</a> sau <a href="../plan-pro.html">Pro</a> pentru alergători experimentați.</p>""",
        ),
    }

    for fname, (h1, lede, body) in concurs_bodies.items():
        pages.append(
            (
                PUB / "concurs" / fname,
                page_shell(
                    title=f"{h1} — Denisa Dragomir",
                    depth=1,
                    active="",
                    h1=h1,
                    lede=lede,
                    body_html=body,
                ),
            )
        )

    pages.append(
        (
            PUB / "testimoniale.html",
            page_shell(
                title="Testimoniale — Denisa Dragomir",
                depth=0,
                active="",
                h1="Testimoniale",
                lede="Vocea celor cu care am împărțit kilometri și obiective.",
                body_html="""<div class="quote">„Planul m-a ajutat să nu mai sar peste recuperare. În sfârșit progres constant.”<cite>— Alergătoare, plan Basic</cite></div>
<div class="quote">„Explicațiile din săptămână mă fac să înțeleg de ce există fiecare alergare.”<cite>— Alergător, plan Advanced</cite></div>
<p class="lead">Înlocuiește cu testimoniale reale de pe site-ul curent.</p>""",
            ),
        )
    )

    plan_hub = """<p class="lead">Alege nivelul care reflectă unde ești acum — volumul, disponibilitatea și obiectivul.</p>
<div class="plan-grid">
<a class="plan-card" href="plan-beginners.html"><div class="tier">Beginners</div><div class="meta">Bază aerobă, obiceiuri, primii pași montan</div></a>
<a class="plan-card" href="plan-basic.html"><div class="tier">Basic</div><div class="meta">Consistență și structură săptămânală</div></a>
<a class="plan-card" href="plan-advanced.html"><div class="tier">Advanced</div><div class="meta">Volum mai mare, ținte de concurs</div></a>
<a class="plan-card" href="plan-pro.html"><div class="tier">Pro</div><div class="meta">Obiective ambițioase, ultra &amp; skyrunning</div></a>
</div>
<h2>Întrebări frecvente</h2>
<p><strong>Cum primesc planul?</strong> Placeholder — descrie procesul (email, platformă, plată).</p>
<p><strong>Pot schimba nivelul?</strong> Placeholder — politică de upgrade/downgrade.</p>"""

    pages.append(
        (
            PUB / "planuri-de-antrenament.html",
            page_shell(
                title="Planuri de antrenament — Denisa Dragomir",
                depth=0,
                active="planuri",
                h1="Planuri de antrenament",
                lede="De la început calm până la sezoane exigente — același limbaj, alt volum.",
                body_html=plan_hub,
            ),
        )
    )

    tiers = [
        (
            "plan-beginners.html",
            "Plan Beginners",
            "Fundație: respirație, ritm, primele ture ușoare pe deal.",
            "<p class=\"lead\">4–5 zile de alergare ușoară, mers alert, exerciții de mobilitate. Ideal dacă revii după pauză sau vrei să intri civilizat pe potecă.</p><p><a class=\"btn btn-primary\" href=\"contact.html\">Întreabă disponibilitatea</a></p>",
        ),
        (
            "plan-basic.html",
            "Plan Basic",
            "Structură clară: volum progresiv, o zi de calitate, recuperare respectată.",
            "<p class=\"lead\">Include o alergare mai lungă la weekend și introducere ușoară de deal/potecă.</p><p><a class=\"btn btn-primary\" href=\"contact.html\">Întreabă disponibilitatea</a></p>",
        ),
        (
            "plan-advanced.html",
            "Plan Advanced",
            "Pentru alergători cu istoric — două sesiuni de calitate, volum mediu-mare.",
            "<p class=\"lead\">Potrivit pentru semi-maraton până la maraton sau trail mediu, cu atenție la somn și stres.</p><p><a class=\"btn btn-primary\" href=\"contact.html\">Întreabă disponibilitatea</a></p>",
        ),
        (
            "plan-pro.html",
            "Plan Pro",
            "Ultra și skyrunning — volum, vertical, periodizare fină.",
            "<p class=\"lead\">Necesită experiență anterioară și timp de recuperare real. Discutăm obiectivul înainte de start.</p><p><a class=\"btn btn-primary\" href=\"contact.html\">Întreabă disponibilitatea</a></p>",
        ),
    ]
    for fname, h1, lede, body in tiers:
        pages.append(
            (
                PUB / fname,
                page_shell(
                    title=f"{h1} — Denisa Dragomir",
                    depth=0,
                    active="planuri",
                    h1=h1,
                    lede=lede,
                    body_html=body + '<p><a href="planuri-de-antrenament.html">← Toate planurile</a></p>',
                ),
            )
        )

    blog_body = """<p class="lead">Articole despre antrenament, nutriție la efort lung și povești de concurs.</p>
<div class="grid">
<article class="card"><h3>Cum îți alegi primul ultra</h3><p>Checklist mental și fizic înainte să apeși „înscriere”.</p></article>
<article class="card"><h3>Deal sau plat — cum împarți săptămâna</h3><p>Echilibru între vertical și viteză pe șosea.</p></article>
<article class="card"><h3>Recuperarea pe care o sari</h3><p>Somnul și mersul ca parte din plan.</p></article>
</div>
<p><em>Postările complete pot fi migrate din WordPress sau legate extern.</em></p>"""

    pages.append(
        (
            PUB / "blog.html",
            page_shell(
                title="Blog — Denisa Dragomir",
                depth=0,
                active="blog",
                h1="Blog",
                lede="Note scurte, tehnice și sincere despre alergare.",
                body_html=blog_body,
            ),
        )
    )

    pages.append(
        (
            PUB / "sponsori.html",
            page_shell(
                title="Sponsori — Denisa Dragomir",
                depth=0,
                active="",
                h1="Sponsori",
                lede="Parteneri care susțin performanța responsabilă.",
                body_html="""<p class="lead">Înlocuiește placeholder-ele cu logo-uri și link-uri reale.</p>
<div class="sponsor-row">
<div class="sponsor-placeholder">Logo partener</div>
<div class="sponsor-placeholder">Logo partener</div>
<div class="sponsor-placeholder">Logo partener</div>
</div>
<p><a class="btn btn-primary" href="mailto:contact@denisadragomir.ro">Propune un parteneriat</a> <span style="color:var(--slate);font-size:0.9rem">(actualizează adresa)</span></p>""",
            ),
        )
    )

    contact_body = """<p class="lead">Scrie-mi pentru planuri, întrebări sau colaborări. Formularul este demonstrativ — conectează backend sau serviciu de email.</p>
<form action="#" method="post">
<div class="form-row"><label for="n">Nume</label><input id="n" name="name" type="text" autocomplete="name" required /></div>
<div class="form-row"><label for="e">Email</label><input id="e" name="email" type="email" autocomplete="email" required /></div>
<div class="form-row"><label for="m">Mesaj</label><textarea id="m" name="message" required></textarea></div>
<button class="btn btn-primary" type="submit">Trimite</button>
</form>"""

    pages.append(
        (
            PUB / "contact.html",
            page_shell(
                title="Contact — Denisa Dragomir",
                depth=0,
                active="contact",
                h1="Contact",
                lede="Hai să vorbim despre obiectivul tău și cum putem lucra împreună.",
                body_html=contact_body,
            ),
        )
    )

    for path, html in pages:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")

    print(f"Wrote {len(pages)} pages under {PUB}")


if __name__ == "__main__":
    main()
