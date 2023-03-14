import os

class BatchRename():

    def __init__(self):
        self.path = '/path/to/depth'

    def rename(self):
        filelist = os.listdir(self.path)
        filelist.sort()
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.png'):
                src = os.path.join(os.path.abspath(self.path), item)
                s = str(i)
                s = s.zfill(10)
                dst = os.path.join(os.path.abspath(self.path), s +'.png')

                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
