def get_event_date(events):
	return event.date

def current_users(events):
	events.sort(key = get_event_date)
	machines = {}
	for event in events:
		if event.machine not in machines:
			machines[event.machine] = set()
		if event.type = "login":
			machines[event.machine].add(event.user)
		else event.type = "logout":
			machines[event.machine].remove(event.user)
	return machines

def generate_report(machines):
	for machine,user in machines.items():
		if len(users) > 0:
			user_list = ",".join(users)
			print("{} : {}").format(manchine,user_list)
