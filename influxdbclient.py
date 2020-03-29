from influxdb import InfluxDBClient

client = InfluxDBClient(host="52.163.90.194", port=8086)
dblist = client.get_list_database()
print(dblist)
client.switch_database("juniarto")
measurement = client.get_list_measurements()
print(measurement)
'''
json_body = {
        "origin": "raspberry4",
        "payload": {
            "temperature": 21.644272300990785,
            "humidity": 78.56935158645383
        }
    }
'''
json_body = [{ "measurement":"temperature",
                   "tags":{
                     "tag1":"val1"
                   },
                  "fields":{
                        "value1": 100.0
                  }
                }]

client.write_points(json_body)


measurement = client.get_list_measurements()