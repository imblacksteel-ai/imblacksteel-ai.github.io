"""Build the static SD Importer pages (home, support, privacy) in every language.

    python3 tools/build_sdimporter.py

Writes sd-importer/**/index.html. Edit tools/sdimporter_content.py for text.
The app's source is https://github.com/imblacksteel-ai/photo-manager.
"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sdimporter_content import EFFECTIVE_DATE, LANGUAGES, T  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "sd-importer")
BASE = "/sd-importer"
SITE = "https://imblacksteel-ai.github.io"
REPO = "https://github.com/imblacksteel-ai/photo-manager"
ISSUES_URL = f"{REPO}/issues"
RELEASES_URL = f"{REPO}/releases/latest"
# Set this once the app is live on the Mac App Store; until then the button is hidden.
APP_STORE_URL = ""

ICON_VERSION = 1
PAGES = ("home", "support", "privacy")


def esc(text):
    return html.escape(text, quote=True)


def page_path(lang, page):
    return f"{BASE}/{lang}/" if page == "home" else f"{BASE}/{lang}/{page}/"


def language_menu(current, page):
    current_attr = ' aria-current="page"'
    items = "".join(
        f'<a href="{page_path(code, page)}" lang="{meta[0]}"'
        f'{current_attr if code == current else ""}>{esc(meta[1])}</a>'
        for code, meta in LANGUAGES.items()
    )
    return f'<nav class="languages" aria-label="{esc(T[current]["language"])}">{items}</nav>'


def contact_block(lang):
    t = T[lang]
    return (f'<section class="card"><h2>{esc(t["contact"])}</h2><p>{esc(t["contact_note"])}</p>'
            f'<a class="button" href="{ISSUES_URL}" rel="noopener">{esc(t["contact_button"])}</a></section>')


def layout(lang, page, title, body):
    html_lang, _, direction, app_name = LANGUAGES[lang]
    t = T[lang]
    alternates = "".join(
        f'<link rel="alternate" hreflang="{meta[0]}" href="{SITE}{page_path(code, page)}">'
        for code, meta in LANGUAGES.items()
    )
    nav = (
        f'<nav class="pages">'
        f'<a href="{page_path(lang, "home")}">{esc(app_name)}</a>'
        f'<a href="{page_path(lang, "support")}">{esc(t["support"])}</a>'
        f'<a href="{page_path(lang, "privacy")}">{esc(t["privacy"])}</a>'
        f"</nav>"
    )
    return f"""<!doctype html>
<html lang="{html_lang}" dir="{direction}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(t["tagline"])}">
<link rel="icon" type="image/png" href="{BASE}/assets/favicon.png?v={ICON_VERSION}">
<link rel="apple-touch-icon" href="{BASE}/assets/apple-touch-icon.png?v={ICON_VERSION}">
<link rel="stylesheet" href="{BASE}/assets/style.css">
<link rel="canonical" href="{SITE}{page_path(lang, page)}">
{alternates}
</head>
<body>
<header class="top">
<a class="brand" href="{page_path(lang, "home")}"><img src="{BASE}/assets/icon-256.png?v={ICON_VERSION}" alt="" width="40" height="40"><span>{esc(app_name)}</span></a>
{nav}
</header>
<main>
{body}
</main>
<footer>
{language_menu(lang, page)}
<p>© 2026 SD Importer</p>
</footer>
</body>
</html>
"""


def home(lang):
    t = T[lang]
    app_name = LANGUAGES[lang][3]
    intro = "".join(f"<p>{esc(p)}</p>" for p in t["intro"])
    features = "".join(f"<li>{esc(f)}</li>" for f in t["features"])
    store = f'<a class="button" href="{APP_STORE_URL}" rel="noopener">Mac App Store</a>' if APP_STORE_URL else ""
    body = f"""<section class="hero">
<img src="{BASE}/assets/icon-256.png?v={ICON_VERSION}" alt="{esc(app_name)}" width="128" height="128">
<h1>{esc(app_name)}</h1>
<p class="tagline">{esc(t["tagline"])}</p>
</section>
<section class="card">{intro}<ul class="features">{features}</ul></section>
<section class="links">
{store}
<a class="button{' secondary' if store else ''}" href="{RELEASES_URL}" rel="noopener">{esc(t["github_release"])}</a>
<a class="button secondary" href="{page_path(lang, "support")}">{esc(t["support"])}</a>
<a class="button secondary" href="{page_path(lang, "privacy")}">{esc(t["privacy"])}</a>
</section>"""
    return layout(lang, "home", f"{app_name} – {t['tagline']}", body)


def support(lang):
    t = T[lang]
    app_name = LANGUAGES[lang][3]
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in t["faq"])
    body = f"""<h1>{esc(app_name)} {esc(t["support"])}</h1>
<section class="card"><h2>{esc(t["faq_title"])}</h2>{faq}</section>
{contact_block(lang)}"""
    return layout(lang, "support", f"{t['support']} – {app_name}", body)


def privacy(lang):
    t = T[lang]
    app_name = LANGUAGES[lang][3]
    sections = "".join(
        f"<h2>{esc(heading)}</h2>" + "".join(f"<p>{esc(p)}</p>" for p in paragraphs)
        for heading, paragraphs in t["privacy_sections"]
    )
    body = f"""<h1>{esc(app_name)} {esc(t["privacy"])}</h1>
<p class="meta">{esc(t["effective"])}: {esc(EFFECTIVE_DATE[lang])}</p>
<section class="card prose">{sections}</section>
{contact_block(lang)}"""
    return layout(lang, "privacy", f"{t['privacy']} – {app_name}", body)


def redirect(page):
    """Language-neutral URL for store listings; sends visitors to their language."""
    links = "".join(
        f'<li><a href="{page_path(code, page)}" lang="{meta[0]}">{esc(meta[1])}</a></li>'
        for code, meta in LANGUAGES.items()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SD Importer</title>
<link rel="stylesheet" href="{BASE}/assets/style.css">
<script>
(function () {{
  var langs = navigator.languages || [navigator.language || "en"];
  var pick = "en";
  for (var i = 0; i < langs.length; i++) {{
    var l = langs[i].toLowerCase();
    if (l.indexOf("zh") === 0) {{
      pick = /hant|tw|hk|mo/.test(l) ? "zh-hant" : "zh-hans"; break;
    }}
    var base = l.split("-")[0];
    if (["en", "ja", "ko"].indexOf(base) !== -1) {{ pick = base; break; }}
  }}
  location.replace("{BASE}/" + pick + "/{'' if page == 'home' else page + '/'}");
}})();
</script>
</head>
<body><main><h1>SD Importer</h1><ul class="language-list">{links}</ul></main></body>
</html>
"""


def write(rel, content):
    path = os.path.join(OUT, rel, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    for lang in LANGUAGES:
        write(lang, home(lang))
        write(f"{lang}/support", support(lang))
        write(f"{lang}/privacy", privacy(lang))
    write("", redirect("home"))
    write("support", redirect("support"))
    write("privacy", redirect("privacy"))
    print(f"Built {len(LANGUAGES) * len(PAGES) + 3} pages.")
