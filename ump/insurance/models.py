from django.db import models


class CompanyInformation(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255,null=True,blank=True)
    Address=models.TextField(null=True,blank=True)
    Phone=models.CharField(max_length=100,null=True,blank=True)
    Fax=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Web=models.CharField(max_length=100,null=True,blank=True)
    Bin=models.CharField(max_length=255,null=True,blank=True)
    Logo=models.ImageField(upload_to='logo',null=True,blank=True)
    objects=models.Manager()


    def __str__(self):
        return self.Name


class Mrcreate(models.Model):
    id = models.AutoField(primary_key=True)
    Branch_name=models.CharField(max_length=255,null=True,blank=True)
    Mr_No=models.CharField(max_length=255,null=True,blank=True)
    Class=models.CharField(max_length=100,null=True,blank=True)
    Doc_No=models.CharField(max_length=255,null=True,blank=True)
    Date = models.DateField(null=True, blank=True)
    Insured_Name=models.CharField(max_length=1500,null=True,blank=True)
    Insured_Address=models.CharField(max_length=1500,null=True,blank=True)
    Bank_Name=models.CharField(max_length=1500,null=True,blank=True)
    Bank_Address=models.CharField(max_length=1500,null=True,blank=True)
    Premium=models.CharField(max_length=255,null=True,blank=True)
    Vat=models.CharField(max_length=255,null=True,blank=True)
    Stamp=models.CharField(max_length=255,null=True,blank=True)
    ServiceCharge=models.CharField(max_length=255,null=True,blank=True)
    CoIns_Net=models.CharField(max_length=255,null=True,blank=True)
    Other=models.CharField(max_length=255,null=True,blank=True)
    Total_amount=models.CharField(max_length=255,null=True,blank=True)
    Mode_Of_Payment=models.CharField(max_length=255,null=True,blank=True)
    inword=models.CharField(max_length=1000,null=True,blank=True)
    objects=models.Manager()




    def __str__(self):
        return self.Mr_No


class MCcovernoteM(models.Model):
    id = models.AutoField(primary_key=True)
    Via=models.CharField(max_length=255,null=True,blank=True)
    IssueDate=models.DateField()
    CoverNoteNumber=models.CharField(max_length=255,null=True,blank=True)
    AddnNo=models.CharField(max_length=255,null=True,blank=True)
    Bank=models.CharField(max_length=255,null=True,blank=True)
    Print=models.CharField(max_length=255,null=True,blank=True)
    Party=models.CharField(max_length=255,null=True,blank=True)
    Addressinfull =models.CharField(max_length=255,null=True,blank=True)
    Item =models.CharField(max_length=255,null=True,blank=True)
    FC =models.CharField(max_length=255,null=True,blank=True)
    LCValue =models.CharField(max_length=255,null=True,blank=True)
    ConvRate =models.CharField(max_length=255,null=True,blank=True)
    Calc =models.CharField(max_length=255,null=True,blank=True)
    PrintExtra =models.CharField(max_length=255,null=True,blank=True)
    BDT =models.CharField(max_length=255,null=True,blank=True)
    ModCalc =models.CharField(max_length=255,null=True,blank=True)
    ByForPrint =models.CharField(max_length=255,null=True,blank=True)
    Inv =models.CharField(max_length=255,null=True,blank=True)
    gap =models.CharField(max_length=255,null=True,blank=True)
    From =models.CharField(max_length=255,null=True,blank=True)
    To =models.CharField(max_length=255,null=True,blank=True)
    ICC =models.CharField(max_length=255,null=True,blank=True)
    Rate =models.CharField(max_length=255,null=True,blank=True)
    war =models.CharField(max_length=255,null=True,blank=True)
    WarSRCC =models.CharField(max_length=255,null=True,blank=True)
    LessforCalc =models.CharField(max_length=255,null=True,blank=True)
    Prints =models.CharField(max_length=255,null=True,blank=True)
    VAT =models.CharField(max_length=255,null=True,blank=True)
    MR =models.CharField(max_length=255,null=True,blank=True)
    Security =models.CharField(max_length=255,null=True,blank=True)
    Ref =models.CharField(max_length=255,null=True,blank=True)
    gap1 =models.CharField(max_length=255,null=True,blank=True)
    gap2 =models.CharField(max_length=255,null=True,blank=True)
    Gross =models.CharField(max_length=255,null=True,blank=True)
    Consignee =models.CharField(max_length=255,null=True,blank=True)
    NotifyParty =models.CharField(max_length=255,null=True,blank=True)
    CEMISAgent =models.CharField(max_length=255,null=True,blank=True)
    Net =models.CharField(max_length=255,null=True,blank=True)
    WS =models.CharField(max_length=255,null=True,blank=True)
    VATs =models.CharField(max_length=255,null=True,blank=True)
    SD =models.CharField(max_length=255,null=True,blank=True)
    Grs =models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()


    def __str__(self):
        return self.MR








