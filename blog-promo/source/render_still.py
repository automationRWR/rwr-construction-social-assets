import sys,os
from playwright.sync_api import sync_playwright
# render_still.py kind row out [t]
kind,row,out=sys.argv[1:4]; t=float(sys.argv[4]) if len(sys.argv)>4 else 99
h=1350 if kind=='post' else 1920
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':h})
    pg.goto('file://'+os.path.abspath(f'{kind}_{row}.html'));pg.wait_for_function('document.fonts.status==="loaded" && typeof render==="function"');pg.wait_for_timeout(300)
    pg.evaluate('render(%f)'%t)
    if out.endswith('.jpg'): pg.screenshot(path=out,type='jpeg',quality=93)
    else: pg.screenshot(path=out)
    b.close()
