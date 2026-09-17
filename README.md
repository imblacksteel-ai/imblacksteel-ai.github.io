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
