# Annotation guidelines

## Segmentation and splitting

A split should only be made when the result constitutes a valid free unit in the language. For example,


## File format

| ID | Morph | Morpheme | Type | ? | Level | Leipzig | UniMorf | WALS | Features  |
|----|-------|----------|------|---|-------|---------|---------|------|-----------|
| 2.2 | ım | ım | INFL | _ | 1 | POSS.1SG | PSS1S | 59A | _ | 


e.g.

```
1	Kırılacak	_	_	_	_	_	_	_	_
1.1	Kır	kır	ROOT	_	0	_	_	_	_
1.2	ıl	ıl	DERIV	_	1	PASS	PASS	107A	_
1.3	acak	acak	INFL	_	2	FUT	FUT	67A	_
2	kızım	_	_	_	_	_	_	_	_
2.1	kız	kız	ROOT	_	0	_	_	_	_
2.2	ım	ım	INFL	_	1	POSS.1SG	PSS1S	59A	_
3	yavaş	_	_	_	_	_	_	_	_
3.1	yavaş	yavaş	ROOT	_	0	_	_	_	_
4	.	_	_	_	_	_	_	_	_
4.1	.	_	_	_	_	_	_	_	_
```
