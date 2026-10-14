import os,sys,shutil,subprocess
from playwright.sync_api import sync_playwright
here=os.path.dirname(os.path.abspath(__file__)); out=os.path.dirname(os.path.dirname(here))+'/labour-day'
def go(pg,m):
    pg.goto(f'file://{here}/ld.html'+('?m=reel' if m else ''));pg.wait_for_function('document.fonts.status==="loaded" && typeof render==="function"');pg.wait_for_timeout(300)
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':1080,'height':1350}); go(pg,0)
    pg.screenshot(path=out+'/RC_LABOUR_DAY_2026_post_logo.jpg',type='jpeg',quality=93)
    if len(sys.argv)>1:
        pg=b.new_page(viewport={'width':1080,'height':1920}); go(pg,1)
        fr='/tmp/frames_ld';shutil.rmtree(fr,ignore_errors=True);os.makedirs(fr)
        n=int(pg.evaluate('window.DURATION')*30)
        for f in range(n):
            pg.evaluate('render(%f)'%(f/30));pg.screenshot(path=f'{fr}/f{f:04d}.jpg',type='jpeg',quality=95)
            if f in(30,120,200,n-1): shutil.copy(f'{fr}/f{f:04d}.jpg',f'/tmp/ldf{f}.jpg')
        subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',fr+'/f%04d.jpg','-c:v','libx264','-pix_fmt','yuv420p','-r','30','-crf','17','-preset','medium','-an','-movflags','+faststart',out+'/RC_LABOUR_DAY_2026_reel.mp4'],check=True)
