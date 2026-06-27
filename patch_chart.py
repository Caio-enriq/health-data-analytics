import re

with open("/home/caio/Projetos/analise_specs/dashboard.html", "r") as f:
    html = f.read()

# 1. Fix HTML subtitle
html = html.replace('<span style="font-size:0.75rem;color:var(--text-muted);">Últimas 30 execuções</span>', '<span style="font-size:0.75rem;color:var(--text-muted);">Todos os processamentos agregados</span>')

# 2. Fix JS logic for chart-line
old_js_regex = r"const exLast = execucoesData\.value\.slice\(0, ?30\)\.reverse\(\);\s*const lineEl = document\.getElementById\('chart-line'\);\s*if \(lineEl && exLast\.length\) \{.*?charts\.line\.render\(\);\s*\}"

new_js = """
      const funcCount = {};
      execucoesData.value.forEach(e => {
        const fn = e.funcao || 'Outros';
        if (!funcCount[fn]) funcCount[fn] = { sucesso: 0, erro: 0 };
        funcCount[fn].sucesso += (+e.total_sucesso || 0);
        funcCount[fn].erro += (+e.total_erro || 0);
      });
      const fnLabels = Object.keys(funcCount);
      
      const lineEl = document.getElementById('chart-line');
      if (lineEl && fnLabels.length) {
        charts.line = new ApexCharts(lineEl, {
          ...base,
          chart: { ...base.chart, type: 'bar', height: 240, stacked: true },
          series: [
            { name: 'Sucesso', data: fnLabels.map(k => funcCount[k].sucesso) },
            { name: 'Erro',    data: fnLabels.map(k => funcCount[k].erro) },
          ],
          xaxis: { ...base.xaxis, categories: fnLabels },
          plotOptions: { bar: { borderRadius: 4, columnWidth: '50%' } },
          colors: ['var(--color-success)', 'var(--color-error)'],
          dataLabels: { enabled: false },
        });
        charts.line.render();
      }
"""

html = re.sub(old_js_regex, new_js.strip(), html, flags=re.DOTALL)

with open("/home/caio/Projetos/analise_specs/dashboard.html", "w") as f:
    f.write(html)
print("Chart patched successfully")
