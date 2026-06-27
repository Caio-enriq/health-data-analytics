
# write_dashboard.py — Escreve o dashboard.html completo
HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<meta name="color-scheme" content="dark"/>
<meta name="description" content="HealthData Platform — Dashboard de Observabilidade e Analytics Operacional."/>
<title>sosdocs | HealthData Platform</title>
<script>
(function(){const s=localStorage.getItem('sos-theme')||'dark';document.querySelector('meta[name="color-scheme"]').content=s;document.documentElement.setAttribute('data-theme',s);})();
</script>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/apexcharts/dist/apexcharts.css"/>
<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
<script src="https://unpkg.com/vue@3/dist/vue.global.prod.js"></script>
<style>
@layer reset,base,theme,components,utilities;
@layer reset{*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}img,svg{display:block}button{cursor:pointer;border:none;background:none;font:inherit}ul,ol{list-style:none}a{text-decoration:none;color:inherit}input,textarea,select{font:inherit}}
@layer theme{
:root{
--dn:#000a69;--bb:#0065ff;--vd:#000126;--dk:#02041e;--lb:#9ac2ff;--gd:#dea511;--ow:#f7f7f7;
--ok:#00b86b;--er:#e63946;
--bg-r:var(--dk);--bg-s:var(--vd);--bg-c:color-mix(in oklab,var(--dn) 88%,white 12%);--bg-ch:color-mix(in oklab,var(--dn) 65%,var(--bb) 35%);
--bg-sb:var(--vd);--bg-tb:rgba(0,1,38,.86);--bg-in:rgba(0,10,105,.42);
--tx:#f7f7f7;--tx2:var(--lb);--txm:rgba(154,194,255,.55);
--bo:rgba(154,194,255,.12);--ba:rgba(0,101,255,.5);
--ac:var(--bb);--ag:rgba(0,101,255,.22);
--sh:0 4px 24px rgba(0,0,0,.42),0 1px 4px rgba(0,0,0,.28);--sg:0 0 32px rgba(0,101,255,.18);
--rsm:8px;--rmd:12px;--rlg:16px;--rxl:24px;--rfl:9999px;
--sw:260px;--th:64px;--tr:.22s cubic-bezier(.4,0,.2,1);
scrollbar-color:var(--ba) transparent;scrollbar-width:thin;color-scheme:dark;
}
[data-theme="light"]{
--bg-r:var(--ow);--bg-s:#edf1fb;--bg-c:#fff;--bg-ch:#f0f5ff;
--bg-sb:#fff;--bg-tb:rgba(255,255,255,.93);--bg-in:rgba(0,101,255,.07);
--tx:var(--vd);--tx2:#2d4a8a;--txm:#6b82b0;
--bo:rgba(0,10,105,.1);--ba:rgba(0,101,255,.28);
--sh:0 2px 16px rgba(0,10,105,.08),0 1px 4px rgba(0,0,0,.05);--sg:0 0 24px rgba(0,101,255,.1);
color-scheme:light;
}
}
@layer base{
html{font-family:'Inter',system-ui,sans-serif;font-size:15px;line-height:1.5;color:var(--tx);background:var(--bg-r);transition:background var(--tr),color var(--tr);accent-color:var(--ac);}
body{min-height:100dvh;overflow-x:hidden;}
::-webkit-scrollbar{width:5px;height:5px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:var(--ba);border-radius:var(--rfl)}
h1{font-size:clamp(1.35rem,2vw,1.7rem);font-weight:700;text-wrap:balance}
h2{font-size:clamp(1.05rem,1.5vw,1.2rem);font-weight:600}
h3{font-size:.98rem;font-weight:600}
::selection{background:var(--ac);color:#fff}
}
@layer components{
/* SHELL */
.shell{display:grid;grid-template-columns:var(--sw) 1fr;grid-template-rows:var(--th) 1fr;min-height:100dvh;transition:grid-template-columns var(--tr)}
.shell.col{--sw:70px}

/* SIDEBAR */
.sb{grid-row:1/-1;background:var(--bg-sb);border-right:1px solid var(--bo);display:flex;flex-direction:column;position:sticky;top:0;height:100dvh;overflow:hidden;z-index:100;transition:background var(--tr),border-color var(--tr)}
.sb-logo{display:flex;align-items:center;gap:10px;padding:0 18px;height:var(--th);border-bottom:1px solid var(--bo);white-space:nowrap;overflow:hidden;flex-shrink:0}
.logo-ic{width:34px;height:34px;border-radius:var(--rsm);background:linear-gradient(135deg,var(--bb),var(--dn));display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 2px 12px var(--ag);font-size:16px;font-weight:900;color:#fff;letter-spacing:-1px}
.logo-t{font-weight:800;font-size:1.05rem;color:var(--tx)}
.logo-s{font-size:.62rem;color:var(--txm);font-weight:500;letter-spacing:.05em;text-transform:uppercase}
.sb-nav{flex:1;padding:10px 0;overflow-y:auto}
.nl{font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--txm);padding:14px 20px 5px;white-space:nowrap;overflow:hidden;transition:opacity var(--tr)}
.col .nl{opacity:0}
.ni{display:flex;align-items:center;gap:11px;padding:9px 18px;margin:2px 8px;border-radius:var(--rsm);color:var(--txm);font-weight:500;font-size:.88rem;cursor:pointer;transition:background var(--tr),color var(--tr),transform .15s;white-space:nowrap;overflow:hidden;position:relative}
.ni:hover{background:var(--bg-ch);color:var(--tx);transform:translateX(2px)}
.ni.on{background:linear-gradient(90deg,var(--ag),transparent);color:var(--bb);font-weight:600}
.ni.on::before{content:'';position:absolute;left:0;top:20%;bottom:20%;width:3px;background:var(--ac);border-radius:0 var(--rfl) var(--rfl) 0}
.ni-ic{flex-shrink:0;width:17px;height:17px}
.ni-lb{transition:opacity var(--tr)}
.col .ni-lb{opacity:0;width:0}
.nbadge{margin-left:auto;padding:1px 7px;border-radius:var(--rfl);font-size:.68rem;font-weight:700;flex-shrink:0}
.nbadge.e{background:rgba(230,57,70,.2);color:var(--er)}
.nbadge.i{background:var(--ag);color:var(--bb)}
.col .nbadge{display:none}
.sb-bot{padding:10px 8px;border-top:1px solid var(--bo);flex-shrink:0}

/* TOPBAR */
.tb{grid-column:2;height:var(--th);background:var(--bg-tb);backdrop-filter:blur(16px) saturate(1.8);-webkit-backdrop-filter:blur(16px) saturate(1.8);border-bottom:1px solid var(--bo);display:flex;align-items:center;gap:10px;padding:0 22px;position:sticky;top:0;z-index:90;transition:background var(--tr),border-color var(--tr)}
.tb-tog{width:34px;height:34px;border-radius:var(--rsm);display:flex;align-items:center;justify-content:center;color:var(--txm);transition:background var(--tr),color var(--tr);flex-shrink:0}
.tb-tog:hover{background:var(--bg-c);color:var(--tx)}
.tb-title{font-weight:700;font-size:1rem;color:var(--tx);flex:1}
.srch{display:flex;align-items:center;gap:7px;background:var(--bg-in);border:1px solid var(--bo);border-radius:var(--rmd);padding:6px 12px;width:250px;transition:border-color var(--tr),box-shadow var(--tr)}
.srch:focus-within{border-color:var(--ba);box-shadow:0 0 0 3px var(--ag)}
.srch input{background:none;border:none;outline:none;color:var(--tx);font-size:.83rem;width:100%;caret-color:var(--ac)}
.srch input::placeholder{color:var(--txm)}
.tb-acts{display:flex;align-items:center;gap:7px;margin-left:auto}
.icb{width:34px;height:34px;border-radius:var(--rsm);display:flex;align-items:center;justify-content:center;color:var(--txm);position:relative;transition:background var(--tr),color var(--tr)}
.icb:hover{background:var(--bg-c);color:var(--tx)}
.icb .dot{position:absolute;top:4px;right:4px;width:8px;height:8px;border-radius:50%;background:var(--er);border:2px solid var(--bg-r)}
.tt-btn{width:56px;height:28px;border-radius:var(--rfl);background:var(--bg-in);border:1px solid var(--bo);padding:3px;display:flex;align-items:center;transition:background var(--tr);cursor:pointer}
.tt-knob{width:21px;height:21px;border-radius:50%;background:linear-gradient(135deg,var(--bb),var(--lb));box-shadow:0 2px 8px var(--ag);transition:transform var(--tr);display:flex;align-items:center;justify-content:center}
[data-theme="light"] .tt-knob{transform:translateX(27px)}
.av{width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--dn),var(--bb));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.75rem;color:#fff;border:2px solid var(--ba);cursor:pointer;box-shadow:0 2px 8px var(--ag)}

/* MAIN */
.mc{grid-column:2;padding:26px;overflow-y:auto;background:var(--bg-r)}
.ph{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:26px;gap:14px;flex-wrap:wrap}
.ph-sub{color:var(--txm);font-size:.83rem;margin-top:3px}

/* CARDS */
.card{background:var(--bg-c);border:1px solid var(--bo);border-radius:var(--rlg);padding:18px 22px;box-shadow:var(--sh);transition:background var(--tr),border-color var(--tr),transform .2s,box-shadow .2s}
.card:hover{transform:translateY(-1px);box-shadow:var(--sh),var(--sg)}

/* KPI */
.kgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(195px,1fr));gap:14px;margin-bottom:26px}
.kcard{background:var(--bg-c);border:1px solid var(--bo);border-radius:var(--rlg);padding:18px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:var(--sh);transition:transform .2s,box-shadow .2s,border-color var(--tr);cursor:default;position:relative;overflow:hidden}
.kcard::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--ka,var(--ac));border-radius:var(--rlg) var(--rlg) 0 0}
.kcard:hover{transform:translateY(-3px);box-shadow:var(--sh),0 8px 32px var(--ag);border-color:var(--ba)}
.ktop{display:flex;align-items:center;justify-content:space-between}
.klbl{font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--txm)}
.kic{width:34px;height:34px;border-radius:var(--rsm);display:flex;align-items:center;justify-content:center;background:color-mix(in oklab,var(--ka,var(--ac)) 15%,transparent);color:var(--ka,var(--ac))}
.kval{font-size:clamp(1.55rem,3vw,2.1rem);font-weight:800;letter-spacing:-.02em;color:var(--tx);line-height:1;font-variant-numeric:tabular-nums}
.kft{font-size:.73rem;color:var(--txm)}

/* CHARTS GRID */
.cgrid{display:grid;grid-template-columns:2fr 1fr;gap:14px;margin-bottom:26px}
@media(max-width:1100px){.cgrid{grid-template-columns:1fr}}

/* TABLES */
.twrap{overflow-x:auto}
.dt{width:100%;border-collapse:collapse;font-size:.83rem}
.dt th{padding:9px 13px;font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--txm);text-align:left;border-bottom:1px solid var(--bo);white-space:nowrap}
.dt td{padding:11px 13px;border-bottom:1px solid var(--bo);color:var(--tx);vertical-align:middle}
.dt tr:last-child td{border-bottom:none}
.dt tbody tr{transition:background var(--tr)}
.dt tbody tr:hover{background:var(--bg-ch)}

/* CHIPS */
.chip{display:inline-flex;align-items:center;gap:4px;padding:2px 9px;border-radius:var(--rfl);font-size:.7rem;font-weight:700;letter-spacing:.03em;white-space:nowrap}
.chip::before{content:'';width:5px;height:5px;border-radius:50%;background:currentColor}
.chip.s{background:rgba(0,184,107,.15);color:var(--ok)}
.chip.e{background:rgba(230,57,70,.15);color:var(--er)}
.chip.w{background:rgba(222,165,17,.15);color:var(--gd)}
.chip.i{background:rgba(0,101,255,.15);color:var(--bb)}
.chip.r{background:rgba(154,194,255,.15);color:var(--lb)}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:6px;padding:7px 15px;border-radius:var(--rsm);font-weight:600;font-size:.83rem;transition:all var(--tr);white-space:nowrap}
.bp{background:linear-gradient(135deg,var(--bb),color-mix(in oklab,var(--bb) 72%,var(--lb)));color:#fff;box-shadow:0 4px 16px var(--ag)}
.bp:hover{box-shadow:0 6px 24px rgba(0,101,255,.42);transform:translateY(-1px)}
.bg{background:var(--bg-in);color:var(--tx2);border:1px solid var(--bo)}
.bg:hover{background:var(--bg-ch);border-color:var(--ba);color:var(--tx)}

/* INPUTS */
.fi{background:var(--bg-in);border:1px solid var(--bo);border-radius:var(--rsm);padding:7px 11px;color:var(--tx);font-size:.83rem;outline:none;transition:border-color var(--tr),box-shadow var(--tr);width:100%}
.fi:focus{border-color:var(--ba);box-shadow:0 0 0 3px var(--ag)}
.fs{appearance:none;background:var(--bg-in) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='11' height='11' viewBox='0 0 24 24' fill='none' stroke='%239ac2ff' stroke-width='2'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E") no-repeat right 9px center;border:1px solid var(--bo);border-radius:var(--rsm);padding:7px 30px 7px 11px;color:var(--tx);font-size:.83rem;outline:none;cursor:pointer;transition:border-color var(--tr),box-shadow var(--tr)}
.fs:focus{border-color:var(--ba);box-shadow:0 0 0 3px var(--ag)}

/* PAGINATION */
.pag{display:flex;align-items:center;gap:5px;justify-content:flex-end;padding-top:14px}
.pbtn{min-width:30px;height:30px;padding:0 7px;border-radius:var(--rsm);display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:600;background:var(--bg-in);color:var(--txm);border:1px solid var(--bo);transition:all var(--tr)}
.pbtn:hover:not(:disabled){background:var(--bg-ch);color:var(--tx);border-color:var(--ba)}
.pbtn.on{background:var(--ac);color:#fff;border-color:var(--ac);box-shadow:0 2px 8px var(--ag)}
.pbtn:disabled{opacity:.35;cursor:not-allowed}
.pinf{font-size:.78rem;color:var(--txm);margin-right:auto}

/* FILTER BAR */
.fbar{display:flex;flex-wrap:wrap;gap:9px;align-items:center;margin-bottom:16px}

/* STAT ROW */
.srow{display:flex;gap:20px;flex-wrap:wrap;margin-bottom:18px}
.sitm{display:flex;align-items:center;gap:7px;font-size:.81rem}
.sdot{width:9px;height:9px;border-radius:50%}
.sval{font-weight:700;color:var(--tx)}
.slbl{color:var(--txm)}

/* EXEC ITEMS */
.ei{display:grid;grid-template-columns:auto 1fr auto;gap:12px;align-items:start;padding:14px 0;border-bottom:1px solid var(--bo)}
.ei:last-child{border-bottom:none}
.edot{width:9px;height:9px;border-radius:50%;margin-top:5px;flex-shrink:0}
.edot.s{background:var(--ok);box-shadow:0 0 6px var(--ok)}
.edot.e{background:var(--er);box-shadow:0 0 6px var(--er)}
.edot.w{background:var(--gd);box-shadow:0 0 6px var(--gd)}
.edot.r{background:var(--lb);box-shadow:0 0 6px var(--lb);animation:pd 1s infinite}
.etit{font-weight:600;font-size:.86rem;margin-bottom:3px}
.emeta{font-size:.76rem;color:var(--txm)}
.edur{font-size:.76rem;color:var(--txm);text-align:right;font-variant-numeric:tabular-nums}

/* PROGRESS */
.pb{height:5px;border-radius:var(--rfl);background:var(--bo);overflow:hidden}
.pf{height:100%;border-radius:var(--rfl);transition:width 1.1s cubic-bezier(.4,0,.2,1)}

/* EMPTY */
.emp{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:50px 20px;gap:10px;color:var(--txm);text-align:center}
.emp-ic{font-size:2.2rem;margin-bottom:6px}

/* BACKGROUND PATTERN */
.bgp{position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(circle,rgba(154,194,255,.04) 1.5px,transparent 2px) 0 0/28px 28px}
[data-theme="light"] .bgp{background:radial-gradient(circle,rgba(0,10,105,.05) 1.5px,transparent 2px) 0 0/28px 28px}

/* TOP LOADER */
.tl{position:fixed;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--bb),var(--gd),var(--bb));background-size:200% 100%;z-index:9999;animation:ls 1.2s infinite}
@keyframes ls{from{background-position:200% 0}to{background-position:-200% 0}}

/* ANIMATIONS */
.sea{animation:fsi .32s cubic-bezier(.4,0,.2,1)}
@keyframes fsi{from{opacity:0;transform:translateY(14px)}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pd{0%,100%{box-shadow:0 0 0 0 rgba(154,194,255,.5)}50%{box-shadow:0 0 0 5px rgba(154,194,255,0)}}
@keyframes pdb{0%,100%{box-shadow:0 0 0 0 rgba(0,184,107,.5)}50%{box-shadow:0 0 0 5px rgba(0,184,107,0)}}
@keyframes bd{0%,80%,100%{transform:translateY(0)}40%{transform:translateY(-6px)}}
@keyframes mi{from{opacity:0;transform:translateY(8px)}}

/* VIEW TRANSITIONS */
@keyframes sfr{from{transform:translateX(38px);opacity:0}}
@keyframes stl{to{transform:translateX(-38px);opacity:0}}
@keyframes sfl{from{transform:translateX(-38px);opacity:0}}
@keyframes str{to{transform:translateX(38px);opacity:0}}
::view-transition-group(root){animation-duration:.28s;animation-timing-function:cubic-bezier(.4,0,.2,1)}
html:active-view-transition-type(forward)::view-transition-old(root){animation-name:stl}
html:active-view-transition-type(forward)::view-transition-new(root){animation-name:sfr}
html:active-view-transition-type(backward)::view-transition-old(root){animation-name:str}
html:active-view-transition-type(backward)::view-transition-new(root){animation-name:sfl}
@media(prefers-reduced-motion:reduce){::view-transition-group(root){animation:none!important}}

/* AI PANEL */
.aifab{position:fixed;bottom:26px;right:26px;width:54px;height:54px;border-radius:50%;background:linear-gradient(135deg,var(--bb),var(--dn));color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 32px rgba(0,101,255,.42);z-index:200;transition:transform .25s cubic-bezier(.34,1.56,.64,1),box-shadow var(--tr)}
.aifab:hover{transform:scale(1.1);box-shadow:0 12px 40px rgba(0,101,255,.52)}
.aifab.op{transform:scale(.9) rotate(180deg)}
.aipan{position:fixed;bottom:92px;right:26px;width:375px;max-height:555px;background:var(--bg-c);border:1px solid var(--ba);border-radius:var(--rxl);box-shadow:0 24px 64px rgba(0,0,0,.48),var(--sg);display:flex;flex-direction:column;z-index:200;overflow:hidden;transition:opacity .24s,transform .28s cubic-bezier(.34,1.56,.64,1)}
.aipan.hd{opacity:0;transform:translateY(18px) scale(.96);pointer-events:none}
.aihdr{padding:14px 16px;background:linear-gradient(135deg,rgba(0,101,255,.14),rgba(0,10,105,.18));border-bottom:1px solid var(--bo);display:flex;align-items:center;gap:9px}
.aiav{width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--bb),var(--dn));display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:0 2px 8px var(--ag)}
.ait{font-weight:700;font-size:.88rem}
.ais{font-size:.7rem;color:var(--ok);font-weight:600}
.aiind{width:7px;height:7px;border-radius:50%;background:var(--ok);margin-left:auto;animation:pdb 2s infinite}
.aimsg{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}
.aim{display:flex;gap:7px;animation:mi .28s ease}
.aim.u{flex-direction:row-reverse}
.aib{max-width:82%;padding:9px 13px;border-radius:var(--rmd);font-size:.83rem;line-height:1.55}
.aim.ai .aib{background:var(--bg-in);border:1px solid var(--bo);color:var(--tx);border-radius:4px var(--rmd) var(--rmd) var(--rmd)}
.aim.u .aib{background:linear-gradient(135deg,var(--bb),color-mix(in oklab,var(--bb) 72%,var(--dn)));color:#fff;border-radius:var(--rmd) 4px var(--rmd) var(--rmd)}
.aitypb{display:flex;gap:4px;padding:9px 13px}
.aitypb span{width:5px;height:5px;border-radius:50%;background:var(--txm);animation:bd 1.4s infinite}
.aitypb span:nth-child(2){animation-delay:.2s}
.aitypb span:nth-child(3){animation-delay:.4s}
.aiinr{padding:11px 14px;border-top:1px solid var(--bo);display:flex;gap:7px;align-items:center}
.aiin{flex:1;background:var(--bg-in);border:1px solid var(--bo);border-radius:var(--rfl);padding:7px 14px;font-size:.83rem;color:var(--tx);outline:none;transition:border-color var(--tr)}
.aiin:focus{border-color:var(--ba)}
.aisnd{width:32px;height:32px;border-radius:50%;background:var(--ac);color:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 2px 8px var(--ag);transition:transform .15s}
.aisnd:hover{transform:scale(1.1)}
.aichs{display:flex;gap:5px;flex-wrap:wrap;padding:0 14px 8px}
.aich{padding:3px 9px;border-radius:var(--rfl);font-size:.7rem;font-weight:600;background:var(--bg-in);border:1px solid var(--bo);color:var(--tx2);cursor:pointer;transition:all var(--tr)}
.aich:hover{background:var(--ag);border-color:var(--ba);color:var(--lb)}

/* RESPONSIVE */
@media(max-width:768px){
.shell{grid-template-columns:0 1fr}
.sb{position:fixed;left:-260px;transition:left var(--tr)}
.sb.op{left:0}
.tb{grid-column:1/-1}
.mc{grid-column:1/-1;padding:14px}
.srch{display:none}
.kgrid{grid-template-columns:1fr 1fr}
.cgrid{grid-template-columns:1fr}
.aipan{right:10px;left:10px;width:auto}
}
}
</style>
</head>
<body>
<div id="app"></div>
<script>
const{createApp,ref,computed,onMounted,watch,nextTick}=Vue;
const SID='1xOentPWi5Yah9nPhtK4vi2-8KH7tSOT0TWuHl_XkIYk';

async function fetchSheet(name){
  try{
    const r=await fetch(`https://docs.google.com/spreadsheets/d/${SID}/gviz/tq?tqx=out:csv&sheet=${encodeURIComponent(name)}`);
    if(!r.ok)throw new Error(r.status);
    return parseCSV(await r.text());
  }catch(e){return null;}
}
function parseCSV(t){
  const ls=t.split('\n').filter(l=>l.trim());
  if(ls.length<2)return[];
  const hs=csvLine(ls[0]).map(h=>h.replace(/"/g,'').trim().toLowerCase().replace(/\s+/g,'_'));
  return ls.slice(1).map(l=>{const v=csvLine(l);const o={};hs.forEach((h,i)=>{o[h]=(v[i]||'').replace(/"/g,'').trim();});return o;});
}
function csvLine(l){
  const r=[];let c='',q=false;
  for(const ch of l){if(ch==='"'){q=!q;}else if(ch===','&&!q){r.push(c);c='';}else{c+=ch;}}
  r.push(c);return r;
}

function mock(){
  const sts=['SUCESSO','SUCESSO COM ERROS','ERRO','EM EXECUCAO'];
  const fns=['registrarCaixasNoDocZ','registrarDocumentosNoDocZ','processarIACaixas','processarIADocumentos'];
  const ecs=['ERRO DOCZ','ERRO DOCZ IA','ERRO IA','REVISÃO MANUAL'];
  const execs=Array.from({length:40},(_,i)=>{
    const st=sts[i%4];const tp=Math.floor(Math.random()*55)+5;
    const er=st==='ERRO'?tp:st==='SUCESSO COM ERROS'?Math.floor(tp*.15):0;
    const d=new Date();d.setHours(d.getHours()-i*2);
    return{execucao_id:`EX-${String(i+1).padStart(4,'0')}`,iniciado_em:d.toISOString().slice(0,19).replace('T',' '),
    funcao:fns[i%4],status:st,total_processado:String(tp),total_sucesso:String(tp-er),total_erro:String(er),
    duracao_ms:String(Math.floor(Math.random()*180000)+5000),mensagem_resumo:`Lote ${i+1}. ${tp} itens.`};
  });
  const errs=Array.from({length:30},(_,i)=>{
    const d=new Date();d.setHours(d.getHours()-i*6);
    return{erro_id:`ERR-${String(i+1).padStart(4,'0')}`,criado_em:d.toISOString().slice(0,19).replace('T',' '),
    status_erro:i%3===0?'RESOLVIDO':i%7===0?'IGNORADO':'ABERTO',
    tipo_entidade:i%2===0?'CAIXA':'DOCUMENTO',
    etiqueta:i%2===0?`CB${String(i+1).padStart(5,'0')}SOS`:`DC${String(i+1).padStart(5,'0')}SOS`,
    codigo_erro:ecs[i%4],mensagem_erro:'DocZ HTTP 500: serviço indisponível.',tentativas:String(1+i%3),
    execucao_id:`EX-${String(i%10+1).padStart(4,'0')}`};
  });
  const itens=Array.from({length:150},(_,i)=>{
    const d=new Date();d.setMinutes(d.getMinutes()-i*30);
    const st=i%7===0?'ERRO':'SUCESSO';
    return{timestamp:d.toISOString().slice(0,19).replace('T',' '),execucao_id:`EX-${String(i%10+1).padStart(4,'0')}`,
    tipo_entidade:i%2===0?'CAIXA':'DOCUMENTO',
    etiqueta:i%2===0?`CB${String(i+1).padStart(5,'0')}SOS`:`DC${String(i+1).padStart(5,'0')}SOS`,
    status_item:st,status_docz:st==='SUCESSO'?'REGISTRADO':'ERRO DOCZ',
    status_arquivo_docz:st==='SUCESSO'?'PDF ENVIADO':'',mensagem_resumida:st==='SUCESSO'?'Registrado com sucesso.':'Falha DocZ.'};
  });
  const logs=Array.from({length:60},(_,i)=>{
    const d=new Date();d.setMinutes(d.getMinutes()-i*10);
    const nv=['INFO','INFO','INFO','WARN','ERROR'];
    return{timestamp:d.toISOString().slice(0,19).replace('T',' '),nivel:nv[i%5],funcao:fns[i%4],
    etiqueta:i%3===0?`CB${String(i+1).padStart(4,'0')}SOS`:`DC${String(i+1).padStart(4,'0')}SOS`,
    mensagem:nv[i%5]==='ERROR'?'Falha crítica ao conectar com DocZ.':nv[i%5]==='WARN'?'Retentativa 2/3.':
    `Item processado. Execução EX-${String(i%10+1).padStart(4,'0')}.`};
  });
  const dash=[
    {indicador:'TOTAL_CAIXAS_REGISTRADAS',valor:'4.821',atualizado_em:new Date().toISOString()},
    {indicador:'TOTAL_DOCUMENTOS_REGISTRADOS',valor:'18.340',atualizado_em:new Date().toISOString()},
    {indicador:'TOTAL_EXECUCOES',valor:'312',atualizado_em:new Date().toISOString()},
    {indicador:'TOTAL_ERROS_ABERTOS',valor:'17',atualizado_em:new Date().toISOString()},
    {indicador:'TAXA_SUCESSO_CAIXAS',valor:'97.4',atualizado_em:new Date().toISOString()},
    {indicador:'TAXA_SUCESSO_DOCUMENTOS',valor:'96.1',atualizado_em:new Date().toISOString()},
  ];
  return{execs,errs,itens,logs,dash};
}

function fmt(ms){if(!ms)return'—';const s=Math.round(+ms/1000);return s<60?`${s}s`:`${Math.floor(s/60)}m${s%60}s`;}
function fdt(dt){if(!dt)return'—';try{return new Date(dt).toLocaleString('pt-BR',{day:'2-digit',month:'2-digit',hour:'2-digit',minute:'2-digit'});}catch{return dt;}}
function sc(s){
  if(!s)return'i';const u=s.toUpperCase();
  if(u.includes('SUCESSO')&&!u.includes('ERRO'))return's';
  if(u.includes('ERRO'))return'e';
  if(u.includes('EXECUCAO')||u.includes('EXECUÇÃO'))return'r';
  if(u.includes('REVISÃO')||u.includes('ABERTO')||u.includes('WARN')||u.includes('WARN'))return'w';
  if(u==='RESOLVIDO')return's';if(u==='IGNORADO')return'i';return'i';
}
function ed(s){if(!s)return'i';const u=s.toUpperCase();if(u.includes('SUCESSO')&&!u.includes('ERRO'))return's';if(u.includes('ERRO'))return'e';if(u.includes('EXECUCAO')||u.includes('EXECUÇÃO'))return'r';return'w';}
function pg(arr,p,lim){return arr.slice((p-1)*lim,p*lim);}
function pns(cur,tot){
  if(tot<=7)return Array.from({length:tot},(_,i)=>i+1);
  const a=[];
  if(cur<=4){for(let i=1;i<=5;i++)a.push(i);a.push('...');a.push(tot);}
  else if(cur>=tot-3){a.push(1);a.push('...');for(let i=tot-4;i<=tot;i++)a.push(i);}
  else{a.push(1);a.push('...');for(let i=cur-1;i<=cur+1;i++)a.push(i);a.push('...');a.push(tot);}
  return a;
}

function cbase(dk){
  return{
    chart:{background:'transparent',fontFamily:"'Inter',sans-serif",toolbar:{show:false},animations:{enabled:true,easing:'easeinout',speed:750}},
    theme:{mode:dk?'dark':'light'},
    colors:['#0065ff','#00b86b','#dea511','#9ac2ff','#e63946'],
    tooltip:{theme:dk?'dark':'light',style:{fontFamily:"'Inter',sans-serif",fontSize:'12px'}},
    grid:{borderColor:dk?'rgba(154,194,255,.1)':'rgba(0,10,105,.07)',strokeDashArray:4,xaxis:{lines:{show:false}}},
    xaxis:{labels:{style:{colors:dk?'#9ac2ff':'#6b82b0',fontSize:'11px'}},axisBorder:{show:false},axisTicks:{show:false}},
    yaxis:{labels:{style:{colors:dk?'#9ac2ff':'#6b82b0',fontSize:'11px'}}},
    legend:{labels:{colors:dk?'#9ac2ff':'#2d4a8a'}}
  };
}

const App={
  template:`
  <div class="bgp"></div>
  <div class="tl" v-if="loading"></div>
  <div class="shell" :class="{col:sc2}">
    <!-- SIDEBAR -->
    <aside class="sb">
      <div class="sb-logo">
        <div class="logo-ic">S</div>
        <div v-show="!sc2">
          <div class="logo-t">sosdocs</div>
          <div class="logo-s">HealthData Platform</div>
        </div>
      </div>
      <nav class="sb-nav">
        <div class="nl">Visão Geral</div>
        <div v-for="n in nav.slice(0,3)" :key="n.id" class="ni" :class="{on:pg2===n.id}" @click="go(n.id)" :title="n.label">
          <i :data-lucide="n.icon" class="ni-ic"></i>
          <span class="ni-lb">{{n.label}}</span>
          <span v-if="n.badge" class="nbadge" :class="n.bt">{{n.badge}}</span>
        </div>
        <div class="nl">Operações</div>
        <div v-for="n in nav.slice(3,7)" :key="n.id" class="ni" :class="{on:pg2===n.id}" @click="go(n.id)" :title="n.label">
          <i :data-lucide="n.icon" class="ni-ic"></i>
          <span class="ni-lb">{{n.label}}</span>
          <span v-if="n.badge" class="nbadge" :class="n.bt">{{n.badge}}</span>
        </div>
        <div class="nl">Sistema</div>
        <div v-for="n in nav.slice(7)" :key="n.id" class="ni" :class="{on:pg2===n.id}" @click="go(n.id)" :title="n.label">
          <i :data-lucide="n.icon" class="ni-ic"></i>
          <span class="ni-lb">{{n.label}}</span>
        </div>
      </nav>
      <div class="sb-bot">
        <div class="ni"><i data-lucide="log-out" class="ni-ic"></i><span class="ni-lb">Sair</span></div>
      </div>
    </aside>

    <!-- TOPBAR -->
    <header class="tb">
      <button class="tb-tog" @click="sc2=!sc2"><i data-lucide="menu" style="width:17px;height:17px"></i></button>
      <span class="tb-title">{{pgLbl}}</span>
      <div class="srch">
        <i data-lucide="search" style="width:13px;height:13px;color:var(--txm);flex-shrink:0"></i>
        <input placeholder="Buscar CB, DC, execução..." v-model="gs"/>
      </div>
      <div class="tb-acts">
        <button class="icb"><i data-lucide="bell" style="width:15px;height:15px"></i><span class="dot" v-if="ec>0"></span></button>
        <button class="icb" @click="load()"><i data-lucide="refresh-cw" style="width:15px;height:15px" :style="loading?'animation:spin 1s linear infinite':''"></i></button>
        <button class="tt-btn" @click="thm()">
          <div class="tt-knob"><i :data-lucide="dk?'moon':'sun'" style="width:11px;height:11px;color:#fff"></i></div>
        </button>
        <div class="av">A</div>
      </div>
    </header>

    <!-- MAIN -->
    <main class="mc" style="position:relative;z-index:1">

      <!-- === DASHBOARD === -->
      <div v-if="pg2==='dash'" class="sea">
        <div class="ph">
          <div><h1>Dashboard</h1><div class="ph-sub">Visão executiva do projeto HealthData · Atualizado {{upd}}</div></div>
          <div style="display:flex;gap:8px;align-items:center">
            <span class="chip" :class="modo==='PRODUCAO'?'s':'w'">{{modo==='PRODUCAO'?'● PRODUÇÃO':'◆ TESTE'}}</span>
            <button class="btn bp" @click="load()"><i data-lucide="refresh-cw" style="width:13px;height:13px"></i> Atualizar</button>
          </div>
        </div>
        <div class="kgrid">
          <div class="kcard" style="--ka:var(--bb)">
            <div class="ktop"><div class="klbl">Total de Caixas</div><div class="kic"><i data-lucide="package" style="width:15px;height:15px"></i></div></div>
            <div class="kval">{{kpis.tc}}</div><div class="kft">Registradas no DocZ</div>
          </div>
          <div class="kcard" style="--ka:var(--ok)">
            <div class="ktop"><div class="klbl">Total de Documentos</div><div class="kic"><i data-lucide="file-text" style="width:15px;height:15px"></i></div></div>
            <div class="kval">{{kpis.td}}</div><div class="kft">Registrados no DocZ</div>
          </div>
          <div class="kcard" style="--ka:var(--gd)">
            <div class="ktop"><div class="klbl">Execuções</div><div class="kic"><i data-lucide="play-circle" style="width:15px;height:15px"></i></div></div>
            <div class="kval">{{kpis.te}}</div><div class="kft">Total de ondas</div>
          </div>
          <div class="kcard" style="--ka:var(--er)">
            <div class="ktop"><div class="klbl">Erros Abertos</div><div class="kic"><i data-lucide="alert-circle" style="width:15px;height:15px"></i></div></div>
            <div class="kval">{{kpis.ea}}</div><div class="kft">Aguardando atenção</div>
          </div>
          <div class="kcard" style="--ka:var(--bb)">
            <div class="ktop"><div class="klbl">Taxa Sucesso CB</div><div class="kic"><i data-lucide="trending-up" style="width:15px;height:15px"></i></div></div>
            <div class="kval">{{kpis.tsc}}%</div>
            <div class="pb" style="margin-top:8px"><div class="pf" :style="{width:kpis.tsc+'%',background:'linear-gradient(90deg,var(--ok),var(--bb))'}"></div></div>
          </div>
          <div class="kcard" style="--ka:var(--lb)">
            <div class="ktop"><div class="klbl">Taxa Sucesso DC</div><div class="kic"><i data-lucide="trending-up" style="width:15px;height:15px"></i></div></div>
            <div class="kval">{{kpis.tsd}}%</div>
            <div class="pb" style="margin-top:8px"><div class="pf" :style="{width:kpis.tsd+'%',background:'linear-gradient(90deg,var(--lb),var(--bb))'}"></div></div>
          </div>
        </div>
        <div class="cgrid">
          <div class="card">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px"><h3>Processamento por Execução</h3><span style="font-size:.73rem;color:var(--txm)">Últimas 15</span></div>
            <div id="cl" style="min-height:230px"></div>
          </div>
          <div class="card">
            <div style="margin-bottom:14px"><h3>Status das Execuções</h3></div>
            <div id="cd" style="min-height:230px"></div>
          </div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px" class="r2c">
          <div class="card">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
              <h3>Últimas Execuções</h3>
              <button class="btn bg" style="font-size:.76rem;padding:4px 11px" @click="go('execs')">Ver todas</button>
            </div>
            <div v-for="x in recExec" :key="x.execucao_id" class="ei">
              <div class="edot" :class="ed(x.status)"></div>
              <div>
                <div class="etit">{{x.funcao}}</div>
                <div class="emeta">{{fdt(x.iniciado_em)}} · {{x.execucao_id}}</div>
                <div style="margin-top:5px"><span class="chip" :class="sc(x.status)">{{x.status}}</span></div>
              </div>
              <div class="edur">{{fmt(x.duracao_ms)}}<br/><span>{{x.total_processado}} itens</span></div>
            </div>
          </div>
          <div class="card">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
              <h3>Erros Recentes</h3>
              <button class="btn bg" style="font-size:.76rem;padding:4px 11px" @click="go('errs')">Ver todos</button>
            </div>
            <div class="twrap">
              <table class="dt">
                <thead><tr><th>Etiqueta</th><th>Código</th><th>Status</th></tr></thead>
                <tbody>
                  <tr v-for="e in recErrs" :key="e.erro_id">
                    <td style="font-family:monospace;font-size:.79rem">{{e.etiqueta}}</td>
                    <td><span class="chip e">{{e.codigo_erro}}</span></td>
                    <td><span class="chip" :class="sc(e.status_erro)">{{e.status_erro}}</span></td>
                  </tr>
                  <tr v-if="!recErrs.length"><td colspan="3"><div class="emp"><div class="emp-ic">✅</div>Sem erros!</div></td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- === EXECUÇÕES === -->
      <div v-if="pg2==='execs'" class="sea">
        <div class="ph"><div><h1>Execuções</h1><div class="ph-sub">Histórico de ondas de processamento</div></div></div>
        <div class="card">
          <div class="fbar">
            <select class="fs" v-model="ef.st" style="width:180px"><option value="">Todos status</option><option>SUCESSO</option><option>SUCESSO COM ERROS</option><option>ERRO</option><option>EM EXECUCAO</option></select>
            <select class="fs" v-model="ef.fn" style="width:230px"><option value="">Todas funções</option><option>registrarCaixasNoDocZ</option><option>registrarDocumentosNoDocZ</option><option>processarIACaixas</option><option>processarIADocumentos</option></select>
            <input class="fi" placeholder="Buscar ID..." v-model="ef.q" style="width:180px"/>
            <span class="pinf" style="margin-left:auto">{{fExec.length}} registros</span>
          </div>
          <div class="twrap">
            <table class="dt">
              <thead><tr><th>ID</th><th>Função</th><th>Status</th><th>Início</th><th>Duração</th><th>Total</th><th>Sucesso</th><th>Erros</th></tr></thead>
              <tbody>
                <tr v-for="x in pgExec" :key="x.execucao_id">
                  <td style="font-family:monospace;font-size:.76rem;color:var(--txm)">{{x.execucao_id}}</td>
                  <td style="font-size:.8rem;max-width:190px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{{x.funcao}}</td>
                  <td><span class="chip" :class="sc(x.status)">{{x.status}}</span></td>
                  <td style="font-size:.78rem;white-space:nowrap">{{fdt(x.iniciado_em)}}</td>
                  <td style="font-variant-numeric:tabular-nums;font-size:.8rem">{{fmt(x.duracao_ms)}}</td>
                  <td style="font-weight:600">{{x.total_processado||'—'}}</td>
                  <td style="color:var(--ok);font-weight:600">{{x.total_sucesso||'—'}}</td>
                  <td style="color:var(--er);font-weight:600">{{x.total_erro||'0'}}</td>
                </tr>
                <tr v-if="!pgExec.length"><td colspan="8"><div class="emp"><div class="emp-ic">📋</div>Sem execuções.</div></td></tr>
              </tbody>
            </table>
          </div>
          <div class="pag">
            <span class="pinf">{{fExec.length}} itens · pág. {{ep}}/{{etot}}</span>
            <button class="pbtn" :disabled="ep===1" @click="ep--">‹</button>
            <button v-for="p in pns(ep,etot)" :key="p" class="pbtn" :class="{on:p===ep}" @click="p!=='...'&&(ep=p)">{{p}}</button>
            <button class="pbtn" :disabled="ep===etot" @click="ep++">›</button>
          </div>
        </div>
      </div>

      <!-- === CAIXAS & DOCS === -->
      <div v-if="pg2==='itens'" class="sea">
        <div class="ph"><div><h1>Caixas &amp; Documentos</h1><div class="ph-sub">Itens processados — consulta operacional</div></div></div>
        <div class="card">
          <div class="fbar">
            <select class="fs" v-model="if2.tp" style="width:140px"><option value="">Todos</option><option>CAIXA</option><option>DOCUMENTO</option></select>
            <select class="fs" v-model="if2.st" style="width:150px"><option value="">Todos status</option><option>SUCESSO</option><option>ERRO</option></select>
            <input class="fi" placeholder="Buscar etiqueta CB/DC..." v-model="if2.q" style="width:220px"/>
            <span class="pinf" style="margin-left:auto">{{fItens.length}} registros</span>
          </div>
          <div class="srow">
            <div class="sitm"><div class="sdot" style="background:var(--bb)"></div><span class="sval">{{ist.cb}}</span><span class="slbl">Caixas</span></div>
            <div class="sitm"><div class="sdot" style="background:var(--lb)"></div><span class="sval">{{ist.dc}}</span><span class="slbl">Documentos</span></div>
            <div class="sitm"><div class="sdot" style="background:var(--ok)"></div><span class="sval">{{ist.ok}}</span><span class="slbl">Sucesso</span></div>
            <div class="sitm"><div class="sdot" style="background:var(--er)"></div><span class="sval">{{ist.er}}</span><span class="slbl">Erro</span></div>
          </div>
          <div class="twrap">
            <table class="dt">
              <thead><tr><th>Data</th><th>Tipo</th><th>Etiqueta</th><th>Status</th><th>DocZ</th><th>Arquivo</th><th>Execução</th></tr></thead>
              <tbody>
                <tr v-for="it in pgItens" :key="it.timestamp+it.etiqueta">
                  <td style="font-size:.76rem;white-space:nowrap;color:var(--txm)">{{fdt(it.timestamp)}}</td>
                  <td><span class="chip" :class="it.tipo_entidade==='CAIXA'?'i':'r'">{{it.tipo_entidade}}</span></td>
                  <td style="font-family:monospace;font-size:.8rem;font-weight:600">{{it.etiqueta}}</td>
                  <td><span class="chip" :class="sc(it.status_item)">{{it.status_item}}</span></td>
                  <td><span class="chip" :class="sc(it.status_docz)">{{it.status_docz||'—'}}</span></td>
                  <td style="font-size:.76rem;color:var(--txm)">{{it.status_arquivo_docz||'—'}}</td>
                  <td style="font-family:monospace;font-size:.74rem;color:var(--txm)">{{it.execucao_id}}</td>
                </tr>
                <tr v-if="!pgItens.length"><td colspan="7"><div class="emp"><div class="emp-ic">📦</div>Nenhum item.</div></td></tr>
              </tbody>
            </table>
          </div>
          <div class="pag">
            <span class="pinf">{{fItens.length}} itens · pág. {{ip}}/{{itot}}</span>
            <button class="pbtn" :disabled="ip===1" @click="ip--">‹</button>
            <button v-for="p in pns(ip,itot)" :key="p" class="pbtn" :class="{on:p===ip}" @click="p!=='...'&&(ip=p)">{{p}}</button>
            <button class="pbtn" :disabled="ip===itot" @click="ip++">›</button>
          </div>
        </div>
      </div>

      <!-- === ERROS === -->
      <div v-if="pg2==='errs'" class="sea">
        <div class="ph"><div><h1>Erros</h1><div class="ph-sub">Falhas registradas pelo sistema</div></div></div>
        <div class="card">
          <div class="fbar">
            <select class="fs" v-model="erf.st" style="width:150px"><option value="">Todos</option><option>ABERTO</option><option>RESOLVIDO</option><option>IGNORADO</option></select>
            <select class="fs" v-model="erf.tp" style="width:140px"><option value="">Todos tipos</option><option>CAIXA</option><option>DOCUMENTO</option></select>
            <select class="fs" v-model="erf.cd" style="width:190px"><option value="">Todos códigos</option><option>ERRO DOCZ</option><option>ERRO DOCZ IA</option><option>ERRO IA</option><option>REVISÃO MANUAL</option></select>
            <input class="fi" placeholder="Buscar etiqueta..." v-model="erf.q" style="width:190px"/>
          </div>
          <div class="twrap">
            <table class="dt">
              <thead><tr><th>Data</th><th>Tipo</th><th>Etiqueta</th><th>Código</th><th>Status</th><th>Tent.</th><th>Execução</th></tr></thead>
              <tbody>
                <tr v-for="e in pgErrs" :key="e.erro_id">
                  <td style="font-size:.76rem;white-space:nowrap;color:var(--txm)">{{fdt(e.criado_em)}}</td>
                  <td><span class="chip" :class="e.tipo_entidade==='CAIXA'?'i':'r'">{{e.tipo_entidade}}</span></td>
                  <td style="font-family:monospace;font-size:.8rem;font-weight:600">{{e.etiqueta}}</td>
                  <td><span class="chip e">{{e.codigo_erro}}</span></td>
                  <td><span class="chip" :class="sc(e.status_erro)">{{e.status_erro}}</span></td>
                  <td style="text-align:center;font-weight:700">{{e.tentativas}}</td>
                  <td style="font-family:monospace;font-size:.74rem;color:var(--txm)">{{e.execucao_id}}</td>
                </tr>
                <tr v-if="!pgErrs.length"><td colspan="7"><div class="emp"><div class="emp-ic">✅</div>Sem erros!</div></td></tr>
              </tbody>
            </table>
          </div>
          <div class="pag">
            <span class="pinf">{{fErrs.length}} erros · pág. {{errp}}/{{errtot}}</span>
            <button class="pbtn" :disabled="errp===1" @click="errp--">‹</button>
            <button v-for="p in pns(errp,errtot)" :key="p" class="pbtn" :class="{on:p===errp}" @click="p!=='...'&&(errp=p)">{{p}}</button>
            <button class="pbtn" :disabled="errp===errtot" @click="errp++">›</button>
          </div>
        </div>
      </div>

      <!-- === LOGS === -->
      <div v-if="pg2==='logs'" class="sea">
        <div class="ph"><div><h1>Logs Operacionais</h1><div class="ph-sub">Eventos gerados pelas execuções</div></div></div>
        <div class="card">
          <div class="fbar">
            <select class="fs" v-model="lf.nv" style="width:140px"><option value="">Todos níveis</option><option>INFO</option><option>WARN</option><option>ERROR</option></select>
            <input class="fi" placeholder="Buscar na mensagem..." v-model="lf.q" style="width:260px"/>
            <span class="pinf" style="margin-left:auto">{{fLogs.length}} eventos</span>
          </div>
          <div class="twrap">
            <table class="dt">
              <thead><tr><th>Data</th><th>Nível</th><th>Função</th><th>Etiqueta</th><th>Mensagem</th></tr></thead>
              <tbody>
                <tr v-for="(l,i) in pgLogs" :key="i">
                  <td style="font-size:.76rem;white-space:nowrap;color:var(--txm)">{{fdt(l.timestamp)}}</td>
                  <td><span class="chip" :class="l.nivel==='ERROR'?'e':l.nivel==='WARN'?'w':'i'">{{l.nivel}}</span></td>
                  <td style="font-size:.78rem;max-width:170px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{{l.funcao}}</td>
                  <td style="font-family:monospace;font-size:.76rem">{{l.etiqueta||'—'}}</td>
                  <td style="font-size:.8rem;max-width:340px">{{l.mensagem}}</td>
                </tr>
                <tr v-if="!pgLogs.length"><td colspan="5"><div class="emp"><div class="emp-ic">📄</div>Sem logs.</div></td></tr>
              </tbody>
            </table>
          </div>
          <div class="pag">
            <span class="pinf">{{fLogs.length}} logs · pág. {{lp}}/{{ltot}}</span>
            <button class="pbtn" :disabled="lp===1" @click="lp--">‹</button>
            <button v-for="p in pns(lp,ltot)" :key="p" class="pbtn" :class="{on:p===lp}" @click="p!=='...'&&(lp=p)">{{p}}</button>
            <button class="pbtn" :disabled="lp===ltot" @click="lp++">›</button>
          </div>
        </div>
      </div>

      <!-- === ANALYTICS === -->
      <div v-if="pg2==='anlx'" class="sea">
        <div class="ph"><div><h1>Analytics</h1><div class="ph-sub">Tendências, rankings e evolução temporal</div></div></div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px" class="r2c">
          <div class="card"><h3 style="margin-bottom:14px">Distribuição Status DocZ</h3><div id="cbs" style="min-height:270px"></div></div>
          <div class="card"><h3 style="margin-bottom:14px">Erros por Código</h3><div id="cpe" style="min-height:270px"></div></div>
        </div>
        <div class="card"><h3 style="margin-bottom:14px">Volume de Processamento — Histórico</h3><div id="car" style="min-height:290px"></div></div>
      </div>

      <!-- === CONFIG === -->
      <div v-if="pg2==='cfg'" class="sea">
        <div class="ph"><div><h1>Configurações</h1><div class="ph-sub">Parâmetros operacionais (somente leitura)</div></div></div>
        <div class="card">
          <div class="twrap">
            <table class="dt">
              <thead><tr><th>Chave</th><th>Valor</th><th>Descrição</th><th>Atualizado</th></tr></thead>
              <tbody>
                <tr v-for="c in cfgD" :key="c.chave">
                  <td style="font-family:monospace;font-size:.78rem;font-weight:600;color:var(--lb)">{{c.chave}}</td>
                  <td>
                    <span v-if="c.valor==='True'||c.valor==='true'" class="chip s">{{c.valor}}</span>
                    <span v-else-if="c.valor==='False'||c.valor==='false'" class="chip e">{{c.valor}}</span>
                    <span v-else style="font-family:monospace;font-weight:700">{{c.valor}}</span>
                  </td>
                  <td style="font-size:.8rem;color:var(--txm)">{{c.descricao}}</td>
                  <td style="font-size:.75rem;color:var(--txm);white-space:nowrap">{{fdt(c.atualizado_em)}}</td>
                </tr>
                <tr v-if="!cfgD.length"><td colspan="4"><div class="emp"><div class="emp-ic">⚙️</div>Sem configurações.</div></td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </main>
  </div>

  <!-- AI FAB -->
  <button class="aifab" :class="{op:aiop}" @click="aiop=!aiop">
    <i :data-lucide="aiop?'x':'sparkles'" style="width:20px;height:20px"></i>
  </button>
  <div class="aipan" :class="{hd:!aiop}">
    <div class="aihdr">
      <div class="aiav">✨</div>
      <div><div class="ait">Assistente IA HealthData</div><div class="ais">● Online</div></div>
      <div class="aiind"></div>
    </div>
    <div class="aimsg" ref="cb">
      <div v-for="(m,i) in msgs" :key="i" class="aim" :class="m.role">
        <div class="aib" v-html="m.text"></div>
      </div>
      <div v-if="aityp" class="aim ai"><div class="aib aitypb"><span></span><span></span><span></span></div></div>
    </div>
    <div class="aichs">
      <button v-for="q in sugs" :key="q" class="aich" @click="send(q)">{{q}}</button>
    </div>
    <div class="aiinr">
      <input class="aiin" placeholder="Pergunte sobre as execuções..." v-model="ain" @keydown.enter="send()"/>
      <button class="aisnd" @click="send()"><i data-lucide="send" style="width:13px;height:13px"></i></button>
    </div>
  </div>
  <style>@media(max-width:900px){.r2c{grid-template-columns:1fr!important}}</style>
  `,
  setup(){
    const sc2=ref(false),loading=ref(false),pg2=ref('dash'),dk=ref(true),aiop=ref(false),ain=ref(''),aityp=ref(false),gs=ref(''),cb=ref(null),upd=ref('—'),modo=ref('PRODUCAO');
    const exD=ref([]),erD=ref([]),itD=ref([]),lgD=ref([]),dkD=ref([]),cfgD=ref([]);
    const msgs=ref([{role:'ai',text:'Olá! Sou o Assistente IA HealthData. Posso pesquisar dados, resumir execuções e identificar padrões. Como posso ajudar?'}]);
    const sugs=['Erros abertos?','Taxa de sucesso?','Última execução','Caixas com erro'];
    const PG=25;
    const ef=ref({st:'',fn:'',q:''}),ep=ref(1);
    const if2=ref({tp:'',st:'',q:''}),ip=ref(1);
    const erf=ref({st:'',tp:'',cd:'',q:''}),errp=ref(1);
    const lf=ref({nv:'',q:''}),lp=ref(1);
    let ch={};

    const nav=computed(()=>[
      {id:'dash',label:'Dashboard',icon:'layout-dashboard'},
      {id:'anlx',label:'Analytics',icon:'bar-chart-3'},
      {id:'itens',label:'Caixas & Docs',icon:'package'},
      {id:'execs',label:'Execuções',icon:'play-circle'},
      {id:'errs',label:'Erros',icon:'alert-circle',badge:ec.value||null,bt:'e'},
      {id:'logs',label:'Logs',icon:'file-text'},
      {id:'smoke',label:'Smoke Tests',icon:'flask-conical'},
      {id:'cfg',label:'Configurações',icon:'settings'},
    ]);
    const pgLbl=computed(()=>({dash:'Dashboard',anlx:'Analytics',itens:'Caixas & Documentos',execs:'Execuções',errs:'Erros',logs:'Logs Operacionais',cfg:'Configurações',smoke:'Smoke Tests'})[pg2.value]||pg2.value);
    const kpis=computed(()=>{
      const f=k=>dkD.value.find(d=>d.indicador===k)?.valor||'—';
      return{tc:f('TOTAL_CAIXAS_REGISTRADAS'),td:f('TOTAL_DOCUMENTOS_REGISTRADOS'),te:f('TOTAL_EXECUCOES')||exD.value.length,ea:f('TOTAL_ERROS_ABERTOS')||erD.value.filter(e=>e.status_erro==='ABERTO').length,tsc:f('TAXA_SUCESSO_CAIXAS'),tsd:f('TAXA_SUCESSO_DOCUMENTOS')};
    });
    const ec=computed(()=>erD.value.filter(e=>e.status_erro==='ABERTO').length);
    const recExec=computed(()=>exD.value.slice(0,6));
    const recErrs=computed(()=>erD.value.slice(0,6));
    const fExec=computed(()=>exD.value.filter(x=>{if(ef.value.st&&x.status!==ef.value.st)return false;if(ef.value.fn&&x.funcao!==ef.value.fn)return false;if(ef.value.q&&!x.execucao_id.toLowerCase().includes(ef.value.q.toLowerCase()))return false;return true;}));
    const etot=computed(()=>Math.max(1,Math.ceil(fExec.value.length/PG)));
    const pgExec=computed(()=>pg(fExec.value,ep.value,PG));
    const fItens=computed(()=>itD.value.filter(i=>{if(if2.value.tp&&i.tipo_entidade!==if2.value.tp)return false;if(if2.value.st&&i.status_item!==if2.value.st)return false;if(if2.value.q&&!i.etiqueta.toLowerCase().includes(if2.value.q.toLowerCase()))return false;return true;}));
    const itot=computed(()=>Math.max(1,Math.ceil(fItens.value.length/PG)));
    const pgItens=computed(()=>pg(fItens.value,ip.value,PG));
    const ist=computed(()=>({cb:fItens.value.filter(i=>i.tipo_entidade==='CAIXA').length,dc:fItens.value.filter(i=>i.tipo_entidade==='DOCUMENTO').length,ok:fItens.value.filter(i=>i.status_item==='SUCESSO').length,er:fItens.value.filter(i=>i.status_item==='ERRO').length}));
    const fErrs=computed(()=>erD.value.filter(e=>{if(erf.value.st&&e.status_erro!==erf.value.st)return false;if(erf.value.tp&&e.tipo_entidade!==erf.value.tp)return false;if(erf.value.cd&&e.codigo_erro!==erf.value.cd)return false;if(erf.value.q&&!e.etiqueta.toLowerCase().includes(erf.value.q.toLowerCase()))return false;return true;}));
    const errtot=computed(()=>Math.max(1,Math.ceil(fErrs.value.length/PG)));
    const pgErrs=computed(()=>pg(fErrs.value,errp.value,PG));
    const fLogs=computed(()=>lgD.value.filter(l=>{if(lf.value.nv&&l.nivel!==lf.value.nv)return false;if(lf.value.q&&!l.mensagem.toLowerCase().includes(lf.value.q.toLowerCase()))return false;return true;}));
    const ltot=computed(()=>Math.max(1,Math.ceil(fLogs.value.length/PG)));
    const pgLogs=computed(()=>pg(fLogs.value,lp.value,PG));

    function dchart(...ids){ids.forEach(id=>{if(ch[id]){ch[id].destroy();delete ch[id];}});}

    function rdash(){
      dchart('cl','cd');
      const b=cbase(dk.value);
      const xl=exD.value.slice(0,15).reverse();
      const clEl=document.getElementById('cl');
      if(clEl&&xl.length){ch.cl=new ApexCharts(clEl,{...b,chart:{...b.chart,type:'area',height:230},series:[{name:'Sucesso',data:xl.map(e=>+e.total_sucesso||0)},{name:'Erros',data:xl.map(e=>+e.total_erro||0)}],xaxis:{...b.xaxis,categories:xl.map((_,i)=>'Ex.'+(i+1))},fill:{type:'gradient',gradient:{opacityFrom:.32,opacityTo:.04}},stroke:{curve:'smooth',width:2.5},dataLabels:{enabled:false}});ch.cl.render();}
      const sc3={};exD.value.forEach(e=>{sc3[e.status]=(sc3[e.status]||0)+1;});
      const cdEl=document.getElementById('cd');
      if(cdEl&&Object.keys(sc3).length){ch.cd=new ApexCharts(cdEl,{...b,chart:{...b.chart,type:'donut',height:230},series:Object.values(sc3),labels:Object.keys(sc3),colors:['#00b86b','#0065ff','#dea511','#e63946'],plotOptions:{pie:{donut:{size:'66%'}}},dataLabels:{enabled:false},legend:{position:'bottom',...b.legend}});ch.cd.render();}
    }

    function ranlx(){
      dchart('cbs','cpe','car');
      const b=cbase(dk.value);
      const dz={};itD.value.forEach(i=>{if(i.status_docz)dz[i.status_docz]=(dz[i.status_docz]||0)+1;});
      const bsEl=document.getElementById('cbs');
      if(bsEl&&Object.keys(dz).length){ch.cbs=new ApexCharts(bsEl,{...b,chart:{...b.chart,type:'bar',height:270},series:[{name:'Itens',data:Object.values(dz)}],xaxis:{...b.xaxis,categories:Object.keys(dz)},plotOptions:{bar:{borderRadius:6,columnWidth:'48%'}},dataLabels:{enabled:false},colors:['#0065ff']});ch.cbs.render();}
      const ec2={};erD.value.forEach(e=>{ec2[e.codigo_erro]=(ec2[e.codigo_erro]||0)+1;});
      const peEl=document.getElementById('cpe');
      if(peEl&&Object.keys(ec2).length){ch.cpe=new ApexCharts(peEl,{...b,chart:{...b.chart,type:'pie',height:270},series:Object.values(ec2),labels:Object.keys(ec2),colors:['#e63946','#dea511','#9ac2ff','#0065ff'],dataLabels:{style:{fontFamily:"'Inter',sans-serif",fontSize:'11px'}},legend:{position:'bottom',...b.legend}});ch.cpe.render();}
      const arEl=document.getElementById('car');
      const ax=exD.value.slice(0,20).reverse();
      if(arEl&&ax.length){ch.car=new ApexCharts(arEl,{...b,chart:{...b.chart,type:'area',height:290},series:[{name:'Processados',data:ax.map(e=>+e.total_processado||0)},{name:'Sucesso',data:ax.map(e=>+e.total_sucesso||0)},{name:'Erros',data:ax.map(e=>+e.total_erro||0)}],xaxis:{...b.xaxis,categories:ax.map((_,i)=>'E'+(i+1))},fill:{type:'gradient',gradient:{opacityFrom:.28,opacityTo:.02}},stroke:{curve:'smooth',width:2},dataLabels:{enabled:false}});ch.car.render();}
    }

    function go(p){
      if(p===pg2.value)return;
      const upd2=()=>{pg2.value=p;};
      if(document.startViewTransition){document.startViewTransition({update:upd2,types:['forward']});}else{upd2();}
      nextTick(()=>{lucide.createIcons();if(p==='dash')setTimeout(rdash,100);if(p==='anlx')setTimeout(ranlx,100);});
    }

    function thm(){
      dk.value=!dk.value;
      const t=dk.value?'dark':'light';
      document.documentElement.setAttribute('data-theme',t);
      document.querySelector('meta[name="color-scheme"]').content=t;
      localStorage.setItem('sos-theme',t);
      setTimeout(()=>{rdash();if(pg2.value==='anlx')ranlx();},60);
    }

    async function load(){
      loading.value=true;
      try{
        const [dR,eR,erR,iR,lR,cR]=await Promise.allSettled([fetchSheet('Dashboard'),fetchSheet('Execucoes'),fetchSheet('Erros'),fetchSheet('Itens_Processados'),fetchSheet('Logs'),fetchSheet('Config_Publica')]);
        const m=mock();
        dkD.value=dR.status==='fulfilled'&&dR.value?.length?dR.value:m.dash;
        exD.value=eR.status==='fulfilled'&&eR.value?.length?eR.value:m.execs;
        erD.value=erR.status==='fulfilled'&&erR.value?.length?erR.value:m.errs;
        itD.value=iR.status==='fulfilled'&&iR.value?.length?iR.value:m.itens;
        lgD.value=lR.status==='fulfilled'&&lR.value?.length?lR.value:m.logs;
        cfgD.value=cR.status==='fulfilled'&&cR.value?.length?cR.value:[];
        const cm=cfgD.value.find(c=>c.chave==='MODO_EXECUCAO');if(cm)modo.value=cm.valor;
        upd.value=new Date().toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit'});
        await nextTick();lucide.createIcons();rdash();if(pg2.value==='anlx')ranlx();
      }finally{loading.value=false;}
    }

    async function send(t){
      const q=t||ain.value.trim();if(!q)return;ain.value='';
      msgs.value.push({role:'u',text:q});aityp.value=true;
      await nextTick();if(cb.value)cb.value.scrollTop=cb.value.scrollHeight;
      await new Promise(r=>setTimeout(r,900+Math.random()*500));
      msgs.value.push({role:'ai',text:aiResp(q)});aityp.value=false;
      await nextTick();if(cb.value)cb.value.scrollTop=cb.value.scrollHeight;
    }

    function aiResp(q){
      const ql=q.toLowerCase();
      const ab=erD.value.filter(e=>e.status_erro==='ABERTO');
      const te=exD.value.length;
      const ts=exD.value.filter(e=>e.status&&e.status.includes('SUCESSO')&&!e.status.includes('ERRO')).length;
      const tx=te?((ts/te)*100).toFixed(1):'—';
      if(ql.includes('erro')&&(ql.includes('caixa')||ql.includes('cb'))){
        const cb2=ab.filter(e=>e.tipo_entidade==='CAIXA');
        if(!cb2.length)return'✅ Nenhuma caixa com erro aberto!';
        return`<strong>${cb2.length} caixas</strong> com erros abertos:<br/>${cb2.slice(0,5).map(e=>`• <code>${e.etiqueta}</code> — ${e.codigo_erro}`).join('<br/>')}`;
      }
      if(ql.includes('taxa')||ql.includes('sucesso geral')||ql.includes('taxa de sucesso')){
        return`Taxa geral de sucesso: <strong>${tx}%</strong><br/>De <strong>${te}</strong> execuções, <strong>${ts}</strong> foram bem-sucedidas.`;
      }
      if(ql.includes('última')||ql.includes('ultima')){
        const l=exD.value[0];if(!l)return'Nenhuma execução registrada.';
        return`Última execução: <strong>${l.execucao_id}</strong><br/>Função: <code>${l.funcao}</code><br/>Status: <strong>${l.status}</strong><br/>Processados: <strong>${l.total_processado}</strong> em ${fmt(l.duracao_ms)}.`;
      }
      if(ql.includes('aberto')||ql.includes('atenção')||ql.includes('atencao')){
        const cds=[...new Set(ab.map(e=>e.codigo_erro))];
        return`<strong>${ab.length} erros abertos</strong>:<br/>${cds.map(c=>`• ${c}: ${ab.filter(e=>e.codigo_erro===c).length}`).join('<br/>')}`;
      }
      return`Para "<em>${q}</em>": encontrei <strong>${ab.length}</strong> erros abertos e <strong>${te}</strong> execuções no total. Taxa de sucesso geral: <strong>${tx}%</strong>. Deseja mais detalhes?`;
    }

    onMounted(async()=>{
      const s=localStorage.getItem('sos-theme')||'dark';dk.value=s==='dark';
      await load();await nextTick();lucide.createIcons();
    });
    watch(pg2,()=>nextTick(()=>lucide.createIcons()));
    watch(dk,()=>nextTick(()=>lucide.createIcons()));

    return{sc2,loading,pg2,dk,aiop,ain,aityp,gs,cb,upd,modo,msgs,sugs,ec,nav,pgLbl,kpis,recExec,recErrs,cfgD,ef,ep,etot,fExec,pgExec,if2,ip,itot,fItens,pgItens,ist,erf,errp,errtot,fErrs,pgErrs,lf,lp,ltot,fLogs,pgLogs,go,thm,load,send,pns,fmt,fdt,sc,ed};
  }
};
createApp(App).mount('#app');
</script>
</body>
</html>"""

with open('/home/caio/Projetos/analise_specs/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"dashboard.html written: {len(HTML)} bytes")
