import re

with open("/home/caio/Projetos/analise_specs/dashboard.html", "r") as f:
    html = f.read()

new_logo = """
        <div style="display:flex; align-items:center; justify-content:center; width:34px; height:34px; border-radius:8px; background: linear-gradient(135deg, #0065ff, #000a69); margin-right: 12px; box-shadow: 0 4px 10px rgba(0,101,255,0.4);">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
            <path d="M2 17l10 5 10-5"></path>
            <path d="M2 12l10 5 10-5"></path>
          </svg>
        </div>
"""

old_logo = '<div class="logo-icon">S</div>'

html = html.replace(old_logo, new_logo)

# Fix the CSS for the logo area so it looks neat
css_fix = """
  .logo-icon {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: linear-gradient(135deg, var(--brand-bright-blue), var(--brand-dark-blue));
    display: flex;
"""
html = html.replace(".logo-icon {\n    width: 32px;\n    height: 32px;\n    border-radius: 8px;\n    background: linear-gradient(135deg, var(--brand-bright-blue), var(--brand-dark-blue));\n    display: flex;", css_fix)

with open("/home/caio/Projetos/analise_specs/dashboard.html", "w") as f:
    f.write(html)
print("Logo patched")
