import sys

def vectorise(feats, col):
	fv = {}
	ov = [0 for i in feats]

	if col == '_':
		return ov
	
	for i in col.split('|'):
		if '=' not in i:
			continue
		(feat, val) = i.split('=')
		if feat not in feats:
			print('ERROR:',feat, 'not in', feats, file=sys.stderr)
			sys.exit(-1)
		fv[feat] = val

	idx = 0
	for feat in feats:
		if feat in fv and fv[feat] == 'Yes':
			ov[idx] = 1
		if feat in fv and fv[feat] == 'No':
			ov[idx] = -1
		idx += 1

	return ov

features = []

for line in open(sys.argv[1]).readlines():
	row = line.split('\t')
	features.append(row[0])


features = list(set(features))
features.sort()


for line in sys.stdin.readlines():
	line = line.strip()
	if line == '':
		print()
		continue
	if line[0] == '#':
		continue
	row = line.split('\t')
	if row[0].count('.') != 1:
		continue
	print('%s\t%s\t%s' % (row[1], row[2], ','.join([str(i) for i in vectorise(features, row[9])])))
