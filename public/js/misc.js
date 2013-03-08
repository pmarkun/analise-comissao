//roubado do acontecenacamara
function gup( name ) {
  name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
  var regexS = "[\\?&]"+name+"=([^&#]*)";
  var regex = new RegExp( regexS );
  var results = regex.exec( window.location.href );
  if( results == null )
    return "";
  else
    var result = results[1].substring(0,results[1].length);
    return decodeURIComponent(result).replace(/\+/g, " ")
}

function loadJson(url) {
        var json = '';
        $.ajax({
        'async': false,
        'global': false,
        'url': url,
        'dataType': "json",
        'success': function (data) {
                json = data;
            }
        });
        return json;
    };

function countWords(text) {
    var minString = 2;
    var stopwords = ["agora","ainda","alguém","algum","alguma","algumas","alguns","ampla","amplas","amplo","amplos","ante","antes","aos","após","aquela","aquelas","aquele","aqueles","aquilo","até","através","cada","coisa","coisas","com","como","contra","contudo","daquele","daqueles","das","dela","delas","dele","deles","depois","dessa","dessas","desse","desses","desta","destas","deste","deste","destes","deve","devem","devendo","dever","deverá","deverão","deveria","deveriam","devia","deviam","disse","disso","disto","dito","diz","dizem","dos","ela","elas","ele","eles","enquanto","entre","era","essa","essas","esse","esses","esta","está","estamos","estão","estas","estava","estavam","estávamos","este","estes","estou","fazendo","fazer","feita","feitas","feito","feitos","foi","for","foram","fosse","fossem","grande","grandes","isso","isto","la","lhe","lhes","mas","mesma","mesmas","mesmo","mesmos","meu","meus","minha","minhas","muita","muitas","muito","muitos","não","nas","nem","nenhum","nessa","nessas","nesta","nestas","ninguém","nos","nós","nossa","nossas","nosso","nossos","num","numa","nunca","outra","outras","outro","outros","para","pela","pelas","pelo","pelos","pequena","pequenas","pequeno","pequenos","per","perante","pode","pôde","podendo","poder","poderia","poderiam","podia","podiam","pois","por","porém","porque","posso","pouca","poucas","pouco","poucos","primeiro","primeiros","própria","próprias","próprio","próprios","quais","qual","quando","quanto","quantos","que","quem","são","seja","sejam","sem","sempre","sendo","será","serão","seu","seus","sido","sob","sobre","sua","suas","talvez","também","tampouco","tem","tendo","tenha","ter","teu","teus","tido","tinha","tinham","toda","todas","todavia","todo","todos","tua","tuas","tudo","última","últimas","último","últimos","uma","umas","uns","vendo","ver","vez","vindo","vir","vos","vós"]
    var customStopwords = ["Dispõe"]
    
    var s = text;
	s = s.replace(/[\.,#!$%\^&\*;:{}=\-_`~()]/g,"").replace(/\s+/g, " ");
    s = s.split(' ');
    b = {}
    for (var x=s.length-1;x>0;x--) { 
        //Remove strings
        if (s[x].length <= minString) {
            s.splice(x,1);
        }
        else if (stopwords.indexOf(s[x]) > -1) {
            s.splice(x,1);           
        }
        else if (customStopwords.indexOf(s[x]) > -1) {
            s.splice(x,1);
        }
        else if (Number(s[x])) {
            s.splice(x,1);
        }
        else {
            if (!b[s[x]]) {
                b[s[x]] = 0;
            }
            b[s[x]] += 1;
        };
    };
    return b;
}
