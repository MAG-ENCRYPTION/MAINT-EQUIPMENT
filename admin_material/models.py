from django.db import models


class Anomalie(models.Model):
    codeAno = models.AutoField(db_column='codeAno', primary_key=True)  
    intitule = models.CharField(db_column='intitule', max_length=100)  
    gravite = models.CharField(db_column='gravite', max_length=100)  
    matriculeCS = models.ForeignKey('ChefSupervision', models.DO_NOTHING, db_column='matriculeCS')


class ChefSupervision(models.Model):
    matriculeCS = models.AutoField(db_column='matriculeCS', primary_key=True)  
    nomCS = models.CharField(db_column='nomCS', max_length=100)  
    passwordCS = models.CharField(db_column='passwordCS', max_length=100)
    roleCS = models.CharField(db_column='roleCS', max_length=100)


class DemandeIntervention(models.Model):
    idDemande = models.AutoField(db_column='idDemande', primary_key=True)  
    codeAno = models.ForeignKey('ChefSupervision', models.DO_NOTHING, db_column='codeAno')  
    dateEmission = models.DateTimeField(db_column='dateEmission')  
    importance = models.CharField(db_column='importance', max_length=100)  
    matriculeCI = models.ForeignKey('ChefIntervention', models.DO_NOTHING, db_column='matriculeCI')
    codeEquipement = models.ForeignKey('Equipement',models.DO_NOTHING ,db_column='codeEquipement')


class ChefIntervention(models.Model):
    matriculeCI = models.AutoField(db_column='matriculeCI', primary_key=True)  
    nomCI = models.CharField(db_column='nomCI', max_length=100)  
    passwordCI = models.CharField(db_column='passwordCI', max_length=100)
    roleCI = models.CharField(db_column='roleCI', max_length=100)



class Equipement(models.Model):
    codeEquipement = models.AutoField(db_column='codeEquipement', primary_key=True) 
    nomEquipement = models.CharField(db_column='nomEquipement', max_length=100)
    matRespoEntretien = models.ForeignKey('Technicien',models.DO_NOTHING ,db_column='matriculeTechnicien')
    site = models.CharField(db_column='site', max_length=100)


class Capteur(models.Model):
    codeCapteur = models.AutoField(db_column='codeCapteur', primary_key=True) 
    nomCapteur = models.CharField(db_column='nomCapteur', max_length=100)
    typeCapteur = models.CharField(db_column='typeCapteur', max_length=100)
    codeEquipement = models.ForeignKey('Equipement',on_delete=models.CASCADE ,db_column='codeEquipement')



class Technicien(models.Model):
    matriculeTechnicien = models.AutoField(db_column='matriculeTechnicien', primary_key=True)  
    nomTechnicien = models.CharField(db_column='nomTechnicien', max_length=100)  
    passwordTechnicien = models.CharField(db_column='passwordTechnicien', max_length=100)
    roleTechnicien = models.CharField(db_column='roleTechnicien', max_length=100)



class RapportMaintenace(models.Model):
    idRapport = models.AutoField(db_column='idRapport', primary_key=True)  
    libelle = models.CharField(db_column='libelle', max_length=100)  
    dateMaintenance = models.DateTimeField(db_column='dateMaintenance')  
    matriculeTechnicien = models.ForeignKey('Technicien', models.DO_NOTHING, db_column='matriculeTechnicien')
    codeEquipement = models.ForeignKey('Equipement',models.DO_NOTHING ,db_column='codeEquipement')
    validite = models.BooleanField(db_column='validite', default=False)


class ChefAmenagement(models.Model):
    matriculeCA = models.AutoField(db_column='matriculeCA', primary_key=True)  
    nomCA = models.CharField(db_column='nomCA', max_length=100)  
    passwordCA = models.CharField(db_column='passwordCA', max_length=100)
    roleCA = models.CharField(db_column='roleCA', max_length=100)

