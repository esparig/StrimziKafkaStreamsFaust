import faust

#class KafkaLog(faust.Record):
#    timestamp: str
#    level: str
#    message: str

#class ClientExample(faust.Record):
#    log: str

#class ClientExample(faust.Record, serializer='raw'):
#    pass

app = faust.App('myfaustapp', broker='kafka://my-cluster-kafka-bootstrap:9092')
topic = app.topic('my-topic', value_type=bytes)

@app.agent(topic)
async def process_logs(logs):
    async for log in logs:
        print(f"Received message: {log.decode('utf-8')}")
        # Extract the number from the log message
        try:
            number = int(log.decode('utf-8').split()[-1])
            print(f"Extracted number: {number}")
        except ValueError:
            # Ignore non-numeric messages
            pass

if __name__ == '__main__':
    app.main()

