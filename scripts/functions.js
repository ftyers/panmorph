counter=0;
function addRowToTable(item, index) {

  if (/^\#/.test(item)) {
		console.log(item);
	}
  else {
		counter+=1;
		if (counter%2==0) { style="even"}else{style="odd"};
    row = item.split('\t');
    for (var i = 0; i < row.length; i++){
      if (row[i] == "_"){
        row[i] = "";
      }
    }
		row = row.join('</td><td contenteditable="true">');
		row = "<tr class='"+style+"'><td contenteditable='true'>"+row+"</td></tr>";
		$('#editor').append($(row));
	}
}


function convertFormat(){
  $('#editor').show();
  let conText = document.getElementById("conllu").value;
  let texts = conText.replace(/\n+$/, "");
  let separateText = texts.split("\n\n");
  let morllu = "";

  for (var i = 0; i < separateText.length; i++) {
    var lines = separateText[i].split("\n");

    for (var k = 0; k < lines.length; k++) {
      var line = lines[k];
      if (line.charAt(0) == "#") {
        morllu += line;
      }
      else if (line.charAt(0).includes(".")) {
        continue;
      }
      else{
        var strings = line.split("\t");
        var token = strings[0] + "\t" + strings[1] + "\t" + ("_" + "\t").repeat(7) + "_";
        morllu += token;
      }
      morllu += "\n";
    }
    morllu += "\n";
  }
  document.getElementById("morllu").innerHTML = morllu;
  morllu = morllu.replace(/\n*$/, "")
  let sentences = morllu.split("\n");
  $('#editor tr:not(:first)').empty();
  sentences.forEach(addRowToTable);

  addFeature();

}

var featuresList =
`loc.1   Indicates location in space?
loc.2   Indicates location in time?
loc.3   Indicates static location?
movement.1    Indicates movement?
away.1    Indicates movement away from somewhere?
towards.1   Indicates movement towards somewhere?
plur.1    Indicates plural quantity?
plur.2    Indicates plural agreement with the subject?
plur.3    Indicates plural agreement with the object?
purp.1    Indicates purposive movement, e.g. going in order to?
realis.1    Indicates a realis mood?
hab.1   Indicates habitual aspect?
agree.1   Is an agreement marker?
prog.1    Indicates progressive aspect?
past.1		Indicates an action in the past?
pres.1		Indicates an action taking place in the present?
npast.1		Indicates an action taking place in the present or future?
def.1		Is the referent specific in the current context?
ind.1		Is the referent non-specific in the current context?
comp.1		Indicates a comparand?
subord.1    Indicates subordination?
manner.1    Indicates manner?
poss.1    Marks possessor?
poss.2    Marks possessed?
cmpnd.1   Indicates compound?
nfh.1   Indicates non-first hand?
pass.1    Promotes direct object to subject?
cmpnd.2   Indicates an adjective compound?
adj.1   Forms attributive adjectives?
type.1    Indicates the relationship between different specimens of the same type
sepr.1		Indicates separation?
source.1  Indicates source?
cause.1		Indicates cause?
route.1		Indicates route?
modif.1		Indicates modifier in a noun phrase?
obliq.1   Marks the oblique object?
compl.1 	Marks the complement of a post-position?
compl.2   Marks the complement of an adjective?
causee.1    Marks the causee of the action in a causative construction?
ben.1   Marks the recipient or beneficiary of an action?
price.1   Indicates the price?
gen.1   Indicates a generic/categorical object?
part.1    Marks the head in partitive constructions?
part.2    Marks the entity or the set in partitive constructions?
nominal.1   Marks a subject complement and indicates nominal predication?
subj.1    Marks the subject of non-finite subordinate clause?
pron.1    Indicates pronominals?
agree.2   Agrees in person?
pers.1    Refers to 1st person?
pers.2    Refers to 2st person?
pers.3    Refers to 3st person?
com.1   Has comitative meaning?
inst.1    Has instrumental meaning?
conj.1    Has conjunctive meaning?
voice.1   Incicates causative?
voice.3   Incicates reflexive?
voice.4   Incicates reciprocal?
neg.1   Indicates negation?
ass.1   Indicates assumption?
oblig.1   Indicates obligation?
perm.1    Indicates permission?
pot.1   Indicates potential modality?
pros.1    Indicates prospective aspect?
imprf.1   Indicates imperfective aspect?
prf.1   Indicates perfective aspect?
cfact.1   Indicates counter-factual?
subj.1    Indicates subjectivity?
abil.1    Indicates ability?
posib.1   Indicates possibility?
spec.1    Indicates speculation?
imp.1   Indicates imperative mood?
cfact.1   Indicates counterfactual?
genrl.1   Indicates generalized modality?
form.1    Expresses formality?
hyp.1   Indicates hypothetical?
fut.1   Expresses future?
nonf.1    Indicates non-fact modality?
ded.1   Indicates deduction?
cont.1    Expresses continuity?
sudd.1    Expresses suddenness?
persu.1   Expresses persuasion?
fin.1   IndiŞimdi düşünüyorum da, galiba o parkın dışında yapamayacağım ben, dedi Kerem.cates finite verb form?
fin.2   Indicates non-finite verb form?
nom.1   Indicates nominatization?`;


var featureDesc = featuresList.split('\n');
var featureName = [];
var descQuestion = [];

for (const feature of featureDesc){
  var nameAndDesc = feature.split(/\s\s+/g)
  featureName.push(nameAndDesc[0])
  descQuestion.push(nameAndDesc[0] + ": " + nameAndDesc[1])
}

function addFeature(){
  $('table td:nth-child(10)').click(function(){
    $(this).replaceWith("<td><select id='selectFeature'>\
      <option selected></option>\
      </select></td>");
    for (var i = 0; i < featureDesc.length; i++){
      $('select#selectFeature').append("\
        <optgroup label='"+descQuestion[i]+"'>\
          <option>"+featureName[i]+"=Yes</option>\
          <option>"+featureName[i]+"=No</option>\
        </optgroup>")
    }
  });
}


$(document).ready( function() {

  $('#editor').hide();

  document.querySelector('button#convert').addEventListener('click', convertFormat);

  $('button#generateInterface').click(function(){
    $('#editor').show();
    let morSen = document.getElementById('morllu').value;
    morSen = morSen.replace(/\n*$/, "");
    let morSentences = morSen.split("\n");
    $('#editor tr:not(:first)').empty();
    morSentences.forEach(addRowToTable);

    addFeature();
  });

})
