from import_export import resources
from .models import *

class BookResource(resources.ModelResource):

    class Meta:
        model = CompanyInformation
        fields='id,Name,Address,Phone,Fax,Email,Web,Bin,Logo'



class MrResource(resources.ModelResource):

    class Meta:
        model = Mrcreate
        fields='id,Branch_name,Mr_No,Class,Doc_No,Date,Insured_Name,Insured_Address,Bank_Name,Bank_Address,Premium,Vat,' \
               'Stamp,ServiceCharge,Total_amount,Mode_Of_Payment,inword'


class MCcovernot(resources.ModelResource):
    class Mera:
        model = MCcovernoteM
        firlds='id ,Via,IssueDate,CoverNoteNumber,AddnNo,Bank,Print,Party,Addressinfull,Item ,FC ,LCValue ,ConvRate ,Calc ,PrintExtra ,BDT ,ModCalc ,ByForPrint ,Inv ,gap ,From ,To ,ICC ,Rate ,war ,WarSRCC ,LessforCalc ,Prints,VAT ,MR ,Security ,Ref ,gap1 ,gap2 ,Gross ,Consignee ,NotifyParty ,CEMISAgent ,Net ,WS ,VATs ,SD ,Grs'