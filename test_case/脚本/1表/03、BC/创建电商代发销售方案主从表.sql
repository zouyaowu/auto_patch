--创建电商代发销售方案主表BC_SalProgramme
if object_id(N'BC_SalProgramme',N'U') is not null
print '存在BC_SalProgramme代发销售方案主表'
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
	--OperatorName   --操作员
	StartDate DATETIME NULL,
	EndDate DATETIME NULL,
	Checker NVARCHAR(20) NULL,
	CheckDate DATETIME NULL,
	--CheckerName   --审核人
	UnChecker T_Name_S NULL,--反审核人ID
	--UnCheckerName --反审核人
	UnCheckDate SMALLDATETIME NULL,
	ShopID T_ID NULL,
	AddDTM DATETIME default getdate(),
	ModifyDTM DATETIME NULL,
    Remark NVARCHAR(250) NULL,
	primary key  (CompanyID,BillNo)
	)  
GO  
--创建电商代发销售方案商品表BC_SalProgrammeShop
if object_id(N'BC_SalProgrammeShop',N'U') is not null
print '存在BC_SalProgrammeShop店铺表'
else 
CREATE TABLE dbo.BC_SalProgrammeShop  
   (CompanyID VARCHAR(10) NOT NULL,  
	BillNo T_BillNo NOT NULL,
	Sequence VARCHAR(20) NOT NULL, 
	ShopID VARCHAR(20) NOT NULL,
	ShopCode VARCHAR(20) NULL,--店铺代码
	ShopName VARCHAR(20) NULL,--店铺名称
	OnlineTypeName VARCHAR(20) NULL,--平台类型
	AddDTM DATETIME default getdate(),
    OnlineType INT NULL,
	Remark NVARCHAR(1000) NULL
	primary key  (CompanyID,BillNo,Sequence)
	)  
GO  
--创建电商代发销售方案主货号表BC_SalProgrammeGoodsNumber
if object_id(N'BC_SalProgrammeGoodsNumber',N'U') is not null
print '存在BC_SalProgrammeGoodsNumber货号表'
else 
CREATE TABLE dbo.BC_SalProgrammeGoodsNumber  
   (CompanyID VARCHAR(10) NOT NULL,  
    BillNo T_BillNo NOT NULL,   
	Sequence VARCHAR(10) NOT NULL,
	MaterialID VARCHAR(20) NULL,
	MaterialCode VARCHAR(20) NULL,
	CardName VARCHAR(20) NULL,--品牌
	KindName VARCHAR(20) NULL,--类别
	YearNo VARCHAR(20) NULL,--年份
	SeasonName VARCHAR(20) NULL,--季节
	RetailPrice T_Numeric6 NULL,--零售价

	--新增4个字段用于货号第二次选择
	MaterialShortName Nvarchar(max) null,--货品简称
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
--创建电商代发销售方案货品表BC_SalProgrammeGoods
if object_id(N'BC_SalProgrammeGoods',N'U') is not null
print '存在BC_SalProgrammeGoods货品表'
else 
CREATE TABLE dbo.BC_SalProgrammeGoods  
   (CompanyID VARCHAR(10) NOT NULL,  
    BillNo T_BillNo NOT NULL, 
	Sequence VARCHAR(10) NOT NULL,
	MaterialID VARCHAR(20) NULL,
	MaterialCode VARCHAR(20) NULL,
	MaterialWhere NVARCHAR(max) NULL,
	MaterialWhereDesc NVARCHAR(max) NULL,--货品条件
	RetailPrice T_Numeric6 NULL,--零售价格
	Price T_Numeric6 NULL,
	DiscountPrice T_Numeric6 NULL,
	IsAdjustPrice BIT NULL,
	IsAdjustDiscountPrice BIT NULL,
	AddDTM DATETIME default getdate(),
	Remark NVARCHAR(1000) NULL
	primary key  (CompanyID,BillNo,Sequence)
	)  
GO  



























