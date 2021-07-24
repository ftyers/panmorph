sentence = `
# sent_id = weblog-blogspot.com_dakbangla_20050210141134_ENG_20050210_141134-0029
# text = One unnamed naval officer was quoted saying, "Arms smuggling is a very profitable business in this region."
1	One	_	_	_	_	_	_	_	_
1.1	One	one	ROOT	_	0	_	_	_	_
2	unnamed	_	_	_	_	_	_	_	_
2.1	un	un	DERIV	_	2	_	_	_	_
2.2	name	name	ROOT	_	0	_	_	_	_
2.3	d	ed	INFL	_	1	_	_	_	_
3	naval	_	_	_	_	_	_	_	_
3.1	naval	naval	ROOT	_	0	_	_	_	_
4	officer	_	_	_	_	_	_	_	_
4.1	officer	officer	ROOT	_	0	_	_	_	_
5	was	_	_	_	_	_	_	_	_
5.1	was	was	ROOT	_	0	_	_	_	_
6	quoted	_	_	_	_	_	_	_	_
6.1	quote	quote	ROOT	_	0	_	_	_	_
6.2	d	ed	INFL	_	1	_	_	_	_
7	saying	_	_	_	_	_	_	_	_
7.1	say	say	ROOT	_	0	_	_	_	_
7.2	ing	ing	INFL	_	1	_	_	_	_
8	,	_	_	_	_	_	_	_	_
8.1	,	,	_	_	_	_	_	_	_
9	"	_	_	_	_	_	_	_	_
9.1	"	"	_	_	_	_	_	_	_
10	Arms	_	_	_	_	_	_	_	_
10.1	Arms	arms	ROOT	_	0	_	_	_	_
11	smuggling	_	_	_	_	_	_	_	_
11.1	smuggl	smuggle	ROOT	_	0	_	_	_	_
11.2	ing	ing	INFL	_	1	_	_	_	_
12	is	_	_	_	_	_	_	_	_
12.1	is	is	ROOT	_	0	_	_	_	_
13	a	_	_	_	_	_	_	_	_
13.1	a	a	ROOT	_	0	_	_	_	_
14	very	_	_	_	_	_	_	_	_
14.1	very	very	ROOT	_	0	_	_	_	_
15	profitable	_	_	_	_	_	_	_	_
15.1	profit	profit	ROOT	_	0	_	_	_	_
15.2	able	able	DERIV	_	1	_	_	_	_
16	business	_	_	_	_	_	_	_	_
16.1	business	business	ROOT	_	0	_	_	_	_
17	in	_	_	_	_	_	_	_	_
17.1	in	in	ROOT	_	0	_	_	_	loc.1=Yes|loc.2=Yes
18	this	_	_	_	_	_	_	_	_
18.1	this	this	ROOT	_	0	_	_	_	_
19	region	_	_	_	_	_	_	_	_
19.1	region	region	ROOT	_	0	_	_	_	_
20	.	_	_	_	_	_	_	_	_
20.1	.	.	_	_	_	_	_	_	_
21	"	_	_	_	_	_	_	_	_
21.1	"	"	_	_	_	_	_	_	_`;

var sentences = sentence.split("\n");
counter = 0;
function addRowToTable(item, index) {
	if (/^\#/.test(item)) {
		console.log(item);
	} else {
		counter+=1;
		console.log(counter);
		console.log(counter%2);
		if (counter%2==0) { style="even"}else{style="odd"};
		row = item.split('\t').join('</td><td>');
		row = "<tr class='"+style+"'><td>"+row+"</td></tr>";
		$("#header").parent().append($(row));
		// console.log(row);
	}
}


$(document).ready( function() {
	sentences.forEach(addRowToTable);
});

