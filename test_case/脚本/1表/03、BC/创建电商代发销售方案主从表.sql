--�������̴������۷�������BC_SalProgramme
if object_id(N'BC_SalProgramme',N'U') is not null
print '����BC_SalProgramme�������۷�������'
else 
CREATE TABLE dbo.BC_SalProgramme  
   (CompanyID T_ComCODE NOT NULL,  
    BillNo T_BillNo NOT NULL,  
	SalProgramCode NVARCHAR(40) NOT NULL,
	Signature VARCHAR(20) DEFAULT NULL,
	ProjectName NVARCHAR(500) NOT NULL,
    BillTypeID T_BillType NOT NULL,  
    BillDate DATETIME NOT NULL,
	BillStatus INT NOT NULL,
	ExecutionState INT NOT NULL,
	Operator T_ID NULL,
	--OperatorName   --����Ա
	StartDate DATETIME NULL,
	EndDate DATETIME NULL,
	Checker NVARCHAR(20) NULL,
	CheckDate DATETIME NULL,
	--CheckerName   --�����
	UnChecker T_Name_S NULL,--�������ID
	--UnCheckerName --�������
	UnCheckDate SMALLDATETIME NULL,
	ShopID T_ID NULL,
	AddDTM DATETIME default getdate(),
	ModifyDTM DATETIME NULL,
    Remark NVARCHAR(250) NULL,
	primary key  (CompanyID,BillNo)
	)  
GO  
--�������̴������۷�����Ʒ��BC_SalProgrammeShop
if object_id(N'BC_SalProgrammeShop',N'U') is not null
print '����BC_SalProgrammeShop���̱�'
else 
CREATE TABLE dbo.BC_SalProgrammeShop  
   (CompanyID VARCHAR(10) NOT NULL,  
	BillNo T_BillNo NOT NULL,
	Sequence VARCHAR(20) NOT NULL, 
	ShopID VARCHAR(20) NOT NULL,
	ShopCode VARCHAR(20) NULL,--���̴���
	ShopName VARCHAR(20) NULL,--��������
	OnlineTypeName VARCHAR(20) NULL,--ƽ̨����
	AddDTM DATETIME default getdate(),
    OnlineType INT NULL,
	Remark NVARCHAR(1000) NULL
	primary key  (CompanyID,BillNo,Sequence)
	)  
GO  
--�������̴������۷��������ű�BC_SalProgrammeGoodsNumber
if object_id(N'BC_SalProgrammeGoodsNumber',N'U') is not null
print '����BC_SalProgrammeGoodsNumber���ű�'
else 
CREATE TABLE dbo.BC_SalProgrammeGoodsNumber  
   (CompanyID VARCHAR(10) NOT NULL,  
    BillNo T_BillNo NOT NULL,   
	Sequence VARCHAR(10) NOT NULL,
	MaterialID VARCHAR(20) NULL,
	MaterialCode VARCHAR(20) NULL,
	CardName VARCHAR(20) NULL,--Ʒ��
	KindName VARCHAR(20) NULL,--���
	YearNo VARCHAR(20) NULL,--���
	SeasonName VARCHAR(20) NULL,--����
	RetailPrice T_Numeric6 NULL,--���ۼ�

	--����4���ֶ����ڻ��ŵڶ���ѡ��
	MaterialShortName Nvarchar(max) null,--��Ʒ���
	PromotionID varchar(20) null,
	Discount numeric(24,6) null,
	Qty bigint null,

	Price T_Numeric6 NULL,
	DiscountPrice T_Numeric6 NULL,
	AddDTM DATETIME default getdate(),
	IsAdjustPrice BIT NULL,
	IsAdjustDiscountPrice BIT NULL,
	Remark NVARCHAR(1000) NULL
	primary key  (CompanyID,BillNo,Sequence)
	)  
GO  
--�������̴������۷�����Ʒ��BC_SalProgrammeGoods
if object_id(N'BC_SalProgrammeGoods',N'U') is not null
print '����BC_SalProgrammeGoods��Ʒ��'
else 
CREATE TABLE dbo.BC_SalProgrammeGoods  
   (CompanyID VARCHAR(10) NOT NULL,  
    BillNo T_BillNo NOT NULL, 
	Sequence VARCHAR(10) NOT NULL,
	MaterialID VARCHAR(20) NULL,
	MaterialCode VARCHAR(20) NULL,
	MaterialWhere NVARCHAR(max) NULL,
	MaterialWhereDesc NVARCHAR(max) NULL,--��Ʒ����
	RetailPrice T_Numeric6 NULL,--���ۼ۸�
	Price T_Numeric6 NULL,
	DiscountPrice T_Numeric6 NULL,
	IsAdjustPrice BIT NULL,
	IsAdjustDiscountPrice BIT NULL,
	AddDTM DATETIME default getdate(),
	Remark NVARCHAR(1000) NULL
	primary key  (CompanyID,BillNo,Sequence)
	)  
GO  



























