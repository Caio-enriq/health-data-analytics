import os
import markdown
import glob

# Find all relevant markdown files
md_files = [
    "SPEC.md",
    "README.md"
]

all_md_content = ""

for file_name in md_files:
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            all_md_content += f"\n\n<!-- FILE: {file_name} -->\n\n"
            all_md_content += content

# Convert to HTML with TOC
md = markdown.Markdown(extensions=['toc', 'fenced_code', 'tables'])
html_body = md.convert(all_md_content)
toc_html = md.toc

# HTML Template
html_template = f"""<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HealthData - Documentação Compilada</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc;
            color: #1e293b;
        }}
        .prose h1, .prose h2, .prose h3, .prose h4 {{
            scroll-margin-top: 5rem;
        }}
        /* Markdown styles */
        .markdown-body h1 {{ font-size: 2.25rem; font-weight: 800; margin-top: 2rem; margin-bottom: 1rem; color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }}
        .markdown-body h2 {{ font-size: 1.875rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #1e293b; }}
        .markdown-body h3 {{ font-size: 1.5rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #334155; }}
        .markdown-body p {{ margin-bottom: 1rem; line-height: 1.75; }}
        .markdown-body ul {{ list-style-type: disc; margin-left: 1.5rem; margin-bottom: 1rem; }}
        .markdown-body ol {{ list-style-type: decimal; margin-left: 1.5rem; margin-bottom: 1rem; }}
        .markdown-body li {{ margin-bottom: 0.5rem; }}
        .markdown-body code {{ background-color: #f1f5f9; padding: 0.2rem 0.4rem; border-radius: 0.25rem; font-family: monospace; font-size: 0.875em; color: #db2777; }}
        .markdown-body pre {{ background-color: #1e293b; color: #f8fafc; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; margin-bottom: 1rem; }}
        .markdown-body pre code {{ background-color: transparent; color: inherit; padding: 0; }}
        .markdown-body table {{ width: 100%; border-collapse: collapse; margin-bottom: 1.5rem; }}
        .markdown-body th, .markdown-body td {{ border: 1px solid #e2e8f0; padding: 0.75rem; text-align: left; }}
        .markdown-body th {{ background-color: #f1f5f9; font-weight: 600; }}
        .markdown-body hr {{ border: 0; border-top: 1px solid #e2e8f0; margin: 2rem 0; }}
        .markdown-body a {{ color: #2563eb; text-decoration: underline; }}
        
        .toc ul {{
            list-style-type: none;
            padding-left: 1rem;
        }}
        .toc li {{
            margin-bottom: 0.5rem;
        }}
        .toc a {{
            color: #475569;
            text-decoration: none;
            font-size: 0.875rem;
            transition: color 0.2s;
        }}
        .toc a:hover {{
            color: #2563eb;
            font-weight: 500;
        }}
        .toc > div > ul {{
            padding-left: 0;
        }}
        
        /* Sticky sidebar */
        .sidebar {{
            position: sticky;
            top: 2rem;
            height: calc(100vh - 4rem);
            overflow-y: auto;
        }}
    </style>
</head>
<body class="antialiased">
    <div class="max-w-8xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="py-8">
            <header class="mb-12 border-b border-gray-200 pb-8 text-center">
                <h1 class="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl">HealthData - Documentação Completa</h1>
                <p class="mt-4 text-xl text-gray-500">Compilado das especificações de Arquitetura, API, UI e Regras de Negócio.</p>
            </header>
            
            <div class="flex flex-col lg:flex-row gap-8">
                <!-- Sidebar TOC -->
                <div class="w-full lg:w-1/4 flex-shrink-0 hidden lg:block">
                    <div class="sidebar bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                        <h2 class="text-lg font-bold text-gray-900 mb-4 tracking-wide uppercase text-sm border-b pb-2">Índice</h2>
                        <div class="toc text-gray-600">
                            {toc_html}
                        </div>
                    </div>
                </div>
                
                <!-- Main Content -->
                <div class="w-full lg:w-3/4">
                    <div class="bg-white p-8 sm:p-12 rounded-xl shadow-sm border border-gray-100 markdown-body">
                        {html_body}
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

with open("HealthData_Compilado.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("HealthData_Compilado.html gerado com sucesso!")
