import sys, re

for bloc in sys.stdin.read().split('\n\n'):
	if bloc.strip() == '':
		continue
	
	tokens = []
	morphs = {}
	token_id = 0
	for line in bloc.split('\n'):
		if line.strip() == '':
			continue
		if line[0] == '#':
			continue

		row = line.split('\t')
		
		if re.match('^[0-9]+$', row[0]):
			token_id = int(row[0])
			tokens.append(row[1])
			morphs[token_id] = []
			continue

		if re.match('^[0-9]+\.[0-9]+$', row[0]):
			morphs[token_id].append((row[1], row[3]))	

	for token in tokens:
		print(token, end='\t')
	print('')
	for t in morphs:
		
		for i in range(len(morphs[t])):
			print(morphs[t][i][0], end='')
			sep = '-'
			if i < len(morphs[t]) - 1:
				if morphs[t][i+1][1] == 'INFL':
					sep = '|'
				print(sep, end='')	
		print('\t', end='')
	print('')
