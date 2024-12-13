HEADERS = {'content-type': 'text/xml;charset=utf-8'}

# HEADERS_SOAP_ACTION = {'SOAPAction': "http://opcfoundation.org/webservices/XMLDA/1.0/Write"}

HEADERS_SOAP = {'content-type': 'application/soap+xml'}

XML_VERSION = '<?xml version="1.0" encoding="UTF-8"?>'

ENVELOPE_OPEN = (
    '<soap:Envelope '
    'xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" '
    'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
    'xmlns:xsd="http://www.w3.org/2001/XMLSchema">'
)
ENVELOPE_HEADER = '<soap:Header></soap:Header>'
ENVELOPE_BODY_OPEN = '<soap:Body>'
# PAYLOAD GOES HERE
ENVELOPE_BODY_CLOSE = '</soap:Body>'
ENVELOPE_CLOSE = '</soap:Envelope>'

READ_XMLNS = '"http://opcfoundation.org/webservices/XMLDA/1.0/"'
READ_OPTIONS = (
    '<Options ' 
    'ReturnItemTime="true" '
    'ReturnItemPath="true" '
    'ClientRequestHandle="" '
    'LocaleID="en-us"/>'
)

WRITE_OPTIONS=(
    '<Options ' 
    'ReturnItemTime="true" '
    'ReturnItemName="true" '
    'ClientRequestHandle="" '
    'LocaleID="en-us" />'
)

class DataType:
    BOOL        = 'boolean'
    BYTE        = 'byte'
    UBYTE       = 'unsignedByte'
    SHORT       = 'short'
    USHORT      = 'unsignedShort'
    INT         = 'int'
    UINT        = 'unsignedInt'
    FLOAT       = 'float'
    DOUBLE      = 'double'
    LONG        = 'long'
    ULONG       = 'unsignedLong'
    DECIMAL     = 'decimal'
    STRING      = 'string'
    DATETIME    = 'dateTime'
