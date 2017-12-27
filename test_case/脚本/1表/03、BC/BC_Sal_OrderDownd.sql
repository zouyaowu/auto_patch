If Not Exists (Select top 1 1 From  Sysobjects where  id = object_id(N'BC_Sal_OrderDownd') and type = 'U')
BEGIN
CREATE TABLE [dbo].[BC_Sal_OrderDownd]
(
[CompanyID][dbo].[T_ComCode] NOT NULL,--��˾ID
[ShopBillNo] [dbo].[T_BillNo_L] NOT NULL,--����
[ShopID] [dbo].[T_ID] NULL,--��ƷID
[TranState] [dbo].T_BillNo_L NULL,--����״̬
[PaymentDate] [datetime] NULL,--����ʱ��
[BillDate] [datetime] NULL,--��������
[ModifyDTM] [datetime] NOT NULL,--�޸�����
CONSTRAINT [PK_BC_Sal_OrderDownd] PRIMARY KEY CLUSTERED 
(
	[CompanyID] ASC,
	[ShopBillNo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

END
GO

