def monitor_events():
    event_filter = contract.events.YourEventName.createFilter(fromBlock='latest')
    
    while True:
        for event in event_filter.get_new_entries():
            print(f'New event detected: {event}')
        time.sleep(2)  # Pause between checks

monitor_events()
