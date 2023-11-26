#OUVERTURE FICHIER et MISE DANS TABLEAU
def lecture_fichier_audios (): 
    with open('audios.txt', 'r') as fichier:
        lignes = fichier.readlines()
    tab_audios_tests = []

    for ligne in lignes:
        valeur = ligne.strip().split(',')
        tab_audios_tests.append(valeur)
    return tab_audios_tests
    

#RECUPERATION DU NUMERO DE L'AUDIO DE TEST
import re
def numero_audio(file_path_test): 
    lecture_fichier_audios()
    segments = file_path_test.split('\\')
    resultat = re.search(r'\((\d+)\)', segments[-1])
    if resultat:
        numero_str = resultat.group(1)
        numero = int(numero_str)
    else:
        numero = 1
    return numero

#RECUPERATION DES INFORMATIONS SUR L'AUDIO DE TEST
def info_audio (file_path_test):
    numero = numero_audio(file_path_test)
    mon_audio = lecture_fichier_audios()
    message = ""

    #Proprete de l'audio

    if int(mon_audio[numero][1])==1: 
        message = message + "Proprete : moyenne\n"
    if int(mon_audio[numero][1])==0:
        message = message + "Proprete : mauvaise\n"
    if int(mon_audio[numero][1])==2:
        message = message + "Proprete : bonne\n"

        
    #Urgence
    if int(mon_audio[numero][2])==1: 
        message = message + "Urgence : peu urgent\n"
    if int(mon_audio[numero][2])==0:
        message = message + "Urgence : pas urgent\n"
    if int(mon_audio[numero][2])==2:
        message = message + "Urgence : très urgent\n"

    
    #Coherence de l'audio
    if int(mon_audio[numero][3])==1:
        message = message + "Coherence : coherent\n"
    if int(mon_audio[numero][3])==0:
        message = message + "Coherence : incoherent\n"
        
    return message
       

#ESSAI 
file_path_test = r"C:\Users\Juliette\Documents\Enregistrements audio\Enregistrements courts pour le 16.11\Enregistrement (97).wav"
numero = numero_audio(file_path_test)
info_audio (file_path_test)