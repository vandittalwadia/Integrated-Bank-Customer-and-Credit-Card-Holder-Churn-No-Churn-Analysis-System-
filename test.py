# import pickle
# import pandas as pd
# import numpy as np
# rfc1 = pickle.load(open('fitted_model_1_1_rfc1.pickle', 'rb'))



# def predict(Dependent_count, Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon, Credit_Limit,Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio, Age, Bank_Relationship_Period):
        
#         df=pd.read_csv('1_1.csv')
#         df=df.drop(['Attrition_Flag'],axis=1)
#         num_arr=pd.DataFrame(np.array([[Dependent_count, Total_Relationship_Count,Months_Inactive_12_mon, Contacts_Count_12_mon, Credit_Limit,Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1,Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio, Age, Bank_Relationship_Period]]),columns=df.columns)
#         df_concatnd=pd.concat([df,num_arr],axis=0)
#         df_concatnd.reset_index(drop=True,inplace=True)
#         df_concatnd_last=df_concatnd.iloc[-1,:]
#         prediction=rfc1.predict(np.array([df_concatnd_last]))
#         message=prediction[0]
#         print(message)
# predict(3,5,1,3,12691,777,11914,1.335,1144,42,1.625,0.061,1,3)

