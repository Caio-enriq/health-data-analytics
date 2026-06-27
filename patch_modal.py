import re

with open("/home/caio/Projetos/analise_specs/dashboard.html", "r") as f:
    html = f.read()

# 1. Add docModal ref to setup
html = re.sub(
    r"const smokeData = ref\(\[\]\);",
    "const smokeData = ref([]);\n    const docModal = ref(null);",
    html
)

# 2. Add openDoc function
open_doc_js = """
    async function openDoc(item) {
      docModal.value = null;
      try {
        const r = await fetch(`/api/documento/${encodeURIComponent(item.etiqueta)}`);
        if (r.ok) {
            docModal.value = await r.json();
        } else {
            docModal.value = { dados_planilha: item, dados_appsheet: { status_sync: 'FALHA', nota: 'Erro na busca' } };
        }
      } catch(e) {
        docModal.value = { dados_planilha: item, dados_appsheet: { status_sync: 'FALHA', nota: 'Erro de conexão' } };
      }
      nextTick(() => lucide.createIcons());
    }
"""
html = re.sub(r"async function sendAIMessage", open_doc_js + "\n    async function sendAIMessage", html)

# 3. Expose openDoc and docModal
html = re.sub(r"sendAIMessage,\s*pageNumbers,", "sendAIMessage, pageNumbers, openDoc, docModal,", html)

# 4. Modify the button to call openDoc(it)
# The button in Caixas & Documentos was: <button class="btn-sm">Ver detalhes</button>
html = html.replace(
    '<button class="btn-sm">Ver detalhes</button>',
    '<button class="btn-sm" @click="openDoc(it)">Ver detalhes</button>'
)

# 5. Add Modal HTML to the template (before the AI panel)
modal_html = """
  <!-- MODAL DE DOCUMENTO (AppSheet x Planilha) -->
  <div v-if="docModal" class="modal-overlay" @click.self="docModal=null">
    <div class="modal-content">
      <div class="modal-header" style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border); padding-bottom:10px; margin-bottom:15px;">
        <h3 style="margin:0; font-family:monospace; font-size:1.2rem; color:var(--text)">{{ docModal.dados_planilha?.etiqueta }}</h3>
        <button class="btn-sm" @click="docModal=null" style="background:transparent; border:none; cursor:pointer;"><i data-lucide="x"></i></button>
      </div>
      <div class="modal-body" style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
        <!-- Lado AppSheet -->
        <div style="background:var(--bg-card); padding:15px; border-radius:8px; border:1px solid var(--border)">
          <h4 style="margin-top:0; color:var(--brand-bright-blue); display:flex; align-items:center; gap:8px;"><i data-lucide="database" style="width:16px;"></i> Banco AppSheet</h4>
          <div v-if="docModal.dados_appsheet?.status_sync === 'SINCRONIZADO'" style="display:flex; flex-direction:column; gap:10px;">
            <div><small style="color:var(--text-muted)">Paciente</small><div style="font-weight:600">{{ docModal.dados_appsheet.NomePaciente || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Prontuário</small><div style="font-family:monospace">{{ docModal.dados_appsheet.NumeroProntuario || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Caixa / Palete</small><div style="font-family:monospace">{{ docModal.dados_appsheet.CaixaID || '—' }} / {{ docModal.dados_appsheet.PaleteID || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Tipo Doc</small><div>{{ docModal.dados_appsheet.TipoDocumental || docModal.dados_appsheet.tipoDocumental || '—' }}</div></div>
          </div>
          <div v-else style="color:var(--color-error); font-size:0.9rem; padding:10px; background:rgba(239,68,68,0.1); border-radius:6px;">
            {{ docModal.dados_appsheet?.nota || 'Registro não encontrado no AppSheet.' }}
          </div>
        </div>
        <!-- Lado Planilha -->
        <div style="background:var(--bg-card); padding:15px; border-radius:8px; border:1px solid var(--border)">
          <h4 style="margin-top:0; color:var(--text); display:flex; align-items:center; gap:8px;"><i data-lucide="file-spreadsheet" style="width:16px;"></i> Dados DocZ (Planilha)</h4>
          <div style="display:flex; flex-direction:column; gap:10px;">
            <div><small style="color:var(--text-muted)">Tipo</small><div><span class="chip" :class="docModal.dados_planilha?.tipo_entidade==='CAIXA'?'info':'running'">{{ docModal.dados_planilha?.tipo_entidade }}</span></div></div>
            <div><small style="color:var(--text-muted)">Status Item</small><div><span class="chip" :class="getStatusClass(docModal.dados_planilha?.status_item)">{{ docModal.dados_planilha?.status_item }}</span></div></div>
            <div><small style="color:var(--text-muted)">Status DocZ</small><div><span class="chip" :class="getStatusClass(docModal.dados_planilha?.status_docz)">{{ docModal.dados_planilha?.status_docz || '—' }}</span></div></div>
            <div><small style="color:var(--text-muted)">Mensagem</small><div style="font-size:0.85rem; max-height:80px; overflow-y:auto;">{{ docModal.dados_planilha?.mensagem_resumida || '—' }}</div></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <style>
    .modal-overlay { position: fixed; top:0; left:0; right:0; bottom:0; background:rgba(0,0,0,0.6); backdrop-filter:blur(3px); z-index:9999; display:flex; justify-content:center; align-items:center; }
    .modal-content { background:var(--bg-base); padding:20px; border-radius:12px; width:90%; max-width:800px; box-shadow:0 10px 25px rgba(0,0,0,0.5); border:1px solid var(--border); }
    @media (max-width: 768px) { .modal-body { grid-template-columns: 1fr !important; } }
  </style>
"""
html = html.replace("<!-- ===== IA FLOATING CHAT ===== -->", modal_html + "\n  <!-- ===== IA FLOATING CHAT ===== -->")

with open("/home/caio/Projetos/analise_specs/dashboard.html", "w") as f:
    f.write(html)
print("Modal patched successfully")
