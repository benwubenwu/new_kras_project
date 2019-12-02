# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Colon(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    gene_symbol = models.TextField(
        db_column='Gene Symbol', blank=True, null=True)
    control1 = models.DecimalField(
        blank=True, null=True, decimal_places=5, max_digits=10)
    control2 = models.DecimalField(
        blank=True, null=True, decimal_places=5, max_digits=10)
    control3 = models.DecimalField(
        blank=True, null=True, decimal_places=5, max_digits=10)
    control4 = models.DecimalField(
        blank=True, null=True, decimal_places=5, max_digits=10)
    control5 = models.DecimalField(
        blank=True, null=True, decimal_places=5, max_digits=10)
    # Field name made lowercase.
    kras1 = models.DecimalField(
        db_column='KRAS1', blank=True, null=True, decimal_places=5, max_digits=10)
    # Field name made lowercase.
    kras2 = models.DecimalField(
        db_column='KRAS2', blank=True, null=True, decimal_places=5, max_digits=10)
    # Field name made lowercase.
    kras3 = models.DecimalField(
        db_column='KRAS3', blank=True, null=True, decimal_places=5, max_digits=10)
    # Field name made lowercase.
    kras4 = models.DecimalField(
        db_column='KRAS4', blank=True, null=True, decimal_places=5, max_digits=10)
    # Field name made lowercase.
    kras5 = models.DecimalField(
        db_column='KRAS5', blank=True, null=True, decimal_places=5, max_digits=10)

    class Meta:
        managed = False
        db_table = 'colon'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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


class GraphsGene(models.Model):
    gene_symbol = models.CharField(max_length=100)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    control1 = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    control2 = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    control3 = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    control4 = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    control5 = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    kras1 = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    kras2 = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    kras3 = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    kras4 = models.DecimalField(max_digits=10, decimal_places=5)
    # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    kras5 = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'graphs_gene'


class SearchProtein(models.Model):
    protein_text = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'search_protein'
