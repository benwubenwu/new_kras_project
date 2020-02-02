# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllProteins(models.Model):
    id = models.IntegerField(primary_key=True)
    protein_id = models.TextField(blank=True, null=True)
    gene_symbol = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_proteins'


class ColonTumorPro(models.Model):
    id = models.IntegerField(primary_key=True)
    protein_id = models.TextField(blank=True, null=True)
    gene_symbol = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    number_of_peptides = models.IntegerField(blank=True, null=True)
    wt_1 = models.FloatField(blank=True, null=True)
    wt_2 = models.FloatField(blank=True, null=True)
    wt_3 = models.FloatField(blank=True, null=True)
    wt_4 = models.FloatField(blank=True, null=True)
    wt_5 = models.FloatField(blank=True, null=True)
    g12d_1 = models.FloatField(blank=True, null=True)
    g12d_2 = models.FloatField(blank=True, null=True)
    g12d_3 = models.FloatField(blank=True, null=True)
    g12d_4 = models.FloatField(blank=True, null=True)
    g12d_5 = models.FloatField(blank=True, null=True)
    average_norm_wt = models.FloatField(blank=True, null=True)
    average_norm_g12d = models.FloatField(blank=True, null=True)
    ratio_norm_g12d_norm_wt = models.FloatField(blank=True, null=True)
    p_value = models.FloatField(blank=True, null=True)
    boot_ratio = models.FloatField(blank=True, null=True)
    lower_ci = models.FloatField(blank=True, null=True)
    upper_ci = models.FloatField(blank=True, null=True)
    log_ratio = models.FloatField(blank=True, null=True)
    log_lower_ci_diff = models.FloatField(blank=True, null=True)
    log_upper_ci_diff = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colon_tumor_pro'


class PancreasTumorPro(models.Model):
    id = models.IntegerField(primary_key=True)
    protein_id = models.TextField(blank=True, null=True)
    gene_symbol = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    number_of_peptides = models.IntegerField(blank=True, null=True)
    wt_1 = models.FloatField(blank=True, null=True)
    wt_2 = models.FloatField(blank=True, null=True)
    wt_3 = models.FloatField(blank=True, null=True)
    wt_4 = models.FloatField(blank=True, null=True)
    wt_5 = models.FloatField(blank=True, null=True)
    wt_6 = models.FloatField(blank=True, null=True)
    g12d_1 = models.FloatField(blank=True, null=True)
    g12d_2 = models.FloatField(blank=True, null=True)
    g12d_3 = models.FloatField(blank=True, null=True)
    g12d_4 = models.FloatField(blank=True, null=True)
    g12d_5 = models.FloatField(blank=True, null=True)
    average_norm_wt = models.FloatField(blank=True, null=True)
    average_norm_g12d = models.FloatField(blank=True, null=True)
    ratio_norm_g12d_norm_wt = models.FloatField(blank=True, null=True)
    p_value = models.FloatField(blank=True, null=True)
    boot_ratio = models.FloatField(blank=True, null=True)
    lower_ci = models.FloatField(blank=True, null=True)
    upper_ci = models.FloatField(blank=True, null=True)
    log_ratio = models.FloatField(blank=True, null=True)
    log_lower_ci_diff = models.FloatField(blank=True, null=True)
    log_upper_ci_diff = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pancreas_tumor_pro'


class ScrapedColonPro(models.Model):
    id = models.IntegerField(primary_key=True)
    protein_id = models.TextField(blank=True, null=True)
    gene_symbol = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    number_of_peptides = models.IntegerField(blank=True, null=True)
    collapsed = models.TextField(blank=True, null=True)
    wt_1 = models.FloatField(blank=True, null=True)
    wt_2 = models.FloatField(blank=True, null=True)
    wt_3 = models.FloatField(blank=True, null=True)
    wt_4 = models.FloatField(blank=True, null=True)
    g12d_1 = models.FloatField(blank=True, null=True)
    g12d_2 = models.FloatField(blank=True, null=True)
    g12d_3 = models.FloatField(blank=True, null=True)
    g12d_4 = models.FloatField(blank=True, null=True)
    average_wt = models.FloatField(blank=True, null=True)
    average_g12d = models.FloatField(blank=True, null=True)
    ratio_average_g12d_average_wt = models.FloatField(blank=True, null=True)
    norm_wt_1 = models.FloatField(blank=True, null=True)
    norm_wt_2 = models.FloatField(blank=True, null=True)
    norm_wt_3 = models.FloatField(blank=True, null=True)
    norm_wt_4 = models.FloatField(blank=True, null=True)
    norm_g12d_1 = models.FloatField(blank=True, null=True)
    norm_g12d_2 = models.FloatField(blank=True, null=True)
    norm_g12d_3 = models.FloatField(blank=True, null=True)
    norm_g12d_4 = models.FloatField(blank=True, null=True)
    average_norm_wt = models.FloatField(blank=True, null=True)
    average_norm_g12d = models.FloatField(blank=True, null=True)
    ratio_norm_g12d_norm_wt = models.FloatField(blank=True, null=True)
    p_value = models.FloatField(blank=True, null=True)
    boot_ratio = models.FloatField(blank=True, null=True)
    lower_ci = models.FloatField(blank=True, null=True)
    upper_ci = models.FloatField(blank=True, null=True)
    log_ratio = models.FloatField(blank=True, null=True)
    log_lower_ci_diff = models.FloatField(blank=True, null=True)
    log_upper_ci_diff = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scraped_colon_pro'


class WholePancreasPro(models.Model):
    id = models.IntegerField(primary_key=True)
    gene_symbol = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    number_of_peptides = models.IntegerField(blank=True, null=True)
    wt_1 = models.FloatField(blank=True, null=True)
    wt_2 = models.FloatField(blank=True, null=True)
    wt_3 = models.FloatField(blank=True, null=True)
    wt_4 = models.FloatField(blank=True, null=True)
    g12d_1 = models.FloatField(blank=True, null=True)
    g12d_2 = models.FloatField(blank=True, null=True)
    g12d_3 = models.FloatField(blank=True, null=True)
    norm_wt_1 = models.FloatField(blank=True, null=True)
    norm_wt_2 = models.FloatField(blank=True, null=True)
    norm_wt_3 = models.FloatField(blank=True, null=True)
    norm_wt_4 = models.FloatField(blank=True, null=True)
    norm_g12d_1 = models.FloatField(blank=True, null=True)
    norm_g12d_2 = models.FloatField(blank=True, null=True)
    norm_g12d_3 = models.FloatField(blank=True, null=True)
    average_norm_wt = models.FloatField(blank=True, null=True)
    average_norm_g12d = models.FloatField(blank=True, null=True)
    ratio_norm_g12d_norm_wt = models.FloatField(blank=True, null=True)
    p_value = models.FloatField(blank=True, null=True)
    boot_ratio = models.FloatField(blank=True, null=True)
    lower_ci = models.FloatField(blank=True, null=True)
    upper_ci = models.FloatField(blank=True, null=True)
    log_ratio = models.FloatField(blank=True, null=True)
    log_lower_ci_diff = models.FloatField(blank=True, null=True)
    log_upper_ci_diff = models.FloatField(blank=True, null=True)
    protein_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'whole_pancreas_pro'
