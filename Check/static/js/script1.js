//function myfunc(){
//    alert(document.getElementById("language").value);
//}

var countQues=0;
var lang;
var score=0;
var a;
var HTMLquestions=[
    {
        question: "How old are you?",
        choices: ["Below 10","Between 10 and 30","Between 30 and 60","60 and Above"],
        answer: [0,5,10,20]
    },
    {
        question: "Please select your gender?",
        choices: ["Male","Female","Others","physically challenged"],
        answer: [5,10,10,15]  
    },
    {
        question: "Please let us know your current body temperature in degree Fahrenheit (Normal body temperature is 98.6°F):",
        choices: ["light Fever (98°F-99.6°F)","Fever (99.6°F-102°F)","High Fever (>102°F)","Normal (96°F-98.6°F)"],
        answer: [5,10,20,0]
    
    },
    {
        question: "Are you experiencing any of the symptoms below (mark all those applicable)?",
        choices: ["Dry Cough","Sore Throat","Weakness","no symptoms"],
        answer: [15,20,5,0]
    
    },
    {
        question: "Additionally, please verify if you are experiencing any of the symptoms below (mark all those applicable)",
        choices: ["Difficultly in breathing","Moderate to Severe Cough","Feeling Breadthless","None of the above"],
        answer: [30,15,20,0]
    
    },
    {
        question: "We would like to know about your smoking history",
        choices: ["Never Smoke","Current Smoker","Previous smoker(before 6 months)"],
        answer: [0,20,15,5]
    }, 
    {
        question: "Please select your travel and exposure details",
        choices: ["No travel history","No contact with nyone with symptoms","Any history of travel in affected area for past 14 days","Close contact with any of fever patients"],
        answer: [0,0,15,20]
    
    }, 
    {
        question: "How have your symptoms progressed over the last 48 hrs?",
        choices: ["Improved", "No change","Worsend","no symptoms"],
        answer: [5,10,20,0]    
    }                
];
document.querySelector(".view-results").style.display="none";
document.querySelector(".quiz").style.display="none";
document.querySelector(".final-result").style.display="none";
    document.querySelector(".quiz").style.display="block";
    
    document.querySelector(".question").innerHTML="<h1>"+window[lang][countQues].question+"</h1>";
     for (i=0;i<=3;i++){                     
        document.getElementById("opt"+i).value=window[lang][countQues].choices[i];
        document.getElementById("lb"+i).innerHTML=window[lang][countQues].choices[i];        
    };/*For loop Closed*/
     //window.location.href="#score";
});
document.querySelector(".submit-answer").addEventListener("click",function(){
    //alert(window[lang][countQues].choices[window[lang][countQues].answer-1]);
    //alert(document.querySelector('input[name="options"]:checked').value);
            if(document.querySelector('input[name="options"]:checked').id === "opt0") {
                a=0;
            }
            else if(document.querySelector('input[name="options"]:checked').id === "opt1"){
                a=1;
            }
            else if (document.querySelector('input[name="options"]:checked').id === "opt2") {
                a=2;
            }
            else{
                a=3;
            }
        score+= window[lang][countQues].answer[a];
        
    if (countQues<window[lang].length-1){
        countQues++;
    }else{
        document.querySelector(".submit-answer").style.display="none";
        document.querySelector(".view-results").style.display="unset";
    }
    document.querySelector(".question").innerHTML="<h1>"+window[lang][countQues].question+"</h1>";
    for (i=0;i<=3;i++){                     
        document.getElementById("opt"+i).value=window[lang][countQues].choices[i];
        document.getElementById("lb"+i).innerHTML=window[lang][countQues].choices[i];  
    };/*For loop Closed*/
});

document.querySelector(".view-results").addEventListener("click",function(){
    
    document.querySelector(".final-result").style.display="block";
    document.getElementById("display-final-score").innerHTML="Your Final Score is: "+ score;
    
    if (score>130){
        document.querySelector(".remark").innerHTML="Remark: Very High :((";
    }else if(score>90){
        document.querySelector(".remark").innerHTML="Remark: High :(";
    
    }else if(score>50){
        document.querySelector(".remark").innerHTML="Remark: Medium ! :)";
    }else if(score>30){
        document.querySelector(".remark").innerHTML="Remark: low ! :)";
    }
    else{
        document.querySelector(".remark").innerHTML="Remark: Very low ! :))";
    }
    
//    window.location.href="#display-final-score";

});

document.getElementById("restart").addEventListener("click",function(){
    location.reload();

});

 

});
/*Smooth Scroll*/
$(document).on('click', 'a[href^="#"]', function (event) {
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 1000);
});

