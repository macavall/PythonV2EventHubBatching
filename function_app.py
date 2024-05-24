from typing import List
import azure.functions as func
import logging

app = func.FunctionApp()

@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="eventhub56eh2",
                               connection="eventhub56NS_RootManageSharedAccessKey_EVENTHUB", cardinality='many') 
def ehtrigger1(azeventhub: List[func.EventHubEvent]):
    for event in azeventhub:
        logging.info('Python EventHub trigger processed an event:')
        
