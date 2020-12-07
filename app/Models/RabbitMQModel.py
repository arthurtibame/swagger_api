import pika

class RabbitMQModel(object):
    def __init__(self, host, topic, message, exchange_type="topic", 
            routing_key='anonymous.info', connection_attempts=5, retry_delay=1):
        self._parameters = (    
                        pika.ConnectionParameters(host=host,
                        connection_attempts=connection_attempts, retry_delay=retry_delay)
                        )
        self._connection=pika.BlockingConnection(self._parameters)                        
        self.topic=topic
        self.exchange_type=exchange_type
        self.routing_key=routing_key    
        self.message=message
        self._channel = self._exchange_declare()        
    
    def _exchange_declare(self):
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self.topic, exchange_type=self.exchange_type)
        return self._channel
    
    def basic_publish(self):
        try:
            self._channel.basic_publish(
            exchange=self.topic, routing_key=self.routing_key, body=self.message)
            return True
        except Exception as e:
            print(e)
            return False

    def __del__(self):
        return self._connection.close()