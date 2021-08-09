from textacy.spacier import utils
import spacy
import re
import textacy
nlp = spacy.load(r"C:\Users\vadde2\Desktop\Jobb Ai\sv_pipeline-0.0.0\sv_pipeline\sv_pipeline-0.0.0")
inp = input("Skriv din mening: ")
doc = nlp(inp+".")
counts_dict = doc.count_by(spacy.attrs.IDS['POS'])
Det_Noun_Adv2 = [{"POS": "DET", "OP": "*"}, {"POS": "NOUN", "OP": "*"}, {"POS": "ADV", "OP": "*"}] #Fusk fuinktion som är utnför for loopen under, så jag slipper göra om hela grejen.
Det_noun_adv2 = textacy.extract.token_matches(doc, Det_Noun_Adv2)
for Det_noun_advs in Det_noun_adv2:
    Det_noun_adv3 = (Det_noun_advs)
def tid():
    for words in sentence:
        if str(words) == "igår"or str(words) =="Igår" and str(sista) =="igår":
            fråga = str(Verb1)+" "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+'?'
            fråga2 = "Var "+str(Verb1)+" "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+'?'
            fråga3 = "Vad gjorde "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv3)+'?'
            print(fråga)
            print(fråga2)
            print(fråga3)
            break
        elif str(words) == "igår"or str(words) =="Igår" and str(sista) != "igår":
            fråga = str(Verb1)+" "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+" igår"+'?'
            fråga2 = "Var "+str(Verb1)+" "+str(Pron_cconj_propn)+" igår"+'?'
            fråga3 = "Vad gjorde "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+" igår"+'?'
            print(fråga)
            print(fråga2)
            print(fråga3)
            break
        elif str(words) == "imorgon"or str(words) =="Imorgon" and str(sista) == "imorgon":
            fråga = str(Verb1)+" "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+'?'
            fråga2 = "Var "+str(Verb1)+" "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+'?'
            fråga3 = "Vad gör "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv3)+'?'
            print(fråga)
            print(fråga2)
            print(fråga3)
            break
        elif str(words) == "imorgon"or str(words) =="Imorgon" and str(sista) != "imorgon":
            fråga = str(Verb1)+" "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+" imorgon"+'?'
            fråga2 = "Var "+str(Verb1)+" "+str(Pron_cconj_propn)+" imorgon"+'?'
            fråga3 = "Vad gör "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+" imorgon"+'?'
            print(fråga)
            print(fråga2)
            print(fråga3)
            break
def label_PRS():
    for pos, count in counts_dict.items():
        human_readable_tag = doc.vocab[pos].text
        if human_readable_tag == "NOUN" and count >=1:
            fråga = str(Verb1)+" "+str(Pron_cconj_propn)+" "+str(Det_noun_adv1)+'?'
            fråga2 = 'var är '+str(Pron_cconj_propn)+'?'
            fråga3 = 'vad är '+str(Det_noun_adv1)+'?'
            print(fråga)
            print(fråga2)
            print(fråga3)
            break
        else:
            fråga = str(Verb1)+" "+str(Pron_cconj_propn)+" "+str(Det_noun_adv1)+'?'
            fråga2 = 'var är '+str(Pron_cconj_propn)+'?'
            fråga3 = 'vem är '+str(Det_noun_adv1)+'?'
            print(fråga)
            print(fråga2)
            print(fråga3)
            break


for sentence in doc.sents:
    root = sentence.root
    for i in sentence.ents:
        if i.label_ == "TME":
            label = i.label_
            break
        else:
            label = i.label_
    for pos, count in counts_dict.items():
        human_readable_tag = doc.vocab[pos].text
        if (human_readable_tag == "PRON" and count >=1) and (human_readable_tag == "PROPN" and count >=1):
            label = "PRS"
            break
    try:
        label
    except NameError:
        label = "L"
    if label =="ORG":
        for ent in doc.ents:
            Pron_cconj_propn = str(ent.text)

    sista  = sentence[-2]
    näst = sentence[-3]
    tredje = sentence[-4]
    första = sentence[0]
    for words in sentence:
        if words.pos_=="PRON":
            Pron_Cconj_Propn = [{"POS": "PRON", "OP": "+"}, {"POS": "CCONJ", "OP": "*"}, {"POS": "PROPN", "OP": "*"}]
            break
        elif words.pos_=="PROPN":
            Pron_Cconj_Propn = [{"POS": "PROPN", "OP": "+"}, {"POS": "CCONJ", "OP": "*"}, {"POS": "PROPN", "OP": "*"}]
            break
        else:
            Pron_Cconj_Propn = [{"POS": "NOUN", "OP": "*"}, {"POS": "CCONJ", "OP": "*"}, {"POS": "PROPN", "OP": "*"}]
    Pron_cconj_propn1 = textacy.extract.token_matches(doc, Pron_Cconj_Propn)
    for Pron_cconj_propns in Pron_cconj_propn1:
        Pron_cconj_propn = (Pron_cconj_propns)
    for pos, count in counts_dict.items():
        human_readable_tag = doc.vocab[pos].text
        if (första.pos_ == "PRON" or första.pos_ == "PROPN")  and human_readable_tag == "PRON" and count >=2:
            Pron_cconj_propn = str(första)+" "+str(Pron_cconj_propn)
            break
    for pos, count in counts_dict.items():
        human_readable_tag = doc.vocab[pos].text
        if human_readable_tag == "NOUN" and count ==0:
            Det_noun_adv1 = ""
            break
    for words in sentence:
        if words.pos_ == "VERB":
            VERB = [{"POS": "VERB"}]
            break
        elif words.pos_ =="AUX":
            VERB = [{"POS": "AUX"}]
            break
    Verb = textacy.extract.token_matches(doc, VERB)
    for Verbs in Verb:
        Verb1 = (Verbs)
    for words in sentence:
        AUX = [{"POS": "AUX"}]
        Aux = textacy.extract.token_matches(doc, AUX)
        for Auxs in Aux:
            Aux1 = (Auxs)
    if sista.pos_ and näst.pos_ =="ADV":
        Det_Noun_Adv = [{"POS": "DET", "OP": "*"}, {"POS": "NOUN", "OP": "*"}, {"POS": "ADV", "OP": "+"}, {"POS": "ADV", "OP": "+"}]
    elif sista.pos_ =="ADV" and näst.pos_ =="NOUN" and tredje.pos_ == "DET":
        Det_Noun_Adv = [{"POS": "DET", "OP": "+"}, {"POS": "NOUN", "OP": "+"}, {"POS": "ADV", "OP": "+"}]
    elif sista.pos_ =="ADV" and näst.pos_ =="NOUN":
        Det_Noun_Adv = [{"POS": "DET", "OP": "*"}, {"POS": "NOUN", "OP": "+"}, {"POS": "ADV", "OP": "+"}]
    elif sista.pos_ =="ADV" and näst.pos_ !="NOUN":
        Det_Noun_Adv = [{"POS": "DET", "OP": "*"}, {"POS": "NOUN", "OP": "*"}, {"POS": "ADV", "OP": "+"}]
    elif sista.pos_ =="NOUN" and näst.pos_ =="DET":
        Det_Noun_Adv = [{"POS": "ADP", "OP": "*"}, {"POS": "DET", "OP": "+"}, {"POS": "NOUN", "OP": "+"}]
    elif sista.pos_ =="ADV" and näst.pos_ =="ADJ":
        Det_Noun_Adv = [{"POS": "ADP", "OP": "*"}, {"POS": "ADJ", "OP": "+"}, {"POS": "ADV", "OP": "+"}]
    elif sista.pos_ =="ADJ":
        Det_Noun_Adv = [{"POS": "ADP", "OP": "*"}, {"POS": "ADJ", "OP": "+"}]
    else:
        Det_Noun_Adv = [{"POS": "ADP", "OP": "*"}, {"POS": "DET", "OP": "*"}, {"POS": "NOUN", "OP": "+"}]
    Det_noun_adv = textacy.extract.token_matches(doc, Det_Noun_Adv)
    for Det_noun_advs in Det_noun_adv:
        Det_noun_adv1 = (Det_noun_advs)
    if Verb1.lemma_ == "vara":
        if label == "PRS":
            label_PRS()
        elif label == "TME":
            tid()
        else:
            if Verb1.lemma_[-1]=="a":
                Verb1=str(Verb1)+"r"
            fråga = str(Verb1)+" "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+'?'
            fråga2 = "Vad "+str(Verb1)+" "+str(Pron_cconj_propn)+'?'
            fråga3 = "Vad gör "+str(Pron_cconj_propn)+'?'
            print(fråga)
            print(fråga2)
            print(fråga3)
    elif Verb1.lemma_ =="gå":
        if label == "PRS":
            label_PRS()
        elif label == "TME":
            tid()

    else:
        if label == "TME":
            tid()
        elif label == "PRS":
            label_PRS()
        elif label =="ORG":
            for ents in doc.ents:
                fråga = str(ent.text)
                print(fråga)

        else:
            for words in sentence:
                if words.pos_ != "AUX":
                    fråga = str(Verb1)+" "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+'?'
                    fråga2 = "När "+str(Verb1)+" "+str(Pron_cconj_propn)+" "+str(Det_noun_adv1)+'?'
                    fråga3 = "Vad "+str(Verb1)+" "+str(Pron_cconj_propn)+'?'
                    print(fråga)
                    print(fråga2)
                    print(fråga3)
                    break
                else:
                    fråga = str(Aux1)+" "+str(Pron_cconj_propn)+" "+ str(Det_noun_adv1)+'?'
                    fråga2 = "Vilken"+str(Det_noun_adv3)+" "+str(Verb1)+" "+str(Pron_cconj_propn)+'?'
                    print(fråga)
                    print(fråga2)
