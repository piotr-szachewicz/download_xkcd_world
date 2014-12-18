import Image
import os, re

files = [] 

mx={ 'e':0, 'w':0, 'n':0, 's':0 }

for file in os.listdir('.'):
    base, extension = os.path.splitext(file)
    if extension != '.png':
        continue
    result = re.match(r'(\d+)([a-z]+)(\d+)([a-z]+)', base)
    if not result:
        continue
    vd, vw, hd, hw = result.groups()
    hd = int(hd)
    vd = int(vd)
    files.append((vd,vw,hd,hw))
#    print base,hd,hw,vd,vw
    mx[hw] = max(mx[hw], hd)
    mx[vw] = max(mx[vw], vd)
print mx 
print files

a = 500 
width = (mx['e']+mx['w'])*a
height = (mx['n']+mx['s'])*a

print 'size %d, %d' % (width, height)
merged_image = Image.new("RGB", (width,height), "white")

print 'XXXXXXXXC'
for file in files:
    print file
    vd, vw, hd, hw  = file
    image = Image.open("%s%s%s%s.png"% (vd,vw, hd, hw))
    image = image.resize((a,a))
    posx = mx['w'] + (-1 if hw=='w' else 1) * (hd - 1*(hw=='w'))
    posy = mx['n'] + (-1 if vw=='n' else 1) * (vd - 1*(vw=='n'))
    merged_image.paste(image, (posx*a,posy*a))

print 'MAX'
print mx
merged_image.save("000_merged.png")
