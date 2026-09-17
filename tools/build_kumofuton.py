"""Build the static Kumofuton pages (home, support, privacy) in every language.

    python3 tools/build_kumofuton.py

Writes kumofuton/**/index.html. Edit tools/kumofuton_content.py for text and
CONTACT_FORM_URL below for the contact form.
"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from kumofuton_content import EFFECTIVE_DATE, LANGUAGES, T  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "kumofuton")
BASE = "/kumofuton"
SITE = "https://imblacksteel-ai.github.io"

# Contact forms, one Google Form per language, created by
# kumofuton/tools/google_forms/create_forms.gs in the app repository.
CONTACT_FORM_URLS = {
    "en": "https://docs.google.com/forms/d/e/1FAIpQLSf9jJMpZbI1oEfFb9UMc_7qvD7_MdS1RcZhGjVnbNcBV5UOqQ/viewform",
    "ja": "https://docs.google.com/forms/d/e/1FAIpQLSdm7jJsmeIFo4DUIb2kGfqSsR592Pr0oKRM7F7bopLs-wCbOQ/viewform",
    "ko": "https://docs.google.com/forms/d/e/1FAIpQLSerNjHUrUFcKzecekg7_WHg1SPqWvqdH0h9XsToFQx-Oushdg/viewform",
    "zh-hans": "https://docs.google.com/forms/d/e/1FAIpQLSfP9BkZrxL1VKyK8iE8xclaCoxankPUd9hRONSYjpGR6ec0Kw/viewform",
    "zh-hant": "https://docs.google.com/forms/d/e/1FAIpQLSemcI838S8zMIPUEIM7X8Wroj7oeMnkbRWIdvRhQP1uwNzHlA/viewform",
    "fr": "https://docs.google.com/forms/d/e/1FAIpQLSf_z0vMkI5Ev4PtzUp-p_7nG6-1ifIgNTiIC-o7Jx0iF2s5kg/viewform",
    "de": "https://docs.google.com/forms/d/e/1FAIpQLSe5RHy3rk27GrdMORxgkIEj5rC7_h9w_tV82x4YViKwZr-8UA/viewform",
    "ar": "https://docs.google.com/forms/d/e/1FAIpQLScfCpE2F7dPcQFZF-fpDVWf1UEUlQY9Nnnx_NoMIhw2TpyRIA/viewform",
}

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
    button = f'<a class="button" href="{esc(CONTACT_FORM_URLS[lang])}" rel="noopener">{esc(t["contact"])}</a>'
    return f'<section class="card"><h2>{esc(t["contact"])}</h2><p>{esc(t["contact_note"])}</p>{button}</section>'


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
<link rel="icon" type="image/png" href="{BASE}/assets/favicon.png">
<link rel="apple-touch-icon" href="{BASE}/assets/apple-touch-icon.png">
<link rel="stylesheet" href="{BASE}/assets/style.css">
<link rel="canonical" href="{SITE}{page_path(lang, page)}">
{alternates}
</head>
<body>
<header class="top">
<a class="brand" href="{page_path(lang, "home")}"><img src="{BASE}/assets/icon-256.png" alt="" width="40" height="40"><span>{esc(app_name)}</span></a>
{nav}
</header>
<main>
{body}
</main>
<footer>
{language_menu(lang, page)}
<p>© 2026 Kumofuton</p>
</footer>
</body>
</html>
"""


def home(lang):
    t = T[lang]
    app_name = LANGUAGES[lang][3]
    intro = "".join(f"<p>{esc(p)}</p>" for p in t["intro"])
    features = "".join(f"<li>{esc(f)}</li>" for f in t["features"])
    body = f"""<section class="hero">
<img src="{BASE}/assets/icon-256.png" alt="{esc(app_name)}" width="128" height="128">
<h1>{esc(app_name)}</h1>
<p class="tagline">{esc(t["tagline"])}</p>
</section>
<section class="card">{intro}<ul class="features">{features}</ul></section>
<section class="links">
<a class="button" href="{page_path(lang, "support")}">{esc(t["support"])}</a>
<a class="button secondary" href="{page_path(lang, "privacy")}">{esc(t["privacy"])}</a>
</section>"""
    return layout(lang, "home", f"{app_name} – {t['tagline']}", body)


def support(lang):
    t = T[lang]
    app_name = LANGUAGES[lang][3]
    faq = "".join(
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in t["faq"]
    )
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
<title>Kumofuton</title>
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
    if (["en", "ja", "ko", "fr", "de", "ar"].indexOf(base) !== -1) {{ pick = base; break; }}
  }}
  location.replace("{BASE}/" + pick + "/{'' if page == 'home' else page + '/'}");
}})();
</script>
</head>
<body><main><h1>Kumofuton</h1><ul class="language-list">{links}</ul></main></body>
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
    missing = [lang for lang in LANGUAGES if not CONTACT_FORM_URLS.get(lang)]
    if missing:
        sys.exit(f"Missing contact form URL for: {', '.join(missing)}")
    print(f"Built {len(LANGUAGES) * len(PAGES) + 3} pages.")
