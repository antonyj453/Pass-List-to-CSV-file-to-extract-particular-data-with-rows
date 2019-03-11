import pandas as pd
data=pd.read_csv('/home/uvionics/data/Latest_mar6/shoppe/shopee_milkformula_SG_2019-01-31.csv')
sku_list=['433637172','1108747978','1204923277','1454670817','1454671126','1454673145','1461455725','1513387328','376728304_281703064','1608233862']
df=data[data[' SKU'].isin(sku_list)]
df.to_csv('/home/uvionics/data/Latest_mar6/shoppe_result/shopee_milkformula_SG_2019-01-31_sku.csv', sep='\t', encoding='utf-8',index=False)
