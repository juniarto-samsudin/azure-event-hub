import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
 	    # the event hub name.
    #producer = EventHubProducerClient.from_connection_string(conn_str="EVENT HUBS NAMESPACE - CONNECTION STRING", eventhub_name="EVENT HUB NAME")
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://i3eventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=VY9VS8ascXPcbEM6zhk7lXifEwY5u0WRot9nprAwXTI=",
                                                             eventhub_name="iothubevent")

    '''
    json_body = { "measurement":"temperature",
                   "tags":{
                     "tag1":"val1"
                   },
                  "fields":{
                        "value1": 100.0
                  }
                }
    '''
    json_body = {
        "origin": "raspberry4",
        "payload": {
            "temperature": 21.644272300990785,
            "humidity": 78.56935158645383
        }
    }
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData(json_body))
        #event_data_batch.add(EventData('Second event'))
        #event_data_batch.add(EventData('Third event'))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())