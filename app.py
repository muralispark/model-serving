import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model-dt.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_one_customer',methods=['POST'])
def predict_one_customer():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [int(x) for x in request.form.values()]
    int_features = [ x for x in request.form.values()]

    cust_no = int_features[0]

    final_features = [[0.0049546010503599,0.002202044911271,0.0033030673669066,0.0066061347338132,0.0066061347338132,0.3282881955219984,0.3319582703741168,0.3451705398417434,0.086980773995208,0.1915779072805848,0.2312147156834645,0.2873668609208772,0.4514192068105735,0.0187173817458042,0.0,0.0005505112278177,0.0220204491127109,0.0187173817458042,0.0159648256067154,0.4954601050359953,0.7217202196690999,0.7844784996403259,0.7151140849352866,0.7112605063405621,0.324251113184668,0.4205905780527783,0.987617142705084,0.5752842330695724,0.5962036597266477,0.685386478633127,0.8538429143453653,0.406827797357334,0.6237292211175364,0.7740187863117883,1.0000000000000002,0.8378780887386499,0.5609709411463103,0.7631920654980389,0.5312433348441506,0.5940016148153766,0.7448416912374464,0.6329044082478325,0.4112318871798761,0.3363623601966591,0.3528776970311922,0.3176449784508548,0.6721742091655004,0.4833488580240044,0.3203975345899437,0.510874419414893,0.3192965121343081,0.7409881126427219,0.3264531580959392,0.5439050930839593,0.4227926229640493,0.5262887337937906,0.2363528204764304,0.3796692434516572,0.5978551934101011,0.6650175632038693,0.6006077495491898,0.3512261633477389,0.680431877582767,0.4260956903309559,0.5791378116642968,0.6985987481007535,0.3361788564540532,0.2725030577697974,0.4101308647242405,0.3771001910551742,0.4062772861295162,0.883570520647525,0.7096089726571089,0.6727247203933181,0.3787517247386276,0.5158290204652529,0.0803746392613947,0.0275255613908886,0.0330306736690663,0.0374347634916085,0.0330306736690663,0.0297276063021597,0.0330306736690663,0.0275255613908886,0.0275255613908886,0.7107099951127444,0.6716236979376826,0.5031672622254442,0.3165439559952192,0.680431877582767,0.7206191972134643,0.4266462015587737,0.7497962922878063,0.7756703199952416,0.8224637743597523,0.3402159387913834,0.6132695077889987,0.5879459913093811,0.4767427232901911,0.8114535498033968,0.5114249306427108,0.4321513138369515,0.5257382225659728,0.4905055039856353,0.3815042808777165,0.2224065360383801,0.0616572575155905,0.0809251504892125,0.0792736168057592,0.0583541901486839,0.1167083802973678,0.0825766841726658,0.0682633922494038,0.1029455996019234,0.2411239177841844,0.0963394648681102,0.0600057238321372,0.2345177830503711,0.0693644147050393,0.0545006115539594,0.3594838317650055,0.377650702282992,0.341316961247019,0.1822192164076827,0.104046622057559,0.0930363975012035,0.091935375045568,0.329389217977634,0.2671814492342257,0.1029455996019234,0.086980773995208,0.1012940659184701,0.1090012231079189,0.091935375045568,0.0935869087290213,0.1145063353860967,0.0902838413621147,0.086980773995208,0.1090012231079189,0.1073496894244656,0.0897333301342969,0.1051476445131945,0.2868163496930596,0.1546936550167941,0.2356188055060067,0.1183599139808211,0.062758279971226,0.1012940659184701,0.0825766841726658,0.0968899760959279,0.0952384424124746,0.0979909985515635,0.0836777066283014,0.1012940659184701,0.0963394648681102,0.0941374199568391,0.176714104129505,0.1723100143069628,0.0693644147050393,0.1012940659184701,0.0732179932997637,0.0732179932997637,0.0704654371606749,0.067712881021586,0.0649603248824971,0.0605562350599549,0.0589047013765016,0.0583541901486839,0.0528490778705061,0.0522985666426883,0.0467934543645106,0.2813112374148818,0.2989275967050505,0.0721169708441282,0.2312147156834645,0.4117823984076939,0.0765210606666704,0.0759705494388526,0.0743190157553993,0.0732179932997637,0.0715664596163104,0.0693644147050393,0.0688139034772215,0.0710159483884926,0.4415100047098537,0.2411239177841844,0.0754200382110348,0.0803746392613947,0.0759705494388526,0.0825766841726658,0.0710159483884926,0.0649603248824971,0.0666118585659504,0.0682633922494038,0.0671623697937682,0.067712881021586,0.0715664596163104,0.0726674820719459,0.0660613473381327,0.0633087911990438,0.0644098136546794,0.1205619588920922,0.0897333301342969,0.0913848638177502,0.0787231055779414,0.0935869087290213,0.0941374199568391,0.079824128033577,0.4486666506714847,0.3793022359664453,0.0765210606666704,0.9292629525564,0.3225995795012147,0.074869526983217,0.0704654371606749,0.0704654371606749,0.2906699282877839,0.2862658384652418,0.0715664596163104,0.067712881021586,0.0699149259328571,0.0693644147050393,0.0693644147050393,0.0710159483884926,0.0710159483884926,0.0693644147050393,0.0682633922494038,0.0688139034772215,0.8285193978657478,1.0000000000000002,0.2851648160096062,0.0715664596163104,0.1464359865995275,0.0693644147050393,0.0754200382110348,0.0732179932997637,0.0721169708441282,0.0759705494388526,0.0688139034772215,0.0462429431366929,0.0704654371606749,0.0633087911990438,0.0611067462877727,0.0611067462877727,0.0594552126043194,0.0594552126043194,0.0985415097793813,0.0891828189064791,0.0616572575155905,0.0671623697937682,0.0682633922494038,0.0660613473381327,0.0671623697937682,0.0732179932997637,0.067712881021586,0.0600057238321372,0.0616572575155905,0.0616572575155905,0.0600057238321372,0.0583541901486839,0.0594552126043194,0.0572531676930483,0.0539501003261417,0.0533995890983239,0.0974404873237457,0.055601634009595,0.0561521452374128,0.0561521452374128,0.0578036789208661,0.0589047013765016,0.0611067462877727,0.0561521452374128,0.0500965217314173,0.8956817676595161,0.8780654083693473,0.6055623505995499,0.7063059052902022,0.4998641948585375,0.4657324987338357,0.4266462015587737,0.1315721834484476,0.0495460105035995,0.0495460105035995,0.0445914094532395,0.043490386997604,0.043490386997604,0.0451419206810573,0.0473439655923284,0.050647032959235,0.0511975441870528,0.0533995890983239,0.050647032959235,0.0511975441870528,0.0517480554148706,0.0236719827961642,0.0545006115539594,0.4530707404940268,0.2510331198849043,0.4271967127865915,0.3022306640719572,0.2389218728729133,0.4371059148873115,0.1067991781966478,0.1139558241582789]]
    #final_features = [np.array(int_features)]
    
    if cust_no == "12345":

        final_features = [[0.0049546010503599,0.002202044911271,0.0033030673669066,0.0066061347338132,0.0066061347338132,0.3282881955219984,0.3319582703741168,0.3451705398417434,0.086980773995208,0.1915779072805848,0.2312147156834645,0.2873668609208772,0.4514192068105735,0.0187173817458042,0.0,0.0005505112278177,0.0220204491127109,0.0187173817458042,0.0159648256067154,0.4954601050359953,0.7217202196690999,0.7844784996403259,0.7151140849352866,0.7112605063405621,0.324251113184668,0.4205905780527783,0.987617142705084,0.5752842330695724,0.5962036597266477,0.685386478633127,0.8538429143453653,0.406827797357334,0.6237292211175364,0.7740187863117883,1.0000000000000002,0.8378780887386499,0.5609709411463103,0.7631920654980389,0.5312433348441506,0.5940016148153766,0.7448416912374464,0.6329044082478325,0.4112318871798761,0.3363623601966591,0.3528776970311922,0.3176449784508548,0.6721742091655004,0.4833488580240044,0.3203975345899437,0.510874419414893,0.3192965121343081,0.7409881126427219,0.3264531580959392,0.5439050930839593,0.4227926229640493,0.5262887337937906,0.2363528204764304,0.3796692434516572,0.5978551934101011,0.6650175632038693,0.6006077495491898,0.3512261633477389,0.680431877582767,0.4260956903309559,0.5791378116642968,0.6985987481007535,0.3361788564540532,0.2725030577697974,0.4101308647242405,0.3771001910551742,0.4062772861295162,0.883570520647525,0.7096089726571089,0.6727247203933181,0.3787517247386276,0.5158290204652529,0.0803746392613947,0.0275255613908886,0.0330306736690663,0.0374347634916085,0.0330306736690663,0.0297276063021597,0.0330306736690663,0.0275255613908886,0.0275255613908886,0.7107099951127444,0.6716236979376826,0.5031672622254442,0.3165439559952192,0.680431877582767,0.7206191972134643,0.4266462015587737,0.7497962922878063,0.7756703199952416,0.8224637743597523,0.3402159387913834,0.6132695077889987,0.5879459913093811,0.4767427232901911,0.8114535498033968,0.5114249306427108,0.4321513138369515,0.5257382225659728,0.4905055039856353,0.3815042808777165,0.2224065360383801,0.0616572575155905,0.0809251504892125,0.0792736168057592,0.0583541901486839,0.1167083802973678,0.0825766841726658,0.0682633922494038,0.1029455996019234,0.2411239177841844,0.0963394648681102,0.0600057238321372,0.2345177830503711,0.0693644147050393,0.0545006115539594,0.3594838317650055,0.377650702282992,0.341316961247019,0.1822192164076827,0.104046622057559,0.0930363975012035,0.091935375045568,0.329389217977634,0.2671814492342257,0.1029455996019234,0.086980773995208,0.1012940659184701,0.1090012231079189,0.091935375045568,0.0935869087290213,0.1145063353860967,0.0902838413621147,0.086980773995208,0.1090012231079189,0.1073496894244656,0.0897333301342969,0.1051476445131945,0.2868163496930596,0.1546936550167941,0.2356188055060067,0.1183599139808211,0.062758279971226,0.1012940659184701,0.0825766841726658,0.0968899760959279,0.0952384424124746,0.0979909985515635,0.0836777066283014,0.1012940659184701,0.0963394648681102,0.0941374199568391,0.176714104129505,0.1723100143069628,0.0693644147050393,0.1012940659184701,0.0732179932997637,0.0732179932997637,0.0704654371606749,0.067712881021586,0.0649603248824971,0.0605562350599549,0.0589047013765016,0.0583541901486839,0.0528490778705061,0.0522985666426883,0.0467934543645106,0.2813112374148818,0.2989275967050505,0.0721169708441282,0.2312147156834645,0.4117823984076939,0.0765210606666704,0.0759705494388526,0.0743190157553993,0.0732179932997637,0.0715664596163104,0.0693644147050393,0.0688139034772215,0.0710159483884926,0.4415100047098537,0.2411239177841844,0.0754200382110348,0.0803746392613947,0.0759705494388526,0.0825766841726658,0.0710159483884926,0.0649603248824971,0.0666118585659504,0.0682633922494038,0.0671623697937682,0.067712881021586,0.0715664596163104,0.0726674820719459,0.0660613473381327,0.0633087911990438,0.0644098136546794,0.1205619588920922,0.0897333301342969,0.0913848638177502,0.0787231055779414,0.0935869087290213,0.0941374199568391,0.079824128033577,0.4486666506714847,0.3793022359664453,0.0765210606666704,0.9292629525564,0.3225995795012147,0.074869526983217,0.0704654371606749,0.0704654371606749,0.2906699282877839,0.2862658384652418,0.0715664596163104,0.067712881021586,0.0699149259328571,0.0693644147050393,0.0693644147050393,0.0710159483884926,0.0710159483884926,0.0693644147050393,0.0682633922494038,0.0688139034772215,0.8285193978657478,1.0000000000000002,0.2851648160096062,0.0715664596163104,0.1464359865995275,0.0693644147050393,0.0754200382110348,0.0732179932997637,0.0721169708441282,0.0759705494388526,0.0688139034772215,0.0462429431366929,0.0704654371606749,0.0633087911990438,0.0611067462877727,0.0611067462877727,0.0594552126043194,0.0594552126043194,0.0985415097793813,0.0891828189064791,0.0616572575155905,0.0671623697937682,0.0682633922494038,0.0660613473381327,0.0671623697937682,0.0732179932997637,0.067712881021586,0.0600057238321372,0.0616572575155905,0.0616572575155905,0.0600057238321372,0.0583541901486839,0.0594552126043194,0.0572531676930483,0.0539501003261417,0.0533995890983239,0.0974404873237457,0.055601634009595,0.0561521452374128,0.0561521452374128,0.0578036789208661,0.0589047013765016,0.0611067462877727,0.0561521452374128,0.0500965217314173,0.8956817676595161,0.8780654083693473,0.6055623505995499,0.7063059052902022,0.4998641948585375,0.4657324987338357,0.4266462015587737,0.1315721834484476,0.0495460105035995,0.0495460105035995,0.0445914094532395,0.043490386997604,0.043490386997604,0.0451419206810573,0.0473439655923284,0.050647032959235,0.0511975441870528,0.0533995890983239,0.050647032959235,0.0511975441870528,0.0517480554148706,0.0236719827961642,0.0545006115539594,0.4530707404940268,0.2510331198849043,0.4271967127865915,0.3022306640719572,0.2389218728729133,0.4371059148873115,0.1067991781966478,0.1139558241582789]]
    elif cust_no == "67895":

        final_features = [[0.0728310113900632,0.4273466697740473,0.2126022906018756,0.3732589333740738,0.1215635263642966,0.5076749911601465,0.2511598848672032,0.171099324552391,0.2607992834335351,0.3566577469542801,0.3156903030473695,0.1828808116890189,0.2741873369978849,0.2342909373761224,0.1536948549187363,0.4776857511760027,0.2942694173444097,0.1030880124454938,0.4161007047799934,0.2316133266632524,0.3079252319800466,0.1978754316810907,0.3456795430315131,0.3055153823384636,0.444751139407702,0.2511598848672032,0.2358975038038444,0.2956082227008447,0.3068541876948986,0.3419308880334952,0.6088886761066312,0.1470008281365614,0.0,0.3470183483879482,0.2190285563127635,0.2940016562731228,0.4792923176037247,0.6589599964372997,0.4364505461978052,0.176722307049418,0.1686894749108081,0.0996071185187628,0.1686894749108081,0.2155476623860326,0.3732589333740738,0.3494281980295312,0.3341658169661723,0.1255799424336016,0.3183679137602395,0.1965366263246558,0.3001601609127237,0.2375040702315664,0.3373789498216162,0.2634768941464051,0.3510347644572531,0.3079252319800466,0.3044443380533156,0.361477446237446,0.4418057676235452,0.176722307049418,0.1686894749108081,0.1105853224415297,0.3778108715859528,0.0771151885306551,0.4268111476314732,0.1191536767227137,0.2134055738157366,0.181542006332584,0.0811316045999601,0.3057831434097506,0.2267936273800864,0.3328270116097374,0.2527664512949251,0.1494106777781443,0.3941442969344596,0.2634768941464051,0.2375040702315664,0.2275969105939475,0.2051049806058397,0.4155651826374194,0.2034984141781177,0.3282750733978583,0.1611921649147722,0.3170291084038045,0.3314882062533023,0.1968043873959428,0.3170291084038045,0.3885213144374326,0.1922524491840638,0.2907885234176788,0.2803458416374859,0.2131378127444496,0.2388428755880013,0.0492680371168074,0.2755261423543199,0.3296138787542934,0.1585145542019022,0.263209133075118,0.1188859156514267,0.092377569594014,0.2190285563127635,0.2482145130830462,0.175383501692983,0.2120667684593016,0.1692249970533821,0.1087109949425207,0.1282575531464715,0.2024273698929697,0.27820375306719,0.3298816398255804,0.2198318395266245,0.2136733348870236,0.2174219898850415,0.0966617467346059,0.1654763420553641,0.1839518559741669,0.2051049806058397,0.1579790320593282,0.1668151474117991,0.0417707271207715,0.176990068120705,0.1914491659702028,0.1729736520514,0.1882360331147589,0.1387002349266645,0.1839518559741669,0.1692249970533821,0.1370936684989425,0.1906458827563418,0.1962688652533688,0.1649408199127902,0.1073721895860858,0.1494106777781443,0.2361652648751314,0.2037661752494047,0.1290608363603326,0.1654763420553641,0.2088536356038576,0.1041590567306418,0.1930557323979248,0.3384499941067642,0.2345586984474094,0.1954655820395078,0.181809767403871,0.1424488899246824,0.1748479795504091,0.2010885645365348,0.176722307049418,0.2053727416771267,0.1914491659702028,0.1427166509959694,0.4037836955007915,0.4099422001403924,0.1681539527682341,0.4021771290730696,0.2158154234573195,0.2765971866394679,0.1531593327761622,0.2262581052375125,0.1938590156117858,0.3280073123265714,0.4651009808255139,0.2433948137998803,0.3317559673245893,0.267761071286997,0.1432521731385434,0.2217061670256335,0.6300418007383041,0.3510347644572531,0.3486249148156701,0.3938765358631727,0.5170466286551912,0.5909486843304025,0.5877355514749585,0.6787743157125375,0.5633692939878417,0.5663146657719987,0.639681199304636,0.6659217842907615,0.5355221425739941,0.917349430229252,0.7692775578075425,0.721883848189744,0.7754360624471435,0.7810590449441704,0.537128709001716,1.0,0.7724906906629865,0.7738294960194214,0.6187958357442501,0.45653262654433,0.6163859861026671,0.266154504859275,0.4083356337126704,0.4581391929720519,0.8662070656134354,1.0,0.8554966227619557,0.6825229707105556,0.3858437037245628,0.4466254669067111,0.5805060025502096,0.5724731704115996,0.6474462703719589,0.9376992716470636,1.0,0.6121018089620752,0.7052826617699501,0.9406446434312208,0.8878957123876822,0.6849328203521384,0.9754535826985304,0.7566927874570536,0.7103701221244032,0.545429302211613,0.7660644249520986,0.7789169563738743,0.6423588100175058,0.5888065957601065,0.8030154527897042,0.5636370550591288,0.8429118524114666,0.5494457182809179,0.3534446140988361,0.3689747562334819,0.3981607130037646,0.5060684247324244,0.5095493186591554,0.4835764947443166,0.6038012157521784,0.5020520086631195,0.453051732617599,0.5917519675442634,0.7200095206907351,0.3863792258671367,0.266154504859275,0.9288631562945928,0.5941618171858464,0.9551037412807184,1.0,0.5189209561542003,0.3336302948235984,0.4096744390691055,0.4766147068908547,0.5055329025898504,0.4257401033463253,0.5491779572096309,0.5218663279383572,0.5491779572096309,0.545429302211613,0.5090137965165813,0.3055153823384636,0.3250619405424144,0.2873076294909478,0.3504992423146791,0.1962688652533688,0.1652085809840772,0.2203673616691985,0.2533019734374992,0.354515658383984,0.1951978209682208,0.2618703277186831,0.1957333431107948,0.2238482555959295,0.2310778045206784,0.2455369023701762,0.3247941794711274,0.5992492775402993,0.2179575120276156,0.2562473452216562,0.3494281980295312,0.1965366263246558,0.4396636790532491,0.1523560495623013,0.1261154645761756,0.2728485316414499,0.3478216316018091,0.3081929930513336,0.2203673616691985,0.2380395923741404,0.2519631680810642,0.1298641195741935,0.1006781628039109,0.274455098069172,0.178596634548427,0.2128700516731626,0.180203200976149,0.2077825913187097,0.3148870198335085,0.1700282802672431,0.2883786737760958,0.26749331021571,0.1978754316810907,0.1378969517128034,0.263209133075118,0.176186784906844,0.1890393163286198,0.2358975038038444,0.1427166509959694,0.2091213966751446,0.3462150651740872,0.269367637714719,0.0514101256871034,0.182613050617732]]
    else:
        print("customer not found!")
    

    prediction = model.predict(final_features)
    
   

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='PREDICTION IS {}'.format(output))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
