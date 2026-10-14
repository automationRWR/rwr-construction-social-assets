import os,shutil,subprocess
from playwright.sync_api import sync_playwright
here=os.path.dirname(os.path.abspath(__file__)); out=os.path.dirname(os.path.dirname(here))+'/labour-day'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto(f'file://{here}/ldr.html');pg.wait_for_function('document.fonts.status==="loaded" && typeof render==="function"');pg.wait_for_timeout(300)
    fr='/tmp/frames_ldr';shutil.rmtree(fr,ignore_errors=True);os.makedirs(fr);n=270
    for f in range(n):
        pg.evaluate('render(%f)'%(f/30));pg.screenshot(path=f'{fr}/f{f:04d}.jpg',type='jpeg',quality=95)
        if f in(40,100,140,269): shutil.copy(f'{fr}/f{f:04d}.jpg',f'/tmp/ldr{f}.jpg')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',fr+'/f%04d.jpg','-c:v','libx264','-pix_fmt','yuv420p','-r','30','-crf','17','-preset','medium','-an','-movflags','+faststart',out+'/RC_LABOUR_DAY_2026_reel.mp4'],check=True)
