from textacy.spacier import utils
import spacy
import textacy
from spacy.attrs import ORTH
from collections import Counter
nlp = spacy.load(r"C:\Users\vadde2\Desktop\Jobb Ai\sv_pipeline-0.0.0\sv_pipeline\sv_pipeline-0.0.0")
inp = input("Skriv din mening: ")
doc = nlp(inp+".")
counts = Counter()
fråga=()
Verb = []
string,label = [],""

def ques_time(fraga):
    if len(sentence) > 10 and counts["VERB"]>=1:
        fråga1 =fraga+str(Verb1[0])+" "+str(max(Pron1))+" "+str(Noun1[0])+" "+str(sentence[3:])+"?"
        print(fråga1)
    elif len(sentence) >= 7 and counts["VERB"]==1 and counts["advmod"]>=1 and len(Object1)>1:
        fråga1 =str(Verb1[0])+" "+str(longest_Pron)+" "+str(Object1[0])+" "+str(Advmod1[0])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(longest_Pron)+" "+str(Object1[0])+"?"
        print(fråga1)
        print(fråga2)
    elif len(sentence) >= 7 and counts["VERB"]==1 and counts["NOUN"]>1 and len(Object1)<1:
        fråga1 =str(Verb1[0])+" "+str(max(Pron1))+" "+str(Noun1[0])+" "+str(sentence[4:])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(max(Pron1))+" "+str(Noun1[0])+" "+str(sentence[4:])+"?"
        print(fråga1)
        print(fråga2)
    elif len(Object1) > 1 and counts["advmod"]>=1:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Object1[1])+" "+str(Noun1[0])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Object1[1])+"?"
        print(fråga1)
        print(fråga2)
    elif len(Object1) > 1 and counts["advmod"]==0:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Object1[1])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Object1[1])+"?"
        print(fråga1)
        print(fråga2)
    elif (counts["PRON"] == 1 or counts["PROPN"] ==1) and counts["VERB"] == 1 and counts["NOUN"] ==0:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(max(Pron1))+"?"
        print(fråga1)
        print(fråga2)
    elif (counts["PRON"] == 1 or counts["PROPN"] ==1) and counts["VERB"] == 1 and counts["NOUN"] ==1:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Verb1[0])+"?"
        print(fråga1)
        print(fråga2)
    elif (counts["PRON"] == 1 or counts["PROPN"] ==1) and counts["VERB"] == 2 and counts["NOUN"] ==0:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Verb1[1])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Verb1[1])+"?"
        print(fråga1)
        print(fråga2)

def ques(fraga):
    if len(sentence) > 10:
        fråga1 =str(Verb1[0])+" "+str(Pron1[0])+" "+str(Noun1[0])+" "+str(sentence[6:])+"?"
        fråga2 =fraga
        print(fråga1)
        print(fråga2)
    elif len(sentence) >= 7 and counts["VERB"]==1 and counts["advmod"]>=1 and len(Object1)<1:
        fråga1 =str(Verb1[0])+" "+str(longest_Pron)+" "+str(Object1[0])+" "+str(Advmod1[0])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(longest_Pron)+" "+str(longest_Object)+"?"
        print(fråga1)
        print(fråga2)
    elif len(sentence) > 7 and counts["VERB"]==1 and counts["NOUN"]>1 and len(Object1)<1:
        fråga1 =str(Verb1[0])+" "+str(max(Pron1))+" "+str(Noun1[0])+" "+str(sentence[4:])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(max(Pron1))+" "+str(Noun1[0])+" "+str(sentence[4:])+"?"
        print(fråga1)
        print(fråga2)
    elif len(Object1) > 1 and counts["advmod"]>=1:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Advmod1[0])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(Object1[0])+" "+str(Advmod1[0])+"?"
        print(fråga1)
        print(fråga2)
    elif len(Object1) > 1 and counts["advmod"]==0:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Advmod1[0])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(Object1[0])+" "+str(Object1[1])+"?"
        print(fråga1)
        print(fråga2)
    elif (counts["PRON"] == 1 or counts["PROPN"] ==1) and counts["VERB"] == 1 and counts["NOUN"] ==0:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+"?"
        fråga2 = fraga+str(Verb1[0])
        print(fråga1)
        print(fråga2)
    elif (counts["PRON"] >= 1 or counts["PROPN"] >=1) and counts["VERB"] == 1 and counts["NOUN"] ==1:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+" "+str(Noun1[0])+"?"
        fråga2 = fraga+str(Verb1[0])+"?"
        print(fråga1)
        print(fråga2)
    elif (counts["PRON"] >= 1 or counts["PROPN"] >=1) and counts["VERB"] == 1 and counts["NOUN"] >=1 and counts["advmod"]>=1:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+" "+str(Noun1[0])+"?"
        fråga2 = fraga+str(Verb1[0])+"?"
        print(fråga1)
        print(fråga2)
    elif (counts["PRON"] == 1 or counts["PROPN"] ==1) and counts["VERB"] == 2 and counts["NOUN"] ==0:
        fråga1 = str(Verb1[0])+" "+str(max(Pron1))+" "+str(Object1[0])+" "+str(Verb1[1])+"?"
        fråga2 = fraga+str(Verb1[0])+" "+str(Object1[0])+" "+str(Verb1[1])+"?"
        print(fråga1)
        print(fråga2)




for sentence in doc.sents:
    root = sentence.root
    sista  = sentence[-2]
    näst = sentence[-3]
    första = sentence[0]
    for token in sentence:
        counts[token.pos_] += 1
    for token in sentence:
        counts[token.dep_] += 1
    for token in sentence.ents:
        counts[token.label_] += 1
    for words in sentence:
        if words.pos_ == "VERB":
            VERB = [{"POS": "VERB"}]
            break
        elif words.pos_ =="AUX":
            VERB = [{"POS": "AUX"}]
    Verb = textacy.extract.token_matches(sentence, VERB)
    Verb1 = [str(verb) for verb in Verb]
    for words in sentence:
        if words.pos_=="PRON":
            Pron_Cconj_Propn = [{"POS": "PRON", "OP": "+"}, {"POS": "CCONJ", "OP": "*"}, {"POS": "PROPN", "OP": "*"}]
            break
        elif words.pos_=="PROPN":
            Pron_Cconj_Propn = [{"POS": "PROPN", "OP": "+"}, {"POS": "CCONJ", "OP": "*"}, {"POS": "PROPN", "OP": "*"}]
            break
        else:
            Pron_Cconj_Propn = [{"POS": "NOUN", "OP": "*"}, {"POS": "CCONJ", "OP": "*"}, {"POS": "PROPN", "OP": "*"}]
    Pron_cconj_propn = textacy.extract.token_matches(sentence, Pron_Cconj_Propn)
    Pron1 = [str(pron) for pron in Pron_cconj_propn]
    Advmod = [{"DEP": "advmod"}]
    Advmod_ = textacy.extract.token_matches(sentence, Advmod)
    Advmod1 = [str(advmod) for advmod in Advmod_]


    if sista.pos_ and näst.pos_ =="ADV":
        Det_Noun_Adv = [{"POS": "DET", "OP": "*"}, {"POS": "NOUN", "OP": "*"}, {"POS": "ADV", "OP": "+"}, {"POS": "ADV", "OP": "+"}]
    elif sista.pos_ =="ADV" and näst.pos_ =="NOUN" and sentence[-4].pos_ == "DET":
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
    for words in sentence:
        if words.pos_ =="ADJ":
            Det_Noun_Adv = [{"POS": "ADP", "OP": "*"}, {"POS": "DET", "OP": "*"}, {"POS": "ADJ", "OP": "+"}]
            break
    Det_noun_adv = textacy.extract.token_matches(sentence, Det_Noun_Adv)
    Noun1 = [str(noun) for noun in Det_noun_adv]
    for words in sentence:
        if words.pos_ == "ADP" and counts["NOUN"] >=1:
            Object = [{"POS": "ADP", "OP": "+"}, {"POS": "NOUN", "OP": "+"},]
            break
        elif words.pos_ != "ADP":
            Object = [{"POS": "DET", "OP": "*"}, {"POS": "NOUN", "OP": "+"},]
    Object_ = textacy.extract.token_matches(sentence, Object)
    Object1 = [str(object) for object in Object_]
    #longest_Object = max(Object1, key=len)
    longest_Pron = max(Pron1, key=len)
    for ent in sentence.ents:
        label = ent.label_
        try:
            label
        except NameError:
            label = "L"
        if label == "PRS":
            for words in sentence:
                if words.pos_ == "PROPN" or str(words) in ["jag", "Vi", "han", "hon", "de"]:
                    ques("Vem ")
                    break
                elif str(words) in ["alla", "båda", "både"]:
                    ques("Vilka ")
                    break
        elif label == "TME":
            ques_time("När ")
            break
        else:
            ques("Vad ")
    for words in sentence:
        if str(words) in ["kan"]:
            ques("Kan "+str(Pron1[0])+" "+str(Verb1[0])+" "+str(Noun1[0])+"?")
            break
        elif words.pos_ == "PROPN" or str(words) in ["Jag", "Vi", "han", "hon", "de"]:
            ques("Vem ")
            break
        elif str(words) in ["alla", "båda", "både"]:
            ques("Vilka ")
            break
        elif str(words) in ["till", "på", "under", "brevid",]:
            ques("Var ")
            ques("Varför ")
            break
        elif words.pos_!="VERB":
            ques("var "+ str(Verb1[0])+" "+str(Pron1[0])+" "+str(Noun1[0])+"?")
            break
