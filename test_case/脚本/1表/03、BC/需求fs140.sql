if COL_LENGTH('BC_Sal_OrderMaster_Downd','CompanyBalanceAmount') is null
begin
Alter Table BC_Sal_OrderMaster_Downd Add CompanyBalanceAmount NUMERIC(24,6) DEFAULT(0) 
end
GO
if COL_LENGTH('BC_Sal_OrderMaster_Downd','CompanyMemberCode') is null
begin
Alter Table BC_Sal_OrderMaster_Downd Add CompanyMemberCode VARCHAR(20)
end
go
if COL_LENGTH('BC_Sal_OrderMaster','CompanyBalanceAmount') is null
begin
Alter Table BC_Sal_OrderMaster Add CompanyBalanceAmount NUMERIC(24,6) DEFAULT(0) 
end
GO
if COL_LENGTH('BC_Sal_OrderMaster','CompanyMemberCode') is null
begin
Alter Table BC_Sal_OrderMaster Add CompanyMemberCode VARCHAR(20)
end
go

