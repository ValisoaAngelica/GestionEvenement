DROP DATABASE IF EXISTS evenement;

CREATE DATABASE IF NOT EXISTS evenement;
USE evenement;
# -----------------------------------------------------------------------------
#       TABLE : PARTICIPANT
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS PARTICIPANT
 (
   ID_P INTEGER NOT NULL AUTO_INCREMENT ,
   NOM_P CHAR (200) NULL  ,
   NUM_P CHAR (200) NULL  ,
   MDP_P CHAR (10) NULL  ,
   EMAIL_P CHAR (200) NULL  
   , PRIMARY KEY (ID_P) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       TABLE : EVENEMENT
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS EVENEMENT
 (
   ID_E INTEGER NOT NULL AUTO_INCREMENT ,
   ID_O INTEGER NOT NULL  ,
   INTITULE_E CHAR (200) NULL  ,
   DESCRIPTION_E CHAR (200) NULL  ,
   DATE_CREATION_E DATE NULL  
   , PRIMARY KEY (ID_E) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       INDEX DE LA TABLE EVENEMENT
# -----------------------------------------------------------------------------


CREATE  INDEX I_FK_EVENEMENT_ORGANISATEUR
     ON EVENEMENT (ID_O ASC);

# -----------------------------------------------------------------------------
#       TABLE : ORGANISATEUR
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS ORGANISATEUR
 (
   ID_O INTEGER NOT NULL AUTO_INCREMENT ,
   NOM_O CHAR (200) NULL  ,
   NUM_O CHAR (200) NULL  ,
   EMAIL_O CHAR (200) NULL  ,
   MDP_O CHAR (10) NULL  
   , PRIMARY KEY (ID_O) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       TABLE : INSCRIRE
# -----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS INSCRIRE
 (
   ID_P INTEGER NOT NULL  ,
   ID_E INTEGER NOT NULL  
   , PRIMARY KEY (ID_P,ID_E) 
 ) 
 comment = "";

# -----------------------------------------------------------------------------
#       INDEX DE LA TABLE INSCRIRE
# -----------------------------------------------------------------------------


CREATE  INDEX I_FK_INSCRIRE_PARTICIPANT
     ON INSCRIRE (ID_P ASC);

CREATE  INDEX I_FK_INSCRIRE_EVENEMENT
     ON INSCRIRE (ID_E ASC);


# -----------------------------------------------------------------------------
#       CREATION DES REFERENCES DE TABLE
# -----------------------------------------------------------------------------


ALTER TABLE EVENEMENT 
  ADD FOREIGN KEY FK_EVENEMENT_ORGANISATEUR (ID_O)
      REFERENCES ORGANISATEUR (ID_O) ;


ALTER TABLE INSCRIRE 
  ADD FOREIGN KEY FK_INSCRIRE_PARTICIPANT (ID_P)
      REFERENCES PARTICIPANT (ID_P) ;


ALTER TABLE INSCRIRE 
  ADD FOREIGN KEY FK_INSCRIRE_EVENEMENT (ID_E)
      REFERENCES EVENEMENT (ID_E) ;

