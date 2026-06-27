import re

with open("/home/caio/Projetos/analise_specs/dashboard.html", "r") as f:
    html = f.read()

# 1. Add smoke tests data to setup()
html = re.sub(
    r"const configData = ref\(\[\]\);",
    "const configData = ref([]);\n    const smokeData = ref([]);",
    html
)

# 2. Add smoke table to HTML just before config
smoke_html = """
        <!-- SMOKE TESTS -->
        <div v-if="currentPage === 'smoke'" class="content-panel animate-fade-in">
          <div class="panel-header">
            <h2 class="panel-title">Smoke Tests (Validação Contínua)</h2>
          </div>
          <div class="table-responsive">
            <table class="data-table">
              <thead><tr>
                <th>Data</th><th>ID Teste</th><th>Entidade</th><th>Alvo</th><th>Status</th><th>Resultado</th>
              </tr></thead>
              <tbody>
                <tr v-for="(s,i) in smokeData" :key="i">
                  <td style="font-size:0.78rem;white-space:nowrap;color:var(--text-muted);">{{ fmtDate(s.criado_em) }}</td>
                  <td style="font-family:monospace;font-weight:600;">{{ s.teste_id }}</td>
                  <td><span class="chip" :class="s.tipo_entidade==='CAIXA'?'info':'running'">{{ s.tipo_entidade }}</span></td>
                  <td style="font-size:0.8rem">{{ s.funcao_alvo }}</td>
                  <td><span class="chip" :class="s.status_teste==='CONCLUIDO'?'success':(s.status_teste==='FALHA'?'error':'warning')">{{ s.status_teste }}</span></td>
                  <td style="font-size:0.8rem;max-width:300px;overflow:hidden;text-overflow:ellipsis;" :title="s.resultado">{{ s.resultado }}</td>
                </tr>
                <tr v-if="!smokeData.length"><td colspan="6" style="text-align:center;padding:20px;color:var(--text-muted)">Nenhum smoke test executado.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
"""
html = html.replace("<!-- CONFIGURAÇÕES -->", smoke_html + "\n        <!-- CONFIGURAÇÕES -->")

# 3. Replace loadAllData
new_load = """
    async function loadAllData() {
      loading.value = true;
      try {
        const resp = await fetch('/api/data');
        if (!resp.ok) throw new Error('Falha HTTP: ' + resp.status);
        const data = await resp.json();
        
        execucoesData.value = data.execs || [];
        errosData.value     = data.errs || [];
        itensData.value     = data.itens || [];
        logsData.value      = data.logs || [];
        configData.value    = data.cfg || [];
        smokeData.value     = data.smoke || [];
        dashData.value      = Object.entries(data.kpis || {}).map(([k,v]) => ({indicador: k, valor: v}));

        const cfgModo = configData.value.find(c => c.chave === 'MODO_EXECUCAO');
        if (cfgModo) modoAtual.value = cfgModo.valor;

        lastUpdated.value = new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });

        await nextTick();
        lucide.createIcons();
        renderDashboardCharts();
        if (currentPage.value === 'analytics') renderAnalyticsCharts();
      } catch(e) {
        console.error('Erro loadAllData:', e);
      } finally {
        loading.value = false;
      }
    }
"""
html = re.sub(r"async function loadAllData\(\)\s*\{.*?(?=\n\s*/\* ---- AI ---- \*/)", new_load, html, flags=re.DOTALL)

# 4. Return smokeData from setup
html = re.sub(r"configData,", "configData, smokeData,", html)

with open("/home/caio/Projetos/analise_specs/dashboard.html", "w") as f:
    f.write(html)
print("Dashboard patched successfully")
