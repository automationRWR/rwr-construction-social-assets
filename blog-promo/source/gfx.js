const PAL = {
  w: { C: '#E6007E', S: '#FCE3F1', L: '#E5E5EA', B: '#FFFFFF', D: '#F5F5F7', A: '#E6007E', LN: '#E5E5EA' },
  p: { C: '#FFFFFF', S: '#F066AB', L: '#F066AB', B: '#E6007E', D: '#FFFFFF', A: '#E6007E', LN: '#FBCFE6' }
};
const person = (cx, cy, s, f) => `<circle cx="${cx}" cy="${cy - .26 * s}" r="${.27 * s}" fill="${f}"/><path d="M${cx - .5 * s} ${cy + .56 * s} A${.5 * s} ${.5 * s} 0 0 1 ${cx + .5 * s} ${cy + .56 * s}Z" fill="${f}"/>`;
const GFX = {};
GFX.cv = P => `
<rect class="e" x="330" y="20" width="420" height="580" rx="32" fill="${P.D}"/>
<g class="e"><circle cx="410" cy="110" r="36" fill="${P.A}"/><rect x="465" y="88" width="200" height="20" rx="10" fill="${P.A}"/><rect x="465" y="122" width="130" height="14" rx="7" fill="${P.LN}"/></g>
<rect class="e" x="314" y="4" width="452" height="220" rx="42" fill="none" stroke="${P.C}" stroke-width="8"/>
${[260, 320, 380, 440, 500, 555].map((y, i) => `<rect class="e" x="370" y="${y}" width="${i % 3 == 2 ? 220 : 340}" height="16" rx="8" fill="${P.LN}"/>`).join('')}`;
GFX.refs = P => `
<rect class="e" x="240" y="296" width="600" height="12" rx="6" fill="${P.L}"/>
<g class="e"><circle cx="240" cy="302" r="100" fill="${P.S}"/>${person(240, 302, 110, P.C)}<circle cx="305" cy="232" r="34" fill="${P.C}"/><path d="M291 232 l11 11 l20 -22" fill="none" stroke="${P.B}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>
<g class="e"><circle cx="840" cy="302" r="100" fill="${P.S}"/>${person(840, 302, 110, P.C)}<circle cx="905" cy="232" r="34" fill="${P.C}"/><path d="M891 232 l11 11 l20 -22" fill="none" stroke="${P.B}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>
<g class="e"><circle cx="540" cy="302" r="150" fill="${P.C}"/>${person(540, 302, 170, P.B)}</g>`;
GFX.foot = P => `
<g class="e"><circle cx="470" cy="270" r="190" fill="${P.S}"/>${person(470, 270, 190, P.C)}</g>
<circle class="e" cx="470" cy="270" r="190" fill="none" stroke="${P.C}" stroke-width="40"/>
<line class="e" x1="600" y1="400" x2="770" y2="565" stroke="${P.C}" stroke-width="64" stroke-linecap="round"/>
<circle class="e" cx="900" cy="90" r="44" fill="${P.S}"/>
<circle class="e" cx="190" cy="560" r="26" fill="none" stroke="${P.C}" stroke-width="8"/>`;
GFX.bench = P => { let s = ''; for (let i = 0; i < 4; i++) { const h = 150 + i * 100, x = 150 + i * 210, y = 590 - h;
  s += `<rect class="e" x="${x}" y="${y}" width="170" height="${h}" rx="28" fill="${i == 3 ? P.C : P.S}"/>`;
  s += i == 2 ? `<circle class="e ring" cx="${x + 85}" cy="${y - 62}" r="42" fill="none" stroke="${P.C}" stroke-width="12"/>` : `<circle class="e" cx="${x + 85}" cy="${y - 62}" r="42" fill="${P.C}"/>`; } return s; };
GFX.check = P => `
<rect class="e" x="250" y="20" width="580" height="580" rx="40" fill="${P.D}"/>
${[0, 1, 2].map(i => `<g class="e"><circle cx="340" cy="${130 + i * 160}" r="40" fill="${P.A}"/><path d="M322 ${130 + i * 160} l14 14 l26 -28" fill="none" stroke="${P.D}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><rect x="410" y="${112 + i * 160}" width="${[330, 290, 240][i]}" height="22" rx="11" fill="${P.A}"/><rect x="410" y="${150 + i * 160}" width="${[220, 260, 180][i]}" height="14" rx="7" fill="${P.LN}"/></g>`).join('')}`;
GFX.magnet = P => `
<circle class="e" cx="540" cy="310" r="240" fill="none" stroke="${P.L}" stroke-width="8"/>
<circle class="e" cx="540" cy="310" r="130" fill="${P.C}"/>
<g class="e"><g id="orb">${[0, 1, 2, 3, 4].map(i => { const a = i * 72 * Math.PI / 180; return `<circle cx="${540 + 240 * Math.cos(a)}" cy="${310 + 240 * Math.sin(a)}" r="${i % 2 ? 34 : 48}" fill="${i % 2 ? P.S : P.C}"/>`; }).join('')}</g></g>`;
GFX.cal = P => { let s = ''; const d = ['M', 'T', 'W', 'T', 'F'];
  for (let i = 0; i < 5; i++) { const x = 130 + i * 165;
    s += `<rect class="e" x="${x}" y="10" width="135" height="520" rx="34" fill="${P.S}"/>`;
    s += `<g class="e">${[0, 1, 2, 3].map(r => `<rect x="${x + 20}" y="${40 + r * 120}" width="95" height="${i == 1 && r == 2 ? 100 : 90}" rx="22" fill="${i == 1 && r == 2 ? P.C : P.B}"/>`).join('')}</g>`;
    s += `<text x="${x + 67}" y="590" text-anchor="middle" font-family="Poppins" font-weight="500" font-size="32" fill="${P.C}">${d[i]}</text>`; }
  return s; };
GFX.rise = P => `
<rect class="e" x="120" y="570" width="840" height="10" rx="5" fill="${P.L}"/>
<polyline id="rp" pathLength="1" points="150,490 400,390 650,290 900,110" fill="none" stroke="${P.C}" stroke-width="18" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1" stroke-dashoffset="0"/>
${[[150, 490], [400, 390], [650, 290]].map(p => `<circle class="e" cx="${p[0]}" cy="${p[1]}" r="30" fill="${P.C}"/>`).join('')}
<g class="e"><circle cx="900" cy="110" r="62" fill="${P.C}"/><circle cx="900" cy="110" r="98" fill="none" stroke="${P.S}" stroke-width="10"/></g>`;
GFX.venn = P => { const t = (x, y, s) => `<text x="${x}" y="${y}" text-anchor="middle" font-family="Poppins" font-weight="500" font-size="34" letter-spacing="3" fill="${P.C}">${s}</text>`;
  return `
<g class="e"><circle cx="370" cy="235" r="200" fill="none" stroke="${P.C}" stroke-width="12"/>${t(285, 225, 'YOU')}</g>
<g class="e"><circle cx="710" cy="235" r="200" fill="none" stroke="${P.C}" stroke-width="12"/>${t(800, 225, 'REFEREES')}</g>
<g class="e"><circle cx="540" cy="405" r="200" fill="none" stroke="${P.C}" stroke-width="12"/>${t(540, 520, 'MARKET')}</g>
<circle class="e" cx="540" cy="305" r="28" fill="${P.C}"/>`; };
GFX.talk = P => `
<g class="e"><rect x="110" y="30" width="520" height="270" rx="70" fill="${P.C}"/><path d="M190 290 L170 385 L285 295Z" fill="${P.C}"/>
<rect x="180" y="100" width="380" height="24" rx="12" fill="${P.B}"/><rect x="180" y="150" width="300" height="24" rx="12" fill="${P.B}"/><rect x="180" y="200" width="220" height="24" rx="12" fill="${P.B}"/></g>
<g class="e"><rect x="450" y="310" width="520" height="260" rx="70" fill="${P.S}"/><path d="M860 560 L890 615 L775 565Z" fill="${P.S}"/>
<rect x="520" y="380" width="380" height="24" rx="12" fill="${P.C}"/><rect x="520" y="430" width="300" height="24" rx="12" fill="${P.C}"/><rect x="520" y="480" width="220" height="24" rx="12" fill="${P.C}"/></g>`;
const GTICK = {
  magnet: (r, t) => { const o = r.querySelector('#orb'); if (o) o.setAttribute('transform', `rotate(${t * 24} 540 310)`); },
  bench: (r, t) => { const g = r.querySelector('.ring'); if (g) g.style.opacity = .55 + .45 * Math.abs(Math.sin(t * 2.2)); },
  rise: (r, t, d) => { const p = r.querySelector('#rp'); if (p) p.setAttribute('stroke-dashoffset', 1 - E.o3(P(t, d.a, 1.5))); }
};
function fit(el, maxW, min) { let fs = parseFloat(getComputedStyle(el).fontSize); while (el.offsetWidth > maxW && fs > min) { fs -= 2; el.style.fontSize = fs + 'px'; } }
