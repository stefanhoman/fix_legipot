import json

boardid=14
already=set()

with open('potential_square_relations.json') as f:
	potential_square_relations=json.load(f)
	potential_square_relations_start=set([x['potential_square_id'] for x in potential_square_relations if not x['prev_potential_square_id']])

with open('potential_squares.json') as f:
	psquares=json.load(f)

with open('potential_events.json') as f:
	potential_events=json.load(f)
	potential_events=set([x['id'] for x in potential_events if x['type']=='PotentialEvent::Select'])

def findway(start,done=set(),way=[]):
	#print('start',start)
	for x in potential_square_relations:
		if x['prev_potential_square_id'] == start and x['prev_potential_square_id']:
			if start not in way:
				way.append(start)
			if x['potential_square_id'] in done:	continue
			done.add(start)
			findway(x['potential_square_id'],done,way)
	return way

allids=set([x['id'] for x in psquares if x['potential_board_id']==boardid and x['id'] not in already and x['event_id'] not in potential_events])
startids=sorted(list([x for x in allids if x in potential_square_relations_start]))
#print(allids)
res=[]
for s in startids:
	res+=findway(s)
print(res)