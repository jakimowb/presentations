import sys, os, apng, re

root = os.path.dirname(os.path.dirname(__file__))


def createLastFrames():
    dirAPNG = os.path.join(root, r'img/apng')


    for file in os.listdir(dirAPNG):
        if file.endswith('.apng'):
            fullpath = os.path.join(dirAPNG, file)
            bn = os.path.splitext(fullpath)[0]
            img = apng.APNG.open(fullpath)
            frames = list(img.frames)
            pathDst = bn + '.lastframe.png'
            png, control = frames[-1]
            png.save(pathDst)


def createPDFIndexHTML():

    pathSrc = os.path.join(root, 'index.html')
    pathDst = os.path.join(root, 'index.pdf.html')

    with open(pathSrc, 'r', encoding='utf-8') as f:
        html = f.read()

    required = []
    required2 = []
    for path in re.findall(r'"([^"]+\.apng)"', html, re.MULTILINE):
        required.append(path)
        path2 = path.replace('.apng', '.pdf.png')
        required2.append(path2)

    print('Required:')
    for s1, s2 in zip(required, required2):
        html = html.replace(s1, s2)
        print('{} -> {}'.format(s1, s2))
    with open(pathDst, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':

    createPDFIndexHTML()
    print('Finished')