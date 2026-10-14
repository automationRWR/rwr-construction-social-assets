import json
# row, slug, label, hl lines, sub lines, graphic, post bg ('w'|'p'), photo or None, accent
ITEMS = [
 (14,'refresh-resume','CANDIDATE TIPS',['Lead with','the headline.'],['Employers read fast.','Make page one count.'],'cv','w',None),
 (15,'referee-prep','CANDIDATE TIPS',['Brief your','referees.'],['A prepared referee','gives a useful answer.'],'refs','p','ph_referee.png'),
 (19,'digital-footprint','CANDIDATE TIPS',['They looked','you up first.'],['Check your digital','footprint before they do.'],'foot','w',None),
 (20,'bench-strength','FOR EMPLOYERS',['Who steps','up next?'],['Build your leadership','bench on purpose.'],'bench','p',None),
 (21,'interview-prep','CANDIDATE TIPS',['Prep wins','the room.'],['Know the business.','Bring the proof.'],'check','w',None),
 (22,'leaders-attract-teams','LEADERSHIP',['People follow','people.'],['Strong leaders','attract strong teams.'],'magnet','w','ph_leader.png'),
 (23,'executive-balance','EXECUTIVE CAREERS',['Delivery shouts.','Strategy waits.'],['Protect time for the','work only you can do.'],'cal','p',None),
 (24,'underperformance','FOR EMPLOYERS',['Act early.','Stay fair.'],['Handle underperformance','without losing good people.'],'rise','w',None),
 (25,'referees-brand','CANDIDATE TIPS',['One story.','Told three ways.'],['You, your referees','and the market.'],'venn','p',None),
 (26,'communication-style','FOR EMPLOYERS',['Say it the way','the role needs.'],['Communication style shapes','a leadership appointment.'],'talk','w','ph_comms.png'),
]
def lines(ls, k=True):
    return '|'.join((ls[0],) + tuple('[k]'+x for x in ls[1:]))
def post(it):
    row,slug,lab,hl,sub,g,bg,ph = it
    art = ''
    if ph:
        acc = '#E6007E' if bg=='w' else '#FFFFFF'
        x = {'ph_referee.png':(540,260),'ph_leader.png':(545,255),'ph_comms.png':(535,265)}[ph]
        art = f'''<img class="ph" src="a/{ph}" style="left:280px;top:10px;width:520px;height:520px">
<div class="ph" style="left:262px;top:30px;width:70px;height:70px;border:8px solid {acc}"></div>
<div class="ph" style="left:700px;top:410px;width:140px;height:140px;background:{acc}"></div>'''
    body = f'''<body class="post {bg}">
<div class="lab">{lab}</div>
<div id="art">{art}</div>
<div class="hl" id="hl">{"".join(f'<span class="ln{" k" if i else ""}">{l}</span>' for i,l in enumerate(hl))}</div>
<div class="sub" id="sub">{"".join(f'<span class="ln">{l}</span>' for l in sub)}</div>
<script src="lib.js"></script><script src="gfx.js"></script>
<script>window.DURATION=1;
function setup(){{ {"" if ph else f"const r=document.getElementById('art');r.innerHTML='<svg viewBox=\"0 0 1080 620\">'+GFX.{g}(PAL.{bg})+'</svg>';"} fit($('#hl'),900,70);fit($('#sub'),900,30); }}
function render(t){{}}
</script></body>'''
    open(f'post_{row}.html','w').write('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="rc.css"></head>'+body+'</html>')
def reel(it):
    row,slug,lab,hl,sub,g,bg,ph = it
    gtick = {'magnet':'magnet','bench':'bench','rise':'rise'}.get(g)
    h = '|'.join((hl[0],)+tuple('[k]'+x for x in hl[1:]))
    s = '|'.join(sub)
    html = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="rc.css"></head><body class="reel">
<section class="sc w" id="s1"><img class="lm" id="lm" src="a/logo_mark.png"><div class="lab" id="lab">{lab}</div><div class="hl" id="h1" data-text="{h}"></div></section>
<section class="sc p" id="s2"><div id="art"></div><div class="sub" id="sb" data-text="{s}"></div></section>
<section class="sc p" id="s3"><img class="lg" id="card" src="a/logo_full_white.png"><div class="cta" id="cta" data-text="Read|the blog."></div><div class="ctas" id="ctas">The full story is a tap away.</div><div class="pill" id="pill">Link in bio</div></section>
<script>window.NO_CIRCLES=true;</script>
<script src="lib.js"></script><script src="gfx.js"></script>
<script>
window.DURATION=11.5;
function setup(){{
  document.getElementById('art').innerHTML='<svg viewBox="0 0 1080 620" style="width:1080px;height:620px;overflow:visible">'+GFX.{g}(PAL.p)+'</svg>';
  fit($('#h1'),900,70); fit($('#sb'),900,30);
}}
function render(t){{
  if(scene($('#s1'),t,0,4.4)){{
    pop($('#lm'),t,.15,{{d:.7}});
    rise($('#lab'),t,.5,{{dy:40,d:.6}});
    words($('#h1'),t,.7,{{st:.12,d:.7}});
  }}
  if(scene($('#s2'),t,3.7,8.6,{{x:540,y:1750,d:.85}})){{
    const root=document.getElementById('art');
    $$('#art .e').forEach((el,i)=>{{const p=P(t,4.2+i*.11,.65),k=E.back(p);el.style.opacity=cl(p*3);el.style.transform='scale('+k+')';}});
    {f"GTICK.{gtick}(root,t-4.2,{{a:.5}});" if gtick else ""}
    words($('#sb'),t,5.7,{{st:.1,d:.65}});
  }}
  if(scene($('#s3'),t,8.1,11.6,{{x:540,y:1750,d:.8}})){{
    pop($('#card'),t,8.6,{{d:.7}});
    words($('#cta'),t,9.0,{{st:.12,d:.7}});
    rise($('#ctas'),t,9.6,{{dy:30,d:.6}});
    pop($('#pill'),t,10.0,{{d:.6}});
  }}
}}
</script></body></html>'''
    open(f'reel_{row}.html','w').write(html)
for it in ITEMS:
    post(it); reel(it)
json.dump([dict(row=i[0],slug=i[1]) for i in ITEMS],open('items.json','w'))
