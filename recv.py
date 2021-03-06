import asyncio
from azure.eventhub.aio import EventHubConsumerClient
#from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore


async def on_event(partition_context, event):
    # Print the event data.
    print("Received the event: \"{}\" from the partition with ID: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id))
    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    #checkpoint_store = BlobCheckpointStore.from_connection_string("AZURE STORAGE CONNECTION STRING", "BLOB CONTAINER NAME")

    # Create a consumer client for the event hub.
    #client = EventHubConsumerClient.from_connection_string("EVENT HUBS NAMESPACE CONNECTION STRING", consumer_group="$Default", eventhub_name="EVENT HUB NAME", checkpoint_store=checkpoint_store)
    client = EventHubConsumerClient.from_connection_string("Endpoint=sb://i3eventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=VY9VS8ascXPcbEM6zhk7lXifEwY5u0WRot9nprAwXTI=",consumer_group="$Default", eventhub_name="iothubevent")
    async with client:
        # Call the receive method.
        await client.receive(on_event=on_event)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(main())