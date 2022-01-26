window._checkLikert = function(name) // TODO: change back to _checkRadios when releasing
{
    var radios = document.getElementsByName(name),
        value;

    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked)
        {
            value = radios[i].value;
            exec.log(value,name);
            break;
        }
    }
}


var likert = function(message,message1,message2,response_name,size,id,querystring)
{
    var choices1, choices2;

    if (Array.isArray(message1)) {
        choices1 = message1;
    }

    if (Array.isArray(message2)) {
        choices2 = message2;
    }

    size = (choices1 ? choices1.length : (choices2 ? choices2.length : size) ) || 5;

    exec.required(message,"scale","message");
    exec.required(response_name,"scale","response_name");

    id = id || response_name;

    var s = "<div style='margin-bottom:1em;'><label for='" + id + "'>" + message.format(exec.response)
            + "</label></div>"
            + "<div id='radiocontainer1' style='font-size:smaller;' "
            + "onkeypress='_inputKeyPress(event);'>",
        payload;

    if (!choices1 && !choices2) {
        s =+ message1.format(exec.response) + " ";
    }

    for (var i = 0; i < size; i++)
    {
        if (choices1 || choices2) {
            s += "<div style='display:inline-block;padding:0.5em;font-size:smaller;'>";
        }
        if (choices1) {
            s += choices1[i] + " <br />";
        }
        s += "<input style='margin-left:0.5em;margin-right:0.5em;width:.7em;height:0.7em;' type='radio' name='"
             + response_name;
        if (i === 0)
        {
            s += "' id='" + id + "' checked='checked' ";
        }
        s += "' value='" + (i+1) + "'></input>";
        if (choices2) {
            s += "<br />" + choices2[i];
        }
        if (choices1 || choices2) {
            s += "</div>";
        }
    }

    if (!choices1 && !choices2) {
        s += " " + message2.format(exec.response);
    }

    s += "</div>";

    if (!exec.groupactive)
    {
        s += "<button style='margin-top:1em;' id='inputbutton' "
            + "onclick='_checkLikert(\"" + id + "\");'>OK</button>";
    }
    else
    {
        payload = function()
        {
            var number = exec.addharvester(function()
            {
                _checkRadios(id);
            });

            if (number === 1) // If this is the first control in the
            {
                document.getElementById(id).focus();
            }
        }
    }

    this.text(s,querystring,payload);

    if (!exec.groupactive)
    {
        // controls.focus(id); // TODO: reactive when releasing
    }
    return this;
}

main.centerblock.likert = likert;





var subject_id = increase('Subject ID', 'script');
var language = radio('Choose your language:',['English', 'Dutch']);
main.setfontsize(60);



// language switch
if (language === 'English')
{



    ///// informed consent //////
    function getpdf(name) {
        return $$;
    }

    main.setfontsize(60);

    instruction("Dear participant, <br> You are being invited to participate in a research study about individual differences in learning foreign languages. This study is a project by Klaudia Parisi, Joanna Kuczynska, Olivia Von Greve- Dierfeld, Paul Hosek, Yu Qing Yao and Bibi Stikvoort from the University of Amsterdam under supervision of Prof. Jaap Murre.","Next","Informed Consent");
    instruction("The purpose of this research study is to examine how individual differences influence foreign language learning. The experiment will take approximately 30-40 minutes to complete. <br /><br />Your participation in this study is entirely voluntary. You may refuse to take part in the research or exit the survey at any time without penalty.","Next","Informed Consent");
    instruction("If you have questions at any time about the study or the procedures, you may contact Bibi Stikvoort, via email at bibistikvoort3@gmail.com or our research supervisor, Professor Jaap Murre, via email at jaap@murre.com.<br>  If you have any complaints about the task, you can send them to a member (Yaïr Pinto Y.Pinto@uva.nl) of the Commissie Ethiek (Ethics Committee) at the Psychology Department of the University of Amsterdam.","Next","Informed Consent");
    instruction("You are free to decline to answer any particular question you do not wish to answer for any reason.<br /><br />We believe there are no known risks associated with this research study; however, as with any online related activity a breach is always possible. Therefore, data will be anonymised and it will not be possible to trace your answers back to you.<br /><br /> If you have questions at any time about the study or the procedures, you may contact jaap@murre.nl","Next","Informed Consent");

    var s, b1, b2, b3;
    startform();
        b1 = addblock("center",10,80,50).text("<h2>Informed Consent</h2><div>" + 'By checking the box you indicate that:<br>1. You read and agreed to the terms stated in the text displayed previously.<br>2. You are over 18 years old.<br>3. You participate voluntarily.<br> 4. You do not speak Basque.' + "</div>");
        b2 = addblock("center",40,80,40).check("<br /><br />Check the box to indicate informed consent",[["Accept"]],"accept");
        b3 = addblock("center",70,30,10);
        b3.button("Confirm").await("click");
    endform();

    b1.destroy();
    b2.destroy();
    b3.destroy();

    if (response["accept_Accept"] == "false") {
        text("You did not accept the informed consent and will not do the experiment.");
        await(5000);
        window.location.href = "https://google.com"; // Send subject somewhere else
    }

    text("Good luck with the experiment!");
    await(1500);
    /////// end informed consent //////////


    // INSTRUCTIONS //
    instruction("Dear participant, thank you for your participation. <br> This study consists of several phases, first you will be asked to fill in a few short questionnaires. Then you will participate in a vocabulary learning task, where you will study 20 Basque words.",'Next','Welcome');
    instruction("Depending on your performance, the study will take about 40 minutes. Please perform the task in a quiet environment and avoid distractions in your surroundings (e.g. your mobile phone) as much as possible." , 'Next', "Welcome");
    instruction("The vocabulary learning task will be explained in more detail after the questionnaires. <br /><br />When you are ready to start, click on the button below.",'Start Experiment', 'Welcome');


    gender=[];
    select("Which gender do you identify with?",[['Man',0],['Woman',1],['Non-binary',2],['Genderqueer',3],['Prefer not to say',4]],'gender');
    log(gender,"gender");
    age=[];
    input("Please enter your age.",'age');
    log(age,"age");
    education=[];
    select("What is the highest degree or level of school you have completed?",[['Bachelor’s degree',0],['Master’s degree',1],['High school graduate, diploma or the equivalent',2],['Trade/technical/vocational training',3],['Professional degree',4]], "education");
    log(education,"education");

    // SELF EFICACY //
    instruction('This scale consists of a number of statements.<br>'
        +'Read each item; <br> Indicate on the scale to what extent you agree with this statement.','Ok','Self Efficacy').align("left");

     var questions=['When I want to learn a foreign language, I am certain I can succeed at doing so.',
    'I give up on learning a foreign language before I become good at it.',
    'If a foreign language seems too complicated, I will not even bother to try and learn it.',
    'When trying to learn a foreign language, I soon give up if I am not initially successful.',
    'Failure to remember words in a foreign language just makes me try harder.',
     'I feel insecure about my ability to learn a foreign language.',
     'When I set the goal of learning a foreign language for myself, I rarely achieve it.',
     'If I don’t succeed at learning a new language initially, I keep trying until I do.',
     'I can remember new vocabulary easily.',
     'When I have to do an unpleasant exercise, I stick to it until I finish it.',
     'I am good at learning languages.', 'I give up trying to learn a language easily.'], self_efficacy,
     likert_self_efficacy = ['skip question','strongly disagree','disagree','agree','strongly agree'];

    for (i=0; i<questions.length; ++i)
    {
        main.centerblock.likert(questions[i],'',likert_self_efficacy,'self_efficacy');
        main.centerblock.await('button:click');
    //   radio(questions[i],likert_self_efficacy,"self_efficacy");
        log(self_efficacy,"self_efficacy");
    }


    /// Mindfulness ///
    instruction('This scale consists of a number of sentences that describe different aspects of mindfulness. <br> Please: <br /><br /> Read each sentence. <br> Indicate to what extent you agree with each sentence. <br>  Use the following scale to record your answers.',"OK",'Mindfulness');

    var questions_mind = ["When I walk outside, I am aware of smells or how the air feels against my face.",
    "I do jobs or tasks automatically, without being aware of what I'm doing.",
    "I criticize myself for having irrational or inappropriate emotions.",
    "I accept myself as I am.",
    "I try to stay busy to keep thoughts or feelings from coming to mind.",
    "Usually when I have distressing thoughts or images, I am able just to notice them without reacting.",
    "Usually when I have distressing thoughts or images, I just notice them and let them go."];
    var likert_mind = ['skip question','strongly disagree','disagree','neutral','agree','strongly agree'],
        mindfulness;

    for (i = 0; i<questions_mind.length; ++i){
        main.centerblock.likert(questions_mind[i],'',likert_mind,"mindfulness");
        main.centerblock.await("button:click");
        log(mindfulness,'mindfulness');
    }


    // EMOTIONS //
    main.setfontsize(46);
    instruction('This scale consists of a number of words that describe different feelings and emotions.<br>'
    +'Read each item. <br> Choose from the drop-down menu when you experienced the emotion. <br> Indicate on the scale to what extent you experienced it.','OK','Emotions').align("left");
    var emotions=['interested','distressed','excited','upset','guilty',
    'strong','scared','hostile','enthusiastic','proud','irritable','alert',
    'ashamed','inspired','nervous','determined','attentive','jittery'], emotions_when, emotion_extent;
    for (i=0; i<emotions.length; ++i)
    {
        select("When did you experience the following emotion: " +  emotions[i], ['Never','Moment (you feel this way right now, that is, at the present moment)','Today (you have felt this way today)','Past few days (you have felt this way during the past few days)','Week (you have felt this way during the past week)','Past few weeks (you have felt this way during the past few weeks)','Year (you have felt this way during the past year)','General (you generally feel this way, this is how you feel on average)', 'Skip question'], "emotions_when");
        log(emotions_when,'emotions_when');
        main.centerblock.likert("To what extent did you experience this emotion: " +  emotions[i],'',['very slightly or not at all','a little', 'moderately','quite a bit','extremely','Skip question'], "emotion_extent");
        main.centerblock.await('button:click');
        log(emotion_extent,"emotion_extent");
    }


    /// Extraversion ///
    instruction('This scale consists of a number of statements.<br>'
        +'Read each item <br> Indicate on the scale to what extent you agree with this statement.','Ok','Extraversion').align("left");


    var extraversion = ["Are you a talkative person?",
    "Are you rather lively?",
    "Do you enjoy meeting new people?",
    "Can you usually let yourself go and enjoy yourself at a lively party?",
    "Do you usually take the initiative in making new friends?",
    "Can you easily get some life into a rather dull party?",
    "Do you tend to stay in the background on social occasions?",
    "Do you like mixing with people?",
    "Do you like crowdedness and excitement around you?",
    "Are you mostly quiet when you are with other people?",
    "Do other people think of you as being very lively?",
    "Can you get a party going?"], extraversion_options = ['Skip question','Yes', 'No'],
    extraversion;

    for (i=0;i<extraversion.length;++i){
        main.centerblock.likert(extraversion[i],'', extraversion_options,'extraversion');
        main.centerblock.await("button:click");
        log(extraversion, 'extraversion');
    }



     /// START EXPERIMENT ///
    var ez_eng = getwords('easy_english.txt'),
        ez_bsq = getwords('easy_basque.txt'),
        diff_eng = getwords('difficult_english.txt'),
        diff_bsq = getwords('difficult_basque.txt');


    // counterbalancing
    var condition_alloc = subject_id % 2;
    if (condition_alloc === 0){
        eng_1 = ez_eng;
        bsq_1 = ez_bsq;
        eng_2 = diff_eng;
        bsq_2 = diff_bsq;
        log('easy,difficult','condition_order');

    }else{
        eng_1 = diff_eng;
        bsq_1 = diff_bsq;
        eng_2 = ez_eng;
        bsq_2 = ez_bsq;
        log('difficult,easy','condition_order');

    }

    instruction('Thank you for filling out these questionnaires. The following instructions explain the upcoming vocabulary learning task.','Next','Task instructions');
    instruction("In this task, the foreign language you will be learning is Basque. <br /><br /> For this, you will study two lists of 10 words each. Within one list, every word will be presented separately.","Next",'Task instructions');
    instruction("For every English word we will ask you to type in the Basque translation. If you do not know the correct translation (because it is one of your first runs), you can leave the field blank.<br /><br /> You will be given the chance to see the correct translation of a word after you attempted to translate it or left the field blank. This will allow you to learn the words with every presentation.","Next",'Task instructions');
    instruction("You will be studying one word list at a time by translating English words into Basque and remembering the correct Basque words. <br /><br /> All words in a list will be shown repeatedly one after the other, until you get every word correct in the whole word list.<br /><br /> Then you will move onto the second list. Here we ask you to do the same until you have correctly translated the complete second list.","Next",'Task instructions');
    instruction("Good luck!","Start Vocabulary Task",'Task instructions');


    //English pronounciation
    main.setfontsize(50);
    clear();
    var b = main.addblock(5,10,90,40,"azure",'To give you some idea of how Basque words are pronounced, some examples will follow. <br> “tx” is pronounced as a “ch” like in chair <br> [i] as the ee in beet. <br> The g is always hard. That means that even before e and i, it is pronounced like the g in go.<br> Try to keep this in mind whilst learning the words as it can help you remember them.');
    await(15000);
    clear();
    b.destroy();

    main.setfontsize(60);
    // difficulty loop
    var difficulty = [eng_1,eng_2,bsq_1,bsq_2];
    for (diff_indx = 0; diff_indx<2; diff_indx++){
            eng = difficulty[diff_indx];
            bsq = difficulty[diff_indx + 2];
            text('Welcome to lesson number ' + (diff_indx + 1) + '/2. Good luck!');
            await(1000);

            // lesson loop
            while (true) {
                correct = 0;

                // run loop
                for (word = 0; word < eng.length; word++)
                {
                    input(eng[word], 'translation');
//                    if ($.trim(response.translation) === bsq[word]){
                    if ($.trim(response.translation.toLowerCase()) === bsq[word]){
                        text('Good job! That was correct. <br>' + eng[word] + ' = ' + bsq[word]+ '<br> ');
                        await(5000);
                        correct++;
                    } else {
                        text('Sorry, that is not right. The correct translation is: <br>' + eng[word] + ' = ' + bsq[word]);
                        await(5000);

                    }
                }
                log(correct/eng.length, 'correct');

                // break lesson loop, if perfect performance
                if (correct === 10){
                    text("You got all of the words in this lesson correct! <br> ");
                    await(2000);
                    break;
                } else {
                    text("Your got " + correct + ' out of ' + eng.length + ' correct.');
                    await(2000);
                }
        }
    }
    log(correct/eng.length, 'correct');
    // make sure main task is stored
    closesession();




    text('Thank you for your participation. You were a great help to us! <br> You can close the browser window now.');
    await(10000);




// Dutch
} else {


    ///// informed consent //////
    function getpdf(name) {
        return $$;
    }

    main.setfontsize(60);

    instruction("Geachte deelnemer, <br> U wordt uitgenodigd om deel te nemen aan een onderzoek naar individuele verschillen bij het leren van vreemde talen. Dit onderzoek is een project van Klaudia Parisi, Joanna Kuczynska, Olivia Von Greve- Dierfeld, Paul Hosek, Yu Qing Yao en Bibi Stikvoort van de Universiteit van Amsterdam onder supervisie van Prof. Jaap Murre.", "Volgende", "Geïnformeerde toestemming");
    instruction("Het doel van dit onderzoek is om na te gaan hoe individuele verschillen het leren van vreemde talen beïnvloeden. Het experiment zal ongeveer 30-40 minuten in beslag nemen. <br /><br />Uw deelname aan dit onderzoek is geheel vrijwillig. U kunt op elk moment zonder straf deelname aan het onderzoek weigeren of het onderzoek verlaten.", "Volgende", "Geïnformeerde toestemming");
    instruction("Als u vragen heeft over het onderzoek of de procedures, kunt u contact opnemen met Bibi Stikvoort, via email op bibistikvoort3@gmail.com of onze onderzoeksbegeleider, professor Jaap Murre, via e-mail op jaap@murre.com.<br> Mocht u klachten hebben over het onderzoek, kunt u deze sturen naar een lid (Yaïr Pinto Y.Pinto@uva.nl) van de Commissie Ethiek van de afdeling Psychologie van de Universiteit van Amsterdam.  <br /><br />", "Volgende","Geïnformeerde toestemming");

    instruction("Het staat u vrij om te weigeren een bepaalde vraag te beantwoorden die u om welke reden dan ook niet wenst te beantwoorden.<br /><br />Wij zijn van mening dat er geen bekende risico's verbonden zijn aan dit onderzoek; zoals bij elke online-gerelateerde activiteit is een inbreuk echter altijd mogelijk. Daarom zullen de gegevens worden geanonimiseerd en is het niet mogelijk uw antwoorden tot uzelf te herleiden.<br /><br />Als u op enig moment vragen heeft over het onderzoek of de procedures, kunt u contact opnemen met jaap@murre.nl", "Volgende", "Geïnformeerde toestemming");
    var s, b1, b2, b3;
    startform();
        b1 = addblock("center",10,80,50).text("<h2>Geïnformeerde toestemming</h2><div>" + "Door het vakje aan te vinken geeft u aan dat: <br>1. U de voorwaarden in de bovenstaande tekst heeft gelezen en hiermee akkoord gaat. <br>2. U ouder bent dan 18 jaar. <br> 3.U vrijwillig deelneemt.<br> 4.U spreekt geen Baskisch." + "</div>");
        b2 = addblock("center",40,80,40).check("<br /><br />Vink het vakje aan om geïnformeerde toestemming aan te geven",[["Accepteren"]], "Accepteren");
        b3 = addblock("center",70,30,10);
        b3.button("Bevestig").await("click");
    endform();

    b1.destroy();
    b2.destroy();
    b3.destroy();

    if (response["accept_Accept"] == "false") {
        text("U heeft de geïnformeerde toestemming niet aanvaard en zal het experiment niet doen.Vink het vakje aan om geïnformeerde toestemming aan te geven",[["Accepteren"]], "Accepteren");
        await(5000);
        window.location.href = "https://google.com"; // Send subject somewhere else
    }


    text("Veel succes met het experiment!");
    await(1500);
    /////// end informed consent //////////


    // INSTRUCTIONS //
    instruction("Beste deelnemer, dank u voor uw deelname. <br> Deze studie bestaat uit verschillende fasen, eerst wordt u gevraagd een paar korte vragenlijsten in te vullen. Daarna zult u deelnemen aan een taak om woordenschat te leren, waarbij u 20 Baskische woorden zult bestuderen.",'Volgende','Welkom');
    instruction("Afhankelijk van uw prestaties, zal het onderzoek ongeveer 40 minuten duren. Voer de taak uit in een rustige omgeving en vermijd zo veel mogelijk afleiding in uw omgeving (bijv. uw mobiele telefoon). ", "Volgende", "Welkom");
    instruction("De woordenschat leertaak zal meer in detail worden uitgelegd na de vragenlijsten. <br /><br />Wanneer u klaar bent om te beginnen, klikt u op de knop hieronder.",'Start het Experiment', 'Welkom');

    var gender, age, education;
    select("Met welk geslacht identificeert u zich?",[['Man',0],['Vrouw',1],['non-binair',2],['Genderqueer',3],['Zeg ik liever niet',4]],'gender');
    log(gender,"gender");
    input("Voer alstublieft uw leeftijd in.",'age');
    log(age,"age");
    select("Wat is het hoogste niveau van onderwijs dat u hebt voltooid?",[['Bachelordiploma',0],['Masterdiploma',1],['Middelbare school',2],['Handel / technische / beroepsopleiding',3],['Professionele graad',4]], "education");
    log(education,"education");



    // SELF EFFICACY //
    instruction('Deze vragenlijst bestaat uit een aantal uitspraken.<br>'
        +'Lees elk item; <br> Geef op de schaal aan in hoeverre u het eens bent met deze uitspraak.','OK','Zelfeffectiviteit').align("left");
    var likert_zelf = ['volledig juist','enigszins juist','nauwelijks juist', 'volledig onjuist'],
    zelfeffectiviteit;


    var kwesties=['Als ik een vreemde taal wil leren, ben ik er zeker van dat ik daarin kan slagen.',
    'Ik geef het leren van een vreemde taal op voordat ik er goed in ben.',
    'Als een vreemde taal te ingewikkeld lijkt, zal ik niet eens de moeite nemen om de taal proberen te leren.',
    'Als ik een vreemde taal probeer te leren, geef ik het al gauw op als ik geen succes zie.',
    'Als ik er niet in slaag woorden in een vreemde taal te onthouden, doe ik juist meer mijn best.',
    'Ik voel me onzeker over mijn vermogen om een vreemde taal te leren.',
    'Wanneer ik mezelf ten doel stel een vreemde taal te leren, bereik ik dat zelden.',
    'Als ik er aanvankelijk niet in slaag een nieuwe taal te leren, blijf ik het proberen tot ik er wel in slaag.',
    'Ik kan nieuwe woordenschat gemakkelijk onthouden.',
    'Als ik een lastige oefening moet doen, blijf ik volhouden tot ik het helemaal af heb.',
    'Ik ben goed in het leren van talen.', 'Ik geef het gemakkelijk op om een taal te leren.'];
    var likert_zelf = ['vraag overslaan','volledig juist','enigszins juist','nauwelijks juist'],zelfeffectiviteit;
    for (i=0; i<kwesties.length; i++)
    {
        main.centerblock.likert("In hoeverre bent u het eens met deze uitspraak: <br>"+ kwesties[i],'',likert_zelf,'zelfeffectiviteit');
        main.centerblock.await("button:click");
        log(zelfeffectiviteit, 'zelfeffectiviteit');
       //radio("In hoeverre benueens met deze uitspraak: <br>"+ kwesties[i],['volledig juist','enigszins juist','nauwelijks juist', 'volledig onjuist'] ,"zelfeffectiviteit");
    }

        /// Mindfulness ///
    instruction('Deze schaal bestaat uit een aantal zinnen die verschillende aspecten van mindfulness beschrijven. <br> Please: <br /><br /> Lees elk item. <br> Kies uit de selectie wanneer u de emotie heeft ervaren. <br>  Geef op de schaal aan in welke mate u de emotie heeft ervaren.','OK','Mindfulness');

    var questions_mind = ["Als ik buiten loop, ben ik me bewust van geuren of hoe de lucht tegen mijn gezicht aanvoelt.",
    "Ik doe klussen of taken automatisch, zonder me bewust te zijn van wat ik aan het doen ben.",
    "Ik bekritiseer mezelf omdat ik irrationele of ongepaste emoties heb.",
    "Ik accepteer mezelf zoals ik ben. ",
    "Ik probeer bezig te blijven om te voorkomen dat gedachten of gevoelens bij me opkomen.",
    "Meestal als ik verontrustende gedachten of beelden heb, ben ik in staat om ze gewoon op te merken zonder te reageren.",
    "Meestal als ik verontrustende gedachten of beelden heb, merk ik ze gewoon op en laat ze gaan.",
    "Ik zie hoe ik mijn eigen lijden creëer.",
    "Ik ben goed in het vinden van de woorden om mijn gevoelens te beschrijven."];
    var likert_mind = ['vraag overslaan','zeer mee oneens ','mee oneens ','neutraal','mee eens','zeer mee eens'],
        mindfulness;


    for (i = 0; i<questions_mind.length; i++){
        main.centerblock.likert(questions_mind[i],'',likert_mind,"mindfulness");
        main.centerblock.await("button:click");
        log(mindfulness,'mindfulness');
    }

    // EMOTIONS //
    main.setfontsize(46);
    instruction('Deze schaal bestaat uit een aantal woorden die verschillende gevoelens en emoties beschrijven. <br> Lees elk item; <br> Kies uit het drop-down menu wanneer u de emotie heeft;<br> Geef op de schaal aan in welke mate u de emotie heeft ervaren.', 'OK','Emoties');
    var emoties=['geïnteresseerd','bedroefd','opgewonden','overstuur','sterk','schuldig','bang',
    'vijandig','enthousiast','trots', 'prikkelbaar','alert','beschaamd','geïnspireerd','nerveus','vastberaden',
    'oplettend','zenuwachtig'], emoties_when, emotie_extent;
    for (i=0; i<emoties.length; i++)
    {
        select("Wanneer heeft u deze emotie ervaren: " +  emoties[i], ['Nooit','Moment (u voelt u zo op dit moment, dat wil zeggen, op dit moment)',
        'Vandaag (je hebt u vandaag zo gevoeld)','Afgelopen paar dagen (u hebt u de afgelopen dagen zo gevoeld)','Week (u hebt u de voorbije week zo gevoeld)','Afgelopen paar weken (U heeft u de afgelopen weken zo gevoeld)','Jaar (U heeft u in het afgelopen jaar zo gevoeld)','Algemeen (je voelt u over het algemeen zo, dat wil zeggen, hoe u u gemiddeld voelt)','Vraag overslaan' ], "emoties_when");
        log(emoties_when,"emoties_when");
        main.centerblock.likert("In welke mate heeft u deze emotie ervaren: "+ emoties[i],'',['heel weinig of helemaal niet','een beetje','matig', 'tamelijk veel','extreem','Vraag overslaan'], "emotie_extent");//check if extreem and helemaal niet should be the same item
        main.centerblock.await('button:click');
        log(emotie_extent,"emotie_extent");
    }

        /// Extraversion ///
    instruction('Deze schaal bestaat uit een aantal zinnen die verschillende aspecten van extraversie beschrijven. <br> Alsjeblieft: <br /><br /> Lees elk item. <br> Geef op de schaal aan in welke mate u het eens bent met deze stelling.','OK','Extraversion');


    var extraversion = ["Bent u een spraakzaam persoon?",
    "Bent u een levendig persoon?",
    "Vindt u het prettig om nieuwe mensen te ontmoeten?",
    "Kunt u zich meestal op een levendig feest uitleven en er geheel van genieten?",
    "Bent u degene die meestal het initiatief neemt bij het maken van nieuwe vrienden?",
    "Kunt u gemakkelijk wat leven in een nogal saai feestje brengen?",
    "Bent u iemand die geneigd is zich op de achtergrond te houden tijdens sociale evenementen (bijv. op feestjes)?",
    "Vindt u het prettig om in contact met mensen te komen?",
    "Vindt u het prettig om veel drukte en opwinding om u heen te hebben?",
    "Bent u meestal stil als u in een gezelschap bent?",
    "Vinden anderen u een levendig persoon?",
    "Kunt u een feest op gang brengen?"], extraversion_options = ['Vraag overslaan','Ja', 'Nee'],
    extraversion;

    for (i=0;i<extraversion.length;i++){
        main.centerblock.likert(extraversion[i],'', extraversion_options,'extraversion');
        main.centerblock.await("button:click");
        log(extraversion, 'extraversion');
    }

    /// START EXPERIMENT ///
    var ez_eng = getwords('easy_dutch.txt'),
        ez_bsq = getwords('easy_basque.txt'),
        diff_eng = getwords('difficult_dutch.txt'),
        diff_bsq = getwords('difficult_basque.txt');


    // counterbalancing
    var condition_alloc = subject_id % 2;
    if (condition_alloc === 0){
        eng_1 = ez_eng;
        bsq_1 = ez_bsq;
        eng_2 = diff_eng;
        bsq_2 = diff_bsq;
        log('easy,difficult','condition_order');

    }else{
        eng_1 = diff_eng;
        bsq_1 = diff_bsq;
        eng_2 = ez_eng;
        bsq_2 = ez_bsq;
        log('difficult,easy','condition_order');

    }


    instruction('Dank u voor het invullen van deze vragenlijsten. De volgende instructies verklaren de komende woordenschat leertaak.','Volgende','Taak instucties');
    instruction("In deze taak is de vreemde taal die u zult leren Baskisch. <br /><br /> Hiervoor bestudeert u twee lijsten van elk 10 woorden. Elk woord in een van beide lijsten wordt apart gepresenteerd.", "Volgende", "Taakinstructies");
    instruction("Voor elk Nederlands woord zullen we u vragen de Baskische vertaling in te typen. Als u de juiste vertaling niet weet (omdat het een van uw eerste opgaven is), kunt u het veld leeg laten.<br /><br /> U krijgt de kans om de juiste vertaling van een woord te zien nadat u heeft geprobeerd het te vertalen of het veld leeg heeft gelaten. Zo leert u de woorden bij elke presentatie.", "Volgende", "Taakinstructies");
    instruction("U bestudeert één woordenlijst per keer door Nederlanse woorden in het Baskisch te vertalen en de juiste Baskische woorden te onthouden. <br /><br />Alle woorden in een lijst worden herhaaldelijk achter elkaar getoond, totdat u elk woord in de hele woordenlijst correct heeft.<br /><br /> Daarna gaat u verder met de tweede lijst. Hier vragen we u hetzelfde te doen totdat u de hele tweede lijst correct heeft vertaald.", "Volgende",'Taakinstructies');
    instruction("Veel succes!", "Start woordenschat leertaak",'Taakinstructies');

    ///Dutch pronounciation
    main.setfontsize(50);
    clear ();
    var b = main.addblock(5,10,90,40,"azure",'Om u een idee te geven van hoe Baskische woorden worden uitgesproken, volgen hier enkele voorbeelden. <br> [u] als in boek. <br> "tx" als in tsjilpen. <br> "tz" als in tsaar of als in tsunami. <br> Probeer dit in gedachten te houden terwijl u de woorden leert, het kan u helpen ze te onthouden.');
    await(15000);
    clear();
    b.destroy();



    main.setfontsize(60);
    // // difficulty loop
    var difficulty = [eng_1,eng_2,bsq_1,bsq_2];
    for (diff_indx = 0; diff_indx<2; diff_indx++){
            eng = difficulty[diff_indx];
            bsq = difficulty[diff_indx + 2];
            text('Welkom bij les nummer ' + (diff_indx + 1) + '/2. Veel succes!');
            await(1000);

            // lesson loop
            while (true) {
                correct = 0;

                // run loop
                for (word = 0; word < eng.length; word++)
                {
                    input(eng[word], 'translation');
//                    if ($.trim(response.translation) === bsq[word]){
                    if ($.trim(response.translation.toLowerCase()) === bsq[word]){
                        text('Goed gedaan. Dat was correct. <br>' + eng[word] + ' = ' + bsq[word]);
                        await(5000);

                        correct++;

                    } else {
                        text('Sorry, dat is niet correct. De juste vertaling is: <br>' + eng[word] + ' = ' + bsq[word]);
                        await(5000);

                    }
                }
                log(correct/eng.length, 'correct');

                // break lesson loop, if perfect performance
                if (correct === 10){
                    text("U heeft alle woorden in deze les goed!");
                    await(2000);
                    break;
                } else {
                    text("U heeft " + correct + ' van de ' + eng.length + ' goed.');
                    await(2000);
                }
        }
    }
    log(correct/eng.length, 'correct');
    // make sure main task is stored
    closesession();



  text('Dank u voor uw deelname. U heeft ons goed geholpen! <br> U kunt het browservenster nu sluiten.');
  await(10000);


}
closesession();
