//wtf i speedrun this web 5 days before cmu portfolio round closed
var i=0,text;
        text = "Alternyatic"

        function typing() {
            if(i<text.length){
                document.getElementById("text").innerHTML += text.charAt(i);
                i++;
                setTimeout(typing,100);
            }
        }
        typing();
