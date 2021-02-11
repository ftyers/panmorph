import sys, re

trees = {}

for bloc in open(sys.argv[1]).read().split('\n\n'):
	if bloc.strip() == '':
		continue
	lines = bloc.split('\n')
	sent_id = lines[0]
	if sent_id not in trees:
		trees[sent_id] = {}
	trees[sent_id]['comments'] = []
	trees[sent_id]['tokens'] = []
	for line in lines:
		if line[0] == '#':	
			trees[sent_id]['comments'].append(line)
		elif re.match('^[0-9]+\.[0-9]+', line):
			continue
		else:
			cols = line.split('\t')
			trees[sent_id]['tokens'].append([int(cols[0])]  + cols[1:])

for bloc in open(sys.argv[2]).read().split('\n\n'):
	if bloc.strip() == '':
		continue
	
	tokens = []
	morphs = {}
	token_id = 0
	lines = bloc.split('\n')
	tree = trees[lines[0]]
	for line in lines:
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
			morphs[token_id].append((row[1], row[3], row[6], row[2]))	


	for i in range(len(tokens)):
		print(tokens[i], end='\t')
	print('')
	for i in range(len(tokens)):
		print(tree['tokens'][i][2], end='\t')
	print('')
	for t in morphs:
		for i in range(len(morphs[t])):
			sep = '-'
			if morphs[t][i][1] == 'ROOT':
				print(morphs[t][i][3], end='')
			elif morphs[t][i][1] == 'DERIV':
				print(morphs[t][i][2], end='')
			else:	
				print(morphs[t][i][2], end='')
			if i < len(morphs[t]) - 1:
				print(sep, end='')	

		print('\t', end='')
	print('')
	for t in morphs:
		for i in range(len(morphs[t])):
			print(morphs[t][i][0], end='')
			sep = '·'
			if i < len(morphs[t]) - 1:
				if morphs[t][i+1][1] == 'INFL':
					sep = '|'
				if morphs[t][i+1][1] == 'DERIV':
					sep = '-'
				if morphs[t][i+1][1] == 'ROOT':
					if morphs[t][i][1] == 'DERIV':
						sep = '-'
					elif morphs[t][i][1] == 'INFL':
						sep = '|'
				print(sep, end='')	
		print('\t', end='')
	print('')
	print('')
