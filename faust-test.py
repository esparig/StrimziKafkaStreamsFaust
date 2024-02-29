import faust

app = faust.App('myfaustapp', broker='kafka://my-cluster-kafka-bootstrap:9092')

class KafkaLog(faust.Record):
    timestamp: str
    level: str
    message: str

@app.agent(value_type=KafkaLog)
async def process_logs(logs):
    async for log in logs:
        # Extract the number from the log message
        try:
            number = int(log.message.split()[-1])
            print(f"Extracted number: {number}")
        except ValueError:
            # Ignore non-numeric messages
            pass

if __name__ == '__main__':
    app.main()
