# Generated by Django 3.2.9 on 2021-11-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_auto_20211125_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCcovernoteM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Via', models.CharField(blank=True, max_length=255, null=True)),
                ('IssueDate', models.DateField()),
                ('CoverNoteNumber', models.CharField(blank=True, max_length=255, null=True)),
                ('AddnNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Bank', models.CharField(blank=True, max_length=255, null=True)),
                ('Party', models.CharField(blank=True, max_length=255, null=True)),
                ('Addressinfull', models.CharField(blank=True, max_length=255, null=True)),
                ('Item', models.CharField(blank=True, max_length=255, null=True)),
                ('FC', models.CharField(blank=True, max_length=255, null=True)),
                ('LCValue', models.CharField(blank=True, max_length=255, null=True)),
                ('ConvRate', models.CharField(blank=True, max_length=255, null=True)),
                ('Calc', models.CharField(blank=True, max_length=255, null=True)),
                ('PrintExtra', models.CharField(blank=True, max_length=255, null=True)),
                ('BDT', models.CharField(blank=True, max_length=255, null=True)),
                ('ModCalc', models.CharField(blank=True, max_length=255, null=True)),
                ('ByForPrint', models.CharField(blank=True, max_length=255, null=True)),
                ('Inv', models.CharField(blank=True, max_length=255, null=True)),
                ('gap', models.CharField(blank=True, max_length=255, null=True)),
                ('From', models.CharField(blank=True, max_length=255, null=True)),
                ('To', models.CharField(blank=True, max_length=255, null=True)),
                ('ICC', models.CharField(blank=True, max_length=255, null=True)),
                ('Rate', models.CharField(blank=True, max_length=255, null=True)),
                ('war', models.CharField(blank=True, max_length=255, null=True)),
                ('WarSRCC', models.CharField(blank=True, max_length=255, null=True)),
                ('LessforCalc', models.CharField(blank=True, max_length=255, null=True)),
                ('Print', models.CharField(blank=True, max_length=255, null=True)),
                ('VAT', models.CharField(blank=True, max_length=255, null=True)),
                ('MR', models.CharField(blank=True, max_length=255, null=True)),
                ('Security', models.CharField(blank=True, max_length=255, null=True)),
                ('Ref', models.CharField(blank=True, max_length=255, null=True)),
                ('gap1', models.CharField(blank=True, max_length=255, null=True)),
                ('gap2', models.CharField(blank=True, max_length=255, null=True)),
                ('Gross', models.CharField(blank=True, max_length=255, null=True)),
                ('Consignee', models.CharField(blank=True, max_length=255, null=True)),
                ('NotifyParty', models.CharField(blank=True, max_length=255, null=True)),
                ('CEMISAgent', models.CharField(blank=True, max_length=255, null=True)),
                ('Net', models.CharField(blank=True, max_length=255, null=True)),
                ('WS', models.CharField(blank=True, max_length=255, null=True)),
                ('VATs', models.CharField(blank=True, max_length=255, null=True)),
                ('SD', models.CharField(blank=True, max_length=255, null=True)),
                ('Grs', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='companyinformation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mrcreate',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
