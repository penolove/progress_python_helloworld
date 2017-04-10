from progress.bar import Bar
import time
bar = Bar('Processing', max=10)
for i in range(10):
    # Do some work
    time.sleep(1)
    bar.next()
bar.finish()
