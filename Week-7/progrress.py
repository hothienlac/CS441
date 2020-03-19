from progress.bar import Bar
import time

bar = Bar('Processing', max=200)
for i in range(200):
    # Do some work
    bar.next()
    time.sleep(0.05)
bar.finish()