const trigger = [
  ["what is corona", "what is novel corona", "what is covid 19", "corona", "covid 19", "covid", "what is coronavirus disease"],
  ["vaccine for corona", "is there any vaccine for corona"],
  ["symptoms of covid 19", "what are the symptoms of covid 19"],
  ["what should i do if i have visited corona affected area", "how does corona virus spread", "how does covid 19 spread", "transmission", "can a coronavirus be transmitted from person to person"],

  ["can i catch catch corona from my pet or any other animals", "can animals spread corona", "animals corona", "animals", "chicken", "dogs","does having non veg can gain corona"],
  ["medecines for corona", "are there any medecines for corona", "antibiotics for corona", "what is the treatment for the coronavirus disease", "can we take antibiotics for corona", "can antibiotics treat the coronavirus disease"],
  ["how to protect ourself from corona", "what can i do to protect myself from corona"],
  ["should i wear masks to protect myself", "is it necessary to wear mask when at home", "necessities of masks", "about masks"],
 
  ["key times to wash hands", "how to wash hands properly", "when to wash hands", "proper handwashing", "steps for handwashing"],

  ["how to sanitize ourself", "what are the 3 methods of sanitizing", "what is the importance of cleaning and sanitizing the kitchen tools and equipment"],
  ["how to clean vegetables and fruits during corona", "how to clean fruits"],
  ["how to spent this lockdown effectively"],
  ["where did corona originate", "where did corona start", "origin of corona", "start", "origin"],
  ["what is the recovery time for the coronavirus disease", "how long it takes to recover from corona", "what is the life span of corona", "can people recover from coronavirus disease"],
  
  ["can babies get the coronavirus disease", "what about elderly people"],
  ["thank you"]
  
];

const reply = [
  ["Coronaviruses are a large family of viruses which may cause illness in animals or humans. In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19."],
  [
	"Not yet. To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-2019. Possible vaccines and some specific drug treatments are under investigation.  WHO is coordinating efforts to develop vaccines and medicines to prevent and treat COVID-19.",
	"There is no specific treatment for disease caused by a novel coronavirus. However, many of the symptoms can be treated and therefore treatment based on the patient's clinical condition."
  ],
  [
	"The most common symptoms of COVID-19 are fever,tiredness ,dry cough. Some patients may also have aches and pains, nasal congestion, runny nose, sore throat or diarrhea. These symptoms are usually mild and begin gradually.",
	"The virus can cause a range of symptoms, ranging from mild illness to pneumonia. Symptoms of the disease are fever, cough, sore throat and headaches. In severe cases difficulty in breathing and deaths can occur."
  ],
  [
	"Self-isolate by staying at home if you begin to feel unwell,even with mild symptoms such as low fever ,runny nose or headache untill you recover. If you have fever continuously , seek medical advice promptly in advance.",
	"People can catch COVID-19 from others who have the virus. The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales. These droplets land on objects and surfaces around the person.",
	"Yes, some coronaviruses can be transmitted from person to person, usually after close contact with an infected patient, for example, in a household workplace, or health care centre."
  ],
  
  [
	"To protect yourself, such as when visiting live animal markets, avoid direct contact with animals and surfaces in contact with animals. Ensure good food safety practices at all times. Handle raw meat, milk or animal organs with care to avoid contamination of uncooked foods and avoid consuming raw or undercooked animal products.",
	"It is advisable that pet owners and veterinarians strictly observe hand-washing and other infection-control measures, as outlined by the CDC when handling animals. If sick with COVID-19, you should treat your pet like you would any person you interact with and minimize interactions as much as possible."
  ],
  [
	"No. Antibiotics do not work against viruses, they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work. There is no evidence that current medicine can prevent or cure the disease. WHO does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for COVID-19",
	"There is no specific treatment for disease caused by a novel coronavirus. However, many of the symptoms can be treated and therefore treatment based on the patient's clinical condition."
  ],
  [
	"The most effective ways to protect yourself and others against COVID-19 are to frequently clean your hands, cover your cough with the bend of elbow or tissue and maintain a distance of at least 1 meter (3 feet) from people who are coughing or sneezing.",
	"Firstly, wash your hands properly . 2) Avoid touching your eyes, noes and mouth. 3) Cover your cough with the bend of elbow or tissue. 4) Avoid crowded places. 5) Stay at home if you feel unwell even with mild fever or cough. 6) If you have any symptoms seek for medication in advance but do it in call first. 7) Stay tuned with latest info."
  ],
  [
	"Only wear a mask if you are ill with COVID-19 symptoms (especially coughing) or looking after someone who may have COVID-19. Disposable face mask can only be used once. If you are not ill or looking after someone who is ill then you are wasting a mask. There is a world-wide shortage of masks, so WHO urges people to use masks wisely. WHO advises rational use of medical masks to avoid unnecessary wastage of precious resources and mis-use of masks.",
	"If you are healthy, you only need to wear a mask if you are taking care of a person with COVID-19.Wear a mask if you are coughing or sneezing.Masks are effective only when used in combination with frequent hand-cleaning with alcohol-based hand rub or soap and water."
  ],
  [
    "1) Before, during, and after preparing food. 2) Before eating food. 3) Before and after caring for someone at home who is sick with vomiting or diarrhea. 4) Before and after treating a cut or wound. 5) After using the toilet. 6)After blowing your nose, coughing, or sneezing. 7) After touching an animal feed, or animal waste. 8) After handling pet food or pet treats. 9) After touching garbage.",
	"Step 1: Wet Hands. Wet your hands and apply enough liquid soap to create a good lather. Step 2: Rub Palms Together. Step 3: Rub the Back of Hands. Step 4: Interlink Your Fingers. Step 5: Cup Your Fingers. Step 6: Clean the Thumbs. Step 7: Rub Palms with Your Fingers."
  ],
  [
	"There are important differences between washing hands with soap and water and using hand sanitizer. Soap and water work to remove all types of germs from hands, while sanitizer acts by killing certain germs on the skin. Although alcohol-based hand sanitizers can quickly reduce the number of germs in many situations, they should be used in the right situations.",
	"There are three methods of using heat to sanitize surfaces – steam, hot water, and hot air. Hot water is the most common method used in restaurants. If hot water is used in the third compartment of a three-compartment sink, it must be at least 171oF (77oC).",
	"Sanitizing is defined as cleaning something to make it free of bacteria or disease causing elements. An example of sanitizing is wiping a counter with a bleach solution."
  ],
  ["1) . Before washing produce, wash your hands. 2) Rinse your produce well in running water. 3) Do not use soap or any detergent. 4) Use a brush or sponge if necessary. 5) Certain leafy vegetables and fruits like berries require extra care"],
  ["With one's fitness , we can meditate , practice dance, exercise and find healthy things to eat. With family , we can revisit memories, watch movies, play games , create music, cook together, re-arrange your household items, create music ,reading music and many more. Mainly everything should be done  with extra care and safety."],
  ["Retrospective investigations by Chinese authorities have identified human cases with onset of symptoms in early December 2019. While some of the earliest known cases had a link to a wholesale food market in Wuhan, some did not."],
  [
	"Using available preliminary data, the median time from onset to clinical recovery for mild cases is approximately 2 weeks and is 3-6 weeks for patients with severe or critical disease.",
    "You can recover from the coronavirus disease (COVID-19). Catching the new coronavirus DOES NOT mean you will have it for life. Most of the people who catch COVID-19 can recover and eliminate the virus from their bodies."
  ],
  [
	"We know it is possible for people of any age to be infected with the virus, but so far there are relatively few cases of COVID-19 reported among children.",
	"When it comes to COVID-19, the disease caused by the new coronavirus, older people are especially vulnerable to severe illness. Research is showing that adults 60 and older, especially those with preexisting medical conditions, especially heart disease, lung disease, diabetes or cancer are more likely to have severe — even deadly — coronavirus infection than other age groups.If you’re caring for an older loved one, you might be worried."
  ],
  ["Welcome.Stay Home ! Stay Safe ! Stay Sanitisized !.Let all hold hands together to fight corona."]
 
];

const alternative = [
  "Sorry ! Something went wrong !",
  "Read the description once again and proceed",
  "Sorry for the inconvenience ! Please try again",
  "Try again",
  "Can't get you !"
];

const coronavirus = ["Please stay home"];

document.addEventListener("DOMContentLoaded", () => {
	const inputField = document.getElementById("input")
	inputField.addEventListener("keydown", function(e) {
		if (e.code === "Enter") {
			let input = inputField.value;
			inputField.value = "";
			output(input);
    }
  });
});

function output(input) {
  let product;

  //lowercase input and remove all chars except word characters, space, and digits
  let text = input.toLowerCase().replace(/[^\w\s\d]/gi, "");

  // 'tell me a story' -> 'tell me story'
  // 'i feel happy' -> 'happy'
  text = text
    .replace(/ a /g, " ")
    .replace(/i feel /g, "")
    .replace(/whats/g, "what is")
    .replace(/please /g, "")
    .replace(/ please/g, "");

  //compare function, then search keyword, then random alternative
  if (compare(trigger, reply, text)) {
    product = compare(trigger, reply, text);
  } else if (text.match(/coronavirus/gi)) {
    product = coronavirus[Math.floor(Math.random() * coronavirus.length)];
  } else {
    product = alternative[Math.floor(Math.random() * alternative.length)];
  }

  //update DOM
  addChat(input, product);
}

function compare(triggerArray, replyArray, string) {
  let item;
  for (let x = 0; x < triggerArray.length; x++) {
    for (let y = 0; y < replyArray.length; y++) {
      if (triggerArray[x][y] == string) {
        items = replyArray[x];
        item = items[Math.floor(Math.random() * items.length)];
      }
    }
  }
  return item;
}

function addChat(input, product) {
  const mainDiv = document.getElementById("main");
  let userDiv = document.createElement("div");
  userDiv.id = "user";
  userDiv.innerHTML = `<b>USER:</b> <div id="user-response" class=\"chatcard\">${input} </div>`;
  mainDiv.appendChild(userDiv);

  let botDiv = document.createElement("div");
  botDiv.id = "bot";
  botDiv.innerHTML = `<b>BOT:</b> <div id="bot-response" class=\"chatcard\">${product}</div>`;
  mainDiv.appendChild(botDiv);
  speak(product);
}

const synth = window.speechSynthesis;
let voices = synth.getVoices();

function speak(string) {
  let u = new SpeechSynthesisUtterance(string);
  u.text = string;
  u.lang = "en-US";
  u.volume = 1; //0-1 interval
  u.rate = 1;
  u.pitch = 1; //0-2 interval
  synth.speak(u);
  debugger
}
