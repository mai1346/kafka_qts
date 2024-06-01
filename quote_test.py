# -*- coding: utf-8 -*-
# 简易示例，当OnData回调处理很快，不含打印和写文件等耗时操作，可直接在OnData回调中编写业务逻辑，简捷方便
# 可通过抽样打印的方式确定回调处理是否够快，比如每收到1000条数据打印一次data.size， 正常应该大部分是个位数，
# 如果data.size经常大于100，或有越来越大的趋势，说明回调处理不够快，这时可考虑使用示例二的方法，
# 将数据发送到redis或消息队列中，通过多个进程去消费消息，防止消息堆积

import time
import PyQTSAPI as qts
import numpy as np
import zenoh
import json


stream_data = []


class TestCB(qts.callback2):
    def __init__(self, pool_size=10):
        qts.callback2.__init__(self, pool_size)

    def OnConnectionState(self, msg_type, ret):
        print("OnConnectionState", msg_type, ret)

    def OnLoginState(self, ret):
        print("OnLoginState", ret)

    def OnData(self, msg_type, data):
        print(f'put_side_shape:{data.shape}')
        for d in data:
            print(d)
        # tic = time.time()
        # res_list = [d.tobytes() for d in data]
        # res_array = np.array(res_list)
        # print(res_array[0].dtype)
        pub.put(data.tobytes())
        # rec_dict = dict()
        # for name in data[0].dtype.names:
        #     print(name, data[0][name].dtype)
        #     if isinstance(data[0][name], bytes):
        #         rec_dict[name] = data[0][name].decode('utf-8')
        #     elif data[0][name].dtype in ['int32','int64','uint64','uint32']:
        #         rec_dict[name] = int(data[0][name])
        #     elif isinstance(data[0][name], np.ndarray):
        #         rec_dict[name] = data[0][name].tolist()
        #     else:
        #         rec_dict[name] = data[0][name]
        # data = data[0].tobytes()
        tac = time.time()
        # print(f'{tac - tic:.8f}s')
        # rec_dict = {name: data[0][name] if data[0][name].dtype != 'int32' else int(data[
        #     0][name]) for name in data[0].dtype.names}
        # print({name: data[0][name] for name in data[0].dtype.names})
        # global stream_data
        # stream_data.append(data)
        # print('stream_data length:', len(stream_data))
        # for d in data:
        #     Symbol = str(d['Symbol'], encoding='utf-8')
        #     LocalTimeStamp = d['LocalTimeStamp']


def main():
    cb = TestCB()
    api = qts.api(cb)
    ret = api.RegisterService("183.36.40.4", 8866)
    ret = api.RegisterService("183.36.40.5", 8866)
    ret = api.RegisterService("45.124.127.3", 8888)
    ret = api.RegisterService("45.124.127.2", 8888)
    if ret != qts.RetCode.Ret_Success:
        print(ret)
        return

    ret = api.Login("ydzq", "Vc6bS3Bd")
    if ret != qts.RetCode.Ret_Success:
        print(ret)
        return

    ret = api.Subscribe(qts.MsgType.Msg_SZSEL2_Quotation, '000001,000002,300015')
    if ret != qts.RetCode.Ret_Success:
        print(ret)
        return
    ret = api.Subscribe(qts.MsgType.Msg_SSEL2_Quotation, '601888')
    if ret != qts.RetCode.Ret_Success:
        print(ret)
        return
    # ret = api.Subscribe(qts.MsgType.Msg_SZSEL2_Order, '000001, 300015')
    # if ret != qts.RetCode.Ret_Success:
    #     print(ret)
    #     return

    # 不让主线程退出
    while True:
        time.sleep(1)


if __name__ == "__main__":
    session = zenoh.open()
    key = 'myhome/temp'
    pub = session.declare_publisher(key)
    main()

