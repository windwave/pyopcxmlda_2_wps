from datetime import datetime
from pyopcxmlda import Client
from pyopcxmlda.tag import Tag
from pyopcxmlda.constants import DataType

__ITEMS = [
    Tag(itemName="//path/to/node/item1", value=-10, type=DataType.INT),
    Tag(itemName="//path/to/node/item2", value=10, type=DataType.UINT),
    Tag(itemName="//path/to/node/item3", value=-10.0, type=DataType.FLOAT),
    Tag(itemName="//path/to/node/item4", value=-1000, type=DataType.LONG)
]

__HOST = '192.168.1.15' # REQUIRED
__PORT = 11111           # OPTIONAL: default is 9500
__NAMESPACE = 'ns0'     # OPTIONAL: default is 'ns0'
__INTERVAL = 0.5

with Client(host=__HOST, port=__PORT, namespace=__NAMESPACE) as plc:
    # test  browse  to specified path
    response = plc.browse(itemName="//path/")
    print(response)

    read_result = plc.read(itemList=__ITEMS)
    
    var1_g = read_result[0]['value']
    var2_p = read_result[2]['value']

    #customer logic add here

    var3_o = var1_g+var1_p
    __O_ITEMS = [
        Tag(itemName="//path/to/node/item1", value=var3_0, type=DataType.INT),
    ]
    response = plc.write(itemList=__O_ITEMS)

    time.sleep(INTERVAL)
