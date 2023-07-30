from django.db import models
from django.contrib.auth.models import User

class Employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    adresse = models.CharField(max_length=200,default="not mentioned")
    # nuull true mean that the field is not required in the form and blank true mean that the field can be empty
    email = models.EmailField()
    role = models.CharField(max_length=100)  # Ajout de l'attribut 'role'
    etat = models.BooleanField(default=False)  # Ajout de l'attribut 'état'
  
    def __str__(self):
        return self.user.username
    

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100,default="")
    prenom=models.CharField(max_length=100,default="")
    adresse = models.CharField(max_length=200,default="not mentioned")
    email = models.EmailField()
   
    etat = models.BooleanField(default=False) 

    def __str__(self):
        return self.user.username

class Stagiaire(models.Model):
    employe = models.OneToOneField(Employe, on_delete=models.CASCADE,null=True,blank=True)
    encadrant = models.CharField(max_length=100,default="xx")  
    faculte = models.CharField(max_length=100)  
    specialite = models.CharField(max_length=100) 


    def __str__(self):
        return self.employe.user.username


class ResponsableRH(models.Model):
    employe = models.OneToOneField(Employe, on_delete=models.CASCADE)

    def __str__(self):
        return self.employe.user.username

class DevLogiciel(models.Model):
    employe = models.OneToOneField(Employe, on_delete=models.CASCADE)
    technologies_utilisees = models.CharField(max_length=100)  

    def __str__(self):
        return self.employe.user.username
    
