from progress.bar import Bar
import time
bar = Bar('Loading', fill='@', suffix='%(percent)d%%')
for i in Bar('Processing').iter(range(5)):
    time.sleep(1)

