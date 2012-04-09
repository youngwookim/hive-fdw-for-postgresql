from multicorn import ForeignDataWrapper

from hive_service import ThriftHive
from hive_service.ttypes import HiveServerException
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class HiveForeignDataWrapper(ForeignDataWrapper):
    """
    Hive FDW for PostgreSQL
    """
    
    def __init__(self, options, columns):
        super(HiveForeignDataWrapper, self).__init__(options, columns)
        self.columns = columns
        self.host = options.get("host", "localhost")
        self.port = options.get("port", "10000")
        self.table = options.get("table", None)

    def execute(self, quals, columns):
        try:
            transport = TSocket.TSocket(self.host, self.port)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = ThriftHive.Client(protocol)
            transport.open()
            
            SQL = "SELECT " + ",".join(self.columns.keys()) + " FROM " + self.table
            client.execute(SQL)
            
            for row in client.fetchAll():
                line = {}
                cols = row.split("\t");
                idx = 0
                for column_name in self.columns:
                    line[column_name] = cols[idx]
                    idx = idx + 1
                yield line
            
            transport.close()
        
        except Thrift.TException, tx:
            print '%s' % (tx.message)
    
