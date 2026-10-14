import os, sys, json, shutil, subprocess
from playwright.sync_api import sync_playwright
here=os.path.dirname(os.path.abspath(__file__)); out=os.path.dirname(here)
items=json.load(open(here+'/items.json')); FPS=30
def nm(i,k): return f"RC_BLOG_row{i['row']}_{i['slug']}_{k}"
def posts():
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
        for i in items:
            pg.goto(f"file://{here}/post_{i['row']}.html"); pg.wait_for_function('document.fonts.status==="loaded" && typeof render==="function"'); pg.wait_for_timeout(200)
            pg.screenshot(path=f"{out}/posts/{nm(i,'post')}.jpg",type='jpeg',quality=93)
        b.close()
def reels(sel):
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
        for i in items:
            if i['row'] not in sel: continue
            fr=f"/tmp/frames_{i['row']}"; shutil.rmtree(fr,ignore_errors=True); os.makedirs(fr)
            pg.goto(f"file://{here}/reel_{i['row']}.html"); pg.wait_for_function('document.fonts.status==="loaded" && typeof render==="function"'); pg.wait_for_timeout(300)
            n=int(pg.evaluate('window.DURATION')*FPS)
            for f in range(n):
                pg.evaluate('render(%f)'%(f/FPS)); pg.screenshot(path=f'{fr}/f{f:04d}.jpg',type='jpeg',quality=95)
            subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',fr+'/f%04d.jpg','-c:v','libx264','-pix_fmt','yuv420p','-r','30','-crf','17','-preset','medium','-an','-movflags','+faststart',f"{out}/reels/{nm(i,'reel')}.mp4"],check=True)
            shutil.rmtree(fr); print('done',i['row'],flush=True)
        b.close()
if sys.argv[1]=='posts': posts()
else: reels([int(x) for x in sys.argv[2].split(',')])
