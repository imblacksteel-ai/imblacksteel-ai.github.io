# imblacksteel-ai.github.io

Public pages for apps, served by GitHub Pages.

## Kumofuton

- Home: https://imblacksteel-ai.github.io/kumofuton/
- Support: https://imblacksteel-ai.github.io/kumofuton/support/
- Privacy policy: https://imblacksteel-ai.github.io/kumofuton/privacy/

The language-neutral URLs above send visitors to their browser language;
each language also has its own URL, such as `/kumofuton/ja/privacy/`.

Pages are generated. Edit `tools/kumofuton_content.py` (text, 8 languages)
or `tools/build_kumofuton.py` (layout, contact form URLs per language), then run:

```sh
python3 tools/build_kumofuton.py
```

Keep the privacy policy in step with the app, and update the effective date
when it changes.

## SD Importer

- Home: https://imblacksteel-ai.github.io/sd-importer/
- Support: https://imblacksteel-ai.github.io/sd-importer/support/
- Privacy policy: https://imblacksteel-ai.github.io/sd-importer/privacy/

English, Japanese, Korean, and Chinese (Simplified and Traditional). The language-neutral
URLs send visitors to their browser language, as with Kumofuton.

Pages are generated. Edit `tools/sdimporter_content.py` (text) or `tools/build_sdimporter.py`
(layout; set `APP_STORE_URL` once the app is live), then run:

```sh
python3 tools/build_sdimporter.py
```

The app's source is https://github.com/imblacksteel-ai/photo-manager. Keep the privacy policy
in step with the app, and update the effective date when it changes.

## Yesternews

- Home: https://imblacksteel-ai.github.io/yesternews/
- Privacy policy: https://imblacksteel-ai.github.io/yesternews/privacy/
- Terms of use: https://imblacksteel-ai.github.io/yesternews/terms/

Japanese only for now, styled like the app (a 1998 PC window with the
DotGothic16 font). Pages are generated in the Yesternews repository: edit
`docs/site/src/*.html` (text) or `docs/site/yesternews/assets/style.css`
(look), then run `docs/site/build.py` there. It writes the pages, a font cut
down to the characters in use, and copies everything here. Update the
effective date when the policy or terms change.

`yesternews/ads.json` is the ad list the app downloads (free users only).
Its source is `assets/data/ads.json` in the Yesternews repository; see
`docs/ads.md` there. Changing it here changes the ads without an app update.
