# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Evenement(models.Model):
    id_e = models.AutoField(db_column='ID_E', primary_key=True)  # Field name made lowercase.
    id_o = models.IntegerField(db_column='ID_O')  # Field name made lowercase.
    intitule_e = models.CharField(db_column='INTITULE_E', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description_e = models.CharField(db_column='DESCRIPTION_E', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date_creation_e = models.DateField(db_column='DATE_CREATION_E', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evenement'


class Inscrire(models.Model):
    id_p = models.IntegerField(db_column='ID_P', primary_key=True)  # Field name made lowercase. The composite primary key (ID_P, ID_E) found, that is not supported. The first column is selected.
    id_e = models.IntegerField(db_column='ID_E')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscrire'
        unique_together = (('id_p', 'id_e'),)


class Organisateur(models.Model):
    id_o = models.AutoField(db_column='ID_O', primary_key=True)  # Field name made lowercase.
    nom_o = models.CharField(db_column='NOM_O', max_length=200, blank=True, null=True)  # Field name made lowercase.
    num_o = models.CharField(db_column='NUM_O', max_length=200, blank=True, null=True)  # Field name made lowercase.
    email_o = models.CharField(db_column='EMAIL_O', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mdp_o = models.CharField(db_column='MDP_O', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organisateur'


class Participant(models.Model):
    id_p = models.AutoField(db_column='ID_P', primary_key=True)  # Field name made lowercase.
    nom_p = models.CharField(db_column='NOM_P', max_length=200, blank=True, null=True)  # Field name made lowercase.
    num_p = models.CharField(db_column='NUM_P', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mdp_p = models.CharField(db_column='MDP_P', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email_p = models.CharField(db_column='EMAIL_P', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participant'
