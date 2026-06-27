import re

with open("/home/caio/Projetos/analise_specs/dashboard.html", "r") as f:
    html = f.read()

appsheet_fields_html = """
          <div v-if="docModal.dados_appsheet?.status_sync === 'SINCRONIZADO'" style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
            <div><small style="color:var(--text-muted)">Caixa ID</small><div style="font-family:monospace">{{ docModal.dados_appsheet.CaixaID || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Palete ID</small><div style="font-family:monospace">{{ docModal.dados_appsheet.PaleteID || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Status OCR</small><div>{{ docModal.dados_appsheet.Status_ocr_documento || '—' }}</div></div>
            <div style="grid-column: 1 / -1"><small style="color:var(--text-muted)">Link Foto Doc</small><div style="word-break:break-all"><a v-if="docModal.dados_appsheet.LinkFotoDocumento" :href="docModal.dados_appsheet.LinkFotoDocumento" target="_blank" style="color:var(--brand-bright-blue)">Visualizar Foto</a><span v-else>—</span></div></div>
            <div style="grid-column: 1 / -1"><small style="color:var(--text-muted)">Paciente</small><div style="font-weight:600">{{ docModal.dados_appsheet.NomePaciente || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Data Nasc.</small><div>{{ docModal.dados_appsheet.DataNascimento || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">CPF</small><div>{{ docModal.dados_appsheet.CPF || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Prontuário</small><div style="font-family:monospace">{{ docModal.dados_appsheet.NumeroProntuario || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Volume</small><div>{{ docModal.dados_appsheet.VolumeProntuario || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Último Atend.</small><div>{{ docModal.dados_appsheet.DataUltimoAtendimento || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Sexo</small><div>{{ docModal.dados_appsheet.sexo || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Tipo Doc</small><div>{{ docModal.dados_appsheet.tipoDocumental || docModal.dados_appsheet.TipoDocumental || '—' }}</div></div>
          </div>
"""

old_appsheet_html = """          <div v-if="docModal.dados_appsheet?.status_sync === 'SINCRONIZADO'" style="display:flex; flex-direction:column; gap:10px;">
            <div><small style="color:var(--text-muted)">Paciente</small><div style="font-weight:600">{{ docModal.dados_appsheet.NomePaciente || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Prontuário</small><div style="font-family:monospace">{{ docModal.dados_appsheet.NumeroProntuario || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Caixa / Palete</small><div style="font-family:monospace">{{ docModal.dados_appsheet.CaixaID || '—' }} / {{ docModal.dados_appsheet.PaleteID || '—' }}</div></div>
            <div><small style="color:var(--text-muted)">Tipo Doc</small><div>{{ docModal.dados_appsheet.TipoDocumental || docModal.dados_appsheet.tipoDocumental || '—' }}</div></div>
          </div>"""

html = html.replace(old_appsheet_html, appsheet_fields_html)

with open("/home/caio/Projetos/analise_specs/dashboard.html", "w") as f:
    f.write(html)
print("Modal fields patched")
