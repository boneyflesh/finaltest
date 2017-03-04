import sys
sys.path.insert(0, 'lib')

import requests
import re
import mysql.connector
from urlparse import urlparse
from urlparse import urljoin
from bs4 import BeautifulSoup

places = ["Abra","Bangued","Boliney","Bucay","Bucloc","Daguioman","Danglas","Dolores","La Paz","Lacub","Lagangilang","Lagayan","Langiden","Licuan-Baay","Luba",
          "Malibcong","Manabo","Penarrubia","Pidigan","Pilar","Sallapadan","San Isidro","San Juan","San Quintin","Tayum","Tineg","Tubo","Villaviciosa",
          "Agusans del Norte","Butuan City","Cabadbaran City","Buenavista","Carmen","Jabonga","Kitcharao","Las Nieves","Magallanes",
          "Nasipit","Remedios T. Romualdez","Santiago","Tubay","Agusans del Sur","Bayugan","Bunawan","Esperanza","Loreto",
          "Prosperidad","Rosario","San Francisco","San Luis","Santa Josefa","Sibagat","Talacogon","Trento","Veruela","Aklan","Altavas",
          "Balete","Banga","Batan","Buruanga","Ibajay","Kalibo","Lezo","Libacao","Madalag","Makato","Malay","Malinao","Nabas","New Washington","Numancia","Tangalan",
          "Albay","Ligao City","Tabaco City","Bacacay","Camalig","Daraga","Guinobatan","Jovellar","Libon","Malilipot",
          "Malinao","Manito","Oas","Pio Duran","Polangui","Rapu-Rapu","Santo Domingo","Tiwi","Antique","Anini-y","Barbaza","Belison",
          "Bugasong","Caluya","Culasi","Hamtic","Laua-an","Libertad","Pandan","Patnongon","San Jose","San Remigio","Sebaste","Sibalom","Tibiao","Tobias Fornier","Valderrama",
          "Apayao","Calanasan","Conner","Flora","Kabugao","Luna","Pudtol","Santa Marcela","Aurora","Baler","Casiguran",
          "Dilasag","Dinalungan","Dingalan","Dipaculao","Maria Aurora","San Luis","Basilan","Isabela City","Lamitan City","Akbar","Al-Barka",
          "Hadji Mohammed Ajul","Lantawan","Maluso","Sumisip","Tipo-Tipo","Tuburan","Ungkaya Pukan","Bataan","Balanga City","Abucay","Bagac",
          "Dinalupihan","Hermosa","Limay","Mariveles","Morong","Orani","Orion","Pilar","Samal","Batanes","Basco","Itbayat","Ivana","Mahatao","Sabtang",
          "Uyugan","Batangas","Batangas City","Lipa City","Tanauan City","Agoncillo","Alitagtag","Balayan","Balete","Bauan","Calaca",
          "Calatagan","Cuenca","Ibaan","Laurel","Lemery","Lian","Lobo","Mabini","Malvar","Mataas na Kahoy","Nasugbu","Padre Garcia","Rosario","San Juan","San Luis",
          "San Nicolas","San Pascual","Santa Teresita","Santo Tomas","Taal","Talisay","Taysan","Tingloy","Tuy","Benguet","Baguio City",
          "Atok","Bakun","Bokod","Buguias","Itogon","Kabayan","Kapangan","Kibungan","La Trinidad","Mankayan","Sablan","Tuba","Tublay","Biliran","Almeria",
          "Biliran","Cabucgayan","Caibiran","Culaba","Kawayan","Maripipi","Naval","Bohol","Tagbilaran City","Alburquerque","Alicia","Anda",
          "Antequera","Baclayon","Balilihan","Batuan","Bien Unido","Bilar","Buenavista","Calape","Candijay","Carmen","Catigbian","Clarin","Corella","Cortes","Dagohoy","Danao","Dauis",
          "Dimiao","Duero","Garcia Hernandez","Guindulman","Inabanga","Jagna","Jetafe","Lila","Loay","Loboc","Loon","Mabini","Maribojoc","Panglao","Pilar","Pres Carlos P Garcia",
          "Sagbayan","San Isidro","San Miguel","Sevilla","Sierra Bullones","Sikatuna","Talibon","Trinidad","Tubigon","Ubay","Valencia","Bukidnon","Malaybalay City",
          "Valencia City","Baungon","Cabanglasan","Damulog","Dangcagan","Don Carlos","Impasug-Ong","Kadingilan","Kalilangan","Kibawe","Kitaotao","Lantapan","Libona",
          "Malitbog","Manolo Fortich","Maramag","Pangantucan","San Fernando","Sumilao","Talakag","Bulacan","Malolos City","Meycauayan City",
          "del Monte City","Angat","Balagtas","Baliuag","Bocaue","Bulacan","Bustos","Calumpit","Dona Remedios Trinidad","Guiguinto","Hagonoy","Marilao","Norzagaray",
          "Obando","Pandi","Paombong","Plaridel","Pulilan","San Ildefonso","San Rafael","Santa Maria","Cagayan","Tuguegarao City",
          "Abulug","Alcala","Allacapan","Amulung","Aparri","Baggao","Ballesteros","Buguey","Calayan","Camalaniugan","Claveria","Enrile","Gattaran","Gonzaga","Iguig","Lal-Lo","Lasam",
          "Pamplona","Penablanca","Piat","Rizal","Sanchez-Mira","Santa Ana","Santa Praxedes","Santa Teresita","Santo Nino","Solana","Tuao","Camarines Norte",
          "Basud","Capalonga","Daet","Jose Panganiban","Labo","Mercedes","Paracale","San Lorenzo Ruiz","San Vicente","Santa Elena","Talisay","Vinzons","Camarines Sur",
          "Iriga City","Naga City","Baao","Balatan","Bato","Bombon","Buhi","Bula","Cabusao","Calabanga","Camaligan","Canaman","Caramoan","Del Gallego",
          "Gainza","Garchitorena","Goa","Lagonoy","Libmanan","Lupi","Magarao","Milaor","Minalabac","Nabua","Ocampo","Pamplona","Pasacao","Pili","Presentacion","Ragay","Sagnay",
          "Fernando","Sipocot","Siruma","Tigaon","Tinambac","Camiguin","Catarman","Guinsiliban","Mahinog","Mambajao","Sagay","Capiz",
          "Roxas City","Cuartero","Dao","Dumalag","Dumarao","Ivisan","Jamindan","Ma-ayon","Mambusao","Panay","Panitan","Pilar","Pontevedra","President",
          "Roxas","Sapi-an","Sigma","Tapaz","Catanduanes","Bagamanoc","Baras","Bato","Caramoran","Gigmoto","Pandan","Panganiban","San Andres",
          "Viga","Virac","Cavite","Cavite City","Tagaytay City","Trece Martires City","Alfonso","Amadeo","Bacoor","Carmona","Dasmarinas","Gen.",
          "Mariano Alvarez","Gen. Emilio Aguinaldo","Gen. Trias","Imus","Indang","Kawit","Magallanes","Maragondon","Mendez","Naic","Noveleta","Rosario","Silang","Tanza","Ternate",
          "Cebu","Argao City","Bogo City","Carcar City","Cebu City","Danao City","Lapu-Lapu City","Mandaue City","Talisay City","Toledo City",
          "Alcantara","Alcoy","Alegria","Aloguinsan","Argao","Asturias","Badian","Balamban","Bantayan","Barili","Boljoon","Borbon","Carmen","Catmon","Compostela",
          "Consolacion","Cordoba","Daanbantayan","Dalaguete","Dumanjug","Ginatilan","Liloan","Madridejos","Malabuyoc","Medellin","Minglanilla","Moalboal","Oslob","Pilar","Pinamungahan",
          "Poro","Ronda","Samboan","San Fernando","San Remigio","Santa Fe","Santander","Sibonga","Sogod","Tabogon","Tabuelan","Tuburan","Tudela",
          "Compostella Valley","Compostela","Laak","Mabini","Maco","Maragusan","Mawab","Monkayo","Montevista","Nabunturan","New Bataan","Pantukan",
          "Cotabato","Kidapawan City","Alamada","Aleosan","Antipas","Arakan","Banisilan","Carmen","Kabacan","Libungan","M'Lang","Magpet","Makilala",
          "Matalam","Midsayap Pigkawayan","Pikit","President Roxas","Tulunan","Davaos del Norte","Island Garden City of Samal","Panabo City","Tagum City",
          "Asuncion","Braulio E. Dujali","Carmen","Kapalong","New Corella","San Isidro","Santo Tomas","Talaingod","Davaos del Sur","Davao",
          "Digos City","Bansalan","Don Marcelino","Hagonoy","Jose Abad Santos","Kiblawan","Magsaysay","Malalag","Malita","Matanao","Padada","Santa Cruz",
          "Santa Maria","Sarangani","Sulop","Davao Oriental","Mati City","Baganga","Banaybanay","Boston","Caraga","Cateel","Governor Generoso",
          "Lupon","Manay","San Isidro","Tarragona","Davao Oriental","Mati City","Baganga","Banaybanay","Boston","Cateel","Governor",
          "Generoso","Lupon","Manay","San Isidro","Tarragona","Dinagat Islands","Basilisia","Cagdianao","Dinagat","Libjo","Albor","Loreto",
          "Jose","Tubajon","Eastern Samar","Borongan City","Arteche","Balangiga","Balangkayan","Can-avid","Dolores","General MacArthur","Giporlos",
          "Guiuan","Hernani","Jipapad","Lawaan","Llorente","Maslog","Maydolong","Mercedes","Oras","Quinapondan","Salcedo","San Julian","San Policarpo","Sulat","Taft",
          "Guimaras","Buenavista","Jordan","Nueva Valencia","San Lorenzo","Sibunag","Aguinaldo","Alfonso Lista",
          "Asipulo","Banaue","Hingyon","Hungduan","Kiangan","Lagawe","Lamut","Mayoyao","Tinoc","Ilocos Norte","Laoag City","Batac City",
          "Adams","Bacarra","Badoc","Bangui","Banna","Burgos","Carasi","Currimao","Dingras","Dumalneg","Marcos","Nueva Era","Pagudpud","Paoay","Pasuquin","Piddig","Pinili",
          "Nicolas","Sarrat","Solsona","Vintar","Ilocos Sur","Candon City","Vigan City","Alilem","Banayoyo","Bantay","Burgos","Cabugao","Caoayan",
          "Cervantes","Galimuyod","Gregorios del Pilar","Lidlidda","Magsingal","Nagbukel","Narvacan","Quirino","Salcedo","San Emilio","San Esteban","San Ildefonso","San Juan",
          "Vicente","Santa","Santa Catalina","Santa Cruz","Santa Lucia","Santa Maria","Santiago","Santo Domingo","Sigay","Sinait","Sugpon","Suyo","Tagudin","Iloilo",
          "Passi City","Iloilo City","Ajuy","Alimodian","Anilao","Badiangan","Balasan","Banate","Barotac Nuevo","Barotac Viejo","Batad","Bingawan",
          "Cabatuan","Calinog","Carles","Concepcion","Dingle","Duenas","Dumangas","Estancia","Guimbal","Igbaras","Janiuay","Lambunao","Leganes","Lemery","Leon","Maasin","Miagao",
          "Mina","New Lucena","Oton","Pavia","Pototan","San Dionisio","San Enrique","San Joaquin","San Rafael","Santa Barbara","Sara","Tigbauan","Tubungan","Zarraga",
          "Isabela","Cauayan City","Santiago City","Alicia","Angadanan","Aurora","Benito Soliven","Burgos","Cabagan","Cabatuan","Cordon","Delfin Albano",
          "Dinapigue","Divilacan","Echague","Gamu","Ilagan","Jones","Luna","Maconacon","Mallig","Naguilian","Palanan","Quezon","Quirino","Ramon","Reina Mercedes","Roxas","San Agustin",
          "San Guillermo","San Isidro","San Manuel","San Mariano","San Mateo","San Pablo","Santa Maria","Santo Tomas","Tumauini","Kalinga","Tabuk City",
          "Balbalan","Lubuagan","Pasil","Pinukpuk","Rizal","Tanudan","Tinglayan","La Union","San Fernando City","Agoo","Aringay",
          "Bacnotan","Bagulin","Balaoan","Bangar","Bauang","Burgos","Caba","Luna","Naguilian","Pugo","Rosario","San Gabriel","San Juan","Santo Tomas","Santol","Sudipen","Tubao","Laguna",
          "Calamba City","San Pablo City","Santa Rosa City","Alaminos","Bay","Binan","Cabuyao","Calauan","Cavinti","Famy","Kalayaan","Liliw","Los Banos",
          "Luisiana","Lumban","Mabitac","Magdalena","Majayjay","Nagcarlan","Paete","Pagsanjan","Pakil","Pangil","Pila","Rizal","San Pedro","Santa Cruz","Santa Maria","Siniloan","Victoria",
          "Lanaos del Norte","Iligan City","Bacolod","Baloi","Baroy","Kapatagan","Kauswagan","Kolambugan","Lala","Linamon","Magsaysay","Maigo","Matungao","Munai",
          "Nunungan","Pantao Ragat","Pantar","Poona Piagapo","Salvador","Sapad","Sultan Naga Dimaporo","Tagoloan","Tangcal","Tubod","Lanaos del Sur","Marawi City",
          "Bacolod-Kalawi","Balabagan","Balindong","Bayang","Binidayan","Buadiposo-Buntong","Bubong","Bumbaran","Butig","Calanogas","Ditsaan-Ramain","Ganassi","Kapai",
          "Kapatagan","Lumba-Bayabao","Lumbaca-Unayan","Lumbatan","Lumbayanague","Madalum","Madamba","Maguing","Malabang","Marantao","Marogong","Masiu","Mulondo","Pagayawan","Piagapo",
          "Poona Bayabao","Pualas","Saguiaran","Sultan Dumalondong","Picong","Tagoloan Ii","Tamparan","Taraka","Tubaran","Tugaya","Wao","Leyte","Baybay City",
          "Ormoc City","Tacloban City","Abuyog","Alangalang","Albuera","Babatngon","Barugo","Bato","Burauen","Calubian","Capoocan","Carigara","Dagami","Dulag",
          "Hilongos","Hindang","Inopacan","Isabel","Jaro","Javier","Julita","Kananga","Leyte","Macarthur","Mahaplag","Matag-ob","Matalom","Mayorga","Merida","Palo","Palompon",
          "Pastrana","San Isidro","Santa Fe","Tabango","Tabontabon","Tanauan","Tolosa","Tunga","Villaba","Maguindanao","Cotabato City",
          "Ampatuan","Buluan","Datu Abdullah Sangki","Datu Anggal Midtimbang","Datu Paglas","Datu Piang","Datu Saudi-Ampatuan","Datu Unsay","Gen. S. K. Pendatun","Guindulungan",
          "Mamasapano","Mangudadatu","Pagagawan","Pagalungan","Paglat","Pandag","Rajah Buayan","Shariff Aguak","South Upi","Sultan sa Barongis","Talayan","Talitay","Marinduque",
          "Boac","Buenavista","Gasan","Mogpog","Santa Cruz","Torrijos","Masbate","Masbate City","Aroroy","Baleno","Balud","Batuan",
          "Cataingan","Cawayan","Claveria","Dimasalang","Esperanza","Mandaon","Milagros","Mobo","Monreal","Palanas","Pio V. Corpuz","Placer","San Fernando","San Jacinto","San Pascual",
          "Uson","Metro Manila","Caloocan","Las Pinas","Makati","Malabon","Mandaluyong","Manila","Marikina","Muntinlupa","Navotas","Paranaque","Pasay","Pasig",
          "Quezon City","San Juan","Taguig","Valenzuela","Pateros","Misamis Occidental","Oroquieta City","Ozamis City","Tangub City",
          "Aloran","Baliangao","Bonifacio","Calamba","Clarin","Concepcion","Don Victoriano Chiongbian","Jimenez","Lopez Jaena","Panaon","Plaridel","Sapang",
          "Dalaga","Sinacaban","Tudela","Misamis Oriental","Cagayan de Oro","Gingoog City","El Salvador City","Alubijid","Balingasag",
          "Balingoan","Binuangan","Claveria","El Salvador","Gitagum","Initao","Jasaan","Kinoguitan","Lagonglong","Laguindingan","Libertad","Lugait","Magsaysay","Manticao","Medina",
          "Naawan","Opol","Salay","Sugbongcogon","Tagoloan","Talisayan","Villanueva","Mountain Province","Barlig","Bauko","Besao","Bontoc","Natonin",
          "Paracelis","Sabangan","Sadanga","Sagada","Tadian","Negros Occidental","Bacolod City","Bago City","Cadiz City","Escalante City","Himamaylan City",
          "Kabankalan City","La Carlota City","Sagay City","San Carlos City","Silay City","Sipalay City","Talisay City","Victorias City","Binalbagan",
          "Calatrava","Candoni","Cauayan","Enrique B. Magalona","Hinigaran","Hinoba-an","Ilog","Isabela","La Castellana","Manapla","Moises Padilla","Murcia","Pontevedra",
          "Pulupandan","Salvador Benedicto","San Enrique","Toboso","Valladolid","Negros Oriental","Bais","Bayawan","Canlaon","Dumaguete","Guihulngan","Tanjay",
          "Amlan","Ayungon","Bacong","Basay","Bindoy","Dauin","Jimalalud","La Libertad","Mabinay","Manjuyod","Pamplona","Santa Catalina","Siaton","Sibulan","Tayasan",
          "Valencia","Vallehermoso","Zamboanguita","Northern Samar","Allen","Biri","Bobon","Capul","Catarman","Catubig","Gamay","Laoang","Lapinig","Las Navas","Lavezares",
          "Lope de Vega","Mapanas","Mondragon","Palapag","Pambujan","Rosario","San Antonio","San Isidro","San Roque","San Vicente","Silvino Lobos","Victoria",
          "Nueva Ecija","Cabanatuan City","Gapan City","Palayan City","San Jose City","Science City of Munoz","Aliaga","Bongabon","Cabiao","Carranglan","Cuyapo",
          "Gabaldon","General Mamerto Natividad","General Tinio","Guimba","Jaen","Laur","Licab","Llanera","Lupao","Nampicuan","Pantabangan","Penaranda","Quezon","Rizal","San Antonio",
          "San Isidro","San Leonardo","Santa Rosa","Santo Domingo","Talavera","Talugtug","Zaragoza","Nueva Vizcaya","Alfonso Castaneda","Ambaguio","Aritao","Bagabag",
          "Bambang","Bayombong","Diadi","Dupaxs del Norte","Dupaxs del Sur","Kasibu","Kayapa","Quezon","Santa Fe","Solano","Villaverde","Occidental Mindoro","Abra de","Ilog",
          "Calintaan","Looc","Lubang","Magsaysay","Mamburao","Paluan","Rizal","Sablayan","Santa Cruz","Oriental Mindoro","Calapan City","Baco","Bansud",
          "Bongabong","Bulalacao","Gloria","Mansalay","Naujan","Pinamalayan","Pola","Puerto Galera","Roxas","San Teodoro","Socorro","Victoria","Palawan","Puerto",
          "Princesa City","Aborlan","Agutaya","Araceli","Balabac","Bataraza","Brooke's Point","Busuanga","Cagayancillo","Coron","Culion","Cuyo","Dumaran","El Nido","Kalayaan","Linapacan",
          "Magsaysay","Narra","Quezon","Rizal","Roxas","San Vicente","Sofronio Espanola","Taytay","Pampanga","Angeles City","City of San Fernando",
          "Apalit","Arayat","Bacolor","Candaba","Floridablanca","Guagua","Lubao","Mabalacat","Macabebe","Magalang","Masantol","Mexico","Minalin","Porac","San Luis","San Simon","Santa Ana",
          "Santa Rita","Santo Tomas","Sasmuan","Pangasinan","Alaminos City","Dagupan City","San Carlos City","Urdaneta City","Agno","Aguilar","Alcala","Anda",
          "Asingan","Balungao","Bani","Basista","Bautista","Bayambang","Binalonan","Binmaley","Bolinao","Bugallon","Burgos","Calasiao","Dasol","Infanta","Labrador","Laoac","Lingayen",
          "Mabini","Malasiqui","Manaoag","Mangaldan","Mangatarem","Mapandan","Natividad","Pozzorubio","Rosales","San Fabian","San Jacinto","San Manuel","San Nicolas","San Quintin",
          "Santa Barbara","Santa Maria","Santo Tomas","Sison","Sual","Tayug","Umingan","Urbiztondo","Villasis","Quezon","Lucena City","Tayabas City",
          "Agdangan","Alabat","Atimonan","Buenavista","Burdeos","Calauag","Candelaria","Catanauan","Dolores","General Luna","General Nakar","Guinayangan","Gumaca","Infanta","Jomalig",
          "Lopez","Lucban","Macalelon","Mauban","Mulanay","Padre Burgos","Pagbilao","Panukulan","Patnanungan","Perez","Pitogo","Plaridel","Polillo","Quezon","Real","Sampaloc",
          "Andres","San Antonio","San Narciso","Sariaya","Tagkawayan","Tiaong","Unisan","Quirino","Aglipay","Cabarroguis","Diffun","Maddela","Nagtipunan",
          "Saguday","Rizal","Antipolo City","Angono","Baras","Binangonan","Cainta","Cardona","Jalajala","Morong","Pililla","Rodriguez","San Mateo","Tanay","Taytay",
          "Teresa","Romblon","Alcantara","Banton","Cajidiocan","Calatrava","Concepcion","Corcuera","Ferrol","Looc","Magdiwang","Odiongan","Romblon","San Agustin",
          "Andres","San Fernando","Santa Fe","Santa Maria","Samar","Catbalogan City","Calbayog City","Almagro","Basey","Calbiga","Daram",
          "Gandara","Hinabangan","Jiabong","Marabut","Matuguinao","Motiong","Pagsanghan","Paranas","Pinabacdao","San Jorge","San Jose De Buan","San Sebastian","Santa Margarita",
          "Santa Rita","Santo Nino","Tagapul-an","Talalora","Tarangnan","Villareal","Zumarraga","Sarangani","Alabel","Glan","Kiamba","Maasim","Maitum","Malapatan","Malungon",
          "Shariff Kabunsuan","Barira","Buldon","Datu Blah T. Sinsuat","Datu ,Odin Sinsuat","Kabuntalan","Matanog","Northern Kabuntalan","Parang","Sultan Kudarat","Sultan",
          "Mastura","Upi","Siquijor","Enrique Villanueva","Larena","Lazi","Maria","San Juan","Siquijor","Sorsogon","Sorsogon City","Barcelona",
          "Bulan","Bulusan","Casiguran","Castilla","Donsol","Gubat","Irosin","Juban","Magallanes","Matnog","Pilar","Prieto Diaz","Santa Magdalena","South Cotabato",
          "General Santos City","Koronadal City","Banga","Lake Sebu","Norala","Polomolok","Santo Nino","Surallah","T'Boli","Tampakan","Tantangan","Tupi","Southern",
          "Leyte","Maasin City","Anahawan","Bontoc","Hinunangan","Hinundayan","Libagon","Liloan","Limasawa","Macrohon","Malitbog","Padre Burgos","Pintuyan","Saint",
          "Bernard","San Juan","San Ricardo","Silago","Sogod","Tomas Oppus","Sultan Kudarat","Tacurong City","Bagumbayan","Columbio",
          "Esperanza","Isulan","Kalamansig","Lambayong","Lebak","Lutayan","Palimbang","President Quirino","Sen. Ninoy Aquino","Sulu","Hadji Panglima Tahil","Indanan",
          "Jolo","Kalingalan Caluang","Lugus","Luuk","Maimbung","Old Panamao","Omar","Pandami","Panglima Estino","Pangutaran","Parang","Pata","Patikul","Siasi","Talipao","Tapul","Tongkil",
          "Surigao del Norte","Surigao City","Alegria","Bacuag","Burgos","Claver","Dapa","Del Carmen","General Luna","Gigaquit","Mainit","Malimono","Pilar","Placer",
          "San Benito","San Isidro","Santa Monica","Sison","Socorro","Tagana-an","Tubod","Surigaos del Sur","Bislig City","Tandag City",
          "Barobo","Bayabas","Cagwait","Cantilan","Carmen","Carrascal","Cortes","Hinatuan","Lanuza","Lianga","Lingig","Madrid","Marihatag","San Agustin","Tagbina","Tago",
          "Tarlac","Tarlac City","Anao","Bamban","Camiling","Capas","Concepcion","Gerona","Mayantoc","Moncada","Paniqui","Pura","Ramos","San Clemente",
          "San Manuel","Santa Ignacia","Victoria","Tawi-Tawi","Bongao","Languyan","Mapun","Panglima Sugala","Sapa-Sapa","Sibutu","Simunul","Sitangkai","South Ubian",
          "Tandubas","Turtle Islands","Zambales","Olongapo City","Botolan","Cabangan","Candelaria","Castillejos","Iba","Masinloc","Palauig","San Antonio",
          "Felipe","San Marcelino","San Narciso","Santa Cruz","Subic","Zamboangas del Norte","Dapitan City","Dipolog City","Bacungan","Baliguian",
          "Godod","Gutalac","Jose Dalman","Kalawit","Katipunan","La Libertad","Labason","Liloy","Manukan","Mutia","Pinan","Polanco","Pres Manuel A Roxas","Rizal","Salug","Sergio",
          "Osmena Sr","Siayan","Sibuco","Sibutad","Sindangan","Siocon","Sirawai","Tampilisan","Zamboangas del Sur","Pagadian City","Zamboanga City","Aurora",
          "Bayog","Dimataling","Dinas","Dumalinao","Dumingag","Guipos","Josefina","Kumalarang","Labangan","Lakewood","Lapuyan","Mahayag","Margosatubig","Midsalip","Molave","Pitogo","Ramon",
          "Magsaysay","San Pablo","Sominot","Tabina","Tambulig","Tigbao","Tukuran","Vincenzo A Sagun","Zamboanga Sibugay","Alicia","Buug","Diplahan","Imelda",
          "Ipil","Kabasalan","Mabuhay","Malangas","Naga","Olutanga","Payao","Roseller Lim","Siay","Talusan","Titay","Tungawan","Mayon Volcano","Kanlaon Volcano","Bulusan Volcano","Canlaon City","Boracay",]


geohazardterms = ["Volcano","earthquake","landslide","tsunami"]

mineralterms = ["acanthite","actinolite","adamite","aegirine","aeschynite","agate","ajoite","albite","alexandrite","allanite","alluvial","almandine","altaite","aluminum","alunite","amber",
                "amblygonite","amethyst","analcime","anapaite","anatase","andalusite","andersonite","andesine","andesite","andradite","angelite","anglesite","anhydrite","ankerite","annabergite",
                "anorthite","anorthosite","anthophyllite","antimony","antlerite","apatite","apophyllite","aquamarine","aragonite","arfvedsonite","argentite","argyrodite","arsenic","arsenopyrite",
                "arsentsumebite","arthurite","artinite ","asteroids","astrophyllite","atacamite","augelite ","augite","aurichalcite","austinite","autunite","axinite","azurite","babingtonite",
                "bakerite","baratovite","barite","basalt","bastnasite","baumhauerite","bayldonite","becquerelite","benitoite","beraunite","berlinite","berthierite","bertrandite","beryl",
                "beryllonite","betafite","beudantite","bideauxite","bif","bindheimite","biotite","bismuth","bismuthinite","bixbyite","blodite","bloodstone","boleite","boltwoodite","boracite",
                "borax","bornite","boulangerite","bournonite","brannerite","brass","brazilianite","breccia","brochantite","brookite","brucite","buergerite","burbankite","buttgenbachite",
                "bytownite","cacoxenite","calaverite","calciovolborthite","calcite","caledonite","calomel","cancrinite","carbocernaite","carbonates","carletonite","carnallite","carnelian",
                "carnotite","cassiterite","catapleiite","cavansite","celestite ","cerussite","chabazite","chalcanthite","chalcedony","chalcocite","chalcophyllite","chalcopyrite","chalcosiderite",
                "chalcotrichite","chalk","charoite","chengdeite","childrenite","chkalovite","chlorapatite","chlorargyrite","chlorite","chondrodite","chromite","chromium","chrysoberyl",
                "chrysocolla","chrysoprase","chrysotile","churchite","cinnabar","citrine","clausthalite","clays","cleavelandite","cliffordite","clinochlore","clinoclase","clinohedrite",
                "clinohumite","clinoptilolite","coal","cobalt","cobaltite","cobaltite","cobaltocalcite","coconinoite","coesite","colemanite","collinsite","columbite","comets","conichalcite",
                "connellite","copiapite","copper","cordierite","cordylite","cornetite ","cornwallite","corundum","covellite","creedite","cristobalite","crocoite","crocidolite","cryolite",
                "cubanite","cumengite","cummingtonite","cuprite","cuproadamite","cuprosklodowskite","cyanotrichite","cylindrite","danburite","datolite","datolite","descloizite","demantoid",
                "deposits","diaboleite","diamond ","digenite","diopside","dioptase","dolomite","domeykite","dravite","dufrenite","duftite","dumortierite","dundasite","dyscrasite","edenite",
                "edingtonite","elbaite","elements","elpidite","emerald","emmonsite","emplectite","enargite","enstatite","eosphorite","epididymite","epidote","epistilbite","epsomite","erionite",
                "erythrite","esperite","ettringite","euclase","eucryptite","eudialyte","eudidymite","euxenite","fayalite","fedorite","feldspar","ferberite","ferro edenite","ferroglaucophane",
                "fiedlerite","flint","fluorapatite","fluorite","fluorrichterite","forsterite","franckeite","franklinite","fuchsite","fulgarite","gadolinite","gahnite","galena","galena","garnet",
                "gaspeite","gaylussite","gemstones","geodes","gersdorffite","gibbsite","glauberite","glaucophane","gmelinite","goethite","gold","goosecreekite","gormanite","goshenite","graemite",
                "granite","graphite","gratonite","greenockite","grossular","gypsum","gyrolite","hackmanite","halides","halite","hanksite","hardystonite","harmotome","hausmannite","hedenbergite",
                "hedyphane","heliodor","hematite","hemimorphite","herderite","hessite","hessonite","heulandite","hiddenite","hilairite","hinsdalite","hodgkinsonite","hopeite","hornblend","howlite",
                "huebnerite","humite","hureaulite","hydroboracite","hydromagnesite","hydroxylapatite","hydroxylbastnasite","hydrozincite","hypersthene","ice","idocrase","igneous","ilvaite",
                "ilmenite","indicolite","inesite","iolite","iron","jade","jadeite","jamesonite","jarosite","jasper","joaquinite","jordanite","kaemmererite","kaolinite","kermesite","kernite",
                "kidwellite","kieserite","kinoite","knaufite","kolwezite","kornerupine","kottigite","kovdorskite","ktenasite","kulanite","kunzite","kupletskite","kutnohorite","kyanite","labradorite",
                "larderellite","larimar","laueite","laumontite","laurionite","lazulite","lazurite","lead","leadhillite","lechatelierite","legrandite","leifite","lepidolite","leucite","leucochalcite",
                "leucophanite","libethenite","limestone","limonite","linarite","linnaeite","liroconite","lithiophilite","lollingite","lorenzenite","larimar","ludlamite","macphersonite","magnesite",
                "magnetite","malachite","manganbabingtonite","manganese","manganite","marble","marcasite","marcasite","massicot","melanite","melanophlogite","melanterite","meneghinite","mercury",
                "mesolite","meta ankoleite","meta autunite","meta torbernite","meta uranocircite","meta variscite","meta zeunerite","metamorphic","meteorites","miargyrite","mica","microcline",
                "microlite","milarite","milky_quartz","millerite","mimetite","minasgeraisite  ","mineraloids","minium","mixite","moctezumite","moissanite","moldavite","molybdenum","molybdenite",
                "monazite","montebrasite","montmorillonite","moonstone","mordenite","morganite","moschellandsbergite","mottramite","murmanite","muscovite","nagyagite","nahcolite","narsarsukite",
                "natrojarosite","natrolite","nealite","nepheline","nephrite","neptunite","nickel","nickeline","niter","nitratine","norbergite","obsidian","okenite","oligoclase","olivine","olivine",
                "olivenite","onyx","opal","organics","orpiment","orthoclase","osbornite","osumilite","otavite","oxides","pachnolite","palygorskite","papagoite","paradamite","parasymplesite",
                "paravauxite","parisite","pectolite","pentlandite","periclase","peridot","perovskite","pharmacolite","pharmacosiderite","phenakite","phillipsite","phlogopite","phosgenite",
                "phosphates","phosphophyllite","phosphuranylite","picromerite","pirssonite","plancheite","platinum","plattnerite","polybasite","polyhalite","polylithionite","powellite","prasiolite",
                "prehnite","primordial","proustite","pseudoboleite","pseudobrookite","pseudomalachite","psilomelane","pucherite","purpurite","pyrargyrite","pyrite","pyroaurite","pyrochlore",
                "pyrolusite","pyromorphite","pyrope","pyrophyllite","pyroxene","pyrrhotite","quartz","quetzalcoatlite","raite","rammelsbergite","ramsdellite","realgar","rhabdophane","rheniite",
                "rhodizite","rhodochrosite","rhodolite","rhodonite","richterite","riebeckite","rock_crystal","rockbridgeite","romanechite","rosasite","rose_quartz","roselite","ruby","rutile",
                "safflorite","sainfeldite","sal_ammoniac","samarskite","sanbornite","sandstone","sanidine","sapphire","sard","sardonyx","sartorite","scapolite","scheelite","schmitterite","scholzite",
                "schorl","schrockingerite","scolecite","scorodite","scorzalite","sedimentary","selenite","selenium","semseyite","senarmontite","serandite","serpentine","shattuckite","siderite",
                "silicates","silicon","sillimanite","silver","sinhalite","sjogrenite","sklodowskite","skutterudite","smithsonite","smoky_quartz","sodalite","spangolite","sperrylite","spessartine",
                "sphaerocobaltite","sphalerite","sphene","spinel","spinel","spodumene","staurolite","stellerite","stephanite","stibarsen","stibiconite","stibnite","stichtite","stilbite","stishovite",
                "strengite","strontianite","strunzite","sturmanite","sugilite","sulfates","sulfides","sulfur","sunstone","suolunite","susannite","sussexite","svanbergite","sylvanite","sylvite",
                "symplesite","synchysite","taaffeite","tainiolite","talc","tantalite","tanzanite","tarbuttite","teallite","tektites","tellurium","tennantite","tephroite","tetrahedrite","thaumasite",
                "thenardite","thomsonite","thorite","thorogummite","tin","tinaksite","tincalconite","titanium","titanite","topaz","topazolite","torbernite","tourmaline","tremolite","tridymite",
                "triphylite","trona","tsavorite","tsumcorite","tsumebite","turquoise","tyuyamunite","ulexite","ullmannite","uraninite","uranocircite","uranophane","uranopilite","uvarovite",
                "uvite","valentinite","vanadinite","variscite","vauxite","vermiculite","vesuvianite","veszelyite","villiaumite","vivianite","volborthite","walpurgite","wardite","wavellite",
                "weloganite","wernerite","whewellite","whiteite","whitlockite","willemite","witherite","wolfeite","wolframite","wollastonite","woodhouseite","wulfenite","wurtzite","xenotime",
                "xonotlite","yuksporite","zeolite","zeunerite","zinc","zincite","zinkenite","zinnwaldite","zippeite","zircon","zoisite","magnetite"]

landformterms =["ablation till","accretion","active layer","active slope","Aeolian","aggradation","alas","alluvial fan","alluvial flat","alluvial plain","alluvial plain remnant","alluvial terrace",       
                "lluvium","alpine","alpine glacier","andesitic lahar deposit","angle of repose","annular drainage pattern","anthropogenic feature","anthroscape","anticline","aquiclude","aquifer","aquitard","arete","arroyo","artifact",
                "artificial collapsed depression","artificial","drainage pattern","artificial levee","aspect","atoll","avalanche","avalanche chute","avalanche track","avulsion","axial stream","back barrier beach",
                "cockpit karst","col","collapse sinkhole","collapsed ice floored lakebed","collapsed ice walled lakebed","collapsed lake plain","collapsed outwash plain","colluvial","colluvial apron","colluvium","competence","complex landslide",
                "conformity","congelifraction","congeliturbate","congeliturbation","conglomerate","conservation terrace","constructional","continuous permafrost","continental glacier","coppice mound","coprogenous earth","coprogenic material",
                "coral island","corda","corrosion","coulee","country rock","cove","cove","cradle","knoll","craton","creek","creep","crest","crest","crevasse","crevasse filling","crevasse splay","cross bedding","cross lamination",
                "cross stratification","cryoplanation","cryoturbate","cryoturbation","cryptogamic crust","cuesta","cuesta valley","cut","cut fill","cutoff","cyclothem","dead ice","dead ice moraine","debris","debris avalanche","debris fall",
                "debris flow","debris slide","debris spread","debris topple","deflation basin","degradation","Delmarva Bay","delta","delta plain","dendritic drainage pattern","deranged",
                "drainage pattern","desert pavement","desert varnish","destructional","detritus","diamict","diamictite","diamicton","diaper","diatomaceous earth","diatomaceous earth","dike","dip","dip","dip slope","discontinuity",
                "discontinuous permafrost","disintegration moraine","distal","distributary","ditch","divide","doline","dolomite","dolomite","dolostone","dome","drainage basin","drainage network","drainage pattern","drainageway",
                "drainhead complex","draw","dredge spoils","drift","dropstone","drumlin","drumlin field","drumlinoid ridge","dry wash","dump","dune","dune field","dune lake","dune traces","earth dike","earth fall","earth hummock",
                "earth pillar","earth spread","earth topple","earthflow","elevation","elevated lake plain","elliptical gilgai","end moraine","Eocene","eolian","eolian deposit""eolian sands","ephemeral stream","epiclastic","eroded fan remnant",
                "eroded fan remnant sideslope","erosion","erosional","erosional outlier","erosional pavement","erosion pavement","erosion remnant","erratic","escarpment","esker","estuarine deposit","estuarine subaqueous soils","estuary",
                "everglades","exfoliation","exhumed","extramorainic","extramorainal","extrusive","faceted spur","facies","fall","falling dune","fall line","fan","fan apron","fan collar","fan piedmont","fan remnant","fan remnant sideslope",
                "fan skirt","fan terrace","fanglomerate","fanhead trench","fault","fault block","fault line","fault zone","fault block mountains","fault line scarp","felsenmeer","felsic rock","fen","fenster","fill","filled marshland","finger ridge",
                "first bottom","fissure vent","fjord","flat","flat","flatwoods","flood plain","flood plain landforms","flood plain playa","flood plain splay","flood plain step","flood tidal delta slope","floodwall","floodway","floor","flow",
                "flow till","flute","fluve","fluvial","fluviokarst","fluviomarine bottom","fly ash","fold","foothills","footslope","foredune","formation","fosse","free face","free face","freshwater marl","fringe tidal marsh","frost boil",
                "frost bursting","frost churning","frost polygons","frost riving","frost shattering","frost splitting","frost stirring","frost weathering","frost wedging","furrow","gap","gelifraction","gelivation","geomorphic component",
                "geomorphic surface","geomorphology","geyser","geyser basin","geyser cone","giant ripple","gilgai","glacial","glacial drainage channel","glacial drift","glacial groove","glacial lake","glacial marine sedimentation",
                "glacial outwash","glacial till","glaciation","glacier","glaciofluvial deposit","glaciolacustrine deposit","glaciomarine deposit","glade","glauconite pellets","gorge","graben","granitoid","Grady pond","grassy organic materials",
                "gravel pit","grike","groove","grus","gulch","gulf","gully","gut","gut","hanging valley","head","headland","head slope","headwall","headwall","herbaceous organic materials","herbaceous peat",
                "high center polygon","high hill","highmoor bog","hill","hillock","hills","hillside","hillslope","hillslope profile position","hill top","hogback","Holocene","homoclinal","homoclinal ridge","homocline","hoodoo","horn","horst",
                "hot spring","human transported material","hummock","hummock","ice age","ice pressure ridge","ice contact slope","ice margin complex","ice marginal stream","ice pushed ridge","ice rafting","ice segregation","ice wedge",
                "ice wedge cast","ice wedge polygon","igneous rock","inlet","inselberg","inset fan","integrated drainage","interbedded","interdune","interdune valley","interfluve","interfluve","interfurrow","interior valley","intermediate position",
                "intermittent stream","intermontane basin","interstream divide","intertidal","intramorainal","intrusive","joint","jokulhlaup","kame","kame moraine","kame terrace","karren","karst","karst","drainage pattern","karstic",
                "arstic marine terrace","karst lake","karstland","kegel karst","kettle","kipuka","kluftkarren","knickpoint","knob","knoll","lacustrine deposit","lagoon","lagoon","lagoon bottom","lagoon channel","lagoonal deposit",              
                "submerged wave cut platform","submerged upland tidal marsh","subtidal","subtidal wetlands","superglacial","supraglacial","supraglacial debris flow sediment","supraglacial flow till","supraglacial melt out till",
                "supraglacial till","surface mine","swale","swallow hole","swamp","swash zone","swell","swell","swale","syncline","tableland","talf","talus","talus slope","tank","tarn","tephra","terminal moraine","terrace",
                "terrace slope","terracettes","thalweg","thaw sensitive permafrost","thaw stable permafrost","thermokarst","thermokarst depression","thermokarst","drainage pattern","thermokarst lake","tidal flat",
                "tidal inlet","tidal inlet","tidal marsh","till","till plain","tillage mound","tilted fault block","toe","toeslope","tombolo","topography","topple","translational debris slide","translational earth slide" ,
                "translational rock slide","translational slide","transverse dune","tread","tree throw","tree tip","tree tip mound","tree tip pit","tree tip pit mound topography","trellis","drainage pattern","tripoli","trough",
                "trough end","trough valley","truncated soil","tuff","tunnel valley","tunnel valley lake","turf hummock","unconformity","underfit stream","upland","uplift","upthrust","U shaped valley","uvala","valley","valley fill",
                "valley flat","valley floor","valley side","valley train","valley wall","valley border surfaces","valley floor remnant","valley side alluvium","varve","ventifact","vitric","V shaped valley","wash","washover fan",
                "washover fan apron","washover fan flat","washover fan slope","water lain moraine","waterway","wave built terrace","wave cut platform","wave cut terrace","wave worked till plain","welded soil","welded tuff",
                "welding","wind gap","window","windthrow","wind tidal flat","woody organic materials","woody peat","yardang","yardang trough","zibar","islands","Valley","Banaue Rice Terraces"]
 
url =["http://www.phivolcs.dost.gov.ph/","https://en.wikipedia.org/wiki/Mines_and_Geosciences_Bureau_Region_13_(Philippines)","http://www.brighthub.com/environment/science-environmental/articles/106153.aspx"]
finallinks = ["http://www.phivolcs.dost.gov.ph/","https://en.wikipedia.org/wiki/Mines_and_Geosciences_Bureau_Region_13_(Philippines)","http://www.brighthub.com/environment/science-environmental/articles/106153.aspx"]
#finallinks = ["http://www.phivolcs.dost.gov.ph/index.php?option=com_content&view=article&id=7029:mayon-volcano-bulletin-30-january-2017-800-am-&catid=70:latest-volcano-bulletin&Itemid=500008",
              #"https://watchers.news/2014/09/16/mayon-volcano-philippines-eruption-warning-issued/",
              #"http://r5.denr.gov.ph/index.php/86-region-news-items/495-bush-fire-sa-mayon-volcano-national-park-padagus-na-pigpapatutukan-kan-denr"]

point=0
while point<len(url):    
    urls = [url[point]]
    
    

    while len(urls) >0:
        try:
            htmltext = requests.get(urls[0]).content
        except:
            print urls[0]
        soup = BeautifulSoup(htmltext,"lxml")
    
        urls.pop(0)
          
    
        for tag in soup.findAll('a',{'class': 'mostread'},href=True):
            print (tag['href'])
            tag['href'] = urljoin(url[point],tag['href'])
            if url[point] in tag['href'] and tag['href'] not in finallinks:            
                print (tag['href'])           
                finallinks.append(tag['href'])      
    point+=1

cnx = mysql.connector.connect(user='root', password='root',
                                  host='104.154.169.127',
                                  database='scrapedb')
cursor = cnx.cursor()
cursor.execute("TRUNCATE TABLE Scraped")
cnx.commit()
cursor.close()
cnx.close()

unum=0
while unum<len(finallinks):    
    response = requests.get(finallinks[unum])
    txt = response.content
    soup = BeautifulSoup(txt,"lxml")

    HStore=[]
    MStore=[]
    LStore=[]
     
    
    

    

    table = soup.findAll('tr')  
    i=0
    while(i != len(table)):
        pattern = r'\b({})\b'.format('|'.join(geohazardterms)) 
        if re.search(pattern, table[i].get_text()):
            print(table[i].get_text())
            striped=table[i].get_text()
            striped = re.sub('<[^>]*>', '', striped).replace('\n','')                   
            if(striped in HStore):
                print("Sorry pariha ra table")
            else:
                HStore.append(striped)
        i+=1

    paragraph = soup.findAll('p')    
    x=0
    while(x != len(paragraph)):
        
        pattern = r'\b({})\b'.format('|'.join(geohazardterms)) 
        if re.search(pattern, paragraph[x].get_text()):
            checkS = paragraph[x].get_text()
            checkS = re.sub('<[^>]*>', '', checkS).replace('\n','')
            if any(checkS in phrase for phrase in HStore ):
                print "pariha ra!"
            else:
                indices = [newrd for newrd, newes in enumerate(places) if newes in checkS[0:80]]
                if indices:
                    i=0
                    while(i !=len(indices)):
                        sentence = places[indices[i]]
                        print sentence
                
                        parsed_uri = urlparse(finallinks[unum])
                        Source = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                        cnx = mysql.connector.connect(user='root', password='root',                                
                                                  host='104.154.169.127',
                                                  database='scrapedb')
                        cursor = cnx.cursor()
        
        
        
                        cursor.execute("SELECT count(*) FROM Scraped")
                        count=cursor.fetchone()
       
        
                        if count[0] == 0:
                            Snum= 1
                            add_data = ("INSERT INTO Scraped "
                                        "(Snum, Source, Category, Find, Content) "
                                        "VALUES(%s, %s, %s, %s, %s) ")
            
                            data = (Snum,Source,'Hazard', sentence, checkS)
                            cursor.execute(add_data,data)
                            cnx.commit()
                            cursor.close()
                            cnx.close()
                        else:    
                            cursor.execute("SELECT Snum FROM Scraped ORDER BY Snum DESC LIMIT 1")
                            Unique =cursor.fetchone()   
                            add_data = ("INSERT INTO Scraped "
                                        "(Snum, Source, Category, Find, Content) "
                                        "VALUES(%s, %s, %s, %s, %s) ")
                            data = (Unique[0]+1,Source,'Hazard', sentence,  checkS)
                            cursor.execute(add_data,data)
                            cnx.commit()
                            cursor.close()
                            cnx.close()
                        i+=1
        x+=1

    if len(HStore) ==0:
        print("no info")

    else:
        ss = 0   
        while(ss != len(HStore)):
            storeni = HStore[ss]           
            print ('!!!',storeni,"----h")
            
            indices = [newrd for newrd, newes in enumerate(places) if newes in HStore[ss][0:100]]
            if indices:
                i=0
                while(i !=len(indices)):
                    sentences = places[indices[i]]
                    print sentences
            
                    parsed_uri = urlparse(finallinks[unum])
                    Source = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                    cnx = mysql.connector.connect(user='root', password='root',                              
                                              host='104.154.169.127',
                                              database='scrapedb')
                    cursor = cnx.cursor()
             
                    cursor.execute("SELECT count(*) FROM Scraped")
                    count=cursor.fetchone()
       
        
                    if count[0] == 0:
                        Snum= 1
                        add_data = ("INSERT INTO Scraped "
                                    "(Snum, Source, Category, Find, Content) "
                                    "VALUES(%s, %s, %s, %s, %s) ")
            
                        data = (Snum,Source,'Hazard', sentences, storeni)
                        cursor.execute(add_data,data)
                        cnx.commit()
                        cursor.close()
                        cnx.close()
                    else:    
                        cursor.execute("SELECT Snum FROM Scraped ORDER BY Snum DESC LIMIT 1")
                        Unique =cursor.fetchone()   
                        add_data = ("INSERT INTO Scraped "
                                    "(Snum, Source, Category, Find,  Content) "
                                    "VALUES(%s, %s, %s, %s, %s) ")
                        data = (Unique[0]+1,Source,'Hazard', sentences, storeni)
                        cursor.execute(add_data,data)
                        cnx.commit()
                        cursor.close()
                        cnx.close()
                    i+=1
                
            ss+=1
            
    mparagraph = soup.findAll('p')
    mi=0
    while(mi != len(mparagraph)):
        mpattern = r'\b({})\b'.format('|'.join(mineralterms)) 
        if re.search(mpattern, mparagraph[mi].get_text()):
            print mparagraph[mi].get_text()
            mstriped=mparagraph[mi].get_text()
            mstriped = re.sub('<[^>]*>', '', mstriped).replace('\n','')
            MStore.append(mstriped)
        mi+=1

    mx=0
    while(mx != len(MStore)):
        mstoreni = MStore[mx]           
        print ('!!!',mstoreni,"----m")
        
        mindices = [mnewrd for mnewrd, mnewes in enumerate(places) if mnewes in MStore[mx]]
        if mindices:
            mindktr=0
            while(mindktr !=len(mindices)):
                msentences = places[mindices[mindktr]]
                parsed_uri = urlparse(finallinks[unum])
                Source = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                cnx = mysql.connector.connect(user='root', password='root',                         
                                              host='104.154.169.127',
                                              database='scrapedb')
                cursor = cnx.cursor()
             
                cursor.execute("SELECT count(*) FROM Scraped")
                count=cursor.fetchone()
       
        
                if count[0] == 0:                    
                    Snum= 1
                    add_data = ("INSERT INTO Scraped "
                                "(Snum, Source, Category, Find, Content) "
                                "VALUES(%s, %s, %s, %s, %s) ")
            
                    data = (Snum,Source,'Mineralization', msentences, mstoreni)
                    cursor.execute(add_data,data)
                    cnx.commit()
                    cursor.close()
                    cnx.close()
                else:    
                    cursor.execute("SELECT Snum FROM Scraped ORDER BY Snum DESC LIMIT 1")
                    Unique =cursor.fetchone()   
                    add_data = ("INSERT INTO Scraped "
                                "(Snum, Source, Category, Find,  Content) "
                                "VALUES(%s, %s, %s, %s, %s) ")
                    data = (Unique[0]+1,Source,'Mineralization', msentences, mstoreni)
                    cursor.execute(add_data,data)
                    cnx.commit()
                    cursor.close()
                    cnx.close()
                mindktr+=1
        mx+=1

    lparagraphs = soup.findAll('p')
    li=0
    while(li != len(lparagraphs)):
        lpattern = r'\b({})\b'.format('|'.join(landformterms)) 
        if re.search(lpattern, lparagraphs[li].get_text()[0:100]):
            print lparagraphs[li].get_text()
            lstriped=lparagraphs[li].get_text()
            lstriped = re.sub('<[^>]*>', '', lstriped).replace('\n','')
            LStore.append(lstriped)
        li+=1
    lx=0
    while(lx != len(LStore)):
        lstoreni = LStore[lx]           
        print ('!!!',lstoreni,"----l")
        
        lindices = [lnewrd for lnewrd, lnewes in enumerate(places) if lnewes in LStore[lx]]
        if lindices:
            lindktr=0
            while(lindktr !=len(lindices)):
                lsentences = places[lindices[lindktr]]
                parsed_uri = urlparse(finallinks[unum])
                Source = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                cnx = mysql.connector.connect(user='root', password='root',                         
                                              host='104.154.169.127',
                                              database='scrapedb')
                cursor = cnx.cursor()
             
                cursor.execute("SELECT count(*) FROM Scraped")
                count=cursor.fetchone()
       
        
                if count[0] == 0:                    
                    Snum= 1
                    add_data = ("INSERT INTO Scraped "
                                "(Snum, Source, Category, Find, Content) "
                                "VALUES(%s, %s, %s, %s, %s) ")
            
                    data = (Snum,Source,'Landform', lsentences, lstorenis)
                    cursor.execute(add_data,data)
                    cnx.commit()
                    cursor.close()
                    cnx.close()
                else:    
                    cursor.execute("SELECT Snum FROM Scraped ORDER BY Snum DESC LIMIT 1")
                    Unique =cursor.fetchone()   
                    add_data = ("INSERT INTO Scraped "
                                "(Snum, Source, Category, Find,  Content) "
                                "VALUES(%s, %s, %s, %s, %s) ")
                    data = (Unique[0]+1,Source,'Landform', lsentences, lstoreni)
                    cursor.execute(add_data,data)
                    cnx.commit()
                    cursor.close()
                    cnx.close()
                lindktr+=1
        lx+=1
      
    unum+=1
    
downloadable = [".pdf",".docx",".ppt",".xls"] 
finallinks = ["http://www.mgb.gov.ph/","http://www.phivolcs.dost.gov.ph/","https://en.wikipedia.org/wiki/Mines_and_Geosciences_Bureau_Region_13_(Philippines)","http://www.brighthub.com/environment/science-environmental/articles/106153.aspx"]
dls = []
files =[]

cnx = mysql.connector.connect(user='root', password='root',
                                  host='104.154.169.127',
                                  database='scrapedb')
cursor = cnx.cursor()
cursor.execute("TRUNCATE TABLE Files")
cnx.commit()
cursor.close()
cnx.close()

unum=0
while unum<len(finallinks):
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    response = s.get(finallinks[unum])
    txt = response.content
    soup = BeautifulSoup(txt,"lxml")

    
    for tag in soup.findAll('a',href=True):
            print (tag['href'])
            tag['href'] = urljoin(finallinks[unum],tag['href'])
            if finallinks[unum] in tag['href'] and tag['href'] not in dls:            
                print (tag['href'])
                pattern = r'\b({})\b'.format('|'.join(downloadable)) 
                if re.search(pattern, tag['href']):                   
                    files.append(tag['href'])
    unum+=1
    
x=0
while(x!=len(files)):
    
    print "****",files[x].rsplit('/', 1)[-1]
    print "****",files[x].rsplit('/',1)[0]

    parsed_uri = urlparse(files[x])
    Source = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='104.154.169.127',
                                  database='scrapedb')
    cursor = cnx.cursor()   
    add_data = ("INSERT INTO Files "
                "(Source, Name, Link) "
                "VALUES(%s, %s, %s) ")
    data = (Source,files[x].rsplit('/', 1)[-1],files[x])
    cursor.execute(add_data,data)
    cnx.commit()
    cursor.close()
    cnx.close()

    
    x+=1
    
