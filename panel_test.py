import time
import numpy as np
import pandas as pd
import panel as pn
import zenoh

print('这是一个测试语句')
pn.extension('perspective', template='fast', sizing_mode='stretch_width')
df_stream = pd.DataFrame(np.random.randn(400, 4), columns=list('ABCD')).cumsum()

stream_perspective = pn.pane.Perspective(
    df_stream, plugin='d3_y_line', columns=['A', 'B', 'C', 'D'], theme='material',
    sizing_mode='stretch_width', height=500, margin=0
)

rollover = pn.widgets.IntInput(name='Rollover', value=500)

def stream():
    data = df_stream.iloc[-1] + np.random.randn(4)
    stream_perspective.stream(data, rollover.value)

cb = pn.state.add_periodic_callback(stream, 500)


def listener2(sample):
    print(f"Received {sample.kind} ('{sample.key_expr}': '{sample.payload.decode('utf-8')}')")
#
#
session = zenoh.open()
sub = session.declare_subscriber('myhome/temp', listener2)

pn.Column(cb.param.period, rollover,stream_perspective).servable()




