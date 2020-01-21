# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllPro(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    protein_id = models.TextField(
        db_column='Protein Id', blank=True, null=True)
    # Field name made lowercase.
    id = models.TextField(db_column='Id', blank=True,
                          null=False, primary_key=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    gene_symbol = models.TextField(
        db_column='Gene Symbol', blank=True, null=True)
    # Field name made lowercase.
    description = models.TextField(
        db_column='Description', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_pro'


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


class ColonData(models.Model):
    # Field name made lowercase.
    id = models.TextField(db_column='Id', blank=False,
                          null=False, primary_key=True)
    # Field name made lowercase.
    protein_id = models.TextField(
        db_column='Protein_Id', blank=True, null=True)
    # Field name made lowercase.
    gene_symbol = models.TextField(
        db_column='Gene_Symbol', blank=True, null=True)
    # Field name made lowercase.
    description = models.TextField(
        db_column='Description', blank=True, null=True)
    # Field name made lowercase.
    number_of_peptides = models.TextField(
        db_column='Number_of_peptides', blank=True, null=True)
    control1 = models.TextField(blank=True, null=True)
    control2 = models.TextField(blank=True, null=True)
    control3 = models.TextField(blank=True, null=True)
    control4 = models.TextField(blank=True, null=True)
    control5 = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    kras1 = models.TextField(db_column='KRAS1', blank=True, null=True)
    # Field name made lowercase.
    kras2 = models.TextField(db_column='KRAS2', blank=True, null=True)
    # Field name made lowercase.
    kras3 = models.TextField(db_column='KRAS3', blank=True, null=True)
    # Field name made lowercase.
    kras4 = models.TextField(db_column='KRAS4', blank=True, null=True)
    # Field name made lowercase.
    kras5 = models.TextField(db_column='KRAS5', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colon_data'


class ColonTumorPro(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    protein_id = models.TextField(
        db_column='Protein Id', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    gene_symbol = models.TextField(
        db_column='Gene Symbol', blank=True, null=True)
    # Field name made lowercase.
    description = models.TextField(
        db_column='Description', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_peptides = models.TextField(
        db_column='Number of peptides', blank=True, null=True)
    control1 = models.TextField(blank=True, null=True)
    control2 = models.TextField(blank=True, null=True)
    control3 = models.TextField(blank=True, null=True)
    control4 = models.TextField(blank=True, null=True)
    control5 = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    kras1 = models.TextField(db_column='KRAS1', blank=True, null=True)
    # Field name made lowercase.
    kras2 = models.TextField(db_column='KRAS2', blank=True, null=True)
    # Field name made lowercase.
    kras3 = models.TextField(db_column='KRAS3', blank=True, null=True)
    # Field name made lowercase.
    kras4 = models.TextField(db_column='KRAS4', blank=True, null=True)
    # Field name made lowercase.
    kras5 = models.TextField(db_column='KRAS5', blank=True, null=True)
    # Field name made lowercase.
    id = models.TextField(db_column='Id', blank=True,
                          null=False, primary_key=True)

    class Meta:
        managed = False
        db_table = 'colon_tumor_pro'


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


class DjangoPlotlyDashDashapp(models.Model):
    instance_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)
    base_state = models.TextField()
    creation = models.DateTimeField()
    update = models.DateTimeField()
    save_on_change = models.BooleanField()
    stateless_app = models.ForeignKey(
        'DjangoPlotlyDashStatelessapp', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_dashapp'


class DjangoPlotlyDashStatelessapp(models.Model):
    app_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_statelessapp'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PancreasTumorPro(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    protein_id = models.TextField(
        db_column='Protein Id', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    gene_symbol = models.TextField(
        db_column='Gene Symbol', blank=True, null=True)
    # Field name made lowercase.
    description = models.TextField(
        db_column='Description', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_peptides = models.TextField(
        db_column='Number of peptides', blank=True, null=True)
    # Field name made lowercase.
    pdx_1 = models.TextField(db_column='PDX_1', blank=True, null=True)
    # Field name made lowercase.
    pdx_2 = models.TextField(db_column='PDX_2', blank=True, null=True)
    # Field name made lowercase.
    pdx_3 = models.TextField(db_column='PDX_3', blank=True, null=True)
    # Field name made lowercase.
    pdxp53_1 = models.TextField(db_column='PDXp53_1', blank=True, null=True)
    # Field name made lowercase.
    pdxp53_2 = models.TextField(db_column='PDXp53_2', blank=True, null=True)
    # Field name made lowercase.
    pdxp53_3 = models.TextField(db_column='PDXp53_3', blank=True, null=True)
    # Field name made lowercase.
    d314 = models.TextField(db_column='D314', blank=True, null=True)
    # Field name made lowercase.
    d693 = models.TextField(db_column='D693', blank=True, null=True)
    # Field name made lowercase.
    d705 = models.TextField(db_column='D705', blank=True, null=True)
    # Field name made lowercase.
    d751 = models.TextField(db_column='D751', blank=True, null=True)
    # Field name made lowercase.
    d756 = models.TextField(db_column='D756', blank=True, null=True)
    # Field name made lowercase.
    id = models.TextField(db_column='Id', blank=True,
                          null=False, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pancreas_tumor_pro'


class ScrapedColonPro(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    protein_id = models.TextField(
        db_column='Protein Id', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    gene_symbol = models.TextField(
        db_column='Gene Symbol', blank=True, null=True)
    # Field name made lowercase.
    description = models.TextField(
        db_column='Description', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    group_id = models.TextField(db_column='Group ID', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_peptides = models.TextField(
        db_column='Number of peptides', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    collapsed_field = models.TextField(
        db_column='Collapsed?', blank=True, null=True)
    # Field name made lowercase.
    fabp_1 = models.TextField(db_column='FABP_1', blank=True, null=True)
    # Field name made lowercase.
    fabp_2 = models.TextField(db_column='FABP_2', blank=True, null=True)
    # Field name made lowercase.
    fabp_4 = models.TextField(db_column='FABP_4', blank=True, null=True)
    # Field name made lowercase.
    fabp_5 = models.TextField(db_column='FABP_5', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2171_g12d_1 = models.TextField(
        db_column='2171_G12D_1', blank=True, null=True)
    # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2172_g12d_2 = models.TextField(
        db_column='2172_G12D_2', blank=True, null=True)
    # Field name made lowercase.
    g12d_3 = models.TextField(db_column='G12D_3', blank=True, null=True)
    # Field name made lowercase.
    g12d_4 = models.TextField(db_column='G12D_4', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    average_fabp = models.TextField(
        db_column='Average FABP', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    average_g12d = models.TextField(
        db_column='Average G12D', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    average_g12d_average_fabp = models.TextField(
        db_column='Average G12D/Average FABP', blank=True, null=True)
    # Field name made lowercase.
    id = models.TextField(db_column='Id', blank=True,
                          null=False, primary_key=True)

    class Meta:
        managed = False
        db_table = 'scraped_colon_pro'


class SearchProtein(models.Model):
    protein_text = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'search_protein'


class WholePancreasPro(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    protein_id = models.TextField(
        db_column='Protein Id', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    gene_symbol = models.TextField(
        db_column='Gene Symbol', blank=True, null=True)
    # Field name made lowercase.
    description = models.TextField(
        db_column='Description', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_peptides = models.TextField(
        db_column='Number of peptides', blank=True, null=True)
    wt_1 = models.TextField(blank=True, null=True)
    wt_2 = models.TextField(blank=True, null=True)
    wt_3 = models.TextField(blank=True, null=True)
    wt_4 = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    g12d_1 = models.TextField(db_column='G12D_1', blank=True, null=True)
    # Field name made lowercase.
    g12d_2 = models.TextField(db_column='G12D_2', blank=True, null=True)
    # Field name made lowercase.
    g12d_3 = models.TextField(db_column='G12D_3', blank=True, null=True)
    # Field name made lowercase.
    id = models.TextField(db_column='Id', blank=True,
                          null=False, primary_key=True)

    class Meta:
        managed = False
        db_table = 'whole_pancreas_pro'


# def __str__(self):
#     return self.name
