# -*- coding: utf-8 -*-

# The morphemes are added from the book TURKISH: A COMPREHENSIVE GRAMMAR by Göksel and Kerslake (2005)

# In this dictionary data structure type, we keeps the variants of the same morpheme in order to automatize the writing
# into the MORPHEME column.

# Keys are the common for for all the variants of a suffix.
# Values holds the variants of the key suffix as a list as well as the its label in Leibzig and Unimorph format and
# the corresponding morrlu features

# The morllu features are not fully covered yet but they will be added based on the examples created.

nominal_inflectional_sufffixes = {
    # Nominal inflectional suffixes
    # 3pl or just pl considering subject-verb agreement?
    # 'gidiyorlar', 'evler'
    'lar' : (['lar', 'ler'], 'PL','PL',
             'pul.1=|pul.2=|agree.1='),     # plural marking
    # pul=yes|agree.1=no   e.g. 'kitap-lar-ı' as his/her books
    # pul=yes|agree.1=no   e.g. 'kitap-ları' as their book(s)
    'ları': (['ları', 'leri', 'ların', 'lerin'], 'POSS.3PL', 'POSS3PL',
             'pul.1=|agree.1=|pers.3='),  # plural marking

    # Sould we add 'agree.1' feature?
    'm' : (['m'], 'POSS.1SG|GEN', 'PSS1S|GEN',
           'poss.1=|poss.2=|agree.1'),  # 1st person singular possessive suffix
    'ım': (['im', 'um', 'ım', 'üm'], 'POSS.1SG|GEN.1SG', 'PSS1S|GEN1S',
           'poss.1=|poss.2=|agree.1|pers.1'),  # genitive marker, 1st persn

    # 2st person singular possessive suffix
    'n' : (['n'], 'POSS.2SG', 'PSS2S',
           'poss.1=no|poss.2=yes|agree.1=yes|pers.2=yes'),  # 2st person singular possessive suffix # 'ın', 'in', 'un', 'ün',
    # 'kitab-in-i' as her/his book  (agree.1 + pers.2=|pers.3= -in)
    # 'kitab-in-i' as your book     (agree.1 + pers.2=|pers.3= -in)
    # 'onlar-in kitab-in-i' as your book     (agree.1 + pers.2=|pers.3= -in)
    'ın': (['in', 'un', 'ın', 'ün'], 'POSS.2SG|POSS.3SG|GEN', 'PSS2S|PSS3S|GEN',
           'poss.1=|poss.2=|agree.1=|agree=2|pers.2=|pers.3=|cmpnd.1|part.2|pron.1='),
    # 'onlarin ev-leri'     their home  (pul.1= + agree.1= + pers.3=)
    # 'onlarin ev-ler-i'    their homes (agree.1 + agree.2 for -i)
    # 'onlarin ev-i'        their home  (only agrees in person? -> agree.1 + agree.2 for -i)
    #  what about impersonals?  -> 'okuma-si zor' 'it is hard to read'
    'sı': (['sı','si', 'sın', 'sin', 'su','sü', 'sun', 'sün'], 'POSS.3', 'PSS3',
           'poss.2=|agree.1|agree.2=|pers.3=|cmpnd.1|part.2|pron.1='),  # 3rd person possessive suffix
    'ı': (['ı', 'i', 'u', 'ü'], 'POSS.3|ACC', 'PSS3|ACC',
          'poss.2=|agree.1|agree.2=|pers.3=|cmpnd.1|part.2|def.1=|ind.1=|cat.1=|'),  # 3rd person possessive suffix

    # Should we separate m-iz and n-iz (or does it complicate too much? or would it be necessary?)
    # marking '-m' as only POSS.1 and '-iz' as 'PL' and 'pul.1=yes'
    'mız': (['mız', 'miz', 'müz', 'muz', 'ımız', 'imiz', 'ümüz', 'umuz'], 'POSS.1PL', 'PSS1PL',
            'pul.1=yes|poss.2=|agree.1'),  # 1st person plural possessive suffix
    'nız': (['nız', 'niz', 'nüz', 'nuz', 'ınız', 'iniz', 'ünüz', 'unuz'], 'POSS.2PL', 'PSS2PL',
            'pul.1=yes|poss.2=|agree.1'),  # 2st person plural possessive suffix

    'yı' : (['yı','yi', 'yu', 'yü'], 'ACC', 'ACC', '-'),  # accusative case
    'a' : (['a','e', 'ya','ye'], 'DAT', 'DAT', 'movement.1=|towards.1=|oblique.1='),        # dative case
    'da': (['da', 'de', 'ta', 'te'], 'LOC', ['AT', 'IN', 'ON'], 'loc.1=|loc.2=|loc.3='),    # locative case
    'dan': (['dan', 'den', 'tan', 'ten'], 'ABL', 'ABL', 'away.1='),    # ablative case
    'nın': ([ 'nın', 'nin', 'nun', 'nün'], 'GEN', 'GEN', 'poss.1=|poss.2='),  # genitive case   # 'ın', 'in', 'un', 'ün'

    'la': (['la', 'le', 'yla', 'yle'], 'INS', 'INS', 'com.1|inst.1|conj.1'),  # instrumental/comitative marker

}

verbal_inflectional_sufffixes = {
    # Verbal inflectional suffixes
    'dır': (['dır', 'dir', 'dür', 'dur', 'tur', 'tür', 'tır', 'tir'], 'CAUS', 'CAUS', ''),  # causative marker1
    't': (['t'], 'CAUS', 'CAUS'), # causative marker2
    'ıt': (['ıt', 'it', 'üt', 'ut'], 'CAUS', 'CAUS'), # causative marker3
    'ır': (['ır', 'ir', 'ür', 'ur'], 'CAUS', 'CAUS'),  # causative marker4
    'ar': (['ar', 'er'], 'CAUS', 'CAUS'),  # causative marker5
    'art': (['art', 'ert'], 'CAUS', 'CAUS'),  # causative marker6

    'n': (['n'], 'PASS', 'PASS'), # passive marker1
    'ın': (['in', 'ın', 'ün', 'un'], 'PASS', 'PASS'), # passive marker2
    'ıl': (['ıl', 'il', 'ul', 'ül'], 'PASS', 'PASS'),  # passive marker3

    'in': (['in', 'n', 'ın', 'ün', 'un'], 'REFL', 'REFL'),  # reflexive marker

    'ış': (['ış', 'ş', 'iş', 'üş', 'uş'], 'RECP', 'RECP'),  # reciprocal marker

    'ma': (['ma', 'me'], 'NEG', 'NEG'),  # negation marker
    'mı': (['mı', 'mi', 'mu', 'mü'], 'NEG', 'NEG'),  # negation marker
}

TMA = {
    # TMA suffixes

    # compound verb forms
    # particle + verb
    # ???
    'ıver': (['ıver', 'üver', 'iver', 'uver'], 'ROOT', 'ROOT', ''),  # 'stiffness and suddenness'
    'agel': (['agel', 'egel', 'yagel', 'yegel'], 'ROOT', 'ROOT'),  # 'habitual and customary' also (semi)-lexicalized
    'adur': (['adur', 'edur', 'yadur', 'yedur'], 'ROOT', 'ROOT'),  # 'continuous nature of action' also semi-lexicalized
    'ayaz': (['ayaz', 'eyaz', 'yayaz', 'yeyaz'], 'ROOT', 'ROOT'),  # 'almost', could be modality??
    'akal': (['akal', 'ekal'], 'ROOT', 'ROOT'),  # 'continuous nature of action' also semi-lexicalized


    # Non-fact, only with ol- verb
    # 'Kapı çaldı, Hasan ol-acak.'
    # 'The door bell rang; that’ll be Hasan.’'
    # !! PROSP instead of future, for sentences like 'Eve gidecekti.'pg 287 (relative tense)
    # Geçen/Önümüzdeki yıl yeni bir öğretmen-imiz ol-acak-tı.
    # !! ASSUM only for ol-acak as in 'cantada olacaklar' like 'olsa gerek', non-future predictions non-fact modality (assumption)
    # !! For the occurrence of this usage of olacak in compound verb forms, see 21.5.1.
    # commands
    'acak': (['acak', 'ecek', 'yacak', 'yecek', 'acağ', 'eceğ', 'yacağ', 'yeceğ'], 'FUT', 'FUT|PROSP|ASSUM|IMPR'),       # relative tense ?|SBJV|LKLY

    'malı': (['malı', 'meli'], '', 'OBLIG|DED'),

    # page 300
    'ya': (['ya', 'ye', 'a', 'e'], 'OPT', 'OPT|SUBJ|IRR|LKLY?|ASSUM?|PERM'),

    'abil': (['abil', 'ebil', 'yabil', 'yebil'], '', 'SUBJ|IRR|POT|PERM'),  # possibility marker




    # TMA
    # The forms -mIştI and -DIydI (21.2.1) combine elements of perfectivity and imperfectivity
    'dı': (['dı', 'di', 'dü', 'du', 'tı', 'ti', 'tu', 'tü'], 'PAST|PERF|DRCT||IMPF', 'PAST|PERF|DRCT||IMPF|SUBJV|IND'), # '||' separates features of (y)DI past copula
    # It should be noted that the -mIş component of -mIştIr has no (evidential) modality value
    # of its own; it is purely past/perfective
    'mış': (['mış', 'miş', 'müş', 'muş'], 'PAST|PERF|NFH|DRCT?|INFER', 'PAST|PERF|NFH|DRCT?|INFER'),

    # NHF is "neutrilized" when followed by -(y)DI
    # O hafta çok yağmur yağ-mış-tı.
    # ‘It had rained a lot that week.’
    'ymış': (['ymış', 'ymiş', 'ymüş', 'ymuş'], 'NFH', 'NFH'),  # purely marker of idential modality

    # past copula
    'ydı': (['ydı', 'ydi', 'ydu', 'ydü'], 'PAST|IMPF', 'PAST|IMPF|SUBJV|IRR|IND'),   # not necessarily past e.g. counterfactual events
    # 'Gid-iyor-du-m'   [PAST]
    # 'Evde-ydi-k'      [PAST, IMPF]
    # 'Güzel ol-ur-du.' [PAST?, SUBJ]   (counterfactual)
    # "Haftaya eve gid-iyor-du." [IND]
    # 'Daha uygun bir saat seçebilirdiniz' (counterfactual)

    # Scheduled future
    # Yarın Paris’e gid-iyor-uz.
    # ‘We’re going to Paris tomorrow.’
    # Turkish does not mark present tense.  However, the absance of -(y)DI makes the difference for tense
    'ıyor': (['ıyor', 'iyor', 'yor', 'uyor', 'üyor'], 'PRS|IPFV|PROG|HAB|FUT|IND', 'PRS|IPFV|PROG|HAB|FUT|IND'), # relative tense    'SUBJ' for generalization based on speaker's own experiences
    'makta': (['makta', 'mekte'], 'IPFV|PROG|HAB|IND', 'IPFV|PROG|HAB|IND'),  # relative tense

    # Aspect: PG 290

    # Modality: PG 294
    'er': (['ar', 'er'], '', 'IPFV|INFER|HAB|SBJV?|IRR?|FUT?|ASSUM'),      # 'INFER' for generalizations, 'IRR' and 'SBJV' for hypothetical, counterfactual or assumptions
    'ır': (['ır', 'ir', 'ur', 'ür'], '', 'IPFV|INFER|HAB|SBJV?|IRR?|FUT?|ASSUM'), # 'INFER' for generalizations, 'IRR' and 'SBJV' for hypothetical, counterfactual or assumptions
    'z': (['z'], '', 'IPFV|INFER|HAB|SBJV|IRR?|LKLY?|FUT?|ASSUM'), # 'INFER' for generalizations, 'IRR' and 'SBJV' for hypothetical, counterfactual or assumptions

    # 'FUT' : Oradan iki saatte gel-ir-siniz
    'dir': (['dir', 'dır', 'dür', 'dur', 'tur', 'tür', 'tır', 'tir'], '', 'INFER|ASSUM'), # 'INFER' for generalizations (nominal sentences and formal verbal sentences)
    # assumtions 'umarim hasta degilimdir.'  evidentility
    # modality marker, generalized modality

    # COUNTERFACTUAL with -(y)DI
    # Wishes expressed by -sAydI/(-(y)AydI can have a reproachful, quasiobligative tone
    # [Madem uykun vardı], misafir çağırmasaydın/çağırmayaydın 'you would have done better not to invite guests'
    'ysa': (['ysa', 'yse', 'sa', 'se'], 'COND', 'COND|OPT|OBLIG?'),

    'sa': (['sa', 'se'], 'OPT', 'OPT'),

    # person marker
    # Group 1
    'm': (['m'], '1SG', '1S'),
    'n': (['n'], '2SG', '2S'),  # informal
    'niz': (['nız', 'niz', 'nuz', 'nüz'], '2SG|2PL', '2S|2P|FORM'),  # formal (2sg)
    'k': (['k'], '1PL', '1PL'),

    # Group 2
    'ım': (['ım', 'im', 'um', 'üm', 'yım', 'yim', 'yum', 'yüm'], '1SG', '1S'),
    'sın': (['sın', 'sin', 'sun', 'sün'], '2SG|3|3SG', '2S|3|3SG'), # group 3 -> imperative/optative reading (3/3SG)

    # or separate this and add FORM to the inflected verb
    'sınız': (['sınız', 'siniz', 'sunuz', 'sünüz'], '2PL|2SG', '2PL|2SG|FORM'),  # formal (2sg)
    'ız': (['ız', 'iz', 'uz', 'üz', 'yız','yiz', 'yuz', 'yüz'], '1PL', '1P'),

    # Group 3 (after opt -A)
    'yım': (['yım', 'yim'], '1SG', '1S'),
    'lım': (['lım', 'lim'], '1PL', '1P'),

    # Group 4
    'sana': (['sana', 'sene'], '2SG|OPT', '2S|OPT'),
    'ın': (['ın', 'in', 'un', 'ün', 'yın', 'yin', 'yun', 'yün'], '2PL|2SG|OPT', '2P|2S|OPT'),  # formal
    'ınız': (['ınız', 'iniz', 'unuz', 'ünüz', 'yınız', 'yiniz', 'yunuz', 'yünüz'], '2PL|2SG', '2P|2S|FORM|OPT'),  # formal
    'sanıza': (['sanıza', 'senize'], '2PL|2SG', '2P|2S|FORM|OPT'), # formal
    # persuasive?
    # interjections

}

subordinating_suffixes = {
    # Subordinating suffixes are nominalizing suffixes
    # Any verb form which contains a subordinating suffix is non-finite.
    'yor': (['yor', 'iyor', 'ıyor'], '', 'V.PTCP'),
    'mez': ['mez', 'maz'],
    'eli': ['eli', 'meli', 'malı'],
    'makta': (['makta', 'mekte'], '', 'V.PTCP'),
    'maktansa': (['maktansa', 'mektense'], '', 'V.CVB'),
    # -DIK and -(y)AcAK form all three types of subordinate clause
    # -DIk could be present or part
    'dık': (['dık', 'dik', 'tık', 'tik', 'tiğ', 'tığ', 'diğ', 'dığ'], '', 'V.PTCP|V.MSDR|V.CVB|PST|PRS'),
    'acak': (['acak', 'ecek', 'yacak', 'yecek', 'acağ', 'eceğ', 'yacağ', 'yeceğ'], '', 'V.PTCP|V.MSDR|V.CVB|'),
    # Both -mA and -mAK form verbal nouns and converbs.
    'mak': (['mak', 'mek', 'mak', 'mek','mağ', 'meğ'], '', 'V.MSDR|V.CVB'),
    'ma': ['ma', 'me'],

    'an': (['an', 'en', 'yen', 'yan'], '', 'V.PTCP'),
    'ış': ['ış', 'iş', 'uş', 'üş', 'yiş', 'yış', 'yuş', 'yüş'],
    'ınca': ['ınca', 'ince', 'unca', 'ünce', 'yınca', 'yince', 'yunca', 'yünce'],
    'arak': ['arak', 'erek', 'yerek', 'yarak'],
    'alı': ['alı', 'eli', 'yalı', 'yeli'],
    'casına': ['casına', 'cesine',],
    'ıp': ['ıp', 'ip', 'up', 'üp', 'yıp', 'yip', 'yup', 'yüp'],
    'ken': ['ken', 'yken'],
    'e' : ['e', 'a'],
    'maksızın': ['maksızın', 'meksizin'],

    # 'meden': ['meden', 'madan'],
    # 'mekten': ['mekten', 'maktan'],
    # 'mektense': ['mektense', 'maktansa'],
    # 'inceye': ['inceye', 'ıncaya', 'uncaya', 'ünceye'],
    # 'mişçesine': ['mişçesine', 'mışçasına', 'muştasına', 'müşçesine'],

}

derivational_suffixes = {
    'ki': ['ki', 'kin'],  #

    'aç': ['aç', 'eç', 'ac', 'ec'],
    'can' : ['can', 'eç', 'ac', 'ec'],

}