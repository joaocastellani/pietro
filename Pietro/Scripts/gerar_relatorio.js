#!/usr/bin/env node
/**
 * gerar_relatorio.js — Monta o Relatório de Sessão (HTML) do Prompt
 * Professor Master (Etapa 5.3) a partir de um JSON de dados.
 *
 * Uso: node gerar_relatorio.js dados.json > relatorio.html
 *
 * O Professor (Claude), na Etapa 5.3, computa só os dados da sessão
 * (placar, tópicos, erros) e roda este script já existente no repo —
 * não precisa reescrever o HTML/CSS a cada aula.
 *
 * Schema esperado do JSON de entrada:
 * {
 *   "nomeAluno": "Pietro",
 *   "materia": "Física",
 *   "corMateria": "#4a2080",
 *   "unidade": 1,
 *   "capitulo": 3,
 *   "data": "18/08/2026",
 *   "warmup": { "acertos": 8, "total": 10 },
 *   "progressivo": { "acertos": 4, "total": 5 },
 *   "testeFinal": { "acertos": 8, "total": 10 },
 *   "estrelas": 4,
 *   "nivelDesempenho": "Bom desempenho",
 *   "cronograma": [ { "etapa": "Resumo", "duracao": "12 min" }, ... ],
 *   "dominados": [ "Modelo Heliocêntrico", ... ],
 *   "reforcar": [ { "topico": "Ano-luz", "descricao": "Confundiu com medida de tempo" } ],
 *   "errosEspecificos": [
 *     { "questao": "Q3 — Teste final", "respondeu": "...", "correto": "...", "explicacao": "..." }
 *   ]
 * }
 */

'use strict';

const fs = require('fs');

const BADGE_POR_NIVEL = {
  'Excelente': 'badge-ok',
  'Bom desempenho': 'badge-ok',
  'Regular': 'badge-warn',
  'A reforçar': 'badge-err',
};

function escapeHtml(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function pct(acertos, total) {
  if (!total) return 0;
  return Math.round((acertos / total) * 100);
}

function estrelasHtml(n) {
  let out = '';
  for (let i = 1; i <= 5; i++) {
    out += `<div class="star ${i <= n ? 'star-on' : 'star-off'}"></div>\n      `;
  }
  return out.trim();
}

function metricHtml(label, acertos, total) {
  return `
      <div class="metric">
        <div class="metric-label">${escapeHtml(label)}</div>
        <div class="metric-value">${acertos}<span>/${total}</span></div>
        <div class="metric-sub">${pct(acertos, total)}%</div>
      </div>`;
}

function cronogramaHtml(cronograma) {
  const linhas = (cronograma || []).map(
    (c) => `      <tr><td>${escapeHtml(c.etapa)}</td><td>${escapeHtml(c.duracao)}</td></tr>`
  ).join('\n');
  return linhas;
}

function dominadosHtml(dominados) {
  return (dominados || []).map((topico) => `
    <div class="topic-row">
      <div class="dot dot-ok"></div>
      <div class="topic-name">${escapeHtml(topico)}</div>
    </div>`).join('\n');
}

function reforcarHtml(reforcar) {
  return (reforcar || []).map((r) => `
    <div class="topic-row">
      <div class="dot dot-warn"></div>
      <div>
        <div class="topic-name">${escapeHtml(r.topico)}</div>
        <div class="topic-sub">${escapeHtml(r.descricao)}</div>
      </div>
    </div>`).join('\n');
}

function errosHtml(erros) {
  return (erros || []).map((e) => `
    <div class="topic-row">
      <div class="dot dot-err"></div>
      <div>
        <div class="topic-name">${escapeHtml(e.questao)}</div>
        <div class="topic-sub">
          Respondeu: ${escapeHtml(e.respondeu)} · Correto: ${escapeHtml(e.correto)}<br>
          ${escapeHtml(e.explicacao)}
        </div>
      </div>
    </div>`).join('\n');
}

function gerarHtml(d) {
  const corMateria = d.corMateria || '#4a2080';
  const badge = BADGE_POR_NIVEL[d.nivelDesempenho] || 'badge-warn';

  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Relatório — ${escapeHtml(d.nomeAluno)} — ${escapeHtml(d.materia)} ${escapeHtml(d.data)}</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,sans-serif;font-size:14px;color:#1a1a1a;
     line-height:1.6;background:#fff}
.report{max-width:600px;margin:0 auto;padding:0 0 2rem}
.header{background:${corMateria};color:#fff;padding:18px 20px}
.header h1{font-size:17px;font-weight:500;margin-bottom:2px}
.header p{font-size:12px;opacity:0.8}
.section{padding:14px 20px;border-bottom:1px solid #f0f0f0}
.section:last-child{border-bottom:none}
.section-title{font-size:11px;font-weight:600;color:#888;
               text-transform:uppercase;letter-spacing:0.05em;margin-bottom:10px}
.metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.metric{background:#f8f8f8;border-radius:8px;padding:10px 12px}
.metric-label{font-size:11px;color:#888;margin-bottom:2px}
.metric-value{font-size:20px;font-weight:500}
.metric-value span{font-size:13px;color:#888}
.metric-sub{font-size:11px;color:#888}
.desempenho{display:flex;align-items:center;gap:10px;margin-top:10px}
.stars{display:flex;gap:3px}
.star{width:10px;height:10px;border-radius:50%}
.star-on{background:${corMateria}}
.star-off{background:#e0e0e0}
.badge{font-size:11px;padding:2px 8px;border-radius:20px;font-weight:500}
.badge-ok  {background:#e6f4ec;color:#1a6b3a}
.badge-warn{background:#fef9e6;color:#8a6400}
.badge-err {background:#fdecea;color:#b91c1c}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;font-weight:500;color:#888;font-size:11px;
   padding:6px 0;border-bottom:1px solid #f0f0f0}
td{padding:7px 0;border-bottom:1px solid #f0f0f0;vertical-align:top}
td:last-child,th:last-child{text-align:right}
.topic-row{display:flex;align-items:flex-start;gap:8px;
           padding:6px 0;border-bottom:1px solid #f0f0f0}
.topic-row:last-child{border-bottom:none}
.dot{width:6px;height:6px;border-radius:50%;margin-top:5px;flex-shrink:0}
.dot-ok  {background:#1a6b3a}
.dot-warn{background:#ca8a04}
.dot-err {background:#dc2626}
.topic-name{font-size:13px}
.topic-sub{font-size:11px;color:#888;margin-top:1px}
.footer-note{font-size:11px;color:#aaa;padding:12px 20px 0;text-align:center}
</style>
</head>
<body>
<div class="report">

  <div class="header">
    <h1>Relatório de aula — ${escapeHtml(d.nomeAluno)}</h1>
    <p>${escapeHtml(d.materia)} · Unidade ${escapeHtml(d.unidade)} · Capítulo ${escapeHtml(d.capitulo)} · 9º ano · ${escapeHtml(d.data)}</p>
  </div>

  <div class="section">
    <div class="section-title">Resultado geral</div>
    <div class="metrics">${metricHtml('Warm-Up', d.warmup?.acertos ?? 0, d.warmup?.total ?? 0)}${metricHtml('Progressivo', d.progressivo?.acertos ?? 0, d.progressivo?.total ?? 0)}${metricHtml('Teste final', d.testeFinal?.acertos ?? 0, d.testeFinal?.total ?? 10)}
    </div>
    <div class="desempenho">
      <div class="stars">
      ${estrelasHtml(d.estrelas || 0)}
      </div>
      <span class="badge ${badge}">${escapeHtml(d.nivelDesempenho)}</span>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Cronograma</div>
    <table>
      <tr><th>Etapa</th><th>Duração</th></tr>
${cronogramaHtml(d.cronograma)}
    </table>
  </div>

  <div class="section">
    <div class="section-title">Assuntos dominados</div>${dominadosHtml(d.dominados)}
  </div>

  <div class="section">
    <div class="section-title">Para reforçar</div>${reforcarHtml(d.reforcar)}
  </div>

  <div class="section">
    <div class="section-title">Erros específicos</div>${errosHtml(d.errosEspecificos)}
  </div>

  <div class="footer-note">
    Gerado pelo Sistema de Tutoria · ${escapeHtml(d.data)}
  </div>

</div>
</body>
</html>
`;
}

function main() {
  const caminho = process.argv[2];
  if (!caminho) {
    process.stderr.write('Uso: node gerar_relatorio.js dados.json > relatorio.html\n');
    process.exit(1);
  }
  const dados = JSON.parse(fs.readFileSync(caminho, 'utf8'));
  process.stdout.write(gerarHtml(dados));
}

main();
