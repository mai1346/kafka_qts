import zenoh, time
import numpy as np
import json


def listener(sample):
    np_data = np.frombuffer(sample.payload, dtype=data_dtype)
    print(np_data)
    # print(f'sub_side_shape:{np_data.shape}')
    # print(f"Received {sample.kind} ('{sample.key_expr}': {np_data})")


if __name__ == "__main__":
    data_dtype = np.dtype({'names': ['LocalTimeStamp', 'QuotationFlag', 'Time', 'Symbol', 'SymbolSource',
                                     'PreClosePrice', 'OpenPrice', 'LastPrice', 'HighPrice', 'LowPrice',
                                     'PriceUpLimit', 'PriceDownLimit', 'PriceUpdown1', 'PriceUpdown2', 'TotalNo',
                                     'TotalVolume', 'TotalAmount', 'ClosePrice', 'SecurityPhaseTag', 'PERatio1', 'NAV',
                                     'PERatio2', 'IOPV', 'PremiumRate', 'TotalSellOrderVolume', 'WtAvgSellPrice',
                                     'SellLevelNo', 'SellPrice01', 'SellVolume01', 'TotalSellOrderNo01', 'SellPrice02',
                                     'SellVolume02', 'TotalSellOrderNo02', 'SellPrice03', 'SellVolume03',
                                     'TotalSellOrderNo03', 'SellPrice04', 'SellVolume04', 'TotalSellOrderNo04',
                                     'SellPrice05', 'SellVolume05', 'TotalSellOrderNo05', 'SellPrice06', 'SellVolume06',
                                     'TotalSellOrderNo06', 'SellPrice07', 'SellVolume07', 'TotalSellOrderNo07',
                                     'SellPrice08', 'SellVolume08', 'TotalSellOrderNo08', 'SellPrice09', 'SellVolume09',
                                     'TotalSellOrderNo09', 'SellPrice10', 'SellVolume10', 'TotalSellOrderNo10',
                                     'SellLevelQueueNo01', 'SellLevelQueue', 'TotalBuyOrderVolume', 'WtAvgBuyPrice',
                                     'BuyLevelNo', 'BuyPrice01', 'BuyVolume01', 'TotalBuyOrderNo01', 'BuyPrice02',
                                     'BuyVolume02', 'TotalBuyOrderNo02', 'BuyPrice03', 'BuyVolume03',
                                     'TotalBuyOrderNo03', 'BuyPrice04', 'BuyVolume04', 'TotalBuyOrderNo04',
                                     'BuyPrice05', 'BuyVolume05', 'TotalBuyOrderNo05', 'BuyPrice06', 'BuyVolume06',
                                     'TotalBuyOrderNo06', 'BuyPrice07', 'BuyVolume07', 'TotalBuyOrderNo07',
                                     'BuyPrice08', 'BuyVolume08', 'TotalBuyOrderNo08', 'BuyPrice09', 'BuyVolume09',
                                     'TotalBuyOrderNo09', 'BuyPrice10', 'BuyVolume10', 'TotalBuyOrderNo10',
                                     'BuyLevelQueueNo01', 'BuyLevelQueue', 'WtAvgRate', 'WtAvgRateUpdown',
                                     'PreWtAvgRate'],
                           'formats': ['<i4', 'S4', '<i8', 'S40', 'S5', '<f8', '<f8', '<f8', '<f8', '<f8', '<f8', '<f8',
                                       '<f8', '<f8', '<u8', '<f8', '<f8', '<f8', 'S8', '<f8', '<f8', '<f8', '<f8',
                                       '<f8', '<f8', '<f8', '<u4', '<f8', '<f8', '<u8', '<f8', '<f8', '<u8', '<f8',
                                       '<f8', '<u8', '<f8', '<f8', '<u8', '<f8', '<f8', '<u8', '<f8', '<f8', '<u8',
                                       '<f8', '<f8', '<u8', '<f8', '<f8', '<u8', '<f8', '<f8', '<u8', '<f8', '<f8',
                                       '<u8', '<u4', ('<f8', (50,)), '<f8', '<f8', '<u4', '<f8', '<f8', '<u8', '<f8',
                                       '<f8', '<u8', '<f8', '<f8', '<u8', '<f8', '<f8', '<u8', '<f8', '<f8', '<u8',
                                       '<f8', '<f8', '<u8', '<f8', '<f8', '<u8', '<f8', '<f8', '<u8', '<f8', '<f8',
                                       '<u8', '<f8', '<f8', '<u8', '<u4', ('<f8', (50,)), '<f8', '<f8', '<f8'],
                           'offsets': [0, 4, 8, 16, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168,
                                       176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296,
                                       304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424,
                                       432, 440, 448, 456, 464, 472, 480, 488, 888, 896, 904, 912, 920, 928, 936, 944,
                                       952, 960, 968, 976, 984, 992, 1000, 1008, 1016, 1024, 1032, 1040, 1048, 1056,
                                       1064, 1072, 1080, 1088, 1096, 1104, 1112, 1120, 1128, 1136, 1144, 1152, 1160,
                                       1560, 1568, 1576], 'itemsize': 1584})
    session = zenoh.open()
    sub = session.declare_subscriber('myhome/temp', listener)
    # sub2 = session.declare_subscriber('myhome/temp2', listener)
    # time.sleep(60)
