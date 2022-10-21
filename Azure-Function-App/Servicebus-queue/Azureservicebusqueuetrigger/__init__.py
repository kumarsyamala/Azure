import logging
import json
import azure.functions as func


def main(inmsg: func.ServiceBusMessage,outmsg:func.Out[str]):
    logging.info('Python ServiceBus queue trigger processed message.')

    result = json.dumps({
        'message_id': inmsg.message_id,
        'body': inmsg.get_body().decode('utf-8'),
        'content_type': inmsg.content_type,
        'expiration_time': inmsg.expiration_time,
        'label': inmsg.label,
        'partition_key': inmsg.partition_key,
        'reply_to': inmsg.reply_to,
        'reply_to_session_id': inmsg.reply_to_session_id,
        'scheduled_enqueue_time': inmsg.scheduled_enqueue_time,
        'session_id': inmsg.session_id,
        'time_to_live': inmsg.time_to_live,
        'to': inmsg.to,
        'user_properties': inmsg.user_properties,
        'metadata' : inmsg.metadata
    }, default=str)

    logging.info(result)
