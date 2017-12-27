If Not Exists (Select top 1 1 From  Sysobjects where  id = object_id(N'BC_Sal_OrderDownd') and type = 'U')
BEGIN
CREATE TABLE [dbo].[BC_Sal_OrderDownd]
(
[CompanyID][dbo].[T_ComCode] NOT NULL,--公司ID
[ShopBillNo] [dbo].[T_BillNo_L] NOT NULL,--单号
[ShopID] [dbo].[T_ID] NULL,--货品ID
[TranState] [dbo].T_BillNo_L NULL,--交易状态
[PaymentDate] [datetime] NULL,--付款时间
[BillDate] [datetime] NULL,--开单日期
[ModifyDTM] [datetime] NOT NULL,--修改日期
CONSTRAINT [PK_BC_Sal_OrderDownd] PRIMARY KEY CLUSTERED 
(
	[CompanyID] ASC,
	[ShopBillNo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

END
GO

